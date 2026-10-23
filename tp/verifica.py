"""Il verificatore: un'estrazione vale solo quello che il testo sostiene.

Per ogni file di estrazione controlla:

1. lo **schema** (`estrazione/schema_estrazione.json`);
2. che ogni **citazione** stia davvero nel testo dell'articolo. Prima si cerca
   alla lettera, dopo una normalizzazione innocua (spazi, trattini, gradi,
   virgolette, maiuscole); se non c'e', si misura il pezzo piu' lungo in comune.
   Sopra il 90 % e' `quasi` (di solito un a-capo o un simbolo letto male dal
   PDF), sotto e' `assente`;
3. che ogni **numero** delle condizioni compaia in una citazione dell'evento: un
   numero senza frase che lo dica e' un numero inventato finche' non si prova il
   contrario;
4. che `da` e `a` puntino a forme dichiarate.

Dalla v1.4 controlla allo stesso modo le proprieta' delle molecole (citazione e
numeri), i gruppi coinvolti negli eventi, i motivi di legame H e le strutture
delle forme, e che `da_possibili`, `a_possibili`, `piu_stabile_fra` e le
composizioni puntino a forme dichiarate.

Un evento con una citazione assente o un numero senza appoggio e' `respinto`.

Uso:  python -m tp.verifica estrazione/pilota/<file>.json [...]
      python -m tp.verifica --cartella estrazione/pilota
"""
import argparse
import difflib
import json
import re
import unicodedata
from pathlib import Path

from .comune import LETTI, RADICE, nome_file

SCHEMA = json.loads((RADICE / "estrazione" / "schema_estrazione.json").read_text(encoding="utf-8"))
SPECIALI = {"fuso", "amorfo", "decomposizione", "reazione", "ignota"}


def normalizza(s):
    # I PDF scritti col font Symbol mettono i caratteri nell'area d'uso privato
    # (U+F020-U+F0FF = ASCII + 0xF000): «P» e' «P-1».
    s = re.sub("[-]", lambda m: chr(ord(m.group()) - 0xF000), s or "")
    # Il segno di grado dei PDF giapponesi e' il semi-sonoro «゜» (U+309C), che
    # NFKC trasformerebbe in spazio + segno combinante.
    s = s.replace("゜", "°")
    # Mojibake dei PDF giapponesi (Chem. Pharm. Bull. vecchi): «70•Ž» e' 70 °C,
    # «ƒÊm» e' µm.
    s = s.replace("•Ž", "°C").replace("ƒÊ", "µ")
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("­", "")                                   # trattino morbido
    s = re.sub(r"[‐-―−⁃﹣－]", "-", s)  # trattini e meno
    s = re.sub(r"[º˚∘◦]", "°", s)              # gradi scritti male (anche «◦»)
    s = re.sub(r"[‘’‚′]", "'", s)
    s = re.sub(r"[“”„″]", '"', s)
    s = re.sub(r"(?<=\w)-\s+(?=\w)", "-", s)                        # a-capo con trattino
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def testo_articolo(doi):
    p = LETTI / f"{nome_file(doi)}.json"
    t = json.loads(p.read_text(encoding="utf-8"))
    parti = [t.get("titolo", ""), t.get("abstract", "")]
    parti += [s.get("titolo", "") + " " + s["testo"] for s in t.get("sezioni", [])]
    parti += [(f.get("etichetta") or "") + " " + (f.get("didascalia") or "") for f in t.get("figure", [])]
    parti += [(x.get("etichetta") or "") + " " + (x.get("didascalia") or "") + " " + (x.get("testo") or "")
              for x in t.get("tabelle", [])]
    return normalizza(" \n ".join(parti))


def cerca(citazione, testo):
    c = normalizza(citazione)
    if not c:
        return "assente", 0.0
    if c in testo:
        return "esatta", 1.0
    # Il pezzo piu' lungo in comune, cercato attorno alla parola piu' rara della
    # citazione: SequenceMatcher su un articolo intero sarebbe lento.
    parole = sorted(set(re.findall(r"[a-z0-9]{5,}", c)), key=lambda w: testo.count(w) or 10**9)
    migliore = 0.0
    for w in parole[:3]:
        for m in re.finditer(re.escape(w), testo):
            a = max(0, m.start() - len(c) - 50)
            finestra = testo[a:m.end() + len(c) + 50]
            sm = difflib.SequenceMatcher(None, c, finestra, autojunk=False)
            blocchi = sum(b.size for b in sm.get_matching_blocks())
            migliore = max(migliore, blocchi / len(c))
            if migliore >= 0.98:
                break
    return ("quasi" if migliore >= 0.9 else "assente"), round(migliore, 3)


