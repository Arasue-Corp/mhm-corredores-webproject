import re
import os

steps_names = [
    "Tipo de Seguro",
    "Datos del Auto",
    "Datos Personales",
    "Coberturas",
    "Validación 0Km",
    "Plan de Pago"
]

files_to_active_index = {
    "cotizacion-1.html": 0,
    "cotizacion-3-1.html": 1,
    "cotizacion-4-1.html": 2,
    "cotizacion-7-1.html": 3,
    "cotizacion-8-1.html": 4,
    "cotizacion-9-1.html": 5
}

def generate_list(active_idx):
    html = '<ul class="aurora-list">\n'
    for i, name in enumerate(steps_names):
        if i < active_idx:
            html += f'                        <li class="done"><i class="fa-solid fa-circle-check" style="color: var(--corp-primary);"></i> {name}</li>\n'
        elif i == active_idx:
            html += f'                        <li class="active"><span class="pulse-dot"></span> {name}</li>\n'
        else:
            html += f'                        <li><i class="fa-regular fa-circle"></i> {name}</li>\n'
    html += '                    </ul>'
    return html

base_path = "cotizacion/"

for filename, active_idx in files_to_active_index.items():
    filepath = os.path.join(base_path, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}, not found.")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_list_html = generate_list(active_idx)
    
    # Replace the <ul class="aurora-list">...</ul> block using regex
    # Warning: regex needs to match across newlines
    new_content = re.sub(r'<ul class="aurora-list">.*?</ul>', new_list_html, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Processed {filename}")
