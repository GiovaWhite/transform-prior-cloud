# Giro 04 — 32 articoli estratti (schema v1.4, solo `estrazione/cloud/`)

Estratti gli articoli 1–32 di `compiti/giro_04.md`, nell'ordine dato, da sette sottoagenti: due ondate da tre agenti (G1: 1, 4, 7, 10, 13; G2: 2, 5, 8, 11, 14; G3: 3, 6, 9, 12, 15; G4: 16, 19, 22, 25, 28; G5: 17, 20, 23, 26, 29; G6: 18, 21, 24, 27, 30) e, con il budget avanzato, un settimo agente (G7) per le due riserve 31 e 32. Ogni agente ha verificato, committato e spinto un articolo alla volta; a fine ondata ho rifatto `tp.verifica` sul solo file di ciascuno (stesso esito, nessuna modifica mia ai file). Numeri della tabella ricalcolati da me dai file. «Quasi» = accettato con un avviso. Nessun formato extra.

## Esiti per DOI

| # | DOI | eventi (avv./parz./non avv.) | per via | prep. | rel. | mol. | forme con struttura* | eventi con gruppi | forme con motivi H | verifica (acc./quasi/resp.) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.1021/jacs.3c14800 | 7 (6/0/1) | termica 6, luce 1 | 4 | 1 | 1 | 2/2 | 3 | 0 | 7/0/0 |
| 2 | 10.1021/acs.cgd.9b01281 | 7 (5/0/2) | termica 7 | 5 | 1 | 1 | 0/3 | 1 | 2 | 2/5/0 |
| 3 | 10.1038/s41467-019-11612-z | 11 (7/1/3) | termica 8, meccanica 3 | 3 | 1 | 0 | 0/2 | 2 | 2 | 11/0/0 |
| 4 | 10.1021/jacs.4c09222 | 12 (11/0/1) | termica 11, solvente 1 | 5 | 0 | 1 | 0/5 | 2 | 3 | 12/0/0 |
| 5 | 10.1021/jacs.4c17448 | 8 (7/0/1) | termica 7, desolvatazione 1 | 3 | 0 | 1 | 0/3 | 3 | 2 | 8/0/0 |
| 6 | 10.1021/acs.cgd.5c01210 | 14 (12/0/2) | termica 14 | 3 | 0 | 0 | 1/9 | 6 | 8 | 14/0/0 |
| 7 | 10.1107/s2052252525011601 | 18 (15/0/3) | pressione 13, termica 4, luce 1 | 4 | 1 | 1 | 10/10 | 7 | 8 | 16/2/0 |
| 8 | 10.1107/s2052252523001197 | 14 (13/0/1) | solvente 10, termica 4 | 3 | 3 | 1 | 3/7 | 0 | 0 | 10/4/0 |
| 9 | 10.3390/molecules24112174 | 16 (7/3/6) | pressione 16 | 4 | 2 | 1 | 1/6 | 4 | 6 | 16/0/0 |
| 10 | 10.1038/srep29610 | 15 (9/0/6) | termica 15 | 7 | 0 | 0 | 2/9 | 2 | 1 | 15/0/0 |
| 11 | 10.1038/s41467-017-02549-2 | 7 (7/0/0) | termica 7 | 1 | 0 | 1 | 2/3 | 1 | 2 | 7/0/0 |
| 12 | 10.1021/acs.cgd.7b01065 | 17 (12/0/5) | termica 17 | 5 | 2 | 2 | 0/7 | 2 | 6 | 14/3/0 |
| 13 | 10.1021/jacs.5c03448 | 4 (3/0/1) | termica 4 | 3 | 1 | 1 | 2/3 | 1 | 0 | 4/0/0 |
| 14 | 10.3390/ijms23169073 | 7 (7/0/0) | termica 7 | 2 | 0 | 1 | 2/2 | 2 | 0 | 7/0/0 |
| 15 | 10.1038/s41467-022-30541-y | 2 (2/0/0) | termica 2 | 2 | 0 | 0 | 0/2 | 1 | 2 | 2/0/0 |
| 16 | 10.1038/s42004-020-00401-1 | 21 (21/0/0) | termica 14, altro 7 | 16 | 5 | 1 | 9/10 | 11 | 7 | 13/8/0 |
| 17 | 10.1039/d0sc01687j | 12 (11/0/1) | termica 8, desolvatazione 1, altro 3 | 5 | 0 | 1 | 1/10 | 3 | 2 | 12/0/0 |
| 18 | 10.1107/s2052520625009618 | 16 (14/0/2) | termica 16 | 2 | 0 | 0 | 1/4 | 6 | 2 | 13/3/0 |
| 19 | 10.1107/s205225251701096x | 12 (7/1/4) | pressione 7, termica 5 | 4 | 2 | 2 | 3/6 | 6 | 5 | 12/0/0 |
| 20 | 10.1039/d3sc06800e | 5 (5/0/0) | termica 4, meccanica 1 | 1 | 0 | 1 | 2/2 | 2 | 1 | 5/0/0 |
| 21 | 10.1021/acs.cgd.5c01295 | 5 (3/0/2) | pressione 3, termica 2 | 2 | 1 | 1 | 2/4 | 2 | 2 | 5/0/0 |
| 22 | 10.1039/c8ra10031d | 3 (3/0/0) | termica 3 | 1 | 0 | 1 | 2/2 | 2 | 1 | 3/0/0 |
| 23 | 10.1038/ncomms8793 | 3 (3/0/0) | termica 2, pressione 1 | 6 | 1 | 1 | 2/3 | 3 | 3 | 3/0/0 |
| 24 | 10.1038/s41467-021-22685-0 | 8 (8/0/0) | solvente 5, desolvatazione 3 | 5 | 0 | 2 | 0/9 | 3 | 5 | 8/0/0 |
| 25 | 10.1038/s41598-025-07051-0 | 9 (7/0/2) | termica 7, altro 2 | 1 | 0 | 1 | 2/4 | 4 | 1 | 9/0/0 |
| 26 | 10.1021/jacs.4c05559 | 10 (9/0/1) | termica 10 | 2 | 5 | 1 | 0/6 | 8 | 6 | 10/0/0 |
| 27 | 10.1021/jacsau.3c00059 | 13 (6/0/7) | termica 13 | 4 | 0 | 1 | 0/11 | 1 | 0 | 13/0/0 |
| 28 | 10.1039/d3ra05713e | 7 (6/1/0) | termica 5, desolvatazione 1, altro 1 | 10 | 3 | 2 | 6/7 | 6 | 5 | 7/0/0 |
| 29 | 10.3390/cryst7070224 | 6 (6/0/0) | termica 6 | 2 | 0 | 0 | 4/4 | 4 | 4 | 6/0/0 |
| 30 | 10.1038/s41467-022-33925-2 | 9 (7/0/2) | termica 9 | 4 | 0 | 1 | 0/9 | 1 | 3 | 9/0/0 |
| 31 | 10.3390/pharmaceutics15061747 | 20 (13/1/6) | termica 12, solvente 7, meccanica 1 | 8 | 2 | 2 | 5/10 | 4 | 3 | 20/0/0 |
| 32 | 10.3390/min9060373 | 8 (2/2/4) | termica 6, desolvatazione 2 | 1 | 1 | 1 | 2/3 | 2 | 2 | 8/0/0 |

