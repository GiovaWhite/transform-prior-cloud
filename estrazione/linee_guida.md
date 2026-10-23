# Linee guida di estrazione — v1.4 (2026-10-23)

Valgono per chi annota a mano (gold set) e per l'LLM: stesso schema, stesse regole.
Lo schema formale è `schema_estrazione.json` (v1.4, superinsieme delle precedenti:
un file v0, v1, v1.1, v1.2 o v1.3 resta valido). Ogni file si controlla con
`python -m tp.verifica <file>`. Nelle estrazioni nuove si scrive
`"versione_schema": "v1.4"`.

Ogni regola risponde a un caso vero, citato fra parentesi quadre. La v1 nasce dai
quattro estrattori di `estrazione1`; la v1.1 dal quarto; la v1.2 dai nove di
`pilota1` (proposte in `proposte_v1.2.md`); la v1.3 da `desolvati1` (proposte in
`proposte_v1.3.md`); la v1.4 da `lotto2`, `lotto3` e dall'utente (97 proposte in
`proposte_v1.4.md`, riassunte qui sotto e in `v1.4_cosa_cambia.md`).

## Che cosa porta la v1.4 (la molecola, le competizioni, i dubbi dichiarati)

**La molecola: quello che SOLO l'articolo sa.** I descrittori calcolabili (massa,
donatori, anelli...) li calcola il codice dallo SMILES del CSD: non si estraggono.
Si estrae quello che l'articolo DICHIARA, sempre con la frase.
- `molecole[]`, uno per composto (`composto` = id in `composti`):
  - `proprieta[]`: `tipo` (pKa, solubilita, logP, logD, igroscopicita,
    punto_fusione_amorfo, temperatura_transizione_vetrosa, altro), `grandezza`,
    e quando servono `gruppo` (del pKa), `forma`, `solvente`, `temperatura`,
    `umidita`, `pH`, `metodo`, `calcolato: true` se e' un calcolo
    [«the solubility of Form II in water at 25 °C was 0.25 mg/mL»];
  - `descrizioni[]`: tautomeria, zwitterione, flessibilita (le torsioni che gli
    autori nominano), conformeri, chiralita (enantiomero puro o racemo),
    legame_h_intramolecolare, con `testo` breve [«the molecule adopts the enol
    form stabilized by an intramolecular O–H···N hydrogen bond»].
  - Il punto di fusione di una forma resta nell'evento verso il fuso.
- **`gruppi_coinvolti` negli eventi**: i gruppi funzionali o i sintoni che
  l'articolo dice coinvolti NELLA TRASFORMAZIONE. `gruppo` COME SCRITTO
  («carboxylic acid dimer», «amide N–H», «hydroxyl groups»), `ruolo`
  (donatore, accettore, sintone, coordina_ospite, torsione, protonazione),
  `con` (ospite, altra_molecola, stessa_molecola, controione), `cambia`
  (si_forma, si_rompe, cambia_partner, ruota, resta) e la `citazione`
  [«on dehydration the water-mediated N–H···O chains are replaced by direct
  amide–amide dimers»]. Solo se il testo lo dice: niente gruppi dedotti dalla
  struttura.
- **`motivi_hb` nelle forme**: R2²(8), catene C(4), «acid–pyridine heterosynthon»,
  con `chi` e la citazione.

**Sospensione competitiva** [«A 1 : 1 mixture of CTN I and II was suspended in
isoamyl alcohol ... complete conversion to CTN I»]: `sottovia:
sospensione_competitiva`, `da` = la miscela come forma `miscela` (come prima),
`a` = la forma che resta, e in `condizioni.composizione_iniziale` le forme di
partenza con la frazione nominale e, se c'e', quella misurata (`tipo`). La
raccolta ne fa una relazione di stabilita' a quella T e in quel solvente.

**Partenze e prodotti incerti**: niente forme finte.
- `da_possibili` [«AH-I, AH-II, or Hy1-I ... Hy1-I formed»] e `a_possibili`
  [«transformed to either one of the three anhydrous forms or a hydrate»]: le
  forme candidate, tutte dichiarate. `da`/`a` restano `ignota`. Con esito
  `non_avvenuta`, `a_possibili` vuol dire che NESSUNA di quelle si e' formata.
  «A or B», «A and/or B»: `a_possibili`.
- `da_dedotto: true` quando la forma di partenza si capisce solo per deduzione
  (una nota di tabella, una pseudomorfosi).

**Piu' strutture per una forma**: `strutture[]` con `refcode`, `ccdc`,
`temperatura`, `fonte` (SCXRD, PXRD, neutroni, calcolata) e la citazione
[«ZZZEEU01 to ZZZEEU04 ... measured at 90, 100, 110, and 150 K»]. Il refcode
attaccato al numero di un rimando [«SOGUAN0158», «KONTIQ0310/0511»]: si stacca
(SOGUAN01), `refcode_ricostruito: true`, il testo letto in `note`.
`refcode_dedotto` resta «attribuito per ordine». Famiglia di refcode senza voce:
`refcode_famiglia`. Voce del CSD che gli autori dicono sbagliata:
`voce_contestata`. Nella `cella` anche `Z_primo`, `fonte` (le celle da
indicizzazione PXRD non hanno T), `T_scritta` e `T_probabile` quando il PDF
rovina la temperatura [«250 °C», «2105»]. Gruppo in impostazione non standard
o diverso fra testo e tabella: `gruppo_spaziale_numero`.

**Quanto e quanto spesso**
- `osservazioni.variazione_massa` CON SEGNO [«0.68% of weight gain»],
  `frazione_convertita` [«only ca. 25% of form II° transformed»], `conversione`
  chimica [% di prodotto di degradazione, forma non controllata],
  `composizione_prodotto` [«predominantly form A with slight form B»],
  `picchi_dsc` con il segno endo/eso.
