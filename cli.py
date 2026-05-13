# log_file_a_open	: fonction qui ouvre en mode append le fichier du projet corespondant : log/log_<nom_du_projet>.txt
# now_str			: fonction qui retourne "%Y-%m-%d %H:%M:%S"
# cmd_start			: fonction qui est appeler par le terminal
from datetime import datetime
from pathlib import Path
from typing	import TextIO
import sys
import json

def now_str() -> str:
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S");
	
def load_config() -> dict:
	config_path = Path(__file__).parent / "LaForge.config.json"
	print(f"{config_path}")
	if not config_path.exists():
		raise FileNotFoundError(f"Confi not found: {config_path}")
	with config_path.open("r", encoding="utf-8") as f:
		return json.load(f)

def log_file_a_open(project_name: str) -> TextIO:
	cfg = load_config()
	log_path = Path(cfg[project_name + "_log_path"])
	return log_path.open("a", encoding="utf-8")
	
def cmd_stop(project_name: str) -> int:
	with log_file_a_open(project_name) as f:
		f.write(f"stop  [{now_str()}]\n")

def cmd_start(project_name: str) -> int:
	with log_file_a_open(project_name) as f:
		f.write(f"start [{now_str()}]\n")

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
	if command == "stop":
		return cmd_stop(project_name)
	print_usage()
	return 1

if __name__ == "__main__":
	raise SystemExit(main())
