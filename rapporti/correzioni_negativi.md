# Correzioni dei negativi — fase A del giro 02

Articoli già estratti in `estrazione/cloud/` (esclusi 10.1021/cg101162a e 10.1248/cpb.51.807). Per ognuno: grep delle frasi negative su `testi/<file>.md`, lettura del paragrafo, eventi `non_avvenuta` aggiunti dove nessun evento copriva già la frase (id successivo all'ultimo).

## Articoli senza aggiunte

Per questi articoli ho cercato nel testo le parole indicate e riletto il paragrafo di ogni frase sulle forme solide: tutte erano già coperte da un evento (o non riguardano forme solide dell'articolo). Frasi valutate e non trasformate in eventi, con il motivo:

- **10.3390/cryst10080667** — nessuno. «no changes of 1 were observed in DCM solutions» (riga 31) riguarda una soluzione, non un solido; «no additional exothermic and endothermic events or changes in XRPD, which could indicate the formation of potential intermediary monohydrate or hemihydrate phases» è già in E3 ed E9 (`esito_dettaglio: senza_intermedio`); gli intermedi non sono forme dell'articolo.
- **10.3390/cryst11040342** — nessuno. Coperti da E19–E22 (solvati stabili nell'acqua madre / a bassa T), E30 e E32 (0–43 % RH e 0 % RH), E33–E35 e E41 (atmosfere di cloroformio).
- **10.1021/acs.cgd.1c00886** — nessuno. Coperti da E6, E11, E28, E34, E40, E49 («stable from 100 K to rt»), E29/E35 (forno a 30 K sotto il punto di fusione), E33 (non si idrata), E48 (KOH), E18 (il sale non ricristallizza).
- **10.1002/chem.201404693** — nessuno. «remain unchanged between room temperature and 120 °C» è E2; «no weight loss ... up to 80 °C» (TGA, riga 102) è la stessa prova dell'intervallo più ampio di E2 (termomicroscopia) e non diventa un evento (regola 4).
- **10.1107/s2053229621013164** — nessuno. «no solvent-based processes were identified that provided single-phase Polymorph A or Polymorph B» e il metodo del solvato di metanolo sono preparazioni, non eventi.
- **10.1248/cpb.c22-00817** — nessuno. Coperti da E4 (campione non asciugato: resta monoidrato), E6 (TG del campione asciugato senza perdita), E14 («remained unchanged»).
- **10.3390/pharmaceutics15041196** — nessuno. Coperti da E9 («No mass loss ... below the melting point»), E15–E25 (stabilità a 60 °C, 90 % RH, luce) e E27–E31 (DVS e tampone).
- **10.1107/s2052252525006785** — nessuno. «Gentler conditions were also tested, but they resulted in only partial desolvation» (riga 90) non dice per quali solvati né a quali condizioni: non c'è un evento estraibile (E1 lo annota). I negativi dell'acetone e del diossano sono E6 ed E7; «no phase transitions were observed» dopo la dissoluzione è E11/E12.
- **10.3390/cryst13081241** — nessuno. «Form III was obtained stably in mixed solvents ... without transforming to Form I» (riga 171) è una cristallizzazione rapida con PXRD immediata: è già in due preparazioni con la cautela degli autori in `note`, non una prova di stabilità di un solido; non aggiunto. «no significant weight loss before decomposition» è in E10–E12.
- **10.1021/acs.cgd.3c01011** — nessuno. Le trasformazioni dichiarate sono tutte E1–E16; «the transformation ... does not affect the resulting crystal habit» riguarda il habitus, non la forma.

- **10.1107/s2052252517004043** — nessuno. La macinazione con metanolo è la sintesi chimica del composto A, non una trasformazione di forma. Coperti: E20–E23 (B e C senza risposta termica), E24 (TGA senza perdita di massa), E17 (sospensione competitiva).
- **10.1039/c7ce00651a** — nessuno. Nel DVS «Two samples show a mass change greater than 1 %» (LON-IMID.EtOAc 1.9 %, LON-HALO.3H2O 2.6 %): che le altre sei forme non cambino è dedotto dal silenzio (il testo non dice «nessun cambio di forma»), quindi non aggiunto. Coperti: E25–E28 (sospensione, «stable samples»), E29–E35 (40 °C / 75 % RH, «all samples appear stable with the exception of the imidazole salt solvate»).
- **10.1021/acs.cgd.3c01313** — nessuno. «all the anhydrous phases are stable towards re-hydration» è E17–E25 (tre prove per tre anidri); «stable from r.t to melting» è E12; il mancato ritorno A2 → A1 è E10.
- **10.3390/pharmaceutics17020152** — nessuno. «No significant structural changes occurred ... slightly more amorphous» e «do not undergo phase transitions» sono E17–E20.
- **10.22159/ijpps.2017v9i10.20795** — nessuno. «consistency in DSC and PXRD pattern of the form H, B and S» sono E10–E12; Form MS → B è E9.
- **10.1021/acs.cgd.2c00035** — nessuno. «could not be obtained as phase-pure solids ... neither by milling nor by scaling up» è già in due preparazioni `non_ottenuta` (F19, F21); «No change in the XRPD pattern was observed, when the cocrystal was slurried for 48 h in methanol» è E10; il ternario con seb che non si forma per macinazione è E6.
- **10.1107/s2052252522010983** — nessuno. Gli esiti di Tabella 4 e 5 (10 giorni a 90 % RH, 333 K, sospensione in acqua e in HCl diluito) sono già un evento per forma: E25–E37, E39–E44, E51.
- **10.3390/ijms24043305** — nessuno. «remained unaltered» (cinque sali in acqua) è E12–E16; pH 1.2 è E17–E21; 40 °C / 75 % RH per 2 mesi è E22–E28; «integrity of the molecular salts below ...» è E42–E47.
- **10.3390/pharmaceutics16050623** — nessuno. «No significant changes were recorded over time» è E19–E22 (GW-1, GW-2, GW-3, GW-5; GW-4 non è stato riottenuto e non è nella prova).
- **10.1021/acs.cgd.5c00860** — nessuno. I negativi del testo («was not observed as a product of methanol-assisted grinding», «no TPH·PMLA·MeOH 2:1:2 phase was observed», «inhibition of the cocrystallization process» a 175 °C, «stable up to 203 / 205 °C», «remains stable» sotto 45 °C) sono E9, E24, E18, E27, E30, E31, E37.

Segnalazioni fuori dal compito (nessuna modifica fatta):
- 10.1107/s2052252525006785, riga 64: «a high tendency toward partial desolvation during even minimal handling» (VEN EA filtrato e asciugato in azoto prima di TGA e NMR). È un evento positivo (desolvatazione parziale, flusso di gas) che non c'è; non è un negativo e la fase A riguarda solo i negativi.
- 10.3390/cryst11040342, E18 (SCHCl3 → SCHCl3-H2O): è `umidita` / `assorbimento` perché il solvato «incorporates one water molecule». Il punto 3 della sezione nuova ammetterebbe `desolvatazione` / `aria` per un solvato che cambia fuori dall'acqua madre, ma qui il testo dice che il cloroformio resta e entra l'acqua, quindi l'ho lasciato com'è.

## Articoli con aggiunte

- **10.3390/cryst10110996** — aggiunto E21 (Lor-Oxa CAB → ignota, `non_avvenuta`, termica / riscaldamento, TGA, T sotto 150 °C): «The TGA profile of Lor-Oxa CAB (Figure 5a) showed negligible weight loss below 150 °C, suggesting acceptable thermal stability.» È il lato «sotto soglia» di E3 (perdita significativa «at ≥150 °C»); l'`E3` la citava solo nella nota. Certezza `media` («negligible» e non «nessuna»).

## Esito della fase A

21 articoli controllati; 1 evento aggiunto in totale (E21 di 10.3390/cryst10110996, `accettato` dal verificatore, nessun respinto). Gli altri 20 articoli coprivano già ogni frase negativa con un evento (o la frase non riguarda un cambio di forma dell'articolo). Nessun errore evidente da correggere.

Come ho cercato: `grep -n -i` con le parole del compito, più (dal terzo articolo in poi, e poi ripassato sui primi dieci) «negligible», «no significant», «no weight/mass loss», «up to N °C/K/%», «below N °C/K/%», perché le soglie del punto 2 («stable up to», «only below») non sempre hanno le parole del compito. Il ripasso ha fatto emergere l'unico mancante (la TGA «negligible weight loss below 150 °C»).

Token (contatore della sessione, nessun sottoagente in questa fase): lettura iniziale di CLAUDE.md, compiti, linee guida, istruzioni e schema circa 139 mila (a carico dell'intera sessione); fase A circa 160 mila, cioè circa 7.6 mila per articolo (da 5 a 12 mila secondo la lunghezza del testo). Entro il tetto di circa 500 mila della fase A.
