# Blocco 05 (schema v1.4, solo estrazione principale)

Cinque articoli, estratti da tre sottoagenti (A: 2 articoli di questo blocco, B: 3). Dopo ogni articolo ho rifatto `tp.verifica` sul solo file, poi commit e push. I numeri della tabella sono ricalcolati da me dai file. «Quasi» = accettato con avviso di unità. Nessun formato extra.

| DOI | pert. | eventi (avv./parz./non avv.) | per via | prep. | rel. | molecole | verifica (acc./quasi/resp.) |
|---|---|---|---|---|---|---|---|
| 10.3390/cryst12040550 | sì | 14 (5/0/9) | termica 6, solvente 5, umidità 3 | 8 | 0 | 1 | 14/0/0 |
| 10.1038/s41467-023-44214-x | sì | 10 (7/0/3) | termica 5, altro (campo elettrico) 3, desolvatazione 1, umidità 1 | 2 | 1 | 2 | 10/0/0 |
| 10.3390/pharmaceutics15020449 | sì | 30 (17/0/13) | termica 12, meccanica 5, solvente 6, umidità 5, desolvatazione 2 | 12 | 0 | 6 | 30/0/0 |
| 10.1021/acs.cgd.2c00861 | sì | 23 (17/0/6) | termica 11, solvente 9, umidità 3 | 7 | 3 | 1 | 23/0/0 |
| 10.3390/ijms22020928 | sì | 4 (3/0/1) | termica 2, desolvatazione 2 | 2 | 0 | 2 | 4/0/0 |

Totale: 81 eventi (49 avvenuti, 32 negativi), 31 preparazioni, 4 relazioni, 12 molecole; nessun respinto, nessun «quasi». I negativi sono il 40 % degli eventi del blocco (nel blocco 04 erano circa la metà dei 190 senza la regola nuova, ma concentrati in pochi articoli).

Note per articolo (fatti incontrati, non proposte):
- **cryst12040550** (baloxavir marboxil): «DSC curve of Form II and III shows stability up to approximately 235.5 °C and 238.7 °C» → due negativi con soglia; fusione di II e III senza temperatura (certezza bassa). Form III → Form I in dissoluzione a pH 1.2; Form I e II invariate (anche 7 giorni in acqua). Table 1: temperature e CCDC non legati alle forme (attribuiti per ordine di colonna).
- **s41467-023-44214-x** (HOF-FJU-52): SCSC Ccce → C2cb a 200 K, nessun ritorno a 250 K, nessuna transizione sopra 200 K (lato opposto della soglia); tre stati con tensione applicata (0.6 V, −0.1 V, 19 V a 100 K). Metodi e Risultati danno miscele di sintesi diverse.
- **pharmaceutics15020449** (sali metformina–FANS): 13 negativi (sospensione a pH 6.8, 40 °C / 75 % RH per quattro mesi, «only one endothermic event»). Testo e Table 3 danno fattori di solubilità diversi (111× contro 119×, 208×); aging «two months» nei Metodi contro «four months» nei Risultati (tenuto il secondo, con `conflitto`). I CCDC 2232928–2232933 restano a livello di articolo.
- **cgd.2c00861** (hesperetin): 9 sospensioni competitive dalla Table 2 (una per riga e colonna), β + γ in acqua che resta una miscela dopo due settimane; α è il «disappearing polymorph» (preparazione non ottenuta).
- **ijms22020928** (puerarin–prolina): solo due forme e la loro TGA/DSC; nessuna prova solido–solido né dissoluzione con controllo del residuo.

## Proposte nuove per la v1.5 (non ripetono P1–P24 né Q1–Q17)

1. **Campo elettrico e stati della stessa fase** (s41467). «DC voltage of 0.6 V was applied on HOF-FJU-52 along the b axis to obtain the structure of HOF-FJU-52-0.6V»; «no substantial change has been observed in the two structures, except for some subtle changes». La tensione oggi sta nel testo libero di `condizioni.altro`. Proposta: `condizioni.campo_elettrico` {tensione, asse, tipo DC/AC}, e `stato_di` esteso oltre l'idratazione con un `parametro_stato` (T, tensione) per le strutture della stessa fase a condizioni diverse.
2. **Contraddizione fra linee guida e punto 4 dell'aggiornamento** (cgd.2c00861, confermata dall'agente del blocco 06). Le linee guida dicono «un evento per tecnica se le temperature differiscono»; il punto 4 dice che la stessa prova vista con una seconda tecnica non è un evento nuovo. Frasi: «the first being consistent with transformation to a new phase at ca. 182 °C» (DSC) e «vt-PXRD data … also reveals a phase change by 180 °C to a new crystal form». Scelta fatta: un solo evento, la seconda temperatura in `note`. Proposta: una regola sola. Stessa corsa e stesso campione = un evento con `osservazioni.temperatura_per_tecnica`; corse o velocità diverse = eventi distinti.
3. **Slurry senza vincitore e limite di stabilità** (cgd.2c00861, cryst12040550). «even after 2 weeks the resulting powder remained a mixture» (β + γ in acqua) e «stability up to approximately 235.5 °C». Oggi `non_avvenuta` con `esito_dettaglio` libero. Proposta: valori fissi `esito_dettaglio: nessun_vincitore` (e `miscela_persistente`) per le sospensioni competitive, e `temperatura.tipo: limite_stabilita` con un riferimento all'evento che segue.
4. **Intervallo di fusione di un campione contro limiti di un vincolo** (pharmaceutics15020449). «show a melting point in a range between the melting point of the MTF base (117 °C) and the corresponding NSAID coformer»: il tipo `intervallo` confonde il range misurato con gli estremi di un vincolo. Proposta: `tipo: intervallo_fusione` distinto da `limiti` (con `relativo_a` ammesso anche verso una forma) e il flag `unita_da_intestazione` accettato dal verificatore per i numeri di tabella.
5. **Relazioni calcolate** (s41467). «the total energy of HOF-FJU-52-200K is –4019.69 eV, which is about 6.97 eV lower than that of HOF-FJU-52, implying that the HOF-FJU-52-200K is energetically more stable». `fonte_dati` ammette solo propria/citata/riprodotta/incerta: non si può dire che è un calcolo (DFT a 0 K su strutture misurate a T diverse). Proposta: `natura: calcolata` con `metodo` nelle relazioni, come `calcolato` nelle proprietà delle molecole.
