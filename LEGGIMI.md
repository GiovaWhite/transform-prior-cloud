# Transform_Prior nel cloud: come si usa

Questo pacchetto contiene:
- **167 articoli da estrarre**, tutti ad accesso aperto, già nel corpus locale;
- le istruzioni e lo schema **v1.4**;
- il verificatore.

Non contiene dati del CSD né la configurazione locale. Va caricato in un repo GitHub
**PRIVATO**: i testi servono solo all'estrazione e non vanno ridistribuiti.

## 1. Caricarlo (una volta)

Su GitHub crea un repo **privato** vuoto, per esempio `transform-prior-cloud`. Poi,
da questa cartella:

```
git init -b main
git add .
git commit -m "pacchetto di estrazione v1.4"
git remote add origin https://github.com/<tuo-utente>/transform-prior-cloud.git
git push -u origin main
```

## 2. Il blocco di prova (prima di tutto)

Il **blocco 0** ha 3 articoli. Due li abbiamo già estratti in locale (acido
β-resorcilico e troglitazone) e servono a confrontare la qualità; il terzo è nuovo.

Apri una sessione di Claude Code nel cloud sul repo, scegli **Sonnet 5.5** con
sforzo **xhigh**, e scrivi:

> Lavora sul blocco 0 di `assegnazioni.csv`, seguendo `CLAUDE.md`. Un articolo alla
> volta: leggi, estrai, verifica, rileggi, commit e push. Alla fine scrivi il
> rapporto del blocco.

Quando ha finito, in locale si confronta il suo risultato con il nostro e si misura
quanto è costato. Se la qualità regge, si passa ai blocchi veri.

## 3. I blocchi 1–33 (5 articoli ciascuno, 4 l'ultimo)

Una sessione per blocco, con lo stesso messaggio e il numero del blocco. Più sessioni
possono girare insieme: ognuna scrive solo i file dei suoi articoli. I blocchi sono in
ordine di priorità, cioè prima gli articoli che citano più leve, perché danno più
negativi.

## 4. Riportare i risultati in locale

Ogni sessione fa commit sul suo ramo, o su `main`. In locale:

```
git fetch --all
```

Poi, nel progetto Transform_Prior:

```
python estrazione/bozze/importa_cloud.py <questa cartella>
```

Copia le estrazioni accettate in `estrazione/cloud/` del progetto. Lì passano per
verifica, raccolta, collegamento al CSD, impronte, database e i due file finali.

## Che cosa c'è dentro

| | |
|---|---|
| `CLAUDE.md` | le istruzioni che ogni sessione legge da sola |
| `assegnazioni.csv` | blocco, DOI, file, titolo, leve citate |
| `testi/*.md` | i testi da leggere |
| `corpus/letti/` | gli stessi testi in json, per il verificatore |
| `estrazione/` | linee guida, istruzioni, schema v1.4, esempio; `cloud/` riceve le estrazioni |
| `tp/verifica.py` | il verificatore (`python3 -m tp.verifica <file>`) |
| `rapporti/` | un rapporto per blocco |
