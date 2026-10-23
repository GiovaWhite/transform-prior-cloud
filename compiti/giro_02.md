# Giro 02: negativi mancanti, poi blocchi 5–8

Leggi prima `CLAUDE.md`, compresa la sezione «Aggiornamento del 2026-10-23». Due fasi,
in quest'ordine.

## Fase A: i negativi mancanti nei 21 articoli gia' fatti

Gli articoli sono quelli gia' in `estrazione/cloud/`. **Esclusi** 10.1021/cg101162a e
10.1248/cpb.51.807: sono la prova e non si toccano.

Per ogni articolo:
1. Cerca nel testo, con `grep -n -i` su `testi/<file>.md`: only, even at, even after,
   did not, does not, no change, no transformation, no conversion, remained, remains,
   unchanged, stable, not observed, neither, nor, failed, could not.
2. Per ogni frase che parla delle forme solide dell'articolo, leggi il paragrafo
   attorno e controlla se un evento la copre gia'. Se no, aggiungi l'evento come dice
   il punto 2 della sezione nuova, con l'id successivo all'ultimo.
3. Niente rilettura completa dell'articolo e niente riscrittura degli eventi che ci
   sono. Se trovi un errore evidente, correggilo e scrivilo nel rapporto.
4. `python3 -m tp.verifica estrazione/cloud/<file>.json` finche' non c'e' niente di
   respinto, poi `git commit -m "negativi <doi>"` e `git push`.

Alla fine scrivi `rapporti/correzioni_negativi.md`: per ogni DOI gli eventi aggiunti
(id, da → a, la frase citata), oppure «nessuno». Commit e push.

## Fase B: i blocchi 5, 6, 7 e 8 di `assegnazioni.csv`

- In quest'ordine, seguendo `CLAUDE.md` e la sezione nuova.
- Al massimo 3 sottoagenti in parallelo, con 3 o 4 articoli ciascuno, cosi' le linee
  guida si leggono poche volte.
- Dopo ogni articolo rifai tu `tp.verifica` sul file, poi commit e push.
- Per ogni blocco scrivi `rapporti/blocco_NN.md`, corto: la tabella degli esiti e al
  massimo 5 proposte NUOVE per la v1.5 (non ripetere P1–P24).
- Niente script di controllo in piu'.

## Budget

- Tieni il conto dei token, tuoi e degli agenti, come nei rapporti precedenti.
- La fase A non deve superare circa 500 mila token.
- Appena il totale supera 2,5 milioni non cominciare articoli nuovi: finisci e salva
  quello in corso, scrivi i rapporti e fermati.
- Nell'ultimo rapporto metti i token usati per fase e per articolo.