- `frequenza`: sempre, di_norma [«normally resulted in»], talvolta
  [«sometimes concomitantly»], una_volta.
- `copertura: parte_non_detta` [«Most of the alcohol solvates were ... labile»]:
  un evento per forma, certezza bassa.
- Piu' valori provati in parallelo [pH 1.2, 4.5, 6.8; «5 or 10 °C/min»]: UN
  evento con `valori: [...]` nella grandezza, non eventi identici.

**Vocabolario nuovo**
- sottovie: `sospensione_competitiva`, `atmosfera_secca_controllata`,
  `secco_senza_mezzo` (0 % RH, mezzo non detto), `gas`, `durante_misura` (la
  forma cambia mentre la si misura: rotore ssNMR), `macinazione` (generica);
- `esito_dettaglio`: dissociazione, disproporzionamento (sale -> base libera:
  natura fisica, `pH_max` nella relazione), incongruente (un cocristallo perde
  un componente), senza_intermedio, solo_contenuto_ospite, nessun_cocristallo;
- meccanismo `via_vapore` [una forma sublima e l'altra cresce], `perdita_componente`;
  integrita' `deformato`; tipo di forma `soluzione_solida` (frazioni non
  stechiometriche in `componenti`); il fuso ammesso come `da`;
- campione: `torta_umida`, crogiolo `alta_pressione` e `capillare` (con
  `sigillato`), `supporto`, `fase_pura`, `semina_involontaria`, `mezzo_incerto`;
- grandezze: `velocita.tipo: salto` [«transferred directly to 453 K»],
  `tempo.tipo: ciclo` [«cycling between 10 and 30 °C»], `tipo: dispersione`
  [«150 to 170 °C ... depending on sample and heating rate»]; `relativo_a` puo'
  essere una lista;
- condizioni: `contenuto_acqua` (%v/v di un solvente misto), `agitazione` (rpm),
  `rapporto_solido_solvente`, `punto_rugiada`, `condizioni_non_raggiunte`;
- relazioni: `temperatura_transizione` come lista di stime con `metodo` e
  `natura` (sperimentale, termodinamica, derivata, stimata); `piu_stabile_fra`
  invece di n coppie identiche; `certezza`, `attribuzione_dedotta`, `pH_max`;
- entalpie: `temperatura_riferimento` [3.15 kJ/mol a 150 °C, 4.02 a 25 °C];
- preparazioni: metodi `semina`, `liofilizzazione`, `spray_drying`,
  `elettrospruzzatura`; `da_evento` anche lista; `componenti_cercati` per le
  preparazioni non ottenute; `agitazione`; `attribuzione_ricostruita`;
- eventi: `passo` (quale processo dentro un picco DSC che ne contiene piu' d'uno),
  `solventi_alternativi`.

**Regole nuove**
1. Calore con RH > 0: la regola v1.3 «riscaldamento con RH → desolvatazione»
   vale per rampe ed essiccamento. In una camera a RH controllata (40 °C/75 %
   RH), e quando il prodotto e' un idrato, la via segue lo scambio d'acqua:
   `umidita` (assorbimento o desorbimento).
2. «Room environment» senza RH: `umidita` con `umidita_ignota`. Durata in stufa,
   vuoto o essiccatore: `tempo.tipo: processo`.
3. Metodi contro risultati a pari dettaglio, o RH in due versioni: vincono i
   risultati con la figura.
4. Controione scritto solo «HBr»: `nome` normalizzato («hydrobromic acid»),
   quello letto in `nome_scritto`. Sale 1:1: l'ospite e' per unita' formula,
   come in v1.3. Stechiometria del sale mai scritta («citrate»): basta il nome.
5. Soglia detta nel testo e valori provati solo nei metodi [«greater than
   67%», con 0/32/43/67/76/98 %]: si estrae la soglia; i valori in `note`.
6. «RT corresponds to 24 ± 2 °C»: si usa il numero, con la citazione della
   definizione. Senza definizione «room temperature» resta senza numero.
7. Punto di fusione dalla sintesi con forma non identificata: `a: fuso`, `da:
   ignota`. Prodotto dedotto dalla sola massa: `osservato: false`.
8. Dissoluzione di una polvere in sospensione: sottovia `sospensione`; il disco
   resta `dissoluzione`.
9. Ripetizione fra laboratori nello stesso articolo: `fonte_dati: riprodotta`
   (in `note` se il valore non e' fra quelli ammessi). Campione commerciale che
   e' una miscela: «misurato batte etichettato».
10. La regola apremilast (niente eventi per forma con un intervallo comune) vale
    solo quando l'unico dato per forma e' il numero. Se il PRODOTTO e' detto per
    ogni forma [«in all cases yielded Form I (Table S27)»], un evento per forma
    con `dettagli_nel_supplementare`.
11. Una condizione regge le frasi coordinate dopo di lei solo se la frase la
    ripete o la richiama («likewise», «similarly», «at the same temperature»);
    altrimenti `condizioni_ambigue`.
12. Un picco DSC con piu' processi [fusione peritettica, evaporazione del
    solvente a 85 °C, cristallizzazione di I sopra 110 °C]: un evento per
    processo, ciascuno col suo `passo`. «Melting/decomposition»: `a: fuso` con
    `prodotti_secondari: ["decomposizione"]`.
13. Gruppo spaziale normalizzato vuol dire scritto bene (P21/n), NON convertito
    all'impostazione standard. `sistema_cristallino` null se il testo da' solo il
    gruppo.
14. Una frase su «tutti i solvati» che a uno si applica male (una forma mai
    stata in acqua madre): si estrae per quella forma con certezza bassa e una
    nota.
15. Disproporzionamento di un sale (cloridrato -> base libera sopra il pHmax):
    natura fisica, `esito_dettaglio: disproporzionamento`.
16. Cristallo misto di diastereomeri o di componenti in proporzione variabile:
    `tipo: soluzione_solida`, frazioni in `componenti` (anche non intere).

