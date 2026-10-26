# Giro 03 — i 15 articoli con la resa attesa più alta (schema v1.4, solo estrazione principale)

Tutti e 15 gli articoli della tabella di `compiti/giro_03.md` sono estratti, nell'ordine dato, da tre sottoagenti (G1: 1, 4, 7, 10, 13; G2: 2, 5, 8, 11, 14; G3: 3, 6, 9, 12, 15). Dopo ogni articolo ho rifatto `tp.verifica` sul solo file, poi commit e push. L'interruttore di stop per il budget non è mai servito. Numeri della tabella ricalcolati da me dai file. «Quasi» = accettato con un avviso. Nessun formato extra.

## Esiti per DOI

| # | DOI | eventi (avv./parz./non avv.) | per via | prep. | rel. | mol. | forme con struttura* | eventi con gruppi | forme con motivi H | verifica (acc./quasi/resp.) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10.1021/acs.cgd.9b01522 | 14 (13/0/1) | termica 14 | 3 | 3 | 1 | 3/3 | 9 | 1 | 14/0/0 |
| 2 | 10.1107/s2052252521010381 | 8 (6/0/2) | pressione 6, termica 2 | 4 | 0 | 1 | 5/5 | 2 | 3 | 8/0/0 |
| 3 | 10.3390/molecules24102018 | 5 (3/0/2) | pressione 5 | 5 | 0 | 1 | 2/2 | 2 | 2 | 5/0/0 |
| 4 | 10.3390/molecules29184376 | 29 (21/0/8) | termica 16, solvente 7, desolvatazione 6 | 15 | 2 | 2 | 5/11 | 2 | 6 | 29/0/0 |
| 5 | 10.3390/cryst7010013 | 29 (17/1/11) | termica 13, umidità 6, meccanica 4, desolvatazione 3, solvente 3 | 5 | 1 | 4 | 4/14 | 6 | 3 | 29/0/0 |
| 6 | 10.1021/acs.jpcc.1c07297 | 30 (16/1/13) | termica 16, pressione 9, meccanica 4, altro 1 | 5 | 4 | 3 | 0/12 | 5 | 4 | 30/0/0 |
| 7 | 10.3390/molecules27217411 | 7 (5/0/2) | termica 7 | 3 | 1 | 1 | 2/2 | 1 | 2 | 7/0/0 |
| 8 | 10.3390/cryst10121098 | 22 (12/2/8) | solvente 7, meccanica 7, termica 5, desolvatazione 2, senza via 1 | 3 | 1 | 1 | 8/14 | 3 | 5 | 22/0/0 |
| 9 | 10.1021/jacs.3c07060 | 26 (17/5/4) | luce 18, termica 6, desolvatazione 2 | 2 | 0 | 1 | 0/8 | 13 | 2 | 25/1/0 |
| 10 | 10.1107/s2052252523002452 | 9 (4/0/5) | termica 6, pressione 3 | 10 | 1 | 1 | 2/2 | 3 | 2 | 9/0/0 |
| 11 | 10.1038/s42004-025-01715-8 | 20 (15/0/5) | termica 14, solvente 4, desolvatazione 2 | 2 | 3 | 2 | 0/5 | 9 | 5 | 20/0/0 |
| 12 | 10.1039/c5sc04057d | 8 (7/1/0) | termica 7, meccanica 1 | 1 | 1 | 2 | 2/2 | 3 | 0 | 7/1/0 |
| 13 | 10.1107/s2052252519015616 | 19 (12/3/4) | pressione 13, termica 6 | 10 | 3 | 1 | 2/7 | 7 | 3 | 14/5/0 |
| 14 | 10.1021/acs.chemmater.7b02558 | 11 (11/0/0) | termica 8, luce 3 | 1 | 1 | 1 | 0/3 | 3 | 1 | 9/2/0 |
| 15 | 10.1021/jacs.3c09246 | 17 (13/0/4) | solvente 10, desolvatazione 4, altro 2, termica 1 | 10 | 0 | 1 | 0/9 | 6 | 2 | 17/0/0 |

