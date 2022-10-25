eval "$(starship init zsh)"

alias grep="rg"
alias ls="exa --icons"

alias c="clear"

alias v=nvim
alias vi=nvim
alias vim=nvim

alias nf="neofetch --ascii --source ${XDG_CONFIG_HOME}/neofetch/ascii-art.txt"
alias neofetch="neofetch --ascii --source ${XDG_CONFIG_HOME}/neofetch/ascii-art.txt"

alias dotfiles='/usr/bin/git --git-dir=$HOME/code/dotfiles/ --work-tree=$HOME'

newcd() {
    [[ $# -eq 0 ]] && return
    builtin cd "$@"
}
cs() {
	newcd "$@" && ls -a;
}
