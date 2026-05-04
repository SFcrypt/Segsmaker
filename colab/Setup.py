import os
import urllib.request

def download_file(url, dest_path):
    try:
        urllib.request.urlretrieve(url, dest_path)
        print(f"Descargado: {dest_path}")
    except Exception as e:
        print(f"Error descargando {url}: {e}")

def setup_civitai():
    civitai_path = "/content/civitai"
    os.makedirs(civitai_path, exist_ok=True)

    files = {
        "Loras.py": "https://github.com/SFcrypt/Segsmaker/raw/main/colab/Loras.py",
        "Model.py": "https://github.com/SFcrypt/Segsmaker/raw/main/colab/Model.py",
        "Interfaz.py": "https://github.com/SFcrypt/Segsmaker/raw/main/colab/Interfaz.py",
    }

    for name, url in files.items():
        download_file(url, os.path.join(civitai_path, name))

def main():
    setup_civitai()

if __name__ == "__main__":
    main()
