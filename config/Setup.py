import os
import urllib.request

def download_file(url, dest_path):
    try:
        print(f"Descargando: {url}")
        urllib.request.urlretrieve(url, dest_path)
        print(f"Guardado en: {dest_path}")
    except Exception as e:
        print(f"Error descargando {url}: {e}")


def setup_civitai():
    civitai_path = os.path.expanduser("~/.civitai")
    os.makedirs(civitai_path, exist_ok=True)

    files = {
        "Loras.py": "https://github.com/SFcrypt/Segsmaker/raw/main/download/Loras.py",
        "Model.py": "https://github.com/SFcrypt/Segsmaker/raw/main/download/Model.py",
        "Interfaz.py": "https://github.com/SFcrypt/Segsmaker/raw/main/download/Interfaz.py",}

    for name, url in files.items():
        download_file(url, os.path.join(civitai_path, name))


def setup_swarmui():
    swarmui_path = os.path.expanduser("~/.swarmui")
    os.makedirs(swarmui_path, exist_ok=True)

    files = {
        "Install.py": "https://github.com/SFcrypt/Segsmaker/raw/main/config/Install.py",
        "Uninstall.py": "https://github.com/SFcrypt/Segsmaker/raw/main/config/Uninstall.py",
        "Updater.py": "https://github.com/SFcrypt/Segsmaker/raw/main/config/Updater.py",
        "SwarmUI.py": "https://github.com/SFcrypt/Segsmaker/raw/main/config/SwarmUI.py",}

    for name, url in files.items():
        download_file(url, os.path.join(swarmui_path, name))


def main():
    setup_civitai()
    setup_swarmui()


if __name__ == "__main__":
    main()