\* Forme con refcode, CCDC o `strutture[]` su totale forme dell'articolo. Dove è 0 il testo non dà numeri attribuibili alle forme: `jpcc.1c07297` ha un intervallo CCDC (2084039–2084046) senza attribuzione e resta a livello di articolo; `jacs.3c07060`, `s42004-025-01715-8`, `chemmater.7b02558` e `jacs.3c09246` non hanno CCDC né refcode nel testo (le 5 strutture dei solvati di `jacs.3c09246` sono solo nel supplementare). In `c5sc04057d` le due forme hanno `strutture[]` (cella e temperatura) ma i CCDC sono a livello di articolo. Dove l'attribuzione è per ordine di un intervallo, la forma ha `ccdc_dedotto`: `cgd.9b01522`, `s2052252521010381` (29 CCDC su 29 datablock), `molecules24102018`, `molecules27217411`, `cryst10121098`, `s2052252523002452` (33 strutture) e `s2052252519015616`.

**Totale:** 254 eventi (172 avvenuti, 13 parziali, 69 negativi), 79 preparazioni, 21 relazioni, 23 molecole, 99 forme, 74 eventi con `gruppi_coinvolti`, 41 forme con `motivi_hb`. **Nessun respinto**; 9 «quasi» (245 accettati puliti). Per via: termica 121, pressione 36, solvente 31, luce 21, desolvatazione 19, meccanica 16, umidità 6, altro 3, senza via 1 (ricalcolato dai file). I negativi sono il 27 % degli eventi.

