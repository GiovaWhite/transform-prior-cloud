# Rapporto del blocco 00 (schema v1.4)

Blocco di prova: 3 articoli di `assegnazioni.csv`. Estrazioni in `estrazione/cloud/`, ciascuna con il suo `.verifica.json`.
Ogni articolo e' stato letto per intero (testo, tabelle, didascalie), estratto, verificato con `python3 -m tp.verifica <file>` (mai `--cartella`) e riletto accanto al testo per il significato.

## Esito in sintesi

| DOI | pertinente | eventi | forme | preparazioni | relazioni | molecole | verifica |
|---|---|---|---|---|---|---|---|
| 10.1021/cg101162a | si' | 30 | 12 | 14 | 1 | 1 | 30 accettati, 0 quasi, 0 respinti |
| 10.1248/cpb.51.807 | si' | 10 | 8 | 6 | 0 | 3 | 10 accettati, 0 quasi, 0 respinti |
| 10.3390/cryst10080667 | si' | 13 | 4 | 6 | 0 | 1 | 13 accettati, 0 quasi, 0 respinti |
| **totale** | | **53** | **24** | **26** | **1** | **5** | **53 accettati**, 0 errori di schema |

Nessuna citazione e' risultata `quasi` e nessun avviso di unita': tutte le citazioni sono corrispondenze esatte. Questo vuol dire solo che le frasi e i numeri stanno nel testo; il significato l'ho controllato a mano (vedi in fondo gli errori che ho trovato rileggendo).

## 10.1021/cg101162a — acido β-resorcilico (βRA)

Pertinente: si'. 30 eventi: `termica` 8, `desolvatazione` 7, `altro` 7 (instabilita' fuori dall'acqua madre), `solvente` 4, `umidita` 3, `meccanica` 1. Esito: 27 avvenuti, 2 non avvenuti, 1 parziale. Certezza: 10 alta, 17 media, 3 bassa.

