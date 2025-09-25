# To-Do List

Un progetto Python semplice per la gestione di una lista di cose da fare (to-do list) tramite linea di comando.

## Struttura del progetto

- `src/todolist/` — package principale con la logica dell'applicazione
  - `__main__.py` — entrypoint, gestisce il ciclo principale e le interazioni utente
  - `data.py` — funzioni per il salvataggio/caricamento dei task su file JSON
  - `operations.py` — funzioni operative: mostra menu, aggiungi, visualizza, elimina task
  - `__init__.py` — esporta le funzioni principali del package
- `pyproject.toml` — configurazione del progetto
- `tasks.json` — file dati generato automaticamente

## Nozioni teoriche usate

- **Package Python**: uso di `__init__.py` e import relativi per organizzare il codice
- **Gestione file**: lettura/scrittura JSON con gestione errori (`FileNotFoundError`, `JSONDecodeError`)
- **Funzioni**: suddivisione in funzioni per separare la logica (principio di modularità)
- **Gestione input**: ciclo principale con input utente e gestione delle scelte
- **Eccezioni**: uso di `try/except` per gestire errori di input e file

## Nozioni pratiche

- Avvio da linea di comando con `python -m todolist` dalla cartella `src`
- Aggiunta, visualizzazione, eliminazione task tramite menu testuale
- Salvataggio automatico dei dati su file JSON

## Esecuzione

1. Posizionati nella cartella `src`
2. Esegui:
   ```powershell
   python -m todolist
   ```
3. Segui le istruzioni a schermo

## Dipendenze

- Python >= 3.7

## Espansioni possibili

- Gestione avanzata degli errori
- Priorità e scadenze per i task
- Interfaccia grafica
- Test automatici

---
Questo progetto è pensato come esercizio introduttivo per imparare:
- Struttura di un package Python
- Gestione file e dati
- Modularità e best practice
