# Istruzioni per l'estrattore (persona o LLM) — schema v1.4

Cartella del progetto: `C:\Users\giova\Documents\Documenti_Only_Local\Python_CSP\Mace\LLM\Transform_Prior`
(tutti i comandi si lanciano da lì, con `PYTHONIOENCODING=utf-8`).

## Prima di cominciare, leggi

1. `estrazione/linee_guida.md` — che cosa è un evento, una preparazione, le vie,
   i casi difficili, chi prevale quando l'articolo si contraddice. **Vincolante.**
   Le novità della v1.4 (la molecola, le sospensioni competitive, i dubbi
   dichiarati) sono nella prima sezione; quelle della v1.3 (idrati, solvati,
   umidità) nella seconda.
2. `estrazione/schema_estrazione.json` — il formato (v1.4).
3. `estrazione/prove/bap_iucrj2025.json` — un esempio completo e verificato,
   nel formato v1.2 (valido anche in v1.4; i campi nuovi della v1.4 non ci sono).

Ogni file nuovo comincia con `"versione_schema": "v1.4"`.

## Novità della v1.4 da non dimenticare

- **La molecola**: un blocco `molecole` con le proprietà DICHIARATE nel testo
  (pKa, solubilità, logP, igroscopicità...) e i fatti dichiarati (tautomeria,
  zwitterione, flessibilità, chiralità), ciascuno con la sua frase. Niente
  valori calcolati da te o presi da altre fonti.
- **`gruppi_coinvolti` in ogni evento** in cui l'articolo dice quali gruppi o
  sintoni partecipano alla trasformazione, con il gruppo COME SCRITTO e la frase.
  E i `motivi_hb` delle forme. Leggi con attenzione le sezioni di struttura e di
  discussione: è lì che gli autori lo spiegano.
- Sospensioni competitive, `da_possibili`/`a_possibili`, più strutture per forma
  (`strutture`), refcode attaccati ai rimandi (`refcode_ricostruito`),
  `frequenza`, `frazione_convertita`, `variazione_massa` con segno, `valori`
  per le prove parallele: vedi le linee guida.

## Per ogni DOI assegnato

1. Trova il testo:
   `python -c "from tp.comune import LETTI,nome_file; print(LETTI/(nome_file('<DOI>')+'.json'))"`
   e leggilo TUTTO (titolo, abstract, sezioni, figure con didascalie, tabelle).
   Le condizioni stanno spesso nelle didascalie delle figure di DSC/TGA/PXRD e
   nella parte sperimentale.
2. Scrivi l'estrazione in
   `estrazione/<lotto>/<nome>.json`, dove `<nome>` è
   `python -c "from tp.comune import nome_file; print(nome_file('<DOI>').replace('/','__'))"`.
3. Verifica **solo i tuoi file, uno per uno**:
   `python -m tp.verifica estrazione/<lotto>/<nome>.json`. Mai `--cartella`:
   riscrive le verifiche degli altri estrattori che lavorano in parallelo.
   Se un evento o una preparazione è `respinto`:
   - citazione assente → ricopia la frase ESATTAMENTE dal testo letto (anche se
     contiene refusi, simboli strani o «▸»); non parafrasare;
   - numero che non compare → aggiungi la citazione che lo contiene, oppure
     togli il numero (mettilo `null`) se nel testo non c'è. Vale anche per le
     preparazioni: «room temperature» non è 293 K;
   - forma o evento non dichiarato (`da`, `a`, `da_evento`, `inverso_di`,
     `forme_possibili`) → dichiaralo.
   Ripeti finché niente è respinto. Se un evento non si riesce a sostenere con
   il testo, si toglie.
4. Non inventare MAI: niente valori dedotti, niente refcode a memoria, niente
   conoscenza esterna sull'articolo o sul composto. Se l'articolo non contiene
   eventi sperimentali, `pertinente: false` con `motivo_non_pertinente`, ed
   `eventi: []` (le `preparazioni` si estraggono comunque, se ci sono).

