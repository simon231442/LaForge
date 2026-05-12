from datetime import datetime
from pathlib import Path
import json
import sys
from typing import TextIO


def load_config() -> dict: 
    repo_root = Path(__file__).resolve().parent.parent
    config_path = repo_root / "laforge.config.json"

    if not config_path.exists():
        raise FileNotFoundError(f"Config introuvable: {config_path}") 

    with config_path.open("r", encoding="utf-8") as f: 
        return json.load(f) 


def log_file_a_open(project_name: str) -> TextIO:
    """Ouvre en mode append: <log_dir>/log_<nom_du_projet>.txt"""
    cfg = load_config()
    log_dir = Path(cfg["log_dir"])
    log_dir.mkdir(parents=True, exist_ok=True) #est-il possible de lever une exception comme avec config_path.exists

    log_path = log_dir / f"log_{project_name}.txt"
    return log_path.open("a", encoding="utf-8")


def now_str() -> str:
    """Retourne la date au format YYYY-MM-DD HH:MM:SS"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def cmd_start(project_name: str) -> int: #pourquoi retourner un int ?
    """Commande appelée par le terminal"""
    with log_file_a_open(project_name) as f:
        f.write(f"start [{now_str()}]\n")

    cfg = load_config() #ca fait 2 fois qu'on appel load_config, est-ce possible de faire une variable global ? quelle est la bonne pratique ?
    log_path = Path(cfg["log_dir"]) / f"log_{project_name}.txt"#est-ce pour afficher tout le contenu du fichier de log ?
    print(log_path.read_text(encoding="utf-8"), end="")
    return 0


def print_usage() -> None:
    print("Usage: laforge start <nom_projet>")


def main() -> int:u
    # Le script attend exactement 2 arguments utilisateur: la commande et le nom du projet.
    if len(sys.argv) != 3:
        print_usage()
        return 1

    # sys.argv[0] est le nom du script, puis viennent les vrais arguments.
    command = sys.argv[1]
    project_name = sys.argv[2]

    # Route la commande vers la fonction correspondante.
    if command == "start":
        return cmd_start(project_name)

    # Toute commande inconnue affiche l'aide et retourne un code d'erreur.
    print_usage()
    return 1


if __name__ == "__main__":
    # Ce bloc ne s'exécute que si ce fichier est lancé directement (pas importé comme module).
    # SystemExit permet de terminer proprement le programme avec le code renvoyé par main().
    raise SystemExit(main())