## Che cosa porta la v1.3 (idrati, solvati, umidità)

**Ospiti**
- Stechiometria di un sale scritta per unità formula [«2(C21H23N2O2)+·SO42–·5.29(H2O)»]:
  si scrive come nell'articolo (5.29) con `ospite.riferito_a: "unita_formula"`;
  per molecola, `"molecola"` (il caso normale, si può omettere).
- Idrato non stechiometrico [«1.29 to 1.95 molecules of water per DB7»]:
  `ospite.stechiometria_min` / `_max`. Stati di idratazione della stessa fase
  (HyA1.95, HyA1.73, anche con CCDC diversi): forme distinte, e ciascuna punta
  alla fase con `stato_di`; il passaggio fra i due stati resta un evento.
- Frazioni come scritte: `"1/3"`, non 0.3333.
- Perdita di massa in moli [«loss of approximately 3 mol of water per mole»]:
  `perdita_massa` con unità `"mol/mol"`.

**Condizioni**
- Attività dell'acqua e pH sono grandezze, non `altro` [«aw = 0.9, 0.95, and
  1.0», «pH ≥ 6»]: `condizioni.attivita_acqua`, `condizioni.pH` (anche nelle
  preparazioni), senza unità. Il verificatore ne controlla i numeri.
- Crogiolo: `campione.fori` (numero di fori nel coperchio: decide quanto ospite
  esce), `campione.coperchio: false` per un crogiolo senza coperchio,
  `campione.mezzo` per il mezzo intorno al campione [«crystals in silicone oil»:
  sistema chiuso].
- La barra «A/B» [«starting from Hy2/Form III»]: due prove distinte, quindi due
  eventi, a meno che il testo dica che è una miscela; l'altra lettura in
  `lettura_alternativa`.
- RH nota solo come limite [«very dry humidity conditions (<5% RH)»]: resta
  `umidita` con `max: 5` e `limite: "sotto"`; via `desolvatazione` solo con 0 %
  dichiarato o con un essiccante, un gas secco, il vuoto.
- 0 % RH in un analizzatore gravimetrico (DVS) senza essiccante, vuoto o flusso
  detti: via `desolvatazione`, sottovia `atmosfera_secca_controllata`.
- Riscaldamento sopra l'ambiente con un'umidità > 0 [«70 °C ... humidity was
  kept below 10%»]: prevale il riscaldamento, `desolvatazione` / `riscaldamento`
  con `umidita.max`.
- Microonde [«microwave treatment for 5 min ... 700 W»]: sottovia `microonde`,
  con `condizioni.potenza`.
- Vapore di solvente in pressione [«pressure of solvent vapor ... 0.05 MPa»]:
  `pressione.tipo: "vapore"`, mai `applicata`.