Interventi miei: in `chemmater.7b02558` gli eventi E7 ed E8 (fotociclizzazione e riapertura nel cristallo) avevano `temperatura: ambiente`, ma il testo non dà nessuna temperatura per quel fotocromismo («room temperature» non c'è): l'ho tolta e ho rifatto la verifica (resta 9 accettati, 2 «quasi»). Il «quasi» di quell'articolo e di `jacs.3c07060`/`s2052252519015616` sono avvisi del controllo unità (vedi proposte).

## Token

Come nei rapporti precedenti: per me il contatore della sessione, per ogni agente il totale che riporta a fine lavoro; non so se i due misurino la stessa cosa. Non ho il costo per singolo articolo, solo per agente.

| voce | articoli | testo (KB) | token | per articolo | per KB di testo |
|---|---|---|---|---|---|
| G1 | 5 (1, 4, 7, 10, 13) | 241 | 491 072 | 98 mila | 2.0 mila |
| G2 | 5 (2, 5, 8, 11, 14) | 187 | 497 623 | 100 mila | 2.7 mila |
| G3 | 5 (3, 6, 9, 12, 15) | 186 | 449 920 | 90 mila | 2.4 mila |
| sottoagenti, totale | 15 | 614 | 1 438 615 | 96 mila | 2.3 mila |
| io (letture iniziali, prompt, verifiche, commit, note, rapporto) | — | — | ~90 mila | — | — |
| **totale** | | | **~1.53 milioni** | | |

Sotto il tetto di 1,9 milioni (circa 370 mila token di margine). Per tenere il conto durante il lavoro ho stimato 2.4 mila token per KB di testo, ricavati dai conti per agente del giro 02; il risultato reale (2.3) l'ha confermato. Il costo per KB va da 2.0 a 2.7 mila secondo l'agente: la lunghezza del testo spiega solo in parte il costo (G1 ha avuto il 29 % di testo in più di G2 e G3 ma è costato come G2).

## Proposte nuove per la v1.5 (non ripetono P1–P24, Q1–Q17 né i rapporti dei blocchi 05–08)

1. **Strutture ad alta pressione indicizzate per pressione** (proposta da tutti e tre gli agenti). `strutture[]` ha `temperatura` ma non `pressione` né il nome del datablock. Frasi: «contains datablock(s) C4H2N5Cl1@0_09GPa_phase_alpha_xH2O, C4H2N5Cl1@0_10GPa_phase_alpha_xH2O, ...» (CTP, 29 strutture), «Crystal structure: contains datablock(s) alpha_DL_0.01MPa, alpha_DL_0.10GPa, …» e «CCDC references: 2206626, …, 2206658» (dl-mentolo, 33 strutture), e una tabella con colonne a 0.00, 5.00 e 5.49 GPa e «CCDC deposition numbers for the structures listed are 1911442, 1911457, and 1911458» (4-iodobenzonitrile). Il nome del datablock, che porta P o T, oggi sta nella citazione. Proposta: `strutture[].pressione` (grandezza) e `datablock`, e la regola per attribuire un elenco di CCDC a datablock ordinati con `ccdc_dedotto` per voce.
2. **Relazioni che dipendono da una leva diversa dalla temperatura.** Frasi: «polymorph α … is stable at atmospheric pressure … a new β polymorph, which becomes stable above 0.40 GPa» (dl-mentolo) e, per il diariletene, la temperatura di transizione 25.4–25.3 °C del cristallo fresco contro 17 e 15 °C di quello fotoirraggiato («This is due to a decrease in the phase transition temperature caused by the photoisomerization»). `relazioni` ha solo la temperatura. Proposta: `pressione_transizione` e `regioni_stabilita` [{forma, pressione min/max, temperatura}], e `temperatura_transizione[].condizione` («dopo fotoisomerizzazione»).
3. **Negativo per barriera cinetica.** Frasi: «as if a too-high energy barrier existed for the inverse transformation» (tafamidis), «the different symmetries relating the chains constitute a high kinetic barrier for the solid–solid transition between polymorphs α and β» (dl-mentolo), «the sluggishness of the I→II transition» (piridina d5). Il modello deve poter distinguere «non stabile» da «stabile ma cineticamente bloccato». Proposta: `esito_dettaglio: barriera_cinetica` e un flag `atteso_termodinamicamente`.
4. **Equivalenza fra etichette di fase.** (a) Etichette di altri lavori con numerazione diversa: «the ‘phase I’ of Heyns & Venter (1985) is actually the Z′ = 1, P212121 phase II, and the ‘phase II’ of Fanetti et al. (2011) and Zhuravlev et al. (2010) is the Z′ = ½, P41212 phase III» (piridina): senza il riferimento gli eventi `citata` non si collegano alle forme. Proposta: `etichette_alternative` come {etichetta, riferimento}. (b) Isotopologhi: «The same phase is formed by pyridine-d5 on cooling the liquid below the melting point»: i composti sono distinti e il nome di fase comune si perde. Proposta: `stessa_fase_di` fra forme di isotopologhi, con relazioni di stabilità proprie.
5. **Leve quantitative di luce e di sforzo.** `luce` ha lunghezza d'onda, dose e sorgente; `meccanica` non ha una sottovia per il taglio. Frasi: «Irradiation at a higher light intensity of 150 mW mm–2, achieved by switching to a laser light source with a beam diameter of 2 mm, produced ... a strong photomechanical effect» (cocristallo cis-azo) e «σf-trans increased linearly in temperature with a gradient of 0.135 MPa °C–1» (cristallo superelastico). Proposta: `luce.intensita` (con `potenza` e `diametro_fascio`), sottovia `meccanica / taglio` e `condizioni.sforzo` (MPa; nucleazione, trasformazione diretta o inversa; gradiente per °C).

## Altre segnalazioni raccolte (non entrano nelle 5)

Le frasi sono nelle note degli agenti e nei campi `note` e `conflitto` dei JSON; non le ho riverificate tutte sul testo.
- Contatti che cambiano distanza senza rompersi: `cambia: si_allunga / si_accorcia` e `distanza: {da, a, unita}` in `gruppi_coinvolti` («the distance of C−H···F and C−H···C changed from 2.792 and 4.007 Å to 3.159 and 3.852 Å»; CTP: «significant elongation of all the shortest intermolecular distances»).
- Evento con esito solo nel supplementare: `esito: non_riportato` ammesso con `solo_supplementare` («The long-term stability of the co-crystal was also initiated; see Table S1», ivabradina; ho lasciato fuori l'evento).
- Immersione in olio come leva: sottovia `solvente / immersione` e un campo `mezzo_protettivo` («immersing crystals of AIIα and BII in silicone oil triggered conversion to AI and BI crystals»; «paraffin oil to avoid jumping»).
- Scambio di domini nella stessa fase (`da == a`, con `variante`): «α+/α– state» del cristallo superelastico, lasciato in `note` come non-evento.
- Forma poco cristallina distinta da `amorfo` («low-crystallinity solid … nonporous») e proprietà `area_superficiale` / `volume_pori` con adsorbato e T («surface area of 458 m2 g–1»).
- Codice (non toccato): il controllo unità dà «quasi» con l'incertezza scritta con lo spazio prima della parentesi («0.942 (9) GPa», stile IUCr: 5 «quasi» in `s2052252519015616`) e con «365-nm light» (2 «quasi» in `chemmater.7b02558`).
- Le incoerenze degli articoli sono registrate dagli agenti in `note` e `conflitto` dei singoli file. Le più pesanti: le soglie di transizione della CTP a 0.15, 0.16, 0.18 e 0.20 GPa nello stesso articolo; nella desloratadina gli angoli β della Fig. 4 (108.2/113.3/108.2) contro il testo (108.08/113.38/118.78); nell'ivabradina «3 days 80 °C» contro «80 °C and 0% RH».
