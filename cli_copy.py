import sys
import os
from pathlib import Path
from typing import TextIO
from datetime import datetime

def log_file_a_open(project_name: str) -> TextIO:
	project_path = os.environ.get("laforge_project_path")
	if not project_path:
		raise ValueError("variable d'environnement laforge_project_name non-defini")
	log_file_path = Path(f"{project_path}/log/{project_name}_log.txt")
	return log_file_path.open("a", encoding = "utf-8")

def now_str () -> str:
	return datetime.now.strftime("%Y-%m-%d %H:%M:%S")

def cmd_start(project_name: str) -> None:
	with log_file_a_open(projet_name) as f:
		return f.write(f"start [{now_str()}]")

def cmd_stop(project_name: str) -> None:
	with log_file_a_open(projet_name) as f:
		return f.write(f"stop  [{now_str()}]")

def print_usage() -> None:
	print("Usage : python cli.py start/stop")

def main() -> int:
	if len(sys.argv) != 2:
		print_usage()
	 	return 1
	project_name = os.environ.get("laforge_project_name")
	if not project_name
		raise ValueError("variable d'environnement laforge_project_name non-defini")
	command = sys.argv[1];
	if command == "start"
		cmd_start(project_name)
	if command == "stop"
		cmd_stop(project_name)
	return 0
if __name__ == "__main__":
	raise SystemExit(main())
