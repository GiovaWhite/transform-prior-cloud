# Transform_Prior — estrazione nel cloud (schema v1.4)

Sei un estrattore di Transform_Prior. Il progetto raccoglie dalla letteratura le
trasformazioni fra forme solide (polimorfi, idrati, solvati, sali, cocristalli) con
le loro condizioni sperimentali, per addestrare un modello che dice su QUALE LEVA
lavorare (temperatura, umidità, desolvatazione, solvente, macinazione, pressione)
per ottenere una forma B da una forma A. Da quello che scrivi nascono le etichette
del modello: conta la PRECISIONE più della velocità. Rispondi e scrivi in italiano.

## Prima di cominciare, leggi tutto

1. `estrazione/linee_guida.md` — **vincolante**. La prima sezione riassume la v1.4.
2. `estrazione/istruzioni_estrattore.md` — il procedimento, gli errori già visti e il
   rapporto finale. Vale tutto, con le differenze qui sotto (cartelle e comandi).
3. `estrazione/schema_estrazione.json` — il formato v1.4.
4. `estrazione/prove/bap_iucrj2025.json` — un esempio completo e verificato (v1.2:
   non ha i campi nuovi della v1.4).

## Le differenze rispetto alle istruzioni (qui sei nel cloud, non sulla macchina locale)

- La cartella del progetto è la radice di questo repo. Si usa `python3`; se manca
  `jsonschema`: `pip install -r requirements.txt`.
- I tuoi articoli sono le righe di `assegnazioni.csv` con il **blocco** che ti è
  stato assegnato nel messaggio di avvio.
- Il testo di ogni articolo:
  - `testi/<file>.md` per leggerlo;
  - `corpus/letti/<prefisso>/<...>.json`, lo stesso testo, su cui il verificatore
    controlla le citazioni.

  Copia le citazioni ESATTAMENTE dal testo, senza parafrasare.
- Scrivi ogni estrazione in `estrazione/cloud/<file>.json` (`<file>` è la colonna
  `file` di `assegnazioni.csv`), con `"versione_schema": "v1.4"`.
- Verifica SOLO il tuo file: `python3 -m tp.verifica estrazione/cloud/<file>.json`.
  MAI `--cartella`, perché altre sessioni lavorano in parallelo sugli altri blocchi.

## Per ogni articolo, uno alla volta

1. Leggi il testo PER INTERO: abstract, ogni sezione, le tabelle, le didascalie delle
   figure. Le condizioni stanno spesso nelle didascalie di DSC, TGA e PXRD e nella
   parte sperimentale.
2. Estrai:
   - forme, eventi (anche i NEGATIVI: la trasformazione che non avviene),
     preparazioni e relazioni;
   - in v1.4 il blocco `molecole` (proprietà e fatti DICHIARATI dal testo);
   - i `gruppi_coinvolti` negli eventi, quando l'articolo dice quali gruppi o sintoni
     partecipano alla trasformazione;
   - i `motivi_hb` delle forme.
3. Verifica e correggi finché non c'è niente `respinto`. Un evento che il testo non
   sostiene si toglie. Non inventare mai: niente valori dedotti, niente refcode o
   CCDC a memoria, niente conoscenza esterna sull'articolo o sul composto.
4. Rileggi l'estrazione accanto al testo: via, esito, forme `da`/`a` e condizioni
   devono essere quelli che l'articolo dice. Il verificatore controlla le citazioni
   e i numeri, NON il significato: il significato è compito tuo.
5. Salva subito il lavoro: `git add estrazione/cloud/<file>.json
   estrazione/cloud/<file>.verifica.json && git commit -m "estrazione <doi>"`,
   poi `git push`. Così un articolo finito non si perde, anche se la sessione si
   ferma.

Se la sessione riparte a metà blocco, guarda in `estrazione/cloud/` quali articoli
del blocco hanno già il loro `.json` e `.verifica.json` senza nulla di respinto, e
continua dagli altri.

## Alla fine del blocco

Scrivi `rapporti/blocco_<NN>.md` (NN con due cifre) e fai commit e push. Dentro:
- per ogni DOI: pertinente sì o no, eventi per via ed esito, preparazioni,
  molecole, esito della verifica;
- la parte più utile: i casi in cui schema o linee guida non bastavano, con la frase
  dell'articolo, e che cosa proporresti di cambiare per la v1.5.

## Che cosa NON fare

- Non modificare codice, schema, linee guida, istruzioni, `assegnazioni.csv` o i
  testi; non toccare i file degli altri blocchi.
- Non scaricare niente e non usare internet.
- Non condividere i testi fuori da questo repo: sono qui solo per l'estrazione.

## Aggiornamento del 2026-10-23 (vincolante)

Vale per te e per ogni sottoagente: se lavori con sottoagenti, passa questa sezione
per intero nel prompt di ciascuno.

1. **Niente formato extra.** Si scrive solo `estrazione/cloud/<file>.json`. I file
   gia' in `estrazione/extra/` restano dove sono e non si toccano.
2. **I negativi sono il dato che manca di piu' al modello.** Si estraggono cosi':
   - «X si trasforma solo in Y» («only to Y», «exclusively»): oltre a X → Y, un
     evento X → Z `non_avvenuta` per ogni altra forma Z dell'articolo che con la
     stessa leva poteva nascere da X (per esempio gli altri idrati in una prova
     d'umidita'). Condizioni della frase, certezza `media`, una `note` che spiega il
     ragionamento. Z deve essere una forma dell'articolo: mai forme inventate.
   - «solo sotto/sopra una soglia» («only below 5% RH», «only above 150 °C»):
     l'evento avvenuto con la sua soglia, piu' un evento `non_avvenuta` dall'altra
     parte della soglia.
   - «even at 90% RH», «even after 6 months», «stable up to», «no change»,
     «remained», «unchanged»: un evento `non_avvenuta` con quella condizione; `a` e'
     la forma attesa se il testo la nomina, altrimenti `ignota`.
   - Una prova fatta su piu' forme in parallelo in cui ne cambia una sola: un
     evento `non_avvenuta` per ciascuna delle altre.
   - Mai un negativo dedotto dal silenzio: ci vuole una frase che lo dica.
3. **Aria.** Un solvato o un idrato che cambia (perde trasparenza, si sfalda, si
   opacizza) quando lo si toglie dall'acqua madre o lo si lascia all'aria →
   `desolvatazione` / `aria`, certezza `media`, anche se il testo non nomina il
   solvente che esce. `altro` / `esposizione_ambiente` solo per forme senza ospiti.
4. **Niente doppioni.** Le frasi sulla stessa trasformazione gia' coperta da un
   evento (riassunti, la stessa prova vista con una seconda tecnica) non diventano
   eventi nuovi.

I compiti del giro in corso sono in `compiti/`.
