# Mada Advances — sito web

Sito statico (HTML + CSS) di **Mada Advances**, pronto per essere pubblicato su GitHub con **GitHub Pages**.
Questa versione è pensata per essere **indipendente da Wix**: le immagini vengono salvate in una cartella `images/` dentro il sito.

## Pagine incluse
- `index.html` — Home
- `chisiamo.html` — Chi siamo (team)
- `cosafacciamo.html` — Cosa facciamo
- `eventi.html` — Eventi e partecipazioni
- `contattaci.html` — Contattaci
- `madamagazine.html` — Mada Magazine (articoli in evidenza + link alle categorie)
- `css/style.css` — foglio di stile condiviso
- `images/` — qui vanno le immagini (vedi passo 1)

---

## Passo 1 — Scarica le immagini (da fare UNA volta)

Le pagine cercano le immagini nella cartella `images/`. Per riempirla, apri il Terminale/Prompt dei comandi **nella cartella del sito** e lancia UNO di questi comandi:

**Con Python** (Windows, macOS, Linux):
```bash
python scarica-immagini.py
```
(su alcuni sistemi il comando è `python3`)

**Con bash/curl** (macOS, Linux):
```bash
bash scarica-immagini.sh
```

Al termine, nella cartella `images/` dovresti trovare circa 22 file (logo, foto del team, loghi dei partner, copertine articoli).
La corrispondenza tra ogni file e la sua immagine originale è in `images/MAPPATURA.txt`.

> Se un'immagine non si scaricasse, apri l'URL corrispondente da `MAPPATURA.txt` nel browser e salvala a mano dentro `images/` con lo stesso nome file.

Vuoi controllare subito il risultato? Apri `index.html` con un doppio clic: dovresti vedere il sito completo di immagini.

---

## Passo 2 — Pubblica su GitHub (2 metodi)

### Metodo A — dal sito di GitHub (più semplice, senza programmi)
1. Vai su https://github.com/new e crea un nuovo repository.
   - Nome consigliato: **`carlottajarach.github.io`** (il sito sarà su `https://carlottajarach.github.io/`)
     oppure un nome qualsiasi, es. `mada-advances`.
   - Impostalo su **Public** e crea il repository.
2. Nella pagina del repository: **Add file → Upload files**.
3. Trascina dentro **tutti i file e le cartelle** del sito, **inclusa la cartella `images/` con le immagini già scaricate**.
4. **Commit changes**.
5. **Settings → Pages** → Branch `main`, cartella `/ (root)` → **Save**.
6. Dopo un minuto il sito è online all'indirizzo mostrato in quella pagina.

### Metodo B — da terminale (con git)
```bash
git init
git add .
git commit -m "Sito Mada Advances"
git branch -M main
git remote add origin https://github.com/carlottajarach/NOME-REPO.git
git push -u origin main
```
Poi attiva **Settings → Pages** come al punto 5 del Metodo A.
(Nel pacchetto è già presente un repository git inizializzato; se usi il Metodo B puoi saltare `git init`, `git add`, `git commit` e passare direttamente a collegare il remote e fare `git push`.)

---

## Cosa NON è incluso
Il **blog Mada Magazine** contiene molti articoli singoli (uno per pagina su Wix). Qui è ricostruita la **pagina principale** del magazine con gli articoli in evidenza; i link ai singoli articoli e alle categorie puntano ancora al sito Wix attuale. Migrare ogni articolo è un lavoro a parte: se vuoi, possiamo farlo pagina per pagina.
