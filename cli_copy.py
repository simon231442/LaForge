import sys
import os
from pathlib import Path
from typing import TextIO
from datetime import datetime

def log_file_a_open(project_name: str) -> TextIO:
	project_path = os.environ.get("laforge_project_path")
	if not project_path:
		raise ValueError("variable d'environnement laforge_project_path non-definie")
	log_file_path = Path(project_path) / "log" / f"log_{project_name}.txt"
	return log_file_path.open("a", encoding = "utf-8")

def now_str () -> str:
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def cmd_start(project_name: str) -> None:
	with log_file_a_open(project_name) as f:
		f.write(f"start [{now_str()}]\n")

def cmd_stop(project_name: str) -> None:
	with log_file_a_open(project_name) as f:
		f.write(f"stop  [{now_str()}]\n")

def print_usage() -> None:
	script_name = Path(sys.argv[0]).name
	print(f"Usage : python {script_name} <start|stop>")

def main() -> int:
	if len(sys.argv) != 2:
		print_usage()
		return 1
	project_name = os.environ.get("laforge_project_name")
	if not project_name:
		raise ValueError("variable d'environnement laforge_project_name non-defini")
	command = sys.argv[1]
	if command == "start":
		cmd_start(project_name)
	elif command == "stop":
		cmd_stop(project_name)
	else:
		print_usage()
		return 1
	return 0
if __name__ == "__main__":
	raise SystemExit(main())
