# Address Book

Un semplice progetto Python per la gestione di una rubrica contatti da linea di comando.

## Struttura del progetto

- `src/addressbook/` — package principale con la logica dell'applicazione
  - `__main__.py` — entrypoint, gestisce il ciclo principale e le interazioni utente
  - `data.py` — funzioni per il salvataggio/caricamento dei contatti su file JSON
  - `operations.py` — funzioni operative: mostra menu, aggiungi, visualizza, elimina contatti
  - `__init__.py` — esporta le funzioni principali del package
- `pyproject.toml` — configurazione del progetto (es. livello di logging)
- `contacts.json` — file dati generato automaticamente

## Nozioni teoriche usate

- **Package Python**: uso di `__init__.py` e import relativi per organizzare il codice
- **Gestione file**: lettura/scrittura JSON con gestione errori (`FileNotFoundError`, `JSONDecodeError`)
- **Logging**: utilizzo del modulo `logging` per tracciare le operazioni invece di `print`
- **Configurazione**: lettura del livello di logging da `pyproject.toml` (tramite `tomli`)
- **Funzioni**: suddivisione in funzioni per separare la logica (principio di modularità)
- **Gestione input**: ciclo principale con input utente e gestione delle scelte
- **Eccezioni**: uso di `try/except` per gestire errori di input

## Nozioni pratiche

- Avvio da linea di comando con `python -m addressbook` dalla cartella `src`
- Aggiunta, visualizzazione, eliminazione contatti tramite menu testuale
- Salvataggio automatico dei dati su file JSON
- Logging configurabile tramite file di progetto

## Esecuzione

1. Posizionati nella cartella `src`
2. Esegui:
   ```powershell
   python -m addressbook
   ```
3. Segui le istruzioni a schermo

## Dipendenze

- Python >= 3.7
- tomli (per lettura TOML)

## Espansioni possibili

- Gestione avanzata degli errori
- Interfaccia grafica
- Ricerca e filtro contatti
- Test automatici

---
Questo progetto è pensato come esercizio introduttivo per imparare:
- Struttura di un package Python
- Gestione file e dati
- Logging e configurazione
- Modularità e best practice
