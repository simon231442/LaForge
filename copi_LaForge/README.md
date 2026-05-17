copi_LaForge
=============

Single-folder refactor of LaForge utilities.

Usage:

Install shell function (dry-run):

```bash
python3 -m copi_LaForge.cli install --name MyProj --dry-run
```

Actually install (creates backup):

```bash
python3 -m copi_LaForge.cli install --name MyProj
```

Start / stop (requires env vars or pass --name/--path):

```bash
export laforge_project_name=MyProj
export laforge_project_path=$HOME/allRepos/MyProj
python3 -m copi_LaForge.cli start
```
