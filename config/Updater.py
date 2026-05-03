import subprocess
import os
from IPython.display import clear_output
from nenen88 import say

def run_update():
    base = os.path.expanduser("~/SwarmUI")

    say("<b>【{red} Updating SwarmUI{d} 】{red}</b>")

    os.makedirs(f"{base}/dlbackend", exist_ok=True)
    os.makedirs(f"{base}/Models/diffusion_models", exist_ok=True)

    say("<b>【{red} Cloning ComfyUI{d} 】{red}</b>")
    subprocess.run([
        "git", "clone",
        "https://github.com/SFcrypt/ComfyUI",
        f"{base}/dlbackend/ComfyUI"
    ])

    say("<b>【{red} Cloning SwarmUI{d} 】{red}</b>")
    subprocess.run([
        "git", "clone",
        "https://github.com/SFcrypt/SwarmUI",
        f"{base}/SwarmUI_tmp"
    ])

    say("<b>【{red} Copying Files{d} 】{red}</b>")
    subprocess.run(
        f"cp -r {base}/SwarmUI_tmp/* {base}/",
        shell=True
    )

    say("<b>【{red} Cleaning{d} 】{red}</b>")
    subprocess.run(
        f"rm -rf {base}/SwarmUI_tmp",
        shell=True
    )

    clear_output()
    say("<b>【{red} Listo{d} 】{red}</b>")

if __name__ == "__main__":
    run_update()