\* Forme con refcode, CCDC o `strutture[]` su totale forme dell'articolo. Dove è 0 o basso il testo non dà numeri attribuibili alle forme: elenchi o intervalli di CCDC senza attribuzione restano a livello di articolo (2, 3, 10, 17, 18, 19, 25, 27), 12 e 15 rimandano al supplementare, gli altri non danno codici nel testo. Attribuzioni per ordine con `ccdc_dedotto` / `refcode_dedotto`: 7, 8, 11, 14; refcode ricostruiti dalla riga di tabella: 16. Nel 32 (acido urico, nonostante il titolo «minerali») le 13 strutture sono attribuite una per una dalla Tabella 1, con le etichette UA/UAD ricostruite dal PDF.

**Totale:** 326 eventi (254 avvenuti, 9 parziali, 63 negativi), 128 preparazioni, 32 relazioni, 31 molecole, 177 forme, 105 eventi con `gruppi_coinvolti`, 94 forme con `motivi_hb`. Tutti gli articoli pertinenti. **Nessun respinto**; 25 «quasi» (301 accettati puliti). Per via: termica 235, pressione 40, solvente 23, altro 13, desolvatazione 8, meccanica 5, luce 2. I negativi sono il 19 % degli eventi (27 % nel giro 03).

I «quasi» sono tutti avvisi del controllo unità (`°C/min` in tabella, «deg», caratteri di controllo al posto di ° e −, «GPa» mancante nella frase): 2 (5 «quasi»), 7 (2), 8 (4), 12 (3), 16 (8), 18 (3). Nessuna citazione sbagliata.

## Token

Come nei rapporti precedenti: per me il contatore della sessione, per ogni agente il totale che riporta il sistema a fine lavoro (confermato dai loro stessi conti, ±3 %).

| voce | articoli | token | per articolo |
|---|---|---|---|
| G1 | 5 (1, 4, 7, 10, 13) | 391 465 | 78 mila |
| G2 | 5 (2, 5, 8, 11, 14) | 346 257 | 69 mila |
| G3 | 5 (3, 6, 9, 12, 15) | 461 738 | 92 mila |
| G4 | 5 (16, 19, 22, 25, 28) | 321 950 | 64 mila |
| G5 | 5 (17, 20, 23, 26, 29) | 317 988 | 64 mila |
| G6 | 5 (18, 21, 24, 27, 30) | 314 030 | 63 mila |
| G7 (riserve) | 2 (31, 32) | 270 799 | 135 mila |
| sottoagenti, totale | 32 | 2 424 227 | 76 mila |
| io (letture, prompt, verifiche, commit, rapporto) | — | ~0,24 milioni | — |
| **totale** | | **~2,66 milioni** | |

