# Blocco 06 (schema v1.4, solo estrazione principale)

Cinque articoli, estratti da tre sottoagenti (A: 1, B: 1, C: 3 — gli inositoli, l'urea con l'acido nitroisoftalico e il BTBT). Dopo ogni articolo ho rifatto `tp.verifica` sul solo file, poi commit e push. Numeri ricalcolati da me dai file. «Quasi» = accettato con avviso di unità. Nessun formato extra.

| DOI | pert. | eventi (avv./parz./non avv.) | per via | prep. | rel. | molecole | verifica (acc./quasi/resp.) |
|---|---|---|---|---|---|---|---|
| 10.3390/molecules25030449 | sì (solo fusioni) | 10 (10/0/0) | termica 10 | 7 | 0 | 3 | 6/4/0 |
| 10.1107/s2052252513026511 | sì | 33 (25/1/7) | termica 31, desolvatazione 2 | 9 | 0 | 5 | 18/15/0 |
| 10.1039/c6ce00872k | sì | 28 (17/0/11) | desolvatazione 18, termica 6, solvente 4 | 12 | 2 | 2 | 8/20/0 |
| 10.1021/acsomega.1c04866 | sì | 9 (7/0/2) | termica 9 | 3 | 1 | 1 | 9/0/0 |
| 10.1021/acs.cgd.5c00046 | sì | 19 (14/1/4) | termica 16, solvente 2, altro (semina) 1 | 13 | 5 | 1 | 19/0/0 |

Totale: 99 eventi (73 avvenuti, 2 parziali, 24 negativi), 44 preparazioni, 8 relazioni, 12 molecole; nessun respinto; 39 «quasi» (numeri di tabella con l'unità nell'intestazione e, in c6ce00872k, il simbolo «ᵒC», vedi sotto).

Note per articolo:
- **molecules25030449** ((–)-monophyllidin): sei polimorfi/solvati dal microscopio Kofler, solo punti di fusione (`desolvatazione_possibile`); nessuna trasformazione solido–solido e nessun negativo detto. Incoerenze: P-IV «P212121» nel riassunto ma P-IV è P1 e P212121 è P-VI; LCMS di 5 calcolato 426.29, trovato 462.46.
- **s2052252513026511** (inositoli): sette negativi, fra cui la soglia «5-D only above 57 °C» (lato opposto: 5-D → 5-E `non_avvenuta`) e «7-C … is stable at 20 °C», che contraddice «At room temperature, 7-C slowly converts to 7-A» (certezza bassa, `conflitto`). I CCDC 891302–891309 restano a livello di articolo (il supplementare non li attribuisce).
- **c6ce00872k** (urea / acido 5-nitroisoftalico): da «The selective conversion of IM1 – IM7 and CIM2 to NS1, on desolvation, rather than to NS2» ho ricavato 8 negativi (IMx → NS2) con la regola «solo in Y», certezza media; più CIM1 → NS1 non avvenuta. CCDC per ordine con `ccdc_dedotto` (l'intervallo nel testo è troncato: «1471780-147190»).
- **acsomega.1c04866** (cristallo liquido ionico): β-Cr e cold-crystal in una sola forma («we identified the β-Cr phase as the cc-Cr»); Tm1–1 123.6 °C nei Risultati contro 122.5 °C nei Metodi (tenuto il primo, `conflitto`).
- **cgd.5c00046** (ditBuC6-BTBT): eventi distinti per velocità di scansione (5, 10 e 300 °C/min); la sospensione per solvente è solo in Tabella S2, quindi l'evento Ia/I → II ha certezza bassa. Abstract («above 100 °C») e conclusioni («exceeding 138 °C») danno soglie diverse per la forma III.

## Proposte nuove per la v1.5 (non ripetono P1–P24 né Q1–Q17 né quelle del blocco 05)

1. **Mesofasi** (acsomega.1c04866). «from the initial crystal phase (α-Cr) to the liquid crystal phase (SmA) (Tm1–1: 123.6 °C) and melting from SmA to an isotropic liquid phase (Iso)». `tipo_forma` non ha una voce per la fase liquido-cristallina e le linee guida non dicono se l'arrivo in una mesofase è `a: <forma>` o `a: fuso`. Scelta fatta: SmA come forma `altro`, Iso come forma `fuso` usata solo come `da`, `a: fuso` per SmA → Iso. Proposta: `tipo: mesofase` e una riga nelle linee guida.
2. **Ospite di un cocristallo solvatato** (c6ce00872k). «7:4:2 complex of N-phenylurea, 5-nitroisophthalic acid and methanol». La regola «ospite = molecole per UNA molecola del composto principale» non vale se l'host ha due componenti alla pari. Ho messo `componenti` 7 e 4 e `ospite` 2 con `riferito_a: unita_formula`, `tipo: [cocristallo, solvato]`. Proposta: scriverlo nelle linee guida, con un esempio.
3. **Prodotti non identificati ma con nome** (c6ce00872k). «The recrystallisation peak in the DSC traces of IM1 – IM7, CIM2, NS1 and NS2 at ca. Tonset 170 ᵒC suggest conversion to the same unidentified product (UN1)»: UN1, UN2 e UN3 sono fasi distinte, con etichetta e senza struttura. Oggi `a: ignota` le confonde. Proposta: forma `tipo: non_specificato` con `non_identificata: true`, usabile come `a`; e dire che una colonna «Melt» seguita da «Recrystallisation» vale `termica / dal_fuso`.
4. **Negativi derivati e «nessun picco»** (c6ce00872k, cgd.5c00046). (a) Gli 8 negativi IMx → NS2 sono meccanici, nascono da una sola frase: per pesarli meno nell'addestramento servirebbe `derivato: true` o un `esito_dettaglio: prodotto_diverso` fisso. (b) «One possible explanation for the fact that no transition peak was observed in DSC of Form I could be that the transition is extended in a very wide range of temperatures so that the peak almost appeared flat»: «nessun picco» non è «nessuna trasformazione»; non l'ho estratto. Proposta: `esito_dettaglio: non_rilevata_dalla_tecnica`.
5. **Composto sull'evento quando `da` è ignota** (molecules25030449). «(3b, 0.142 g, 0.44 mmol, 25% yield, mp: 148 °C (dec)»: con la regola 7 (`da: ignota`) l'evento perde il legame con il composto (qui un enantiomero), che resta solo nella `note`. Proposta: un campo `composto` sull'evento, obbligatorio se `da` è ignota.

Segnalazione al codice (non è una proposta di schema): in `tp/verifica.py` la normalizzazione NFKC trasforma «ᵒ» (U+1D52) in «o», quindi «5 ᵒC min-1» diventa «5 oc min-1» e il controllo dell'unità fallisce: spiega 20 dei 28 «quasi» di c6ce00872k. Basterebbe mappare U+1D52 a «°» prima di NFKC. Non ho toccato il codice.
