import subprocess

# script ran on boot built in /etc/systemd/system/website_boot.service

### the contents of the file ###
# [Unit]
# Description=Run website_boot.py inside screen
# After=network-online.target
# Wants=network-online.target

# [Service]
# Type=forking
# User=devin
# WorkingDirectory=/home/devin
# ExecStart=/usr/bin/python3 /home/devin/projects/dog/com/website_boot.py      Restart=always
# RestartSec=10

# [Install]
# WantedBy=multi-user.target

### commands ran after ###
# sudo systemctl daemon-reload
# sudo systemctl enable website_boot.service
# sudo systemctl start website_boot.service

### run "sudo systemctl status sudo systemctl status website_boot.service.service" to verify ###

# name of the screen session
screen_name = "ngrok"

# Launch a detached screen session running the ngrok on boot

command = "ngrok http 80"
subprocess.run([
    "screen",
    "-dmS", screen_name,
    "bash", "-c", command
])