- Una disidratazione in crogiolo sigillato (l'acqua resta nel sistema): via
  `termica`. Fusione incongruente di un idrato: `esito_dettaglio: "peritettica"`.

**Osservazioni**
- Più entalpie per lo stesso passaggio (disidratazione misurata, transizione
  derivata, idratazione): lista `osservazioni.entalpie`, una voce per entalpia
  con `tipo`, `grandezza`, `derivata` e la nota di tabella in `nota`.
  `entalpia` resta quella del passaggio dell'evento.
- Cinetica: `modello_cinetico` come scritto (A2, A3, R2, R3, D3, F1...),
  `fattore_frequenza`; meccanismo `confine_di_fase` per R2/R3 e `pseudomorfosi`
  [«turn opaque, but maintain their shape»].
- Tecniche nuove: `VH-PXRD` (PXRD a umidità variabile), `gravimetria`
  (su P2O5 o simili).
- Notazione scientifica che il verificatore non legge, o unità impossibile
  [«21.87 x 10-3 J mol-1»]: il numero in `testo`, e `unita_sospetta: true`.

**Eventi e forme**
- Più prodotti [«form IV and a certain amount of crystal form A»]: `a` è il
  prodotto principale, gli altri in `prodotti_secondari`.
- Una frase riassuntiva già implicata da altri eventi [9 negativi da «none of
  the forms converted»]: gli eventi si estraggono con `generalizzazione: true`.
  Da una tabella di rassegna di lavori citati si prendono le trasformazioni, non
  i punti di fusione.
- Forme attribuite ricostruendo una tabella rimescolata dal PDF:
  `attribuzione_ricostruita: true` anche negli eventi.
- Una forma mai detta «anhydrous» ma senza solvente in formula né perdita in TGA
  [crystal form A, IV, VI]: `anidro` con `tipo_presunto: true`.
- Gruppo spaziale incoerente senza appigli [«P1» con Z = 2]: si scrive come è,
  con `gruppo_spaziale_sospetto: true`.
- Relazione idrato–anidro dichiarata dagli autori [«Form II° is monotropically
  more stable than Forms I, III, and Hy2»]: la parola degli autori va in
  `relazione_scritta`; `relazione` resta `non_dichiarata` se la coppia non è di
  polimorfi. Attività critica fra due idrati [«critical water activity ...
  approximately 13%»]: `relazioni.attivita_critica` (0.13).
- Una forma ottenuta da un altro solido [HyB «prepared by storing HyA at a
  relative humidity ≤12%»]: è un evento, e la sua preparazione ha
  `metodo: "da_evento"` con `da_evento` = l'id dell'evento.
- Confermate dalla v1.2: a parità di fonte il dettaglio più specifico prevale
  (il crogiolo di una didascalia su quello generico dei metodi); un intervallo
  CCDC senza attribuzione alle forme resta in `ccdc` dell'articolo.

## La regola che non si discute

**Ogni valore deve avere una citazione letterale nel testo dell'articolo.** Si
copia la frase (o il pezzo di frase) così com'è, senza parafrasare e **senza
correggere** gli errori, nemmeno quelli della lettura del PDF («B29-form» per
B2'-form, «250 °C» per −50 °C, «P.» per P-1). Il verificatore cerca la
citazione nel testo e respinge l'evento se non la trova. Ogni numero delle
condizioni, delle osservazioni **e delle preparazioni** deve comparire in una
delle citazioni di quell'evento o di quella preparazione (anche in lettere:
«five days» vale 5, «the first day» vale 1; gli zeri finali contano, «2.70» vale
2.7). Un valore dedotto, non scritto, non si mette: si lascia `null` e lo si dice
in `note`. «Room temperature» non diventa 293 K: si scrive `tipo: "ambiente"`
con il numero a `null` [acido acrilico: 293 K era la T della misura in tabella].

Niente conoscenza esterna: niente SMILES ricavati dal nome, niente refcode a
memoria, niente valori «noti» del composto.

## Che cosa è un evento

Un **evento** è un'osservazione riportata di una forma solida che cambia, o che
**non** cambia, sotto una condizione:

- la forma A diventa B (scaldando, raffreddando, in sospensione, macinando, a una
  RH, sotto pressione, sotto luce);
- l'idrato perde l'acqua, l'anidro la prende; il solvato perde il solvente;
- la forma fonde (`a: "fuso"`), decompone (`"decomposizione"`), diventa amorfa
  (`"amorfo"`), reagisce (`"reazione"`: polimerizzazione, reazione topochimica)
  [azobenzene, idrogenomaleati];
- **un negativo** (`esito: "non_avvenuta"`): «did not convert after 4 weeks in
  slurry», «stable up to 200 °C». Se il negativo esclude solo una parte, si dice
  in `esito_dettaglio` (`nessuna_irreversibile`, `nessuna_altra_transizione`)
  [«No irreversible phase transitions ... were induced by the cryogenic bath»].
  I negativi sono dati preziosi: si estraggono sempre.

`parziale` vuol dire: la trasformazione è cominciata ma non si è completata
in quelle condizioni. `non_avvenuta`: nessun cambiamento rilevato.

**Non sono eventi** (vanno in `note` dell'articolo): la transizione vetrosa nel
cristallo, l'ordinamento dell'ospite senza cambio di forma, il disordine che
varia con T o P nella stessa forma [sorbosio a 120 K; acqua di T1 che «si
struttura» con «no thermally induced phase changes»]; l'assenza di un fenomeno
che non è un cambio di forma («do not show ... thermochromism»); la stabilità
chimica in conservazione se la forma non cambia.

**Non è un evento, ma una preparazione**: ottenere una forma cristallizzando da
una soluzione, dal fuso, per sublimazione, o crescendo il cristallo in situ in
cella a pressione. Se si cresce in situ a pressioni diverse e si ottengono forme
diverse, sono preparazioni con la loro `pressione`, non trasformazioni
[eteri: «Single crystals were obtained under isochoric conditions»]. Diventa un
evento solo se si parte da una forma solida e la si vede cambiare. Quando il
testo non dice da che solido si parte, è una preparazione con il dubbio in `note`
[S1 con Fe3+ «change the crystal system from triclinic to monoclinic»]. Coformeri
macinati insieme sono un evento (miscela → cocristallo) solo se il macinato
stesso viene caratterizzato; se poi si cristallizza da soluzione e si analizza
quel cristallo, è una preparazione [NRES: «we ground ... and isolated a
five-component solid-solution cocrystal»]. Un passaggio nell'acqua madre
(«undergoes a crystal transformation from a higher host–guest ratio») è un evento
via `solvente` solo se si sa da quale forma si parte.

Un evento solo calcolato (DFT, MD) non si estrae. Un evento dedotto senza
analizzare il solido (la ricristallizzazione inferita da un calo di
concentrazione in UV-vis) si estrae con `osservato: false`.

**Prove parallele in una frase** («in oven set at 40 °C, 70 °C and 120 °C during
a month»): un evento per valore [fluconazolo]. **Una frase per più forme o
composti** («1–4 appear to be indefinitely stable»): un evento per forma, con
certezza `bassa` se la frase è vaga, `media` se elenca o delimita le forme
[apremilast: «a solid-state transformation did not occur in any of these
cases»]. Ma se il testo dà solo un intervallo per tutte le forme e i valori
puntuali stanno nel supplementare («range from 139°C ... to 190°C ... refer to
the supporting information»), **non** si crea un evento per forma senza
alcun dato suo: si estraggono le due forme agli estremi con il loro valore e il
resto va in `note` dell'articolo [apremilast, 17 fusioni senza valore].

## Pertinente o no

`pertinente: true` se l'articolo riporta almeno un evento sperimentale (anche
negativo, anche solo citato con `fonte_dati: citata`) fra forme solide.
Contano i cristalli **molecolari**: anche un'impalcatura inorganica neutra e
molecolare con ospiti organici [Q8H8, [Si8O12][OH]8 e i suoi solvati]. Non
contano: sali di cluster inorganici senza una molecola organica che faccia
l'impalcatura [anie.201906666], reticoli estesi (MOF, zeoliti, leghe), minerali.
Le rassegne interne (confronti con sistemi di altri lavori) si estraggono solo
se portano un numero o un refcode.

## Reversibilità e verso

L'esito dice che cosa è successo **in quel verso**: `avvenuta`, `parziale`,
`non_avvenuta`. Il valore `reversibile` della v0 non si usa più.

- Se il ritorno ha condizioni sue riportate (isteresi, altra RH, altra T,
  decompressione), **due eventi**, uno per verso, ciascuno con `inverso_di` che
  punta all'altro e `reversibile: true` [CS-834: B2 → B1 a 10% RH, ritorno
  «more than 80%»; composto 1: cicli fra 90 e 170 °C].
- Se l'articolo dice solo «reversible» senza condizioni per il ritorno, **un
  evento** con `reversibile: true`.
