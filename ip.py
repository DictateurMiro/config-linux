import requests
import json
import os

def get_public_ip():
    try:
        # Récupérer l'IP publique à partir d'un service externe
        response = requests.get("https://api.ipify.org?format=text")
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération de l'IP publique : {e}")
        return None

def create_config_file(ip_address):
    config = {
        "autosave": True,
        "cpu": True,
        "opencl": False,
        "cuda": False,
        "pools": [
            {
                "url": "xmrpool.eu:9999",
                "user": "43sQVsiBFu74nhhSiYtYvk5vYbrPetg8KdCR6S5had6V3JXm6VKruXYJSHzUDpyQycfV5a8Fu6K94QaRQCpwyK2JLASXAu3",
                "rig-id": ip_address,
                "keepalive": True,
                "tls": True
            }
        ]
    }

    # Chemin du fichier de configuration
    config_path = os.path.expanduser("~/xmrig/build/config.json")
    try:
        with open(config_path, "w") as config_file:
            json.dump(config, config_file, indent=4)
        print(f"Fichier config.json créé avec succès : {config_path}")
    except IOError as e:
        print(f"Erreur lors de la création du fichier config.json : {e}")

if __name__ == "__main__":
    ip_address = get_public_ip()
    if ip_address:
        print(f"Adresse IP publique détectée : {ip_address}")
        create_config_file(ip_address)
    else:
        print("Impossible de détecter l'adresse IP publique.")
