#!/usr/bin/env python3
"""CLI entrypoint for copi_LaForge package."""
from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path
from .config import LaForgeConfig
from . import log as logmod
from . import shell as shellmod


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
	p = argparse.ArgumentParser(prog="copi_LaForge", description="LaForge helper: start/stop/install zsh function")
	p.add_argument("command", choices=["start", "stop", "install"], help="action to perform")
	p.add_argument("--name", "-n", dest="name", help="project name (function name). Defaults to cwd name for install or env var for start/stop")
	p.add_argument("--path", "-p", dest="path", help="project path. Defaults to cwd for install or env var for start/stop")
	p.add_argument("--dry-run", dest="dry_run", action="store_true", help="preview install changes")
	p.add_argument("--no-backup", dest="no_backup", action="store_true", help="do not create backup when installing")
	return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
	args = parse_args(argv)
	command = args.command
	if command == "install":
		project_path = args.path or os.environ.get("laforge_project_path") or os.getcwd()
		project_name = args.name or os.environ.get("laforge_project_name") or Path(project_path).name
	else:
		project_name = args.name or os.environ.get("laforge_project_name")
		if not project_name:
			print("Erreur: laforge_project_name non défini; utilisez --name ou exportez laforge_project_name")
			return 1
		project_path = args.path or os.environ.get("laforge_project_path")
		if not project_path:
			print("Erreur: laforge_project_path non défini; utilisez --path ou exportez laforge_project_path")
			return 1
	config = LaForgeConfig(command=command, project_name=project_name, project_path=project_path)
	if command == "start":
		logmod.cmd_start(config)
	elif command == "stop":
		logmod.cmd_stop(config)
	elif command == "install":
		shellmod.install_shell_function(config, dry_run=args.dry_run, backup=(not args.no_backup))
	else:
		print("Usage: start|stop|install")
		return 1
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
