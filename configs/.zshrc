export ZSH=$HOME/.oh-my-zsh
ZSH_THEME="candy"
plugins=(git)
source $ZSH/oh-my-zsh.sh

alias cl='clear'
alias ks='ls'
alias lsc='ls'
alias ..='cd ..'
alias cj='clear'
alias ip='ipython'
alias ex='exit'
alias pt='ptpython'
alias cleawr='clear'
alias conf='cd ../conf'
alias sconf='cd /etc/supervisor/conf.d/'
alias slog='cd /var/log/supervisor/'
alias bin='cd ../bin'
alias space='cd ~/space'
alias user='cd ~/code/user_api'
alias wx='cd ~/code/wechat_api'
alias al='cd ~/code/altools'
alias code='cd ~/code'
alias rd='cd ~/code/reading'
alias mc='cd ~/code/mss_client'
alias ms='cd ~/code/mss_core'
alias ssh33='ssh root@45.32.25.33'
alias sshqf='ssh vanshin@172.100.113.124'
alias mc127='mycli -uroot -p123456'
alias mcjd='mycli -uvanshin -pvanshin1111 -h116.196.113.214'
alias my127='mysql -uroot -p123456'
alias sshjd='ssh root@116.196.113.214'
alias ssvjd='ssh vanshin@116.196.113.214'
export EDITOR=vim

export PATH="/home/vanshin/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