- «Reversible» osservato nei due versi **non basta** per dire enantiotropa: la
  relazione si scrive solo se l'articolo la dichiara.
- Una transizione dichiarata **senza verso** («can also induce an enantiotropic
  solid–solid phase transition» fra II e IV): `verso: "ignoto"`, `da` e `a` sono
  la coppia senza ordine.
- **Una sola Ttr senza verso dichiarato** («a Ttr centered at 397 K», curve in
  raffreddamento): un evento per verso misurato, nessun inverso inventato.
- Una frase con due letture: la letterale nei campi, l'altra in
  `lettura_alternativa`, certezza `bassa` [«a monotropic phase transition
  partially occurs by sublimation of I-GABA»].

Relazione `enantiotropa` e transizione osservata irreversibile non si
contraddicono: la prima è termodinamica, la seconda cinetica. Si scrivono
entrambe: la relazione in `relazioni`, il mancato ritorno come evento
`non_avvenuta` con `inverso_di` (che accetta una lista, e vale anche per i
`non_avvenuta`).

## Le forme

Ogni forma citata in un evento va in `forme`, con l'**etichetta dall'occorrenza
più pulita** del testo (l'abstract se il corpo è letto male); le altre scritture
vanno in `etichette_alternative`. Una fase senza nome riceve un'etichetta
descrittiva fra parentesi quadre, es. «[fase fra 259 e 267 K]».

- `tipo` può essere una lista: un sale idrato è `["sale", "idrato"]`.
  `tipo: "non_specificato"` per una forma cristallina mai caratterizzata
  («crystalline PAL», un reagente commerciale).
- **Idrati e solvati: l'acqua o il solvente in `ospite`, MAI in `componenti`.**
  `ospite` è un oggetto o, se gli ospiti sono più d'uno, una lista
  [«1·2DMAc·4THF»]. `ospite.stechiometria` è il numero di molecole di ospite per
  UNA molecola del composto principale: emietanolato 0.5; «the ratio between the
  API and the guest molecule is 2:1» → 0.5.
- **Multicomponente** (sali, cocristalli): `componenti: [{composto,
  stechiometria}]`, stechiometria come nella formula (un cocristallo 2:5 e uno
  1:2 sono forme diverse). Un ospite che a temperatura ambiente è un solido ed è
  stechiometrico (il p-benzochinone in «3D⊃THF·p-benzoquinone») è un coformero:
  va in `componenti`, e la forma è un cocristallo (con il solvente in `ospite`).
- **Sali semplici** (cloridrati, sodici): `componenti` con lo ione attivo e il
  controione come scritti («ambroxol» 1 + «hydrochloric acid» 1, oppure
  «sodium» 1), `tipo: "sale"`; l'etichetta resta quella dell'articolo
  («ambroxol hydrochloride»). Così il collegamento al CSD, che vede due
  componenti, funziona.
- Una **miscela** di forme di partenza (sospensione di D e L, coformeri da
  macinare insieme) è una forma di `tipo: "miscela"` con `forme_componenti` e
  `proporzioni` [«a slurry of d- and l-arabinose crystals in equal parts»]. Un
  picco di una miscela attribuito dagli autori a un componente («reflecting
  dehydration of the monohydrate fraction») ha come `da` la forma del componente,
  con `campione.tipo: "miscela"` e la storia in `pretrattamento` [fluconazolo].
- **Etichetta collettiva** («3′,5′cCMP-H·xH2O (x = 0.25, 3)» quando l'articolo
  non distingue): una forma con `forme_possibili: [F8, F10]`, non una miscela.
- Stessa etichetta ma strutture diverse secondo le condizioni (idrostatica o
  no) → due forme, con una nota [azobenzene «HP» in Ne e senza mezzo].
- `gruppo_spaziale`: SOLO il simbolo normalizzato (P-1, P21/c); se il testo
  letto dice altro, quello va in `gruppo_spaziale_scritto`. Un simbolo rovinato
  dal PDF («crystallizes in the space group P .») si ricostruisce solo con un
  appoggio nel testo (il numero del gruppo, «centrosymmetric» con il sistema):
  `gruppo_spaziale_dedotto: true` e il ragionamento in `note`. Senza appoggio,
  `null`.
- `sistema_cristallino` (triclino, monoclino, ortorombico, tetragonale,
  trigonale, esagonale, cubico) quando il testo lo dice, anche senza gruppo:
  serve al collegamento con le strutture.
- `cella` con tutti i parametri dati (a, b, c, alpha, beta, gamma, V, Z) e in
  `condizioni` T e P della misura. Una cella si attribuisce solo se l'articolo
  la attribuisce. Se il PDF ha rimescolato le colonne di una tabella e
  l'attribuzione si ricostruisce con l'aritmetica (V = abc·…), si scrive con
  `cella_dedotta: true` e il conto in `note` [tabella 1 di cryst11091126].
- `ccdc` e `refcode` per OGNI forma, se una tabella o una frase li attribuisce.
  Dati come intervallo o elenco nello stesso ordine delle forme («cifs for 1-6
  CCDC numbers 984155-984160», «as ELULOV01 and ELUMAC»): si attribuiscono per
  ordine con `ccdc_dedotto: true` (o `refcode_dedotto`). Numeri che non si
  possono attribuire vanno in `ccdc` a livello di articolo [enol-(S)-1: due
  numeri senza dire quale].
- `protonazione`: se distingue la forma. Uno spostamento di protone dentro la
  stessa fase («retaining the C2/c symmetry») non fa una forma nuova, salvo che
  l'articolo la depositi come struttura distinta. Cocristallo → sale è
  `natura: "fisica"`: cambia la forma, non la sostanza.

## I composti

In `nome` il nome chimico COMPLETO in inglese come lo scrive l'articolo
(«1,4-diiodotetrafluorobenzene (14tfib)»), non una sigla da sola e non una
parafrasi. Se il PDF lo ha spezzato («1,2benzothiazine», «− 1-piperazinyl]−»),
`nome` è quello ricomposto e `nome_scritto` quello letto. Una sigla mai sciolta
nel testo (solo in una figura o nel supplementare: «The compounds used in this
study with acronyms are given in Fig. 1») ha `sigla_non_sciolta: true`: senza
nome chimico il collegamento al CSD non si fa. Lo SMILES solo se scritto.
Isotopologhi, enantiomeri e analoghi sono composti diversi, legati da
`analogo_di`.

