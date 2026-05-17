from .interactive import run_interactive_test_command
from .config import LaForgeConfig
from pathlib import Path
from datetime import datetime
from typing import TextIO


def now_str() -> str:
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def ensure_log_dir(path: Path) -> None:
	logdir = path / "log"
	logdir.mkdir(parents=True, exist_ok=True)


def log_file_a_open(config: LaForgeConfig) -> TextIO:
	if not config.project_path:
		raise ValueError("project_path n'est pas défini")
	log_file_path = Path(config.project_path) / "log" / f"log_{config.project_name}.txt"
	ensure_log_dir(Path(config.project_path))
	return log_file_path.open("a", encoding="utf-8")


def cmd_start(config: LaForgeConfig) -> None:
	run_interactive_test_command("git pull")
	with log_file_a_open(config) as f:
		f.write(f"start [{now_str()}]\n")


def cmd_stop(config: LaForgeConfig) -> None:
	with log_file_a_open(config) as f:
		f.write(f"stop  [{now_str()}]\n")
	run_interactive_test_command("git status")
	run_interactive_test_command("git add .")
	run_interactive_test_command("git commit -m \"")
