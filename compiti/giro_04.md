# Giro 04: altri articoli scelti per resa attesa

Leggi prima `CLAUDE.md`, compresa la sezione «Aggiornamento del 2026-10-23», che resta
valida: niente extra, negativi, aria, niente doppioni.

## Perche' questi articoli

Sono scelti come nel giro 03: frasi su trasformazioni fra forme, temperatura variabile o in
situ, punteggio del testo. Rispetto al giro 03 sono tolti gli articoli fuori scopo
(fotochimica, reticoli porosi, polimeri) e quelli con poche frasi di trasformazione fra forme:
nel giro 03 erano quelli che non hanno dato niente. Restano transizioni cristallo singolo →
cristallo singolo, cristalli termosalienti e superelastici, alta pressione, polimorfi e
solvati.

## Che cosa fare

Estrai gli articoli qui sotto **in quest'ordine** (`<file>` e' la colonna `file` di
`assegnazioni.csv`; alcuni stanno in blocchi lontani, non importa). Niente fase di correzione
e nessun altro blocco.

| # | DOI | file |
|---|---|---|
| 1 | 10.1021/jacs.3c14800 | 10.1021__jacs.3c14800_d9682741 |
| 2 | 10.1021/acs.cgd.9b01281 | 10.1021__acs.cgd.9b01281_ed222357 |
| 3 | 10.1038/s41467-019-11612-z | 10.1038__s41467-019-11612-z_81659e9f |
| 4 | 10.1021/jacs.4c09222 | 10.1021__jacs.4c09222_cb050aa3 |
| 5 | 10.1021/jacs.4c17448 | 10.1021__jacs.4c17448_2845f115 |
| 6 | 10.1021/acs.cgd.5c01210 | 10.1021__acs.cgd.5c01210_cfe82aa2 |
| 7 | 10.1107/s2052252525011601 | 10.1107__s2052252525011601_133fe272 |
| 8 | 10.1107/s2052252523001197 | 10.1107__s2052252523001197_ff274a0c |
| 9 | 10.3390/molecules24112174 | 10.3390__molecules24112174_4f564d50 |
| 10 | 10.1038/srep29610 | 10.1038__srep29610_8ce0e88f |
| 11 | 10.1038/s41467-017-02549-2 | 10.1038__s41467-017-02549-2_6f5ad52d |
| 12 | 10.1021/acs.cgd.7b01065 | 10.1021__acs.cgd.7b01065_fa4942d7 |
| 13 | 10.1021/jacs.5c03448 | 10.1021__jacs.5c03448_94c2c69f |
| 14 | 10.3390/ijms23169073 | 10.3390__ijms23169073_752247dd |
| 15 | 10.1038/s41467-022-30541-y | 10.1038__s41467-022-30541-y_c281079f |
| 16 | 10.1038/s42004-020-00401-1 | 10.1038__s42004-020-00401-1_fe46d7fc |
| 17 | 10.1039/d0sc01687j | 10.1039__d0sc01687j_807057ba |
| 18 | 10.1107/s2052520625009618 | 10.1107__s2052520625009618_e9f926a7 |
| 19 | 10.1107/s205225251701096x | 10.1107__s205225251701096x_74c285ed |
| 20 | 10.1039/d3sc06800e | 10.1039__d3sc06800e_55fb2b25 |
| 21 | 10.1021/acs.cgd.5c01295 | 10.1021__acs.cgd.5c01295_bf256b6f |
| 22 | 10.1039/c8ra10031d | 10.1039__c8ra10031d_8916aa0c |
| 23 | 10.1038/ncomms8793 | 10.1038__ncomms8793_302bdb4c |
| 24 | 10.1038/s41467-021-22685-0 | 10.1038__s41467-021-22685-0_8b6567f5 |
| 25 | 10.1038/s41598-025-07051-0 | 10.1038__s41598-025-07051-0_48958411 |
| 26 | 10.1021/jacs.4c05559 | 10.1021__jacs.4c05559_d82aa5a4 |
| 27 | 10.1021/jacsau.3c00059 | 10.1021__jacsau.3c00059_aaf27fcc |
| 28 | 10.1039/d3ra05713e | 10.1039__d3ra05713e_0177176e |
| 29 | 10.3390/cryst7070224 | 10.3390__cryst7070224_b0045724 |
| 30 | 10.1038/s41467-022-33925-2 | 10.1038__s41467-022-33925-2_04f1c27f |
| 31 | 10.3390/pharmaceutics15061747 | 10.3390__pharmaceutics15061747_790b78e8 |
| 32 | 10.3390/min9060373 | 10.3390__min9060373_6f9b6681 |

### Come dividere il lavoro

- Al massimo 3 sottoagenti alla volta, 5 articoli ciascuno, in due ondate:
  - **prima ondata**, articoli 1–15: il primo agente prende 1, 4, 7, 10, 13, il secondo 2, 5,
    8, 11, 14, il terzo 3, 6, 9, 12, 15;
  - **seconda ondata**, articoli 16–30, divisi allo stesso modo, solo quanti ne permette il
    budget (sotto);
  - 31 e 32 sono riserve, se avanza budget.
- Ogni agente legge linee guida, istruzioni e schema UNA volta, all'inizio, non per ogni
  articolo.
- Passa a ogni agente la sezione «Aggiornamento del 2026-10-23» di `CLAUDE.md` per intero e le
  regole qui sotto.

### Regole (come nel giro 03)

- **Gruppi funzionali**: `gruppi_coinvolti` negli eventi e `motivi_hb` nelle forme si
  compilano OGNI volta che il testo descrive legami a idrogeno, sintoni, contatti (alogeno,
  π) o conformazioni che cambiano, o restano, fra A e B, con la frase che lo dice. Mai dedotti
  dalle figure o dalla chimica: solo dal testo.
- Per ogni forma con una struttura scrivi refcode o CCDC **se il testo li riporta**: servono a
  collegare la forma al CSD. Mai a memoria. Un elenco di CCDC in ordine di datablock si
  attribuisce con `ccdc_dedotto`, come nel giro 03.
- Dopo ogni articolo rifai tu `python3 -m tp.verifica estrazione/cloud/<file>.json`, poi commit
  e push.
- Gli **avvisi** («il numero c'e' ma non accanto a ...») non respingono niente: correggi solo se
  la citazione e' davvero sbagliata, non spendere giri per farli sparire. Il verificatore e'
  aggiornato: «0.942 (9) GPa» e «365-nm» ora passano.
- Alla fine scrivi `rapporti/giro_04.md`, corto: la tabella degli esiti per DOI, i token per
  agente e al massimo 3 proposte nuove (non ripetere quelle dei rapporti precedenti).
- Niente script di controllo in piu'.

## Budget

- Tetto: **3,0 milioni di token** in tutto, tuoi e degli agenti, contati come nei rapporti
  precedenti.
- Finita la prima ondata, somma i token. Nella seconda assegna solo gli articoli che ci stanno,
  contando 100 000 token ad articolo e 100 000 di margine per te: (3,0 milioni − totale − 0,1
  milioni) / 0,1 milioni articoli, nell'ordine della tabella, divisi fra i 3 agenti.
- Appena il totale supera 3,0 milioni non assegnare articoli nuovi: gli agenti finiscono e
  salvano quello in corso, tu scrivi il rapporto, fai commit e push e ti fermi.