## La relazione termodinamica è della coppia, non dell'evento

`relazioni` (a livello di articolo): enantiotropa o monotropa fra due forme,
**come la dichiara l'articolo**, con la sua citazione e, se c'è, la temperatura
di transizione. Se l'articolo si contraddice (chiama «monotropic» una
transizione e altrove descrive un'enantiotropia), si riporta quello che dice e
si scrive il conflitto in `conflitto` [composto 1, 1a/1b].

- «Più stabile» dichiarato senza mono/enantiotropia: `relazione:
  "non_dichiarata"` con `piu_stabile`.
- Fra un solvato (o idrato) e il suo non solvato la stabilità dipende
  dall'attività del solvente: non è mono/enantiotropia. Si scrive
  `non_dichiarata` con `piu_stabile` e `condizioni` («in ethanol at 25 °C»)
  [oxicam: «form I is the thermodynamically stable form, whereas form II is
  ... metastable»].
- Una relazione riportata da un altro lavoro: `fonte_dati: "citata"` e
  `riferimento` [ambroxolo, rif. 17].

## Vie e sottovie

| via | sottovie |
|---|---|
| termica | riscaldamento, raffreddamento, isoterma, conservazione, dal_fuso, sublimazione, estrusione_a_caldo |
| solvente | sospensione, vapore, antisolvente, gocce_di_solvente, dissoluzione |
| umidita | assorbimento, desorbimento, conservazione |
| desolvatazione | vuoto, essiccante, flusso_gas, riscaldamento, aria |
| meccanica | macinazione_secca, LAG, compressione |
| pressione | idrostatica, non_idrostatica, uniassiale, DAC, decompressione, grande_volume |
| luce | irraggiamento, raggi_X |
| altro | semina, campo, esposizione_ambiente, altro |

