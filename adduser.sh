#!/bin/bash

echo -n "Entrez le mot de passe pour le nouvel utilisateur : "
stty -echo
read password
stty echo
echo

sudo useradd -m -s /bin/bash miro
echo "miro:$password" | sudo chpasswd

sudo usermod -aG sudo miro

id miro