def _numero(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _numeri(grandezza):
    # `lettura_probabile` NON c'e' di proposito: e' una lettura, non un numero
    # scritto, e il verificatore non la conta.
    if not isinstance(grandezza, dict):
        return []
    return [grandezza[k] for k in ("valore", "min", "max", "onset", "picco", "fine", "delta")
            if _numero(grandezza.get(k))] + [x for k in ("picchi", "valori")
                                             for x in (grandezza.get(k) or []) if _numero(x)]


# Le chiavi che fanno di un dizionario una grandezza. Non «testo» ne' «tipo»:
# anche `macinazione` ed `estrusione` hanno un «testo».
CHIAVI_GRANDEZZA = {"valore", "min", "max", "onset", "picco", "fine", "unita", "picchi", "delta", "valori"}
# Numeri sciolti (non grandezze) dentro le condizioni, che vanno sostenuti lo stesso.
NUMERI_SCIOLTI = ("frequenza_Hz", "eta_uL_mg")


def grandezze(obj, prefisso=""):
    """Tutte le grandezze dentro condizioni o osservazioni, anche annidate
    (luce.lunghezza_onda, macinazione.durata, estrusione.velocita_vite), con il
    loro percorso; piu' i numeri sciolti come grandezze senza unita'."""
    if not isinstance(obj, dict):
        return
    for k, v in obj.items():
        nome = f"{prefisso}{k}"
        if isinstance(v, dict):
            if CHIAVI_GRANDEZZA & set(v):
                yield nome, v
            else:
                yield from grandezze(v, nome + ".")
        elif isinstance(v, list):
            # v1.3: liste di oggetti con grandezze dentro (osservazioni.entalpie).
            for i, x in enumerate(v):
                if isinstance(x, dict):
                    if CHIAVI_GRANDEZZA & set(x):
                        yield f"{nome}[{i}]", x
                    else:
                        yield from grandezze(x, f"{nome}[{i}].")
        elif k in NUMERI_SCIOLTI and _numero(v):
            yield nome, {"valore": v, "unita": None}


PAROLE_NUMERO = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
    9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
    24: "twenty-four", 30: "thirty", 40: "forty", 48: "forty-eight", 50: "fifty", 60: "sixty",
    100: "hundred", 0.5: "half",
}
# «after the first day» vale tempo = 1 giorno.
ORDINALI = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth", 7: "seventh",
            8: "eighth", 9: "ninth", 10: "tenth"}


def _parole(numero):
    n = float(numero) if not float(numero).is_integer() else int(numero)
    return [p for p in (PAROLE_NUMERO.get(n), ORDINALI.get(n)) if p]


def _appare(numero, citazioni):
    """Il numero compare in una delle citazioni, in una delle sue scritture
    (anche in lettere: «after five days», «after the first day»)."""
    testo_parole = " ".join(normalizza(c) for c in citazioni)
    if any(re.search(rf"\b{re.escape(p)}\b", testo_parole) for p in _parole(numero)):
        return True
    # v1.4: «after a year», «within a day» valgono 1.
    if numero == 1 and re.search(rf"\ban?\s+(?:{_TEMPI})\b", testo_parole):
        return True
    forme = {str(numero)}
    if float(numero).is_integer():
        forme.add(str(int(numero)))
    else:
        forme.add(f"{numero:g}")
        forme.add(str(numero).replace(".", ","))
    testo = " ".join(normalizza(c) for c in citazioni)
    # Un decimale scritto «2.70» arriva nel JSON come 2.7: dopo la mantissa si
    # ammettono zeri finali, e solo quelli.
    return any(re.search(rf"(?<![\d.])(?<!\d,){re.escape(f)}{'0*' if ('.' in f or ',' in f) else ''}(?![\d])", testo)
               for f in forme)