**Confine fra umidità e desolvatazione** [CS-834, T1]: RH maggiore di 0 →
`umidita`; 0 % RH (gel di silice, P2O5), vuoto, gas secco → `desolvatazione`.
La disidratazione per riscaldamento va in `desolvatazione` / `riscaldamento`.
Un solvente organico (o l'acqua) che esce all'**aria** ambiente senza RH detta
→ `desolvatazione` / `aria` [Q8H8: «when the crystals were left in the air, the
guest molecules ... evaporated immediately»; ambroxolo: «MeOH desorption
prevented powder preparation at ambient temperature»]. Un cambio all'apertura
del contenitore con agente ignoto → `altro` / `esposizione_ambiente`.

**Umidità ignota**: una prova d'umidità che non dice la RH di quella frase
(«stable at 40 °C storage conditions» in un protocollo a 32/57/75 %) → via
`umidita`, `umidita: null`, `condizioni.umidita_ignota: true`.

**Dissoluzione** (velocità di dissoluzione intrinseca, disco compresso in un
mezzo): `solvente` / `dissoluzione`, con `campione.tipo: "compressa"`
[apremilast IDR].

**Estrusione a caldo (HME)**: `termica` / `estrusione_a_caldo`, con
`condizioni.estrusione` (`temperatura`, `velocita_vite` in rpm, `carico` in %,
come scritti) [azitromicina: «temperature—150 °C; screw speed—75 rpm; and drug
percentage—25%»].

**Macinazione**: `condizioni.macinazione` con chiavi fisse: `mulino`,
`frequenza_Hz`, `durata` (grandezza, tempo di tipo `processo`), `sfere`,
`liquido`, `eta_uL_mg`. Acqua non voluta in una macinazione «a secco»
(«adsorbed water ... must have enabled the hydrate formation»):
`condizioni.acqua_incontrollata: true`.

Pressione: il mezzo (Ne, Ar, He, N2, olio, nessuno) va in `mezzo_pressione`, e
`idrostatica` dice se lo è. Se il valore dichiarato («up to around 3.1 GPa») e
il primo punto in cui compare la forma nuova («first observed at 3.04 GPa») non
coincidono, si tiene il dichiarato e si scrive l'altro in `conflitto`.

Luce: `condizioni.luce` con `lunghezza_onda`, `dose`, `sorgente`. Il danno da
raggi X durante la misura è via `luce`, sottovia `raggi_X`.

Un evento **citato senza alcuna condizione** («Alkhamis et al. [13] have
reported that polymorph II is ... converted to the more stable polymorph III»):
`via: null` (ammesso solo con `fonte_dati: "citata"`).

## Condizioni

**I numeri si riportano come scritti, con la loro unità**: le conversioni le fa
il codice (`tp.raccogli`), non chi estrae.

- `tipo` dice che cosa è il numero.
  - Temperatura: `onset`, `picco`, `fine`, `equilibrio` (calorimetria
    adiabatica), `osservata` (misura a gradini: la forma nuova è vista a quella
    T), `intervallo`, `isoterma`, `ambiente`, `non_specificato`.
  - Pressione: `transizione`, `misura` (dove è stata risolta la struttura),
    `forchetta` (fra due punti di misura), `applicata` (il vuoto o la pressione
    imposta durante il trattamento: «exposure to reduced pressure (400 Pa) for
    27 h»).
  - Tempo: `trasformazione` (quanto ci mette), `attesa` (dopo quanto si guarda,
    a trattamento fissato), `conservazione`, `processo` (durata di una
    macinazione o estrusione), `osservata` (il primo controllo in cui si vede il
    cambio, con `min` = l'ultimo controllo senza cambio: «after one day we
    noticed the disappearance»).
- Un DSC con inizio, picco e fine usa i campi `onset`, `picco`, `fine` della
  stessa grandezza, MAI min/max con il significato nella nota [enol-(S)-1:
  «peak at 2.2 °C ... started at 2.7 °C and ended at 0.1 °C»].
- Una misura a gradini: `valore` è la T dove si vede la forma nuova; `min`
  l'ultima T senza cambiamento, se c'è.
- Limiti aperti («above 22 % RH», «longer than 5 days», «below −70 °C»): il
  numero in `min` (o `max`) e `limite: "sopra"` (o `"sotto"`). Un intervallo
  dato per tutte le forme vale come limite per ciascuna solo se l'articolo lo
  dice.
- «about», «around», «~»: `circa: true`. Valori interpolati o calcolati dagli
  autori: `derivato: true`. Più picchi per una transizione: `picchi: [486.1,
  492.6]`.
- Numeri non numerici («a few days»): `testo`. Numeri rovinati dal PDF («in the
  temperature range 7784°C»): `valore: null`, la scrittura in `testo`, la lettura
  probabile in `lettura_probabile` (77) e `lettura_probabile_max` (84): il
  verificatore non la conta come numero sostenuto.
- Valori relativi («downward shift ... approximately 33 K» rispetto a un altro
  evento): `relativo_a` (id dell'evento) e `delta`.
- Stessa transizione misurata con tecniche diverse a temperature diverse: **un
  evento per tecnica** se le temperature differiscono, ciascuno con la sua
  tecnica; uno solo se coincidono. Vale anche per i negativi.
- Condizioni rimandate a una frase che non dice quali («we have kept it under
  the same conditions mentioned»): `condizioni_ambigue: true`, certezza `bassa`.
- Negativi senza alcuna condizione («No solid–solid phase transition ... under
  standard conditions over time»): `senza_condizioni: true`.

Solventi: il nome come scritto, con le proporzioni delle miscele. Additivi
(sali, tensioattivi) in `additivi`. Velocità di riscaldamento sempre, se c'è.

## Il campione e la sua storia

- `campione.tipo`: cristallo_singolo, polvere, macinato, film, compressa,
  miscela, altro; `campione.dimensione` e `campione.massa` come scritte («6.58
  mg»); `campione.crogiolo` per DSC e TGA (aperto, chiuso, forato, sigillato):
  per una desolvatazione cambia tutto [«sealed ... pans with perforated lids»
  contro «open aluminum pans»]. Lo stesso esperimento su campioni diversi con
  esiti diversi dà eventi diversi [salinazidi; acido acrilico].
- **Quale campione ha subito quale trattamento**: i cristalli lavati in olio
  per la diffrazione non sono quelli usati per il DSC [enol-(S)-1: «Remaining
  crystals were used for DSC»].
- `pretrattamento`: che cosa ha subito il campione prima («raffreddato a −170
  °C», «ottenuto dalla forma II»); `da_evento`: l'evento precedente della stessa
  corsa, quando l'esito dipende da come ci si è arrivati [BDB: II → IV solo dopo
  il raffreddamento].
- Il prodotto di un esperimento non caratterizzato (una TGA) è `a: "ignota"`,
  salvo che l'articolo lo identifichi; se lo identifica con un altro esperimento
  (il desolvato del vuoto), `a` è quella forma, certezza `media`, e lo si dice in
  `note` [Q8H8].

## Osservazioni e meccanismo

- `tecniche`: DSC, TGA, DTA, VT-PXRD, PXRD, SCXRD, NPD, HSM, DVS, Raman, IR,
  ssNMR, calorimetria_adiabatica, dielettrica, tensimetria, microscopia,
  capillare (punto di fusione in capillare), analisi_chimica (elettroforesi,
  HPLC dei prodotti), altro. Si riportano le tecniche come le attribuisce il
  testo, anche se i metodi le descrivono in un intervallo che non torna; la
  stranezza va in `note`.
- `perdita_massa` (grandezza, unità «%»): quanta massa perde la TGA [«a minor
  mass loss of 3.86 ± 0.08%»; «losses of 7.9 wt % and 10.5 wt %»]. Per le
  desolvatazioni è il dato che dice QUANTO ospite esce: sempre, se c'è.
- `desolvatazione_possibile: true` quando l'articolo chiama «fusione» l'evento
  di un solvato o idrato senza dire se prima perde l'ospite [apremilast].
- `meccanismo` è una **lista**, solo valori affermati o mostrati dall'articolo:
  SCSC, cooperativa, nucleazione_crescita, via_amorfo, via_fuso, via_soluzione,
  termosaliente, ordine_disordine, displaciva, ricostruttiva, martensitica,
  desolvato_isomorfo, topochimico, altro.
- `ordine_transizione`: primo o secondo, se detto. `geminazione: true` se il
  cristallo diventa geminato.
- `integrita`: intatto, degradato, opaco, fratturato, polverizzato, salta.
- `direzione_fronte`: l'asse o la faccia da cui avanza la trasformazione
  [T1: «fronts ... along the channel axes [001]»].
- `entalpia` con `tipo` (transizione, fusione, assorbimento, desolvatazione);
  `energia_attivazione` a parte [T1: «Ea,wr = 41 ± 2 kJ mol−1»].
- Reazioni e decomposizioni osservate durante lo studio di una forma sono
  eventi con `natura: "chimica"`; tutto il resto è `natura: "fisica"`. In una
  reazione in fase solida `da` è la forma caricata; se il testo mostra che alla
  temperatura di reazione c'è già un'altra forma, si estrae anche quel passo e
  si scrive il resto in `conflitto` [cGMP: il pentaidrato a 77 °C è già un'altra
  fase].

## Da dove viene il dato

`fonte_dati`:
- `propria`: misurato in questo articolo;
- `citata`: riportato da un altro lavoro, con `riferimento`;
- `riprodotta`: rimisurato qui un risultato noto;
- `incerta`: la frase rimanda a un riferimento ma la figura è nell'articolo
  [CS-834: «as shown in Fig. 2.10)»].

