[program:mss_core]
command=/home/vanshin/.pyenv/shims/uwsgi /home/vanshin/code/mss_core/conf/mss_core_local.ini
directory=/home/vanshin/code/mss_core/bin
stdout_logfile=/home/vanshin/log/mss_core.log
stdout_logfile_maxbytes=16MB
stdout_logfile_backups=10
user=vanshin

