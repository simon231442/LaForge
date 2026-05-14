stop() {
	python3 $HOME/allRepos/LaForge/cli_copy.py stop
	unfunction stop 2>/dev/null
}

# fct dans zshrc lenovo
#LaForge() {
#  cd "$HOME/allRepos/LaForge" || return
#  export laforge_project_path="$HOME/allRepos/LaForge"
#  export laforge_project_name="LaForge"
#  source "$HOME/allRepos/LaForge/laforge.sh"
#  python3 $HOME/allRepos/LaForge/cli_copy.py start
#}


