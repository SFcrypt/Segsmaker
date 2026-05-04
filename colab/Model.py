import os, sys, requests, importlib.util
import ipywidgets as widgets
from IPython.display import display, clear_output
from IPython import get_ipython

def launch_lora_downloader():
    ipy = get_ipython()

    os.chdir("/content")

    civitai_path = "/content/civitai"
    os.makedirs(civitai_path, exist_ok=True)

    # Descargar box.py si no existe
    box_path = os.path.join(civitai_path, "box.py")
    if not os.path.exists(box_path):
        url = "https://raw.githubusercontent.com/SFcrypt/Segsmaker/main/download/box.py"
        r = requests.get(url)
        with open(box_path, "wb") as f:
            f.write(r.content)

    # IMPORTAR box.py correctamente (evita conflicto con paquete 'box')
    spec = importlib.util.spec_from_file_location("box_local", box_path)
    box_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(box_module)

    load_style = getattr(box_module, "load_style", None)
    if load_style:
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
        main_container.children = [output]
        with output:
            clear_output()
            Link = link_input.value.strip()
            Nombre = "-".join(nombre_input.value.strip().split())
            if not Link or not Nombre:
                return
            try:
                output_path = os.path.join(civitai_path, f"{Nombre}.safetensors")
                r = requests.get(Link)
                with open(output_path, "wb") as f:
                    f.write(r.content)
                print(f"Descargado en: {output_path}")
            except Exception as e:
                print(f"Error: {e}")

    download_btn.on_click(descargar_lora)

    form_box = widgets.VBox([
        widgets.HTML("<div class='seg-title'>Descargar</div>"),
        link_input,
        nombre_input,
        download_btn])
    form_box.add_class("seg-box")

    main_container.children = [form_box]
    display(main_container)


# ejecutar
launch_lora_downloader()
