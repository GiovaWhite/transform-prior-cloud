# Blocco 08 (schema v1.4, solo estrazione principale) e conti del giro 02

**Il blocco è incompleto: 2 articoli su 5.** Ho fermato il lavoro per il budget (vedi in fondo). Fatti: `10.1002/chem.202004072` e `10.1021/acsomega.0c03531`. **Non fatti:** `10.3390/molecules28052296`, `10.1021/acs.cgd.3c00641`, `10.1002/anie.202114985`; per questi tre non c'è nessun file in `estrazione/cloud/`. L'agente E aveva letto il testo di `cgd.3c00641` prima che lo fermassi, senza scrivere niente: quella lettura è costo perso.

Dopo ogni articolo ho rifatto `tp.verifica` sul solo file, poi commit e push. Numeri ricalcolati da me dai file.

| DOI | pert. | eventi (avv./parz./non avv.) | per via | prep. | rel. | molecole | verifica (acc./quasi/resp.) |
|---|---|---|---|---|---|---|---|
| 10.1002/chem.202004072 | sì | 20 (14/1/5) | desolvatazione 15, termica 5 | 5 | 0 | 2 | 20/0/0 |
| 10.1021/acsomega.0c03531 | sì | 4 (3/0/1) | desolvatazione 2, termica 2 | 2 | 0 | 1 | 4/0/0 |

Note:
- **chem.202004072** ([FeL2]X2, spin-crossover; agente F): fasi 1 → 2 → 3 del [BF4]2·xMeNO2 letta da PXRD, SQUID, TGA e vuoto; cinque negativi («The phase 2 powder pattern is retained with minor changes upon cooling from 360 to 223 K», nessuna conversione a 1 K/min, tentativi in situ falliti, SCO senza cambio di fase nel polimorfo Pc e nel solvato acetonico). Incoerenze: x ≈ 2.3 nel testo e 2.34 in microanalisi; perclorato acetonico 0.2 H2O nel cristallo contro n = 0.5 in microanalisi; lettere greche perse dal PDF («The - and - forms»).
- **acsomega.0c03531** (drospirenone, solvato di DMSO; agente D): C → amorfo per desolvatazione in TG-MS e DSC (certezza media: gli autori scrivono prima «might transform … to amorphous», poi «confirmed»); nessun altro picco DSC fra 30 e 230 C per il solvato (negativo). Parte sperimentale («placed in a refrigerator … at 10 °C») e Risultati («obtained … by slow evaporation») divergono sulla preparazione.

## Proposte nuove per la v1.5 (non ripetono P1–P24, Q1–Q17 né quelle dei blocchi 05–07)

1. **Magnetometria (SQUID) come tecnica** (chem.202004072). «Repeated scanning of the sample between 5 and 370 K at 5 Kmin−1 revealed two spin transition regimes»: tutta la storia delle fasi 1 → 2 → 3 è letta dalla suscettività magnetica e `tecniche` non ha una voce (usato `altro`). Proposta: `magnetometria` fra le tecniche e una riga che dica quando una fase intermedia vista solo per via magnetica può essere una forma.
2. **Prodotto identificato solo dalla microanalisi, passo a due leve** (chem.202004072). «After drying in vacuo at 80 °C for 16 hrs, followed by exposure to air, the same crystals analysed with a monohydrate formulation»: perdita di solvente più presa d'acqua, forma nota solo dalla formula. Proposta: un campo `identificata_da` (o `fonte_prodotto`) sull'evento e una regola per i passi con due leve in cui il prodotto è un idrato.
3. **«Nessun cambio di fase» con spin-crossover** (chem.202004072). «a high Z’ crystal undergoing stepwise SCO without a crystallographic phase change»: le linee guida non dicono se sia un evento. Proposta: estrarlo come `non_avvenuta` quando c'è un'osservazione cristallografica, con `esito_dettaglio: nessun_cambio_di_fase_cristallografico` e un campo per la T del fenomeno non strutturale (T½ = 255 ± 5 K, oggi in `testo`).
4. **`gruppo_spaziale_dedotto` senza il perché** (chem.202004072). «triclinic, P1 , Z = 2» (il PDF perde la barra di P-1): l'appoggio c'è nel testo («crystallographic inversion center») ma non c'è un campo per dirlo. Proposta: `dedotto_da` (testo breve) o `note` obbligatoria quando `gruppo_spaziale_dedotto` è vero.
5. **Campione «annealed» non nominato come partenza e numero di cicli** (chem.202004072). «The measurement was repeated using a different annealed sample of 1[BF4]2·xMeNO2 … the composition of this sample was unchanged after six thermal cycles at 1 Kmin‒1». `tempo.tipo: ciclo` non porta il numero di cicli (sei a 1 K/min, nove scansioni a 5 K/min, scritti in `condizioni.altro`). Proposta: campo per il numero di cicli e `da_dedotto` con `forme_possibili` per il campione trattato.

## Altre segnalazioni raccolte dagli agenti (non entrano nelle 5 per blocco)

