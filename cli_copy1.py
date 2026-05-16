import sys
import os
import subprocess
import readline
from pathlib import Path
from typing import TextIO
from datetime import datetime

""" commande start et stop """
def cmd_start(project_name: str) -> None:
	with log_file_a_open(project_name) as f
		f.write(f"start [{now_str()}]\n")

def cmd_stop(project_name: str) -> None:
	with log_file_a_open(project_name) as f
		f.write(f"stop  [{now_str()}]\n")

def log_file_a_open(project_name) -> TextIO:
	project_path=os.environ.get("laforgeproject_path")
	if not project_path:
		raise ValueError("undefined environnement variable laforge_project_path")
	log_path = Path(project_path / "log" / f"log_{project_name}.txt")
	return log_path.open("a", encoding="utf-8")

def now_str() -> str:
	return datetime.now.strftime(%Y-%m-%d %H:%M:%S)

def cmd_sync() -> none:

def run_interactive_command(command: str) -> None:
	def _prefill() -> None:
		readline.insert_text(command)
	readline.set_startup_hook(_prefill)
	try:
		user_cmd = input("cmd> ").strip()
	except KeyboardInterrupt:
		print("\nCommand canceled.")
		return
	finally:
		readline.set_start_up_hook(None)
	cmd_to_run = user_cmd
	subprocess.run(cmd_to_run, shell=True, check=False)


def	print_usage() -> None:
	print(f"Usage : python {script_name} <start|stop")

def main() -> int:
	if not len(sys.argv) == 2:
		print_usage()
	project_name = os.environ.get("laforge_project_name")
	if not project_name:
		raise ValueError("undefined environnement variable laforge_project_name")
	command = sys.argv[1]
	if command == "start":
		cmd_start(project_name)
	elif command == "stop":
		cmd_stop(project_name)
	else:
		print_usage()
		return 1
	return 0

if __name__ == "__main__"
	raise SystemExit(main())

