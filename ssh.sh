#!/bin/bash

sudo ufw update
sudo ufw allow 1337

sudo sed -i 's/^#Port 22/Port 1337/' /etc/ssh/sshd_config

sudo systemctl restart ssh
sudo ufw enable
sudo ufw status