_TEMPI = r"second|minute|hour|day|week|month|year"

# Le scritture di un'unita' nel testo normalizzato (minuscolo). Un'unita' non in
# tabella non si controlla: meglio nessun avviso che un avviso sbagliato.
# v1.4: «75–80°» senza C vale °C; «453 Kb», con la lettera di una nota attaccata, vale K.
UNITA = {
    "°c": r"°\s?c|°(?![a-z])|deg(?:rees?)?\s?c|\bc\b", "c": r"°\s?c|°(?![a-z])|\bc\b",
    "k": r"k(?:\b|[a-e]\b)|kelvin",
    "gpa": r"gpa", "mpa": r"mpa", "kpa": r"kpa", "kbar": r"kbar", "bar": r"bar\b", "atm": r"atm",
    "%": r"%", "%rh": r"%", "rh": r"%|rh", "wt%": r"%", "wt.%": r"%", "mass%": r"%",
    "s": r"s\b|sec|seconds?", "min": r"min|minutes?", "h": r"h\b|hrs?\b|hours?",
    "day": r"days?|d\b", "days": r"days?|d\b", "d": r"days?|d\b",
    "week": r"weeks?|wks?", "weeks": r"weeks?", "month": r"months?", "months": r"months?",
    "year": r"years?", "years": r"years?",
    # I testi giapponesi (Yakugaku Zasshi, Chem. Pharm. Bull. vecchi).
    "日": r"日|days?", "時間": r"時間|h\b|hours?", "ヵ月": r"[ヵヶか]月|months?", "ヶ月": r"[ヵヶか]月|months?",
    "分": r"分|min", "週間": r"週間|weeks?",
    "k/min": r"k\s?[·./]?\s?min", "°c/min": r"°\s?c\s?[·./]?\s?min", "kmin-1": r"k\s?[·.]?\s?min",
    "°cmin-1": r"°\s?c\s?[·.]?\s?min",
    "kj/mol": r"kj", "kjmol-1": r"kj", "j/g": r"j\s?/?\s?g|j\s?g", "kcal/mol": r"kcal",
    "nm": r"nm", "rpm": r"rpm", "hz": r"hz", "pa": r"pa\b", "mbar": r"mbar", "torr": r"torr",
    "mmhg": r"mm\s?hg",
}

# Dopo il numero: un'incertezza fra parentesi o con ±, un suffisso ordinale
# («2nd day»), e fino a otto altri numeri legati da trattino, «to», «and», «or»
# o virgola, ciascuno con la sua incertezza: «235.2, 99.9, and 92.8 °C» e
# «from 112.8 ± 0.5 to 149.8 ± 0.6 °C» reggono tutti i loro numeri.
_INCERTEZZA = r"(?:\(\d+\))?(?:\s*±\s*[\d.,]+)?"
_ALTRI = r"(?:\s*(?:,\s*(?:and|or)?|-|to|and|or)\s*-?[\d.,]+" + _INCERTEZZA + r"){0,8}"


def _con_unita(numero, unita, citazioni):
    """Il numero compare ATTACCATO alla sua unita' (con un intervallo, un elenco
    o un'incertezza in mezzo, al massimo): «1 GPa ... for a week» non regge
    `tempo = 1 week`. Restituisce None se l'unita' non e' in tabella."""
    u = re.sub(r"\s+", "", (unita or "")).replace("−", "-").replace("º", "°").lower()
    rx_u = UNITA.get(u)
    if rx_u is None:
        return None
    testo = " ".join(normalizza(c) for c in citazioni)
    scritture = {str(numero)}
    if float(numero).is_integer():
        scritture.add(str(int(numero)))
    coda = _INCERTEZZA + r"(?:st|nd|rd|th)?" + _ALTRI + r"\s*(?:" + rx_u + ")"
    for f in scritture:
        dec = "0*" if ("." in f) else ""
        if re.search(rf"(?<![\d.])(?<!\d,){re.escape(f)}{dec}{coda}", testo):
            return True
    # In lettere, anche con l'articolo in mezzo: «half a month», «five days»; e «a year» = 1.
    if numero == 1 and re.search(rf"\ban?\s+(?:{rx_u})", testo):
        return True
    return any(re.search(rf"\b{re.escape(p)}\s*(?:an?\s+)?(?:{rx_u})", testo) for p in _parole(numero))


