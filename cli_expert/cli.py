#!/usr/bin/env python3
"""CLI entrypoint for the expert LaForge package.""" #la ligne n1 sert elle a quelque chose et si oui, a quoi ??
from __future__ import annotations #montre les endroits dans le code ou cette librairie est utilisée et le terme librairie est-il bien utilisé ici ?

import os # quel genre de fonction puis-je trouver dans cette librairie
import sys # quel genre de fonction puis-je trouver dans cette librairie
from pathlib import Path # quel genre de fonction puis-je trouver dans cette librairie

from .config import LaForgeConfig
from .log import cmd_start, cmd_stop


def print_usage() -> None:
	script_name = Path(sys.argv[0]).name
	print(f"Usage: python {script_name} <start|stop>")


def main() -> int:
	if len(sys.argv) != 2:
		print_usage()
		return 1

	project_name = os.environ.get("laforge_project_name")
	if not project_name:
		raise ValueError("variable d'environnement laforge_project_name non définie")

	project_path = os.environ.get("laforge_project_path")
	if not project_path:
		raise ValueError("variable d'environnement laforge_project_path non définie")

	config = LaForgeConfig(
		command=sys.argv[1],
		project_name=project_name,
		project_path=Path(project_path),
	)

	if config.command == "start":
		cmd_start(config)
	elif config.command == "stop":
		cmd_stop(config)
	else:
		print_usage()
		return 1

	return 0


if __name__ == "__main__":
	raise SystemExit(main())
