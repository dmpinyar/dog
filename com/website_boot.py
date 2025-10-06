"""
script ran on boot built in /etc/systemd/system/website_boot.service

The script is mainly for documentation, this could kind of just be done in the .service file
but it is a useful structure in case I want to add on anything else on boot that requires more
complexity than simple bash commands.

### the contents of the file ###
[Unit]
Description=Run website_boot.py inside screen
After=network-online.target
Wants=network-online.target

[Service]
Type=forking
User=devin
WorkingDirectory=/home/devin
ExecStart=/usr/bin/python3 /home/devin/projects/dog/com/website_boot.py      
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

### commands ran after ###
sudo systemctl daemon-reload
sudo systemctl enable website_boot.service
sudo systemctl start website_boot.service

### run "sudo systemctl status sudo systemctl status website_boot.service" to verify ###
"""

import subprocess

# name of the screen session
# should probably be stored in another file just cause it's used by both scripts but whatever
screen_name = "ngrok"

if __name__ == "__main__":
    # Launch a detached screen session running the ngrok on boot
    command = "ngrok http 80"
    subprocess.run([
        "screen",
        "-dmS", screen_name,
        "bash", "-c", command
    ])