def _controlla_numeri(coppie, citazioni):
    """(problemi, avvisi) per una lista di (nome, grandezza): un numero che non
    compare e' un problema, un numero lontano dalla sua unita' un avviso."""
    problemi, avvisi = [], []
    for nome, g in coppie:
        for n in _numeri(g):
            if not _appare(n, citazioni):
                problemi.append(f"{nome} {n} non compare nelle citazioni")
            elif _con_unita(n, (g or {}).get("unita"), citazioni) is False:
                avvisi.append(f"{nome} {n}: il numero c'e' ma non accanto a «{g.get('unita')}»")
    return problemi, avvisi


def verifica(percorso):
    from jsonschema import Draft202012Validator

    e = json.loads(Path(percorso).read_text(encoding="utf-8"))
    rapporto = {"file": str(percorso), "doi": e.get("doi"), "schema": [], "eventi": [],
                "forme": [], "preparazioni": []}
    errori = sorted(Draft202012Validator(SCHEMA).iter_errors(e), key=lambda x: list(x.path))
    rapporto["schema"] = [f"{'/'.join(map(str, x.path))}: {x.message}" for x in errori][:20]
    try:
        testo = testo_articolo(e["doi"])
    except FileNotFoundError:
        rapporto["errore"] = "testo dell'articolo non trovato in corpus/letti"
        return rapporto
    ids = {f.get("id") for f in e.get("forme", [])}
    eventi_ids = {x.get("id") for x in e.get("eventi", [])}
    composti_ids = {c.get("id") for c in e.get("composti", [])}

    def citate(voci, cosa):
        """v1.4: liste di voci con la loro citazione (motivi_hb, gruppi_coinvolti, strutture)."""
        out = []
        for i, v in enumerate(voci or []):
            if isinstance(v, dict) and v.get("citazione"):
                es, q = cerca(v["citazione"], testo)
                if es == "assente":
                    out.append(f"{cosa}[{i}]: citazione assente ({q:.0%})")
            if isinstance(v, dict) and v.get("forma") and v["forma"] not in ids:
                out.append(f"{cosa}[{i}].forma = {v['forma']!r} non e' una forma dichiarata")
        return out

    for f in e.get("forme", []):
        problemi = [f"forme_possibili: {x!r} non e' una forma dichiarata"
                    for x in (f.get("forme_possibili") or []) + (f.get("forme_componenti") or []) if x not in ids]
        if f.get("stato_di") and f["stato_di"] not in ids:
            problemi.append(f"stato_di = {f['stato_di']!r} non e' una forma dichiarata")
        problemi += citate(f.get("motivi_hb"), "motivi_hb") + citate(f.get("strutture"), "strutture")
        for i, st in enumerate(f.get("strutture") or []):
            sostegno = [x for x in (st.get("citazione"), f.get("citazione")) if x]
            p_num, _ = _controlla_numeri([(f"strutture[{i}].temperatura", st.get("temperatura"))], sostegno)
            problemi += p_num
        voce = {"id": f.get("id"), "problemi": problemi}
        if f.get("citazione"):
            voce["citazione"], voce["quota"] = cerca(f["citazione"], testo)
        rapporto["forme"].append(voce)
    rapporto["molecole"] = []
    for m in e.get("molecole") or []:
        problemi = [] if m.get("composto") in composti_ids else [f"composto = {m.get('composto')!r} non dichiarato"]
        problemi += citate(m.get("descrizioni"), "descrizioni") + citate(m.get("proprieta"), "proprieta")
        for i, pr_ in enumerate(m.get("proprieta") or []):
            p_num, _ = _controlla_numeri([(f"proprieta[{i}].{k}", pr_.get(k))
                                          for k in ("grandezza", "temperatura", "umidita", "pH")],
                                         [pr_.get("citazione") or ""])
            problemi += p_num
        rapporto["molecole"].append({"composto": m.get("composto"), "problemi": problemi,
                                     "verdetto": "respinto" if problemi else "accettato"})
    for p in e.get("preparazioni", []):
        cit = list(p.get("citazioni") or []) + ([p["citazione"]] if p.get("citazione") else [])
        esiti = [cerca(c, testo) for c in cit] or [("assente", 0.0)]
        peggiore = min(esiti, key=lambda x: x[1])
        # Anche i numeri di una preparazione vanno sostenuti dalle sue citazioni.
        problemi, avvisi = _controlla_numeri(grandezze({k: p.get(k) for k in
                                                         ("temperatura", "pressione", "velocita", "tempo", "umidita",
                                                          "attivita_acqua", "pH", "agitazione")}),
                                             cit)
        forme_p = p.get("forme") or ([p["forma"]] if p.get("forma") else [])
        problemi += [f"forma {x!r} non dichiarata" for x in forme_p if x not in ids]
        da_ev = p.get("da_evento")
        for x in ([da_ev] if isinstance(da_ev, str) else (da_ev or [])):          # v1.4: anche una lista
            if x not in eventi_ids:
                problemi.append(f"da_evento = {x!r} non e' un evento")
        if peggiore[0] == "assente":
            problemi.append(f"citazione assente ({peggiore[1]:.0%})")
        rapporto["preparazioni"].append({"forme": forme_p, "citazione": peggiore[0], "quota": peggiore[1],
                                         "problemi": problemi, "avvisi": avvisi,
                                         "verdetto": "respinto" if problemi else "accettato"})
    rapporto["relazioni"] = []
    for rel in e.get("relazioni") or []:
        esito, quota = cerca(rel.get("citazione", ""), testo)
        problemi = [] if esito != "assente" else [f"citazione assente ({quota:.0%})"]
        for chiave in ("temperatura_transizione", "attivita_critica", "pH_max"):
            valore = rel.get(chiave)
            # v1.4: piu' stime della temperatura di transizione, ciascuna con la sua citazione.
            stime = valore if isinstance(valore, list) else [{"grandezza": valore}]
            for st in stime:
                sostegno = [x for x in (st.get("citazione"), rel.get("citazione")) if x]
                for n in _numeri(st.get("grandezza")):
                    if not _appare(n, sostegno):
                        problemi.append(f"{chiave} {n} non compare nella citazione")
            problemi += citate([x for x in stime if x.get("citazione")], chiave) if isinstance(valore, list) else []
        problemi += [f"forma {x!r} non dichiarata" for x in rel.get("forme", []) if x not in ids]
        problemi += [f"piu_stabile_fra: {x!r} non e' una forma dichiarata"
                     for x in rel.get("piu_stabile_fra") or [] if x not in ids]
        for k in ("piu_stabile", "stabile_a_temperatura_ambiente"):
            if rel.get(k) and rel[k] not in ids:
                problemi.append(f"{k} = {rel[k]!r} non e' una forma dichiarata")
        rapporto["relazioni"].append({"forme": rel.get("forme"), "problemi": problemi,
                                      "verdetto": "respinto" if problemi else "accettato"})
    for ev in e.get("eventi", []):
        cit = ev.get("citazioni") or []
        esiti = [cerca(c, testo) for c in cit]
        problemi, avvisi = [], []
        for c, (es, q) in zip(cit, esiti):
            if es == "assente":
                problemi.append(f"citazione assente ({q:.0%}): «{c[:80]}»")
        tutte = list(grandezze(ev.get("condizioni") or {})) + list(grandezze(ev.get("osservazioni") or {}))
        p_num, a_num = _controlla_numeri(tutte, cit)
        problemi += p_num
        avvisi += a_num
        for nome, g in tutte:
            rel_a = (g or {}).get("relativo_a")
            for x in ([rel_a] if isinstance(rel_a, str) else (rel_a or [])):          # v1.4: anche una lista
                if x not in eventi_ids:
                    problemi.append(f"{nome}.relativo_a = {x!r} non e' un evento")
        # v1.4: forme possibili, composizioni e gruppi coinvolti.
        for k in ("da_possibili", "a_possibili"):
            problemi += [f"{k}: {x!r} non e' una forma dichiarata"
                         for x in ev.get(k) or [] if x not in ids and x not in SPECIALI]
        for k, dove in (("composizione_iniziale", "condizioni"), ("composizione_prodotto", "osservazioni")):
            problemi += [f"{k}: {x.get('forma')!r} non e' una forma dichiarata"
                         for x in ((ev.get(dove) or {}).get(k) or []) if isinstance(x, dict) and x.get("forma") not in ids]
        problemi += citate(ev.get("gruppi_coinvolti"), "gruppi_coinvolti")
        inversi = ev.get("inverso_di")
        for x in ([inversi] if isinstance(inversi, str) else (inversi or [])):
            if x not in eventi_ids:
                problemi.append(f"inverso_di = {x!r} non e' un evento")
        problemi += [f"prodotti_secondari: {x!r} non e' una forma dichiarata"
                     for x in ev.get("prodotti_secondari") or [] if x not in ids and x not in SPECIALI]
        if ev.get("da_evento") and ev["da_evento"] not in eventi_ids:
            problemi.append(f"da_evento = {ev['da_evento']!r} non e' un evento")
        if ev.get("via") is None and ev.get("fonte_dati") != "citata":
            problemi.append("via null e' ammessa solo per un evento citato (fonte_dati: citata)")
        for k in ("da", "a"):
            v = ev.get(k)
            if v not in ids and v not in SPECIALI:
                problemi.append(f"'{k}' = {v!r} non e' una forma dichiarata")
        rapporto["eventi"].append({
            "id": ev.get("id"), "via": ev.get("via"), "esito": ev.get("esito"),
            "citazioni": [es for es, _q in esiti],
            "problemi": problemi,
            "avvisi": avvisi,
            # Un avviso non respinge: segnala l'evento per un controllo umano.
            "verdetto": "respinto" if problemi else (
                "accettato" if (all(es == "esatta" for es, _ in esiti) and not avvisi) else "accettato_quasi"),
        })
    return rapporto


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="*")
    ap.add_argument("--cartella")
    args = ap.parse_args()
    files = [Path(f) for f in args.file]
    if args.cartella:
        files += sorted(p for p in Path(args.cartella).glob("*.json")
                       if not p.name.endswith((".verifica.json", ".collega.json")))
    totali = {"accettato": 0, "accettato_quasi": 0, "respinto": 0}
    altri = {"preparazioni respinte": 0, "relazioni respinte": 0, "forme con problemi": 0,
             "molecole respinte": 0}
    for f in files:
        r = verifica(f)
        Path(str(f).replace(".json", ".verifica.json")).write_text(
            json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
        for ev in r["eventi"]:
            totali[ev["verdetto"]] += 1
        stato = r.get("errore") or (f"schema: {len(r['schema'])} errori; " if r["schema"] else "") + \
            ", ".join(f"{ev['id']}:{ev['verdetto']}" for ev in r["eventi"])
        print(f"{r['doi']}: {stato}")
        for ev in r["eventi"]:
            for p in ev["problemi"]:
                print(f"    {ev['id']}: {p}")
            for p in ev.get("avvisi", []):
                print(f"    {ev['id']} (avviso): {p}")
        for i, p in enumerate(r.get("preparazioni", [])):
            altri["preparazioni respinte"] += p.get("verdetto") == "respinto"
            for x in p.get("problemi", []):
                print(f"    preparazione {i + 1} {p.get('forme')}: {x}")
        for rel in r.get("relazioni", []):
            altri["relazioni respinte"] += rel.get("verdetto") == "respinto"
            for x in rel.get("problemi", []):
                print(f"    relazione {rel.get('forme')}: {x}")
        for fo in r.get("forme", []):
            altri["forme con problemi"] += bool(fo.get("problemi"))
            for x in fo.get("problemi", []):
                print(f"    forma {fo.get('id')}: {x}")
        for mo in r.get("molecole", []):
            altri["molecole respinte"] += mo.get("verdetto") == "respinto"
            for x in mo.get("problemi", []):
                print(f"    molecola {mo.get('composto')}: {x}")
        for x in r["schema"]:
            print(f"    schema: {x}")
    print(f"eventi: {totali}")
    print(", ".join(f"{k}: {v}" for k, v in altri.items()))


if __name__ == "__main__":
    main()
