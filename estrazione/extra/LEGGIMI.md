# estrazione/extra — i dati che l'estrazione principale non cattura (formato e0)

Pilota. L'estrazione principale (`estrazione/cloud/<file>.json`, schema v1.4) tiene forme, eventi, preparazioni, relazioni e molecole.
Qui va **tutto il resto che l'articolo dice dei solidi e dei composti**: spettri, geometria, dati cristallografici e di raffinamento,
analisi di composizione, rese e quantita' di sintesi, risultati di calcolo, ecc. Un file per articolo:

    estrazione/extra/<file>.extra.json          # <file> = colonna `file` di assegnazioni.csv, come per l'estrazione principale
    estrazione/extra/<file>.extra.verifica.json # scritto dal controllo

L'estrazione principale del solito articolo deve esistere gia' (e passare `python3 -m tp.verifica`): l'extra la richiama per id di forma e di composto
e non ne ripete il contenuto.

## Formato

```json
{
 "versione_extra": "e0",
 "doi": "10.1021/cg101162a",
 "voci": [
  {
   "id": "X1",
   "categoria": "spettroscopia",
   "proprieta": "ν(O–H) del p-OH (banda IR)",
   "oggetto": {"forma": "F2", "composto": null, "etichetta": "form II°"},
   "tecnica": "FT-IR",
   "valori": [{"valore": 3373, "unita": "cm-1"}],
   "condizioni": null,
   "qualitativo": "banda stretta",
   "calcolato": false,
   "citazione": "In form II° a sharp band occurs at 3373 cm−1, whereas in form I the band is broader and shifted to higher wavenumber (3432 cm−1)",
   "note": null
  }
 ]
}
```

Campi di una voce (nessun altro e' ammesso):

| campo | obbligatorio | contenuto |
|---|---|---|
| `id` | si' | `X1`, `X2`... unico nel file |
| `categoria` | si' | una delle categorie qui sotto |
| `proprieta` | si' | che cosa e' misurato o detto, breve, con le parole dell'articolo («R1 [I > 2σ(I)]», «D–H···A: O1–H1···N2», «ν(S=O)») |
| `citazione` | si' | frase o riga di tabella **letterale** (stessa regola dell'estrazione principale) |
| `valori` | si' (anche `[]`) | lista di `{etichetta, forma, valore, incertezza, unita, testo, circa, limite, lettura_probabile}`, tutti facoltativi |
| `oggetto` | no | `{forma, composto, etichetta}`: id di `forme` / `composti` dell'estrazione principale, e/o l'etichetta come scritta |
| `tecnica` | no | DSC, FT-IR, Raman, NMR, SCXRD, PXRD, TGA, HPLC... |
| `condizioni` | no | in breve: solvente, T, atmosfera, campione |
| `qualitativo` | no | il fatto detto a parole, quando non e' (solo) un numero: «p-OH proton disordered», «isomorphous to H0» |
| `calcolato` | no | `true` se il valore e' un calcolo dell'articolo (DFT, CSP, formula) e non una misura |
| `note` | no | dubbi, difetti del PDF, «citato dal rif. N» |

## Categorie

- `cristallografia`: lunghezza d'onda, strumento e dati numerici di raccolta, dimensioni e colore del cristallo, formula e peso formula, densita' calcolata, F(000), μ, intervallo θ, indici, riflessioni misurate/indipendenti/osservate, parametri, vincoli, R1/wR2/Rwp/GOF, picchi di differenza, parametri di sintesi della struttura (mosse, run). **Non** a, b, c, α, β, γ, V, Z, T, gruppo spaziale, sistema, CCDC e refcode: sono gia' nelle forme.
- `geometria`: legami H (D–H, H···A, D···A, angolo, codice di simmetria), distanze intermolecolari e fra centroidi, angoli diedri e torsioni (con i valori), contatti, rmsd di sovrapposizione.
- `diffrazione_polvere`: picchi PXRD (2θ, intensita'), segnature di identificazione, intervallo di scansione, passo, velocita'.
- `spettroscopia`: IR, Raman, NMR (spostamenti, J, integrali), MS (m/z), UV, ssNMR: una voce per banda o picco, con attribuzione.
- `termica`: dati di DSC, TGA, HSM che non sono nei campi degli eventi (entalpie e perdite di forme che non hanno un evento, calibrazioni numeriche, intervalli, picchi secondari).
- `composizione`: analisi elementare (trovato / calcolato), Karl Fischer, cloruro, contenuto di solvente, purezza.
- `sintesi`: resa, quantita' dei reagenti, tempi e volumi di reazione, TLC Rf, HPLC (tempi di ritenzione relativi, purezza), punto di fusione di sintesi.
- `computazionale`: energie, rmsd, densita' previste, numero di strutture generate, livelli di teoria *quando danno un numero*.
- `proprieta_fisiche`: solubilita', igroscopicita', densita' misurata, dissoluzione, durezza... se non sono gia' in `molecole`.
- `morfologia`: abito, colore, dimensioni, trasparenza/opacita' dei cristalli.
- `metodo`: parametri numerici di acquisizione che qualificano i dati dell'articolo (flussi, velocita' di scansione, masse di campione, potenze) quando non stanno gia' nelle condizioni di un evento.
- `struttura_qualitativa`: fatti strutturali a parole (disordine, isomorfismo, impacchettamento, simmetria, conformazione), con `valori: []`.
- `altro`: ogni altro dato dell'articolo che non entra altrove.

