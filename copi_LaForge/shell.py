import os
import re
import shutil
import tempfile
from pathlib import Path
from .config import LaForgeConfig
from . import __file__ as _pkg_file


def _now_str():
	from datetime import datetime
	return datetime.now().strftime("%Y-%m-%dT%H-%M-%S")


def _atomic_write(path: Path, content: str) -> None:
	dirpath = path.parent
	dirpath.mkdir(parents=True, exist_ok=True)
	fd, tmpname = tempfile.mkstemp(dir=str(dirpath))
	with os.fdopen(fd, "w", encoding="utf-8") as tf:
		tf.write(content)
	Path(tmpname).replace(path)


def _make_shell_block(name: str, project_path: str, laforge_cli_location: str) -> str:
	banner = (
		"/*\n"
		" ,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,\n"
		"  >>           ~ L A F O R G E ~         <<\n"
		" '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'\n"
		" */\n"
	)
	resolved_cli = os.environ.get("laforge_cli_location") or str(Path(_pkg_file).resolve().parent)
	block = (
		f"# LAFORGE BEGIN {name}\n"
		+ banner
		+ f"{name}() {{\n"
		+ f"\tcd \"{project_path}\" || return\n"
		+ f"\texport laforge_project_path=\"{project_path}\"\n"
		+ f"\texport laforge_project_name=\"{name}\"\n"
		+ f"\tsource \"{resolved_cli}/laforge.sh\"\n"
		+ f"\tpython3 \"{resolved_cli}/copi_LaForge/cli.py\" start\n"
		+ f"}}\n"
		+ f"# LAFORGE END {name}\n"
	)
	return block


def install_shell_function(config: LaForgeConfig, dry_run: bool = False, backup: bool = True) -> None:
	zshrc_path = Path(os.path.expanduser(str(config.zshrc)))
	content = zshrc_path.read_text(encoding="utf-8") if zshrc_path.exists() else ""
	name = config.project_name
	block_re = re.compile(rf"(?ms)^# LAFORGE BEGIN {re.escape(name)}.*?# LAFORGE END {re.escape(name)}\n?")
	new_block = _make_shell_block(name, config.project_path, os.environ.get("laforge_cli_location", ""))
	if block_re.search(content):
		new_content = block_re.sub(new_block, content)
		action = "updated"
	else:
		if content and not content.endswith("\n"):
			content += "\n"
		new_content = content + "\n" + new_block
		action = "added"
	if dry_run:
		print(f"[dry-run] Would {action} block for '{name}' in {zshrc_path}")
		print(new_block)
		return
	if backup and zshrc_path.exists():
		bak = zshrc_path.with_name(zshrc_path.name + f".bak_{_now_str()}")
		shutil.copy(zshrc_path, bak)
		print(f"Backup created: {bak}")
	_atomic_write(zshrc_path, new_content)
	print(f"Shell function for '{name}' {action} in {zshrc_path}")