- **II° ⇄ I**: E1 (II° → I, DSC Ttrs = 159.8 ± 0.5 °C, ΔH 2.1 kJ/mol, 10 K/min), E2 (I → II° per macinazione a temperatura ambiente, `inverso_di` E1) ed E3 (I → II° non avvenuta in 18 mesi a condizioni ambiente). Relazione enantiotropa F1/F2 con `piu_stabile` II° e due stime della T di transizione.
- **Idrati e solvati per riscaldamento**: HH → I in HSM (sopra 70 °C, pseudomorfosi) e in DSC/TGA (sopra 60 °C, perdita 5.55%); MH → II° (sotto 60 °C, 9.5%); SAA → II° (40-60 °C); SDMF-II → SDMF-I (50-70 °C, 0.25 mol DMF/mol) → I (ca. 90 °C); SDMSO e SDX attraverso il fuso (fusione peritettica, poi cristallizzazione della forma I dal fuso, `dal_fuso`).
- **Umidita'** (SPS-11, 25 °C): I → HH (completato in 48 h), II° → HH parziale (ca. 25%), HH → miscela di I e II° a 5% RH e meno (ca. cinque giorni).
- **Sospensioni da II°** in dioxano, DMF e DMSO (una frase per tre eventi).
- **Instabilita' fuori dall'acqua madre**: 5 solvati e MH (6 eventi, `a: ignota`, certezza media/bassa) e il negativo di HH.
- **Preparazioni** 14, **forme** 12 (tra cui il sale di piridinio, la miscela I + II° e la voce ZZZEEU), **molecola** 1 (flessibilita', conformeri, legame H intramolecolare). `gruppi_coinvolti` su 4 eventi (disidratazione di HH, SDMSO → I). `motivi_hb` su 5 forme.
- Refcode: ZZZEEU01-04 (con le quattro T) per II°, QIVTUK per HH, ZZZEEU per la voce contestata. Nessun CCDC nel testo.

## 10.1248/cpb.51.807 — troglitazone

Pertinente: si'. 10 eventi: `desolvatazione` 4, `termica` 3, `umidita` 3. Esito: 9 avvenuti, 1 non avvenuto. Certezza: 4 alta, 6 media.

- **MA2 ⇄ MA0** (diidrato ⇄ disidratato del cristallo misto, SCSC): E1 a bassa umidita' (sotto 30% RH, temperatura ambiente, alcuni giorni) ed E2 a 80% RH e 25 °C (`inverso_di` fra i due). `gruppi_coinvolti` sull'acqua e sui legami N3–H3…O30 / O30–H30…O6.
- Disidratazione termica di MA2 (DSC, 40-100 °C, 5 o 10 °C/min: `valori` [5, 10]) e fusioni dei disidratati (175 e 185 °C), di H0 (190 °C) e di L1 (120 °C).
- Negativo: H0 non si trasforma ad alta umidita' (RH non detta: `umidita_ignota`).
- Decomposizione per desolvatazione durante la raccolta dei dati (a temperatura ambiente): L1/2 diclorometano (rapida), metanolo ed etanolo (graduale).
- **Forme** 8 (H0, L1, quattro L1/2 uno per solvente, MA2 e MA0 come `soluzione_solida` con rapporto H:L 64:36 e 67:33), **preparazioni** 6, **molecole** 3 (troglitazone e le due coppie di diastereoisomeri). Nessun refcode ne' CCDC.

## 10.3390/cryst10080667 — 1,2-bis[(1-metil-imidazol-2-il)tio]etano (2a, 2b, 2c)

Pertinente: si'. 13 eventi: `termica` 8, `desolvatazione` 5. Esito: 11 avvenuti, 1 parziale, 1 non avvenuto. Certezza: 9 alta, 4 media.

- **Disidratazione di 2c (diidrato) in vuoto**, 55 °C / 200 mbar: parziale a 30 min (miscela 2c + 2a), completa a 60 min (2a). Stessa corsa campionata a due tempi, quindi due eventi.
- **A pressione atmosferica**: TGA (40-110 °C, 11.31%), fusione DSC (onset 65 °C) e HSM-DSC (40 → ca. 65 °C) tengono eventi separati per tecnica; fuso raffreddato subito → vetro; scaldato a 80 °C in olio → ricristallizza 2c (negativo); a 95 °C in crogiolo aperto → miscela; a 120 °C → 2a per nucleazione e crescita (`senza_intermedio`).
- Fusioni di 2a (89 °C onset; HSM-DSC 89-90 °C), di 2b (208 °C) e perdita di solventi di 2b (35-70 °C).
- **Forme** 4, con i tre numeri CCDC (2013658 per 2a, 2013659 per 2b, 2013660 per 2c); **preparazioni** 6; **molecola** 1. La reazione del metimazolo in dicloroetano e' in soluzione e non e' un cambio di forma (in `note`).

## Che cosa il verificatore non vede (errori miei trovati rileggendo)

Tutti corretti prima del commit:
- **cg101162a**: il crogiolo «pin-holed DSC capsules» della Fig. 6 era solo su un evento (HH); l'ho aggiunto a tutti gli eventi con DSC della figura.
- **cg101162a**, E19: il tempo di 48 h per il 25% di II° convertito era `trasformazione`; e' un tempo di osservazione, quindi `attesa`.
- **cg101162a**, gruppo «acqua» di HH: la citazione era una frase di struttura e non della disidratazione; ora e' «despite the water interactions».
- **cpb.51.807**: la nota di MA0 non riportava che la sua curva DSC e' diversa da quella di H0 pur con un diffrattogramma quasi identico; aggiunto.
- **cryst10080667**: refusi nelle note («dididrato», «Quattro CCDC» per tre numeri) e una frase sgrammaticata in E2; corretti.

## I casi in cui schema o linee guida non bastavano (per la v1.5)

1. **«Qualunque forma» come partenza** (cg101162a). «...by solvent-mediated transformation of any βRA form, using water-free solvents that did not form a solvate» e «heating any βRA form above the transition temperature of the polymorphic transition II° → I (150−170 °C)». `da_possibili` vuol dire «una fra queste» e non «ciascuna di queste». Ho messo `sospensione` come preparazione e `da_evento` verso E1. Proposta: `da_qualsiasi: true` (partenza = ogni forma dell'articolo), con `da: ignota`.
2. **Un processo dentro un picco DSC senza cambio di forma** (cg101162a, SDX). «...peritectic melting/decomposition, evaporation of the solvent (DSC: endotherm at ca. 85 °C), and the crystallization of form I (exotherm above 110 °C)». Per la regola 12 ci vuole un evento per processo, ma per l'evaporazione dal fuso non c'e' un `a` vero: ho messo `ignota` (certezza bassa). Proposta: un valore `a: "fuso"` esplicito oppure un tipo di passo `senza_cambio_forma` per i processi che non cambiano il solido.
3. **Prodotto che e' una miscela senza prevalenza** (cg101162a, Fig. 7: «desorption cycle of HH to a polymorphic mixture of forms I and IIo»). Le linee guida descrivono la miscela solo come partenza e `composizione_prodotto` solo con un prodotto principale. Ho usato una forma `miscela` come `a`. Proposta: dire esplicitamente che per il prodotto misto senza prevalenza si usa una forma `miscela` (e `composizione_prodotto` solo se c'e' una prevalenza).
4. **Decomposizione di una forma non nominata** (cg101162a). «However, decomposition, although slow compared to the polymorphic transformation, starts at ca. 160 °C.» Ho usato `da: ignota` e `a: decomposizione` (certezza bassa), per analogia con il punto di fusione della sintesi (regola 7). Proposta: estendere la regola 7 alle decomposizioni.
5. **Voce del CSD citata nell'introduzione e mai osservata** (cg101162a, ZZZEEU). «...the volume of ZZZEEU corresponds to a monohydrate rather than an anhydrous form but not to the new monohydrate described in this work.» `voce_contestata` esiste, ma non dice se creare una forma senza eventi. L'ho fatto (portava un refcode). Proposta: scriverlo nelle linee guida, con un flag `non_osservata: true` per queste forme.
6. **Temperature associate a refcode per ordine** (cg101162a). «ZZZEEU01 to ZZZEEU04 ... measured at 90, 100, 110, and 150 K». L'attribuzione e' per ordine, ma l'unico flag e' `refcode_dedotto` della forma. Proposta: un flag `attribuzione_per_ordine` dentro ogni voce di `strutture`.
7. **Pressione e temperatura insieme** (cryst10080667). «heated ... at around 55 °C and at reduced pressure of 200 mbar to a constant mass». `desolvatazione` ha una sola sottovia: ho scelto `vuoto`, la T e' in `condizioni.temperatura`. Proposta: `sottovia` come lista, oppure una regola scritta («vuoto con T: sottovia `vuoto`»).
8. **Durata che e' sia tempo di processo sia tempo di completamento** (cryst10080667). «The process was completed after 60 min.» insieme a «dried ... for 60 min». La regola 2 dice `processo` per i trattamenti in vuoto: l'ho seguita, ma l'altra lettura (`trasformazione`) e' ugualmente legittima. Proposta: dire quale vince.
9. **Ricristallizzazione della stessa forma dal fuso** (cryst10080667). «...heated to 80 °C and immersed in oil ... recrystallization of the dihydrate 2c was observed due to the conditions that inhibited efficient water removal.» `da` e `a` coincidono. L'ho registrato come negativo della disidratazione (`non_avvenuta`, `campione.mezzo: oil`). Proposta: `esito_dettaglio: "ricristallizzazione_stessa_forma"` o ammettere esplicitamente `da == a`.
10. **Intermedi cercati e non trovati** (cryst10080667). «...to determine whether dehydration of 2c to 2a proceeds via a metastable monohydrate intermediate ... or as a hemihydrate ... no additional exothermic and endothermic events or changes in XRPD ... were observed.» `senza_intermedio` dice che non c'e' stato un intermedio, ma non quali sono stati cercati, e un negativo con `a_possibili` obbligherebbe a dichiarare forme che non esistono. Proposta: `intermedi_esclusi: ["monohydrate", "hemihydrate"]` (testo libero).
11. **Cella con un valore palesemente sbagliato in tabella** (cryst10080667, Tabella 2: gamma = 180° in una cella trigonale; il volume torna con 120°). C'e' `gruppo_spaziale_sospetto` ma non l'equivalente per la cella. Proposta: `cella_sospetta: true` con la ragione in `note`.
12. **Simboli del PDF giapponese** (cpb.51.807). In tabella il segno meno e' una cifra «2», il piu' una cifra «1», «×» e' «3» e «=» e' «5» (prova: i codici di simmetria della Tabella 3, «211x, 1y, 11z» = −1+x, y, 1+z; «2q55.1» = 2θ = 5.1°; «0.2530.3530.05» = 0.25 × 0.35 × 0.05). Le temperature «250» e «2105» sono −50 e −105 °C. Le linee guida citano `T_scritta` e `T_probabile`, ma non il formato di `T_probabile` (io ho scritto una stringa «-50 °C») ne' questa regola. Proposta: definire `T_probabile` come grandezza e documentare la mappatura dei simboli (vista qui in un solo articolo, Chem. Pharm. Bull. 2003: non so se valga per gli altri PDF giapponesi del corpus).
13. **Gruppo spaziale rovinato ricostruito con Z e Z'** (cpb.51.807: «P1–» con sistema triclino, Z = 4 e «two L-pair troglitazone molecules in an asymmetric unit»). Le linee guida accettano come appiglio il numero del gruppo o «centrosymmetric»; qui l'appiglio e' l'aritmetica di Z/Z'. Proposta: ammetterlo esplicitamente.
14. **Cristallo misto con rapporto percentuale** (cpb.51.807: «the MA0- and MA2-forms have the H- and L-pairs in the ratios of 67 : 33 and 64 : 36»). `soluzione_solida` dice «frazioni in `componenti`» ma non se normalizzare. Ho tenuto 67/33 e 64/36 come scritti e l'ho detto in `note`. Proposta: dire «come scritte» e aggiungere `unita: "%"` a `componenti`.
15. **Diastereoisomeri in coppia racemica** (cpb.51.807: «H-pair» 2R-5S/2S-5R e «L-pair» 2R-5R/2S-5S). Le linee guida dicono che enantiomeri e analoghi sono composti diversi con `analogo_di`; qui il composto e' una coppia di enantiomeri. Ho creato un composto per coppia (`analogo_di` il troglitazone generico). Proposta: dire che un racemato di un diastereoisomero e' un composto a se' e come si scrive il nome.
16. **Frasi spezzate da intestazioni di pagina** (cpb.51.807 e cryst10080667; ad esempio «obtained from an aqueous acetone» / «solution by slow evaporation at room temperature.»). Una citazione non puo' attraversare l'intestazione. Proposta: scriverlo nelle istruzioni: si cita ogni meta' come voce separata di `citazioni`.
17. **Unita' dell'umidita'**: ho usato «%RH», che il verificatore capisce, ma non c'e' una scrittura standard. Proposta: fissare «% RH».

Una nota di processo: nell'ambiente cloud il `git push` e' stato rifiutato con un 403 ("Claude doesn't have GitHub access to GiovaWhite/transform-prior-cloud"): i tre commit di articolo sono solo nella sessione locale finche' non si installa la Claude GitHub App sul repository o si ricollega GitHub da claude.ai.
