# Giro 03: gli articoli con la resa attesa piu' alta

Leggi prima `CLAUDE.md`, compresa la sezione «Aggiornamento del 2026-10-23», che resta
valida: niente extra, negativi, aria, niente doppioni.

## Perche' questi articoli

Sui 98 articoli gia' estratti, rendono (cioe' danno trasformazioni A → B con entrambe le
strutture nel CSD) quelli che seguono trasformazioni fra forme, spesso a temperatura variabile
o in situ: transizioni cristallo singolo → cristallo singolo, alta pressione, idratazione e
desolvatazione con struttura del prodotto. Questi 15 sono i migliori fra i testi disponibili.
Diversi sono di cristalli meccanicamente reattivi (termosalienti, superelastici) o di alta
pressione: sono pertinenti, perche' la via `pressione` e' quella con meno dati.

## Che cosa fare

Estrai, **in quest'ordine**, gli articoli qui sotto (`<file>` e' la colonna `file` di
`assegnazioni.csv`; alcuni stanno in blocchi lontani, non importa). Niente fase di correzione
e nessun altro blocco.

| # | DOI | file |
|---|---|---|
| 1 | 10.1021/acs.cgd.9b01522 | 10.1021__acs.cgd.9b01522_008b723c |
| 2 | 10.1107/s2052252521010381 | 10.1107__s2052252521010381_98f965a9 |
| 3 | 10.3390/molecules24102018 | 10.3390__molecules24102018_ab4548a3 |
| 4 | 10.3390/molecules29184376 | 10.3390__molecules29184376_b63cd71e |
| 5 | 10.3390/cryst7010013 | 10.3390__cryst7010013_eb064f85 |
| 6 | 10.1021/acs.jpcc.1c07297 | 10.1021__acs.jpcc.1c07297_ddc48063 |
| 7 | 10.3390/molecules27217411 | 10.3390__molecules27217411_ea1a94fe |
| 8 | 10.3390/cryst10121098 | 10.3390__cryst10121098_0292273c |
| 9 | 10.1021/jacs.3c07060 | 10.1021__jacs.3c07060_ea22006d |
| 10 | 10.1107/s2052252523002452 | 10.1107__s2052252523002452_360f36bd |
| 11 | 10.1038/s42004-025-01715-8 | 10.1038__s42004-025-01715-8_7f4f3bc6 |
| 12 | 10.1039/c5sc04057d | 10.1039__c5sc04057d_5dc4c3f7 |
| 13 | 10.1107/s2052252519015616 | 10.1107__s2052252519015616_e27f951c |
| 14 | 10.1021/acs.chemmater.7b02558 | 10.1021__acs.chemmater.7b02558_d9a668c4 |
| 15 | 10.1021/jacs.3c09246 | 10.1021__jacs.3c09246_8f18d220 |

- Al massimo 3 sottoagenti in parallelo, con 4 o 5 articoli ciascuno, dati nell'ordine
  della tabella (il primo agente prende 1, 4, 7..., il secondo 2, 5, 8..., il terzo 3, 6, 9...),
  cosi' se ci si ferma prima restano fatti i primi.
- Passa a ogni agente la sezione «Aggiornamento del 2026-10-23» di `CLAUDE.md` per intero.
- **Gruppi funzionali**: `gruppi_coinvolti` negli eventi e `motivi_hb` nelle forme si
  compilano OGNI volta che il testo descrive legami a idrogeno, sintoni, contatti (alogeno,
  π) o conformazioni che cambiano, o restano, fra A e B, con la frase che lo dice. Mai dedotti
  dalle figure o dalla chimica: solo dal testo.
- Per ogni forma con una struttura scrivi refcode o CCDC **se il testo li riporta**: servono a
  collegare la forma al CSD. Mai a memoria.
- Dopo ogni articolo rifai tu `python3 -m tp.verifica estrazione/cloud/<file>.json`, poi commit
  e push.
- Alla fine scrivi `rapporti/giro_03.md`, corto: la tabella degli esiti per DOI, i token per
  agente e al massimo 5 proposte nuove (non ripetere quelle dei rapporti precedenti).
- Niente script di controllo in piu'.

## Budget

- Tieni il conto dei token, tuoi e degli agenti, come nei rapporti precedenti.
- Appena il totale supera **1,9 milioni** non assegnare articoli nuovi: gli agenti finiscono e
  salvano quello in corso, tu scrivi il rapporto, fai commit e push e ti fermi.
