# log_file_a_open	: fonction qui ouvre en mode append le fichier du projet corespondant : log/log_<nom_du_projet>.txt
# now_str			: fonction qui retourne "%Y-%m-%d %H:%M:%S"
# cmd_start			: fonction qui est appeler par le terminal
from datetime import datetime
from pathlib import Path
from typing	import TextIO
import sys
import json
import os

def now_str() -> str:
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	
#def load_config() -> dict:
#	project_path = os.environ.get("laforge_project_path")
#	if not project_path:
#		raise ValueError("Variable d'environnement 'laforge_project_path' non définie")
#	config_path = Path(project_path) / "LaForge.config.json"
#	if not config_path.exists():
#		raise FileNotFoundError(f"Config not found: {config_path}")
#	with config_path.open("r", encoding="utf-8") as f:
#		return json.load(f)

def log_file_a_open(project_name: str) -> TextIO:
#	cfg = load_config()
#	log_key = f"{project_name}_log_path"
#	if log_key not in cfg:
#		raise KeyError(f"La clé '{log_key}' est introuvable dans la configuration.")
	project_path = os.environ.get("laforge_project_path")
	if not project_path:
		raise ValueError("Variable d'environnement 'laforge_project_path' non définie")
	log_path = Path(project_path + "log/log_{project_name}.txt")
	return log_path.open("a", encoding="utf-8")
	
def cmd_stop(project_name: str) -> int:
	with log_file_a_open(project_name) as f:
		f.write(f"stop  [{now_str()}]\n")
	return 0

def cmd_start(project_name: str) -> int:
	with log_file_a_open(project_name) as f:
		f.write(f"start [{now_str()}]\n")
	return 0

def print_usage() -> None:
	print("Usage: python cli.py <start|stop>")

def main() -> int:
	if len(sys.argv) != 2:
		print_usage()
		return 1
	project_name = os.environ.get("laforge_project_name")
	if not project_name:
		raise ValueError("Variable d'environnement 'laforge_project_name' non définie")
	command = sys.argv[1]
	if command == "start":
		return cmd_start(project_name)
	if command == "stop":
		return cmd_stop(project_name)
	print_usage()
	return 1

if __name__ == "__main__":
	raise SystemExit(main())
