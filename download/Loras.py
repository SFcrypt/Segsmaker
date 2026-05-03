import os, sys, requests
import ipywidgets as widgets
from IPython.display import display, clear_output
from IPython import get_ipython

%cd -q $HOME

# crear carpeta destino
os.makedirs(".swarmui/download", exist_ok=True)

# descargar box.py
box_path = os.path.join(os.getcwd(), ".swarmui/download/box.py")
if not os.path.exists(box_path):
    url = "https://raw.githubusercontent.com/SFcrypt/Segsmaker/main/download/box.py"
    r = requests.get(url)
    with open(box_path, "wb") as f:
        f.write(r.content)

# importar box.py
sys.path.append(os.path.join(os.getcwd(), ".swarmui/download"))
from box import load_style

load_style()

main_container = widgets.VBox()
output = widgets.Output()

link_input = widgets.Text(
    placeholder="Link de descarga",
    layout=widgets.Layout(width="80%", margin="0 0 6px 0"))
link_input.add_class("seg-input-html")

nombre_input = widgets.Text(
    placeholder="Nombre del archivo",
    layout=widgets.Layout(width="80%", margin="0 0 6px 0"))
nombre_input.add_class("seg-input-html")

download_btn = widgets.Button(
    description="Download",
    layout=widgets.Layout(height="35px", padding="0 0px"))
download_btn.add_class("seg-button")

def descargar_lora(b):
    %cd -q $LORA
    main_container.children = [output]
    with output:
        clear_output()
        Link = link_input.value.strip()
        Nombre = "-".join(nombre_input.value.strip().split())
        if not Link or not Nombre:
            return
        try:
            get_ipython().run_line_magic(
                "download",
                f"{Link} {Nombre}.safetensors"
            )
        except:
            pass

download_btn.on_click(descargar_lora)

form_box = widgets.VBox([
    widgets.HTML("<div class='seg-title'>Descargar LoRA</div>"),
    link_input,
    nombre_input,
    download_btn
])
form_box.add_class("seg-box")

main_container.children = [form_box]
display(main_container)