Sotto il tetto di 3,0 milioni (margine ~0,34 milioni). Dopo la prima ondata il totale era 1 366 166 (agenti 1 199 460 + io 166 706): (3,0 − 1,366 − 0,1) / 0,1 = 15,3, quindi tutti i 15 articoli 16–30. A fine seconda ondata il totale era ~2,38 milioni: con il margine rimasto, su richiesta di usare tutto quello che si poteva fare, ho lanciato G7 per le riserve 31 e 32 con un tetto di 350 mila token (usati 271 mila), fuori dalla formula del compito perché era già chiusa. Ogni agente spende ~105–114 mila token nella lettura iniziale (linee guida, istruzioni, schema, esempio): 7 × ~108 mila ≈ 0,76 milioni del totale; il costo marginale di un articolo è ~50 mila, la metà dei 100 mila usati per il calcolo (G7: 107 mila per il 31, 50 mila per il 32). Il tetto per agente della seconda ondata (~500 mila) non è mai servito (massimo 322 mila). Con questo giro la tabella è finita: non restano articoli.

All'avvio il classificatore della modalità Auto ha dato più volte un errore transitorio su Bash e Agent (anche un agente l'ha segnalato): nessun effetto sul lavoro, ripreso senza aggirarlo.

## Proposte nuove per la v1.5 (non ripetono i rapporti precedenti; le frasi sono ricontrollate sul testo)

1. **Una transizione, più letture: regola e campi.** Le linee guida dicono «un evento per tecnica se le temperature differiscono», l'aggiornamento del 23/10 dice che «la stessa prova vista con una seconda tecnica» non è un evento nuovo, e gli agenti hanno scelto in modo diverso (G3 ha tenuto un evento solo nel #6, G1, G4 e G6 ne hanno scritti due o tre per tecnica nei #1, #18, #28). Frasi: «Upon warming, a phase transition occurs at about 341 K» (VT-PXRD del #18, mentre il DSC dello stesso passaggio dà 336/321 K) e, nel #6, «due to the heating rate differences between the DSC (10 K min–1) and PXRD measurements (0.16 K min–1)». Proposta: separare solo se l'esperimento è distinto (altro campione, altra velocità, altra corsa) e mettere le altre letture della stessa transizione in `misure_alternative: [{tecnica, temperatura, velocita, citazione}]` nello stesso evento; aggiungere `osservazioni.isteresi` (K) con `definita_su` e `temperatura.tipo: punto_medio_isteresi` («based on the midpoints of thermal hysteresis», #17).
2. **Relazioni con più citazioni e base del confronto.** Il verificatore respinge `temperatura_transizione` se il numero non è nell'unica `citazione` (stringa) della relazione. Nel #26: «The transition II/III is enantiotropic» sta in una frase e «but at 104 °C, there is transition to a new crystal phase» in un'altra; «The monotropic transition V → II» dà il verso ma non c'è un campo per esso. Proposta: `citazioni` come lista (come negli eventi) o una citazione dentro `temperatura_transizione`; `verso_monotropo: {da, a}`; `base` (calcolo, punto_fusione, conversioni_osservate, solubilita, sospensione), perché nel #16 due ordini di stabilità opposti (energia reticolare calcolata contro calore di fusione) oggi convivono senza etichetta.
3. **Parametri della leva senza campi.** Campo elettrico: «An electric field was applied along the polar c direction» (#25) e le fasi IV e V indotte dal campo nel #17 finiscono in `condizioni.altro` come testo. Protocollo di pressione: «The structural transformation was observed at different pressures depending on the pressure-increasing protocol» (#7: la stessa transizione a 2.60, 3.4, 3.51 e 4.9 GPa dà quattro eventi non collegati). Proposta: `condizioni.campo` {tipo, intensita, frequenza, forma_onda, direzione} e `condizioni.protocollo` {passo, tempo_per_punto, tempo_sopra_soglia}, con `confronta_con: [id eventi]` quando la soglia dipende dal protocollo.

Segnalate dagli agenti e non riportate qui per il limite di tre (solo titoli, dettagli nelle loro note e nei campi `note`/`conflitto` dei JSON): sottovia `solvente/evaporazione` (#8); competizione fra solventi da una sola forma (#8); transizione rilevata da SHG, fluorescenza o movimento (#11); fasi modulate e lock-in (#7); danno da fascio di elettroni come artefatto (#1); coesistenza stabile di due fasi nello stesso cristallo (#3); negativo chimico senza forma di partenza, `da: tutte` (#9); seme e nucleazione incrociata come leva (#16); sostituzione isotopica come leva confrontabile (#17); eventi «simili» a quelli di un altro composto (#27); proprietà calcolate per forma (#16, #28); perdita di cristallinità senza prodotto identificato, oggi forzata su `amorfo`/`decomposizione`/`ignota` («it loses crystallinity», #32); minerali con una molecola organica discreta (uricite, tinnunculite: pertinenti, ma le linee guida escludono «minerali») e preparazioni da campioni naturali (`metodo: naturale`, #32).
