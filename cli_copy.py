"""
Module de gestion des logs LaForge.

Ce module fournit des fonctions pour enregistrer le démarrage et l'arrêt
des sessions de projet dans des fichiers de log. Il gère l'accès aux fichiers
de log et les timestamps des événements.
"""

# Imports standards
import sys
import os
import subprocess
import readline
from pathlib import Path
from typing import TextIO
from datetime import datetime


def log_file_a_open(project_name: str) -> TextIO:
	"""
	Ouvre le fichier de log d'un projet en mode ajout.
	
	Args:
		project_name: Nom du projet pour lequel ouvrir le fichier de log.
		
	Returns:
		Un objet fichier ouvert en mode ajout (append).
		
	Raises:
		ValueError: Si la variable d'environnement 'laforge_project_path'
					n'est pas définie.
	"""
	project_path = os.environ.get("laforge_project_path")
	if not project_path:
		raise ValueError("variable d'environnement laforge_project_path non-definie")
	log_file_path = Path(project_path) / "log" / f"log_{project_name}.txt"
	return log_file_path.open("a", encoding="utf-8")


def now_str() -> str:
	"""
	Retourne l'heure actuelle au format chaîne de caractères.
	
	Returns:
		Timestamp actuel au format "YYYY-MM-DD HH:MM:SS".
	"""
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def run_interactive_test_command(default_cmd: str = "ls") -> None:
	"""Pré-remplit une commande dans le terminal, laisse l'utilisateur l'éditer, puis l'exécute."""

	def _prefill() -> None:
		readline.insert_text(default_cmd)

	readline.set_startup_hook(_prefill)
	try:
		user_cmd = input("cmd> ").strip()
	except KeyboardInterrupt:
		print("\nCommande annulée.")
		return
	finally:
		readline.set_startup_hook(None)

	cmd_to_run = user_cmd or default_cmd
	subprocess.run(cmd_to_run, shell=True, check=False)


def cmd_start(project_name: str) -> None:
	"""
	Enregistre le démarrage d'une session pour un projet.
	
	Ajoute une entrée "start" avec timestamp dans le fichier de log
	du projet spécifié.
	
	Args:
		project_name: Nom du projet dont on démarre la session.
	"""
	run_interactive_test_command("git pull")
	with log_file_a_open(project_name) as f:
		f.write(f"start [{now_str()}]\n")


def cmd_stop(project_name: str) -> None:
	"""
	Enregistre l'arrêt d'une session pour un projet.
	
	Ajoute une entrée "stop" avec timestamp dans le fichier de log
	du projet spécifié.
	
	Args:
		project_name: Nom du projet dont on arrête la session.
	"""
	with log_file_a_open(project_name) as f:
		f.write(f"stop  [{now_str()}]\n")
	run_interactive_test_command("git status") # faudra proposer d'iterrompre stop
	run_interactive_test_command("git add .") # faudra proposer d'iterrompre stop
	run_interactive_test_command("git commit -m \"") # faudra proposer d'iterrompre stop


def print_usage() -> None:
	"""
	Affiche le message d'utilisation du script.
	
	Affiche la syntaxe correcte pour utiliser ce script.
	"""
	script_name = Path(sys.argv[0]).name
	print(f"Usage : python {script_name} <start|stop>")


def main() -> int:
	"""
	Point d'entrée principal du script.
	
	Traite les arguments en ligne de commande et exécute la commande
	appropriée (start ou stop) pour le projet configuré.
	
	Returns:
		Code de retour: 0 en cas de succès, 1 en cas d'erreur.
		
	Raises:
		ValueError: Si la variable d'environnement 'laforge_project_name'
					n'est pas définie.
	"""
	if len(sys.argv) != 2:
		print_usage()
		return 1
	
	project_name = os.environ.get("laforge_project_name")
	print(project_name)
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
