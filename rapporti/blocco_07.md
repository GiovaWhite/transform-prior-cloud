# Blocco 07 (schema v1.4, solo estrazione principale)

Cinque articoli su cinque, estratti da quattro sottoagenti (D: 3 articoli, E: 1, F: 1). Dopo ogni articolo ho rifatto `tp.verifica` sul solo file, poi commit e push. Numeri ricalcolati da me dai file. «Quasi» = accettato con avviso di unità. Nessun formato extra.

| DOI | pert. | eventi (avv./parz./non avv.) | per via | prep. | rel. | molecole | verifica (acc./quasi/resp.) |
|---|---|---|---|---|---|---|---|
| 10.3390/cryst14020181 | sì | 14 (11/0/3) | desolvatazione 5, termica 5, solvente 3, meccanica 1 | 8 | 0 | 2 | 14/0/0 |
| 10.1002/advs.202502692 | sì | 15 (15/0/0) | termica 15 | 7 | 0 | 5 | 15/0/0 |
| 10.1021/acs.cgd.4c00279 | sì | 19 (12/0/7) | desolvatazione 12, termica 5, meccanica 2 | 12 | 1 | 2 | 18/1/0 |
| 10.1021/acs.cgd.1c01203 | sì | 20 (17/0/3) | termica 15, desolvatazione 3, solvente 1, meccanica 1 | 7 | 2 | 1 | 20/0/0 |
| 10.1021/acs.cgd.1c01509 | sì | 59 (56/0/3) | termica 30, solvente 12, meccanica 9, desolvatazione 8 | 11 | 0 | 9 | 59/0/0 |

Totale: 127 eventi (111 avvenuti, 16 negativi), 45 preparazioni, 3 relazioni, 19 molecole; nessun respinto; un solo «quasi» (cgd.4c00279, E6: la Tabella 3 scrive «D+28» senza unità). Il blocco ha il rapporto negativi/eventi più basso dei tre fatti in questo giro (13 %): `advs.202502692` e `cgd.1c01509` sono quasi solo fusioni e transizioni termiche, e le loro frasi negative sono poche («show only one endotherm», «the only thermal event … is melting»).

Note per articolo:
- **cryst14020181** (praziquantel–curcumina): 1:1 in IPA/ACN/EtOH/MeOH senza cocristallo (un evento con `solventi_alternativi`), 1:1 in acetato di etile → fase nuova non identificata; il fuso non ricristallizza («No (re)crystallization peaks»). Temperatura di raffreddamento 298 K nei Metodi e 297 (2) K in Tabella 1.
- **advs.202502692** (5FC / acidi grassi, termosalienti): niente negativi sui solidi. Le T di C10 (250 K) e C18 (350 K) sono lette dall'ordine dell'intervallo «250 to 350 K as chain length increased from C10 to C18» (certezza media); C12 e C16 stanno solo in Fig. 1F (valore nullo).
- **cgd.4c00279** (proxillina–4-HBA, fase con CO2): conservazione all'aria di Phase II → I con la regola nuova `desolvatazione / aria`, certezza media; vial chiusa come `termica / conservazione`; la macinazione che non dà mai Phase II viene dalla regola «solo in Y». Il testo si contraddice sui tempi («within a few days» contro IB-40 ancora al 99 % dopo 12 giorni).
- **cgd.1c01203** (OEG-BTBT): la T della transizione I → II è 127, 129, 135 °C o «117–131 °C» secondo la tecnica e la sezione; CCDC 2109678–2109680 per quattro colonne di tabella, attribuiti per ordine con `ccdc_dedotto`.
- **cgd.1c01509** (fluorochinoloni con acidi dicarbossilici): 60 forme; le 12 sospensioni di sali a pH 6.8, 37 °C, 48 h cambiano pattern senza che il prodotto sia identificato (`a: ignota`, `frequenza: sempre`). Il testo dichiara 27 strutture, ne elenca 26 sali + 2 solvati e dà 29 numeri CCDC; molti refusi di formula.

## Proposte nuove per la v1.5 (non ripetono P1–P24, Q1–Q17 né quelle dei blocchi 05 e 06)

1. **Composizione del prodotto e resa nelle preparazioni** (cgd.4c00279). «the proportion of Phase II increased from 12% to 91% when the working temperature was increased from 25 to 51°C». `composizione_prodotto` esiste solo negli eventi e `campione.composizione` non esiste; le percentuali e le rese (58–76 %) sono finite nelle `note`. Proposta: `composizione_prodotto` (forma, frazione, metodo) e `resa` nelle preparazioni, `campione.composizione` negli eventi.
2. **Antisolvente compresso (GAS, SEDS)** (cgd.4c00279). «Phase II is formed in a very CO2-rich liquid or CO2-expanded solvent»; la «CO2 mol fraction … at precipitation pressure» (0.82–0.96) decide la forma. Servono `pressione.tipo: precipitazione` (distinta da `applicata`), `condizioni.frazione_molare_antisolvente` e la portata.
3. **Cocristalli ionici con lo stesso composto come ione e come neutro** (cgd.1c01509). «(nor+)(seb–)·nor·H2O», «(nor+)2(az2–)·az·4H2O». `componenti` ha solo composto e stechiometria: ho scritto nor 2 e az 2 e la divisione ione/neutro in `protonazione`, testo libero. Proposta: `componenti[].stato` (catione, anione, neutro) con la stechiometria per stato.
4. **Partenza = prodotto di un evento precedente, anche se ignoto** (cgd.1c01509). «The loss of the water in (cip+)2(sub2–)·4H2O occurs as two endothermic events at 70.3 and 87.3 °C» e «The melting endotherms of (cip+)2(sub2–)·4H2O … give peaks at 232.8 … °C»: la fusione è dell'idrato già disidratato, che non ha nome. Proposta: `da_prodotto_di: <id evento>`, così non si attribuisce la fusione all'idrato né si inventano forme descrittive.
5. **Esito «cambia ma non si sa in che cosa»** (cgd.1c01509). «Additional peaks or new patterns appeared, indicating that the salts transform in the dissolution medium. However, it was not possible to unambiguously identify possible dissociation or transformation products». Dodici eventi con `a: ignota`; `esito` non dice «parziale o completo, non si sa». Proposta: `esito_dettaglio: cambio_non_identificato` a valore fisso.
