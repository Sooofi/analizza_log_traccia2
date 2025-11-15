"""
Script principale per analizzare i log usando Tabella2D_RO.
L'utente inserisce:
- percorso file di input
- percorso file di output
"""

from utilities.processing import load_logs, analyze_logs, save_results
from pathlib import Path

def main():
    print("=== Analisi Log Anonimizzati ===")

    input_path = input("Percorso file JSON di input: ").strip()
    if input_path == "":
        print("Nessun percorso inserito. Uso default: test_simple.json")
        input_path = "test_data/test_simple.json"

    output_path = input("Percorso file JSON di output: ").strip()
    if output_path == "":
        output_path = "output.json"

    try:
        tabella = load_logs(Path(input_path))
        risultati = analyze_logs(tabella)
        save_results(risultati, Path(output_path))
        print(f"Risultati salvati in: {output_path}")
    except Exception as e:
        print(f"Errore durante l'analisi: {e}")
    save_results

if __name__ == "__main__":
    main()
