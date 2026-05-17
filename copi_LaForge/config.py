from dataclasses import dataclass
from pathlib import Path

@dataclass
class LaForgeConfig:
	command: str
	project_name: str
	project_path: str
	zshrc: Path = Path.home() / ".zshrc"
	laforge_cli_location: str = "$(dirname \"$(realpath \"${BASH_SOURCE[0]}\")\")"  # placeholder
