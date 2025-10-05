#### dysfunctional. Ngrok can boot on its own in startup but it is a pain to manage without a screen. I disabled the service ####
#### but I am going to leave this file in case I want to revisit a similar prospect in the future ####



import subprocess

# script ran on boot built in /etc/systemd/system/website_boot.service

### the contents of the file ###
# [Unit]
# Description=Run website_boot.py inside screen
# After=network.target

# [Service]
# Type=forking
# User=devin
# WorkingDirectory=/home/devin
# ExecStart=/usr/bin/screen -dmS website_boot /usr/bin/python3 /home/devin/projects/dog/com/website_boot.py
# Restart=always
# RestartSec=10

# [Install]
# WantedBy=multi-user.target

### commands ran after ###
# sudo systemctl daemon-reload
# sudo systemctl enable website_boot.service
# sudo systemctl start website_boot.service

### run "sudo systemctl status sudo systemctl status website_boot.service.service" to verify ###

# name of the screen session
screen_name = "grok"

# Launch a detached screen session running the ngrok on boot
subprocess.run([
    "screen",
    "-dmS", screen_name,
    "bash", "-c", "ngrok", "http", "80"
])

print(f"Started ngrok in detached screen session '{screen_name}'")