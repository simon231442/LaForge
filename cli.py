# log_file_a_open	: fonction qui ouvre en mode append le fichier du projet corespondant : log/log_<nom_du_projet>.txt
# now_str			: fonction qui retourne "%Y-%m-%d %H:%M:%S"
# cmd_start			: fonction qui est appeler par le terminal
python
from datetime import datetime
from pathlib import path
from typing	import TextIO
import sys

def load_log_path() -> dict:
	config_path = path(__file__) / "LaForge.config.json"
	if not config_path.exists():
		raise FileNotFounError(f"Confi not found: {config_path}")
	with config_path.open("r", encoding="utf-8") as f:
		return json.load(f)

def log_file_a_open(project_name: str) -> TextIO:
	cfg = load_config()
	log_path = cfg["log_dir"]
	return log_path.open("a", encoding="utf-8")
	

def cmd_start(project_name: str) -> int:
	with log_file_a_open(project_name)


def	print_usage() -> None:
	print("Usage: laforge start <nom_projet>")

def main() -> int:
	if len(sys.argv) != 3:
		print_usage()
		return 1
	command = sys.argv[1]
	project_name = sys.argv[2]
	if command == "start":
		return cmd_start(project_name)
	print_usage()
	return 1

if __name__ == "__main__"
	raise SystemExit(main())
