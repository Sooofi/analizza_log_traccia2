import json
from collections import defaultdict
from pathlib import Path
from utilities.griglia_di_liste_RO import Tabella2D_RO


def load_logs(path):
    """
    Carica un file JSON contenente i log e restituisce una Tabella2D_RO.

    Parametri:
        path (Path): percorso del file JSON

    Ritorna:
        Tabella2D_RO: tabella bidimensionale contenente i log
    """
    with open(path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    return Tabella2D_RO(raw_data)


def analyze_logs(tabella):
    """
    Analizza la Tabella2D_RO ed estrae, per ciascun utente:
      - la lista degli eventi unici
      - il conteggio dei singoli eventi

    Parametri:
        tabella (Tabella2D_RO): tabella dei log

    Ritorna:
        dict: struttura pronta per essere salvata in JSON
    """
    risultati = defaultdict(lambda: defaultdict(int))

    n_righe, _ = tabella.size()

    for i in range(n_righe):
        riga = tabella.get_riga(i)
        user = riga[1]
        evento = riga[4]
        risultati[user][evento] += 1

    # Conversione in formato compatibile JSON
    output = {
        user: {
            "eventi": list(eventi.keys()),
            "conteggi": dict(eventi)
        }
        for user, eventi in risultati.items()
    }

    return output


def save_results(data, path):
    """
    Salva i risultati ottenuti in un file JSON.

    Parametri:
        data (dict): struttura dati da salvare
        path (Path): file di output
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