Una riga ciascuna; le frasi sono nelle note degli agenti, non le ho riverificate tutte sul testo.
- Valore presente solo in una figura del corpo (non nel supplementare): flag `valore_in_figura` (advs.202502692, Fig. 1F).
- Ospite non stechiometrico con limite e dipendente dal processo: `ospite.limite: sotto`, `ospite.dipende_da` («with x and y < 1», cgd.4c00279).
- Sottovia `desolvatazione / recipiente_chiuso` con `condizioni.atmosfera_ospite` (la CO2 stabilizza il solvato in vial chiusa, cgd.4c00279).
- `a` dei negativi: conta solo la frase o anche il contesto della sezione? (`a_atteso`, cgd.4c00279).
- `fonte_dati: non_detta` e flag `assegnazione_per_ordine` per numeri citati senza dire se misurati qui e per picchi DSC assegnati nell'elenco (cgd.1c01509).
- Gel e xerogel di sali, non cristallini (cgd.1c01509: «Tgel increases with increasing gelator concentration»): insieme alle mesofasi del blocco 06.
- Graph set spezzato dal PDF: `motivi_hb.graph_set` e `notazione_ricostruita` (c6ce00872k).
- `delta` con segno ed `incertezza` / `direzione` nelle grandezze: il verificatore respinge `delta: -7.7` perché il segno non è nella citazione (acsomega.1c04866, «7.7 °C lower than that of the initial crystal»).
- Fase vista in PXRD senza struttura: forma tra parentesi quadre; fase solo inferita dal DSC: `ignota` con `da_evento` (cgd.2c00861, cryst12040550).
- Stechiometria scritta come sequenza di colonne («2:1:2») e solventi in sequenza nelle preparazioni (molecules25030449).

## Conti dei token

Il contatore è quello della sessione per me e quello riportato a fine lavoro per ogni sottoagente. Non so se i due misurino la stessa cosa (cache, riletture), come già scritto nei rapporti precedenti. Dei sottoagenti ho il totale per agente, non per articolo: la media per articolo qui sotto include la lettura iniziale delle linee guida e dello schema, che stimo (non misurata) in circa 45 mila per agente.

| voce | token |
|---|---|
| Lettura iniziale (CLAUDE.md, compiti, linee guida, istruzioni, schema, esempio) | ~139 mila |
| Fase A, 21 articoli, io da solo | ~160 mila (circa 7.6 mila per articolo; da 5 a 12 mila) |
| Fase B, coordinamento mio (prompt, verifiche, commit, note, 4 rapporti) | ~140 mila |
| Fase B, sottoagenti | 2 116 557 |
| **Totale** | **~2.56 milioni** |

Sottoagenti (Fase B):

| agente | articoli estratti | token | per articolo (media) |
|---|---|---|---|
| A | 3 (blocchi 5–6) | 317 950 | 106 mila |
| B | 4 (blocchi 5–6) | 317 277 | 79 mila |
| C | 3 (blocco 6) | 449 571 | 150 mila |
| D | 4 (blocchi 7–8) | 430 306 | 108 mila |
| E | 1 (blocco 7) + lettura di un secondo, non estratto | 285 566 | 286 mila |
| F | 2 (blocchi 7–8) | 315 887 | 158 mila |

Media dei sottoagenti: circa 125 mila per articolo estratto (17 articoli); considerando che C ha avuto i tre testi più lunghi (46, 55 e 66 mila caratteri) e D un articolo con 59 eventi, il costo cresce con la lunghezza del testo e con il numero di eventi.

**Budget.** Ho superato i 2,5 milioni: quando è arrivato il conto finale dell'ultimo agente (D) il totale era circa 2,54 milioni, e con i rapporti dei blocchi 07 e 08 arriva a circa 2,56. Non avevo il conto dei sottoagenti in corso, solo una stima basata sugli agenti già finiti (circa 108 mila per articolo): con quella stima, a metà del secondo giro, mi aspettavo di restare intorno a 2,5 milioni solo togliendo tre articoli. Ho quindi fermato E dopo il primo articolo e F dopo il secondo (ordine dei blocchi, prima il 7, poi il 8), lasciando D con i suoi quattro. Con il conto reale a posteriori il margine era più stretto di quanto stimato: l'eccesso è di circa 60 mila token (2,4 %), dovuto al costo di E (286 mila per un solo articolo estratto).

Stato finale del giro: fase A completa (21 articoli, 1 evento aggiunto); fase B: blocchi 5, 6 e 7 completi (15 articoli), blocco 8 con 2 articoli su 5. Totale fase B: 17 articoli, 331 eventi (250 avvenuti, 3 parziali, 78 negativi), 127 preparazioni, 15 relazioni, 46 molecole; nessun respinto, 40 «quasi» (39 nel blocco 06, 1 nel blocco 07), tutti per unità nell'intestazione di tabella o per il simbolo «ᵒC». Per riprendere dal punto in cui mi sono fermato: blocco 8, gli articoli da fare sono `molecules28052296`, `cgd.3c00641` e `anie.202114985`.