Un evento `citato` su un altro composto (l'enantiomero, un analogo) usa un
composto a parte: gli enantiomeri sono composti diversi [L-sorbosio].

**Supplementare.** Valori presenti **solo** nel supplementare: l'evento si
estrae con `solo_supplementare: true` e i campi a `null`. Se il testo dà valori
approssimati e quelli precisi stanno nel supplementare («present up to about
40°C ... see the blue lines in Figure S16»), si tengono i valori del testo e si
scrive `dettagli_nel_supplementare: true`. Un lotto apposito li recupererà.

## Certezza

- `alta`: forme, via e condizioni scritte esplicitamente.
- `media`: una parte va letta in una figura o tabella, o è implicita; o una
  frase esplicita che vale per un elenco di forme.
- `bassa`: l'evento si capisce, ma non è chiaro fra quali forme o in che
  condizioni («Probably, this was the desolvation...»).

## Quando l'articolo si contraddice

L'altra versione va **sempre** in `conflitto` (eventi, forme e preparazioni).
Per scegliere, nell'ordine:

1. **Ciò che è misurato batte ciò che è etichettato**: se la parte sperimentale
   chiama «form II» il campione A e PXRD, IR e DSC dicono forma III, vale la
   forma III [fluconazolo: «The diffraction lines of sample A were identical to
   those of crystalline polymorph III»].
2. **Lo specifico batte il generico**: la didascalia della Fig. 5 «PAL–CIT CM at
   95–105 °C» batte il testo «at 80–100 °C» detto per tutti; la descrizione
   puntuale batte il riepilogo [fluconazolo: «we have a transformation of forms
   III and II in monohydrate form» contro «On the sample C ... we noted no
   polymorphic transformation at 50±5%»].
3. **Corpo e tabelle battono abstract e introduzione**; parte sperimentale e
   risultati battono la discussione [sorbosio: «around 210 K» nell'abstract,
   259 e 267 K in tabella].
4. Fra parte sperimentale e risultati vince quella più circostanziata
   («monoclinic plates 5» con la cella discussa, contro «(triclinic) plates 5» in
   un elenco). A parità di dettaglio fra corpo e didascalia, vince il corpo
   [NRES: «The red crystal was identified as the ternary» contro la didascalia
   della Fig. 11].

## Catene e passi intermedi

A → B → C si spezza in due eventi **solo se** le condizioni di ogni passo sono
riportate. Altrimenti un evento A → C, con il passo intermedio in `note`
[CS-834: B2 → B1 «after storage under 10% RH at 25 °C for 2 h», via B2'].

## Dal fuso

La sottovia `termica/dal_fuso` vuol dire: nella stessa corsa la forma A fonde e
il fuso dà la forma B (A → fuso → B osservato). Cristallizzare dal fuso senza una
forma solida di partenza è una preparazione (`metodo: dal_fuso`), con la sua
`velocita` di raffreddamento [BDB: sul vetrino forma II, nel crogiolo DSC a
0,75 °C/min amorfo]. Un amorfo che cristallizza (o no) è un evento `amorfo →
cristallino` con la sua via; non è una desolvatazione anche se avviene su
essiccante.

## Preparazioni

Una frase che vale per più forme dà **una** preparazione con `forme: [...]`.
`citazioni` è una lista, e **anche i numeri delle preparazioni** devono stare
nelle loro citazioni. Se i solventi elencati sono alternative (una prova per
solvente), `solventi_alternativi: true`; se sono una miscela, `false`.

- `metodo`: evaporazione, raffreddamento, antisolvente, diffusione
  (stratificazione, diffusione di vapore: «layered with a saturated toluene
  solution ... so that liquid diffusion takes place»), sospensione (quando non si
  sa da quale solido si parte), sublimazione, dal_fuso, macinazione,
  in_situ_pressione, commerciale, non_specificato («Crystallization of CRES with
  ... resulted in»), altro.
- `esito: "non_ottenuta"` per una preparazione che non dà la forma cercata
  («Upon drying at room temperature ... no co-crystals formed», «did not
  crystallize under the evaporative conditions»): nelle ricerche di cocristalli
  sono dati preziosi.
- `rapporto_soluzione`: il rapporto dei componenti in soluzione, che nei
  cocristalli decide la forma («a 1:3 anhydrate ... is obtained from a solution
  that contains QUE and TMP in a 1:1 ratio»).
- `umidita`, `tempo`, `atmosfera`, `pressione` (vuoto), `pretrattamento` come
  negli eventi («20 °C±2 °C and RH% 50±5 ... during 72 h»).
- `solo_supplementare: true` se il metodo sta solo nel supplementare;
  `conflitto` se didascalia e metodi si contraddicono [grinding nella Fig. 7,
  slow evaporation nei Metodi].

## Il numero e la sua unità

Il verificatore controlla anche che il numero stia ACCANTO alla sua unità: in
«compressed it to 1 GPa, and left it ... for a week» l'«1» non regge `tempo = 1
week`. Elenchi («235.2, 99.9, and 92.8 °C»), intervalli con incertezza («from
112.8 ± 0.5 to 149.8 ± 0.6 °C»), ordinali («on the 2nd day»), «half a month» e
le unità giapponesi (日, 時間, ヵ月) sono riconosciuti. Se il numero c'è ma l'unità
no (tipico delle righe di tabella, dove l'unità sta nell'intestazione), l'evento
passa come `accettato_quasi` e va controllato a mano: non è un rifiuto, è un
segnale. Per una tabella, la citazione buona contiene anche l'intestazione con
l'unità.
