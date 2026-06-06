from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import TextIO

from .config import LaForgeConfig
from .interactive import run_interactive_test_command


def now_str() -> str:
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_file_path(config: LaForgeConfig) -> Path:
	return config.project_path / "log" / f"log_{config.project_name}.txt"


def append_log_entry(config: LaForgeConfig, entry: str) -> None:
	path = log_file_path(config)
	path.parent.mkdir(parents=True, exist_ok=True)
	with path.open("a", encoding="utf-8") as file:
		file.write(f"{entry} [{now_str()}]\n")


def cmd_start(config: LaForgeConfig) -> None:
	run_interactive_test_command("git pull")
	append_log_entry(config, "start")


def cmd_stop(config: LaForgeConfig) -> None:
	append_log_entry(config, "stop")
	run_interactive_test_command("git status")
	run_interactive_test_command("git add .")
	run_interactive_test_command('git commit -m "')