## Gli errori già visti (non ripeterli)

- Idrati e solvati: l'acqua o il solvente in `ospite` (anche una lista), MAI in
  `componenti`. `ospite.stechiometria` = molecole di ospite per UNA molecola del
  composto principale (emietanolato: 0.5).
- DSC con inizio, picco e fine: i campi `onset`, `picco`, `fine`, non min/max.
- TGA: la perdita di massa in `osservazioni.perdita_massa` (in «%»).
- `campione` (tipo, massa, crogiolo) e `pretrattamento`: attento a QUALE campione
  ha subito QUALE trattamento.
- I negativi (la trasformazione NON avviene) si estraggono sempre.
- Un intervallo dato per tutte le forme, con i valori puntuali nel
  supplementare: niente eventi vuoti per forma (vedi le linee guida).
- Un numero CCDC si attribuisce a una forma solo se il testo lo fa (o per ordine,
  con `ccdc_dedotto: true`); altrimenti va in `ccdc` dell'articolo.
- (v1.3) Attività dell'acqua e pH in `attivita_acqua` / `pH`, non in `altro`;
  fori del crogiolo in `campione.fori`; RH data solo come limite («<5% RH») resta
  `umidita` con `limite`; idrati non stechiometrici con `stechiometria_min/max`;
  più prodotti in `prodotti_secondari`; frasi riassuntive con
  `generalizzazione: true`.
- Il solvente di un solvato col suo nome chimico in `ospite.specie`
  («tetrahydrofuran (THF)»): il collegamento al CSD confronta il solvente.

## Per il collegamento alle strutture (tp.collega)

Ogni forma estratta va poi ritrovata fra le strutture del CSD, e ci si riesce
solo con quello che l'articolo scrive. Quindi, quando il testo li dà:

- **Composti**: in `nome` il nome chimico COMPLETO in inglese come lo scrive
  l'articolo (es. «1,4-diiodotetrafluorobenzene (14tfib)»), non una sigla da
  sola e non una parafrasi in italiano. Nome spezzato dal PDF: ricomposto in
  `nome`, quello letto in `nome_scritto`. Sigla mai sciolta nel testo:
  `sigla_non_sciolta: true`. Lo SMILES solo se scritto.
- **Forme a un componente**: `composto`. **Sali e cocristalli**: `componenti` con
  `composto` e `stechiometria` per ogni componente (un cocristallo 2:5 e uno 1:2
  sono forme diverse; un cloridrato è il farmaco + «hydrochloric acid»).
- **`gruppo_spaziale`**: SOLO il simbolo normalizzato (`P-1`, `P21/c`). Dubbi,
  refusi del PDF e note vanno in `gruppo_spaziale_scritto` o `note`, mai qui.
  **`sistema_cristallino`** sempre, se detto.
- **`cella`**: tutti i parametri che il testo dà (a, b, c, alpha, beta, gamma,
  V, Z) e in `condizioni` temperatura e pressione della misura.
- **`ccdc`** e **`refcode`**: per OGNI forma il suo numero, se una tabella o
  una frase lo attribuiscono (spesso nella parte sperimentale o in una tabella
  cristallografica).
- **`etichetta`**: come la chiama l'articolo («form II», «β», «HT phase»);
  altri nomi in `etichette_alternative`.

## Che cosa NON fare

- Non modificare codice, schema, linee guida o altri file: scrivi solo i tuoi
  file di estrazione (gli script di aiuto vanno nella tua cartella temporanea).
- Non scaricare niente, non usare internet.

## Il rapporto finale (breve)

Per ogni DOI: pertinente sì/no, numero di eventi per via ed esito, preparazioni,
esito della verifica (accettati / quasi / respinti). Poi, **la parte più utile**:
i punti in cui schema o linee guida non bastavano o erano ambigui (casi reali,
con la frase dell'articolo), e che cosa proporresti di cambiare.
