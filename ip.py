import json
import socket
import os

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        print(f"Erreur lors de la récupération de l'adresse IP : {e}")
        return "127.0.0.1"

def create_config_file(ip_address):
    config_data = {
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

    config_path = os.path.join(os.getcwd(), "config.json")

    try:
        with open(config_path, "w") as config_file:
            json.dump(config_data, config_file, indent=4)
        print(f"Fichier config.json créé avec succès à : {config_path}")
    except Exception as e:
        print(f"Erreur lors de la création du fichier config.json : {e}")

if __name__ == "__main__":
    ip_address = get_local_ip()
    print(f"Adresse IP détectée : {ip_address}")
    create_config_file(ip_address)
