def run_interactive_test_command(default_cmd: str = "ls") -> None:
	"""Pré-remplit une commande, laisse l'utilisateur l'éditer, puis l'exécute."""
	try:
		import readline
		def _prefill() -> None:
			readline.insert_text(default_cmd)
		readline.set_startup_hook(_prefill)
	except Exception:
		pass
	try:
		user_cmd = input("cmd> ").strip()
	except KeyboardInterrupt:
		print("\nCommande annulée.")
		return
	finally:
		try:
			readline.set_startup_hook(None)
		except Exception:
			pass
	cmd_to_run = user_cmd or default_cmd
	import subprocess
	subprocess.run(cmd_to_run, shell=True, check=False)