## Regole (lavoro chirurgico)

1. **Una voce = un fatto**: una proprieta' di un oggetto, oppure **una riga di tabella** su piu' forme (un elemento di `valori` per colonna, ciascuno con `forma` o `etichetta`). La citazione e' quella frase o quella riga.
2. **Citazione letterale e la piu' corta che regge il fatto**: una frase, un pezzo di frase, una riga di tabella `«parametro | v1 | v2 | v3»` come sta nel testo. Mai parafrasare, mai correggere i difetti del PDF (ligature e simboli sono tollerati dal controllo). Una frase interrotta da un'intestazione di pagina si cita in due voci o in due pezzi, mai attraverso l'intestazione.
3. **Ogni numero di `valori` (valore e incertezza) deve comparire nella citazione**, scritto come nell'articolo: niente conversioni di unita', niente arrotondamenti, niente numeri calcolati da chi estrae. `incertezza` e' la cifra fra parentesi o dopo ±, in valore assoluto nell'unita' del valore (se il testo scrive `159.8(5)` e' un'incertezza della sola ultima cifra: scrivi `valore: 159.8` e `incertezza: 5` con `note: "ultima cifra"`; con `± 0.5` scrivi `0.5`).
4. **Numero rovinato dal PDF** (segni meno diventati cifre, `×` diventato `3`): `valore: null`, il testo come scritto in `testo`, la lettura probabile in `lettura_probabile` (non e' sostenuta dal testo).
5. **Niente doppioni con l'estrazione principale**: non ripetere cio' che gia' sta in forme (cella, gruppo, CCDC, refcode, motivi H), eventi (condizioni, entalpie, perdite di massa), preparazioni, relazioni e molecole. Un dato che serve in entrambi i posti con un altro ruolo si scrive una volta sola, dove e' piu' utile.
6. **Niente conoscenza esterna**: nessun valore noto del composto, nessun calcolo di chi estrae, nessuna conversione.
7. **Dati citati da altri lavori** (rif. N) sullo stesso composto: si estraggono, con `note: "citato dal rif. N"`.
8. **Cosa non si estrae**: bibliografia, autori, affiliazioni, finanziamenti, intestazioni e pie' di pagina; nomi di software o strumenti senza un valore; affermazioni generali di introduzione su altri composti o su altri lavori senza numeri di questo sistema.
9. `oggetto.forma` / `oggetto.composto` devono essere id dell'estrazione principale; se il dato riguarda una forma che li' non c'e' (una struttura ipotetica, una forma solo calcolata), usa `etichetta` come scritta.

## Controllo e copertura

Lo script `verifica_extra.py` (non incluso nel repo: le istruzioni vietano di aggiungere codice; disponibile su richiesta) controlla ogni voce
(chiavi ammesse, categoria, citazione esatta nel testo, numeri nella citazione, id di forma e di composto), segnala i doppioni e calcola la **copertura**:
la percentuale di numeri dell'articolo che stanno dentro una citazione dell'estrazione principale o dell'extra, con l'elenco delle frasi che hanno ancora numeri non citati.
Non si punta al 100%: restano fuori i rimandi, la bibliografia e le esclusioni della regola 8; ma ogni frase non coperta va o riletta e coperta, o riconosciuta come esclusa.
