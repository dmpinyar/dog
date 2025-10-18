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

[Install]
WantedBy=multi-user.target

### commands ran after ###
sudo systemctl daemon-reload
sudo systemctl enable website_boot.service
sudo systemctl start website_boot.service

### run "sudo systemctl status sudo systemctl status website_boot.service" to verify ###
"""

import apache_push_helper

if __name__ == "__main__":
    apache_push_helper.screen_initialization()
