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

## Articoli con aggiunte

- **10.3390/cryst10110996** — aggiunto E21 (Lor-Oxa CAB → ignota, `non_avvenuta`, termica / riscaldamento, TGA, T sotto 150 °C): «The TGA profile of Lor-Oxa CAB (Figure 5a) showed negligible weight loss below 150 °C, suggesting acceptable thermal stability.» È il lato «sotto soglia» di E3 (perdita significativa «at ≥150 °C»); l'`E3` la citava solo nella nota. Certezza `media` («negligible» e non «nessuna»).

