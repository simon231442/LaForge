# cli_expert

Version refactorisée de LaForge avec une séparation simple des responsabilités:

- `cli.py` pour l'entrée CLI
- `config.py` pour la configuration
- `log.py` pour la logique de journalisation
- `interactive.py` pour l'exécution interactive des commandes

Cette version garde `now_str()` comme fonction module, pas comme méthode, car elle ne dépend pas de l'état d'un objet.
