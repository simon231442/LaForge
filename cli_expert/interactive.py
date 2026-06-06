from __future__ import annotations

import subprocess # quel genre de fonction puis-je trouver dans cette librairie


def run_interactive_test_command(default_cmd: str) -> int:
	"""Prompt for a shell command, falling back to the default command."""
	try:
		user_cmd = input(f"cmd> [{default_cmd}] ").strip()
	except KeyboardInterrupt:
		print("\nCommande annulée.")
		return 130

	cmd_to_run = user_cmd or default_cmd
	completed = subprocess.run(cmd_to_run, shell=True, check=False)
	return completed.returncode
