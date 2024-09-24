#!/bin/bash

read -s -p "Entrez le mot de passe pour le nouvel utilisateur : " password
echo

sudo useradd -m -s /bin/bash miro
echo "miro:$password" | sudo chpasswd

sudo usermod -aG sudo miro

id miro
