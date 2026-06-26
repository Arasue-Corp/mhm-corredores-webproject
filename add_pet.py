import json

file_path = "seguros-personales/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add to the sidebar
sidebar_insert = """                <div class="canvas-menu-item " id="menu-item-2" onmouseenter="updateCanvas(2)">
                    <div class="menu-icon"><i class="fa-solid fa-plane-departure"></i></div>
                    <div class="menu-text">Asistencia en Viaje</div>
                </div>
                <div class="canvas-menu-item " id="menu-item-3" onmouseenter="updateCanvas(3)">
                    <div class="menu-icon"><i class="fa-solid fa-paw"></i></div>
                    <div class="menu-text">Asistencia Veterinaria</div>
                </div>"""

content = content.replace(
    """                <div class="canvas-menu-item " id="menu-item-2" onmouseenter="updateCanvas(2)">
                    <div class="menu-icon"><i class="fa-solid fa-plane-departure"></i></div>
                    <div class="menu-text">Asistencia en Viaje</div>
                </div>""",
    sidebar_insert
)

# Replace the JSON productsData string
import re
match = re.search(r'const productsData = (\[.*?\]);', content)
if match:
    data_str = match.group(1)
    data = json.loads(data_str)
    
    new_product = {
        "title": "Asistencia Veterinaria",
        "icon": "fa-paw",
        "tag": "Mascotas",
        "desc": "Protege a tus mascotas con nuestro seguro de asistencia veterinaria. Cubre gastos médicos, accidentes, y consultas preventivas para que tus peludos amigos siempre estén sanos y salvos.",
        "covers": [
            "Consultas veterinarias de urgencia",
            "Gastos médicos por accidentes",
            "Vacunación y chequeos preventivos",
            "Asistencia telefónica veterinaria 24/7"
        ]
    }
    data.append(new_product)
    
    new_data_str = json.dumps(data, ensure_ascii=False)
    content = content.replace(data_str, new_data_str)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
