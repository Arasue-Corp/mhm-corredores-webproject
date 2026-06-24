import os
import re

files_map = {
    "cotizacion-1.html": 0,
    "cotizacion-3-1.html": 1,
    "cotizacion-4-1.html": 2,
    "cotizacion-5-1.html": 2,
    "cotizacion-6-1.html": 3,
    "cotizacion-7-1.html": 3,
    "cotizacion-8-1.html": 4,
    "cotizacion-9-1.html": 5,
    "cotizacion-10-1-fid.html": 6 # All done
}

steps = [
    "Tipo de Seguro",
    "Datos del Auto",
    "Datos Personales",
    "Coberturas",
    "Validación 0Km",
    "Plan de Pago"
]

def generate_list(active_idx):
    lines = []
    lines.append('<ul class="aurora-list">')
    for i, step in enumerate(steps):
        if i < active_idx:
            lines.append(f'                        <li class="done"><i class="fa-solid fa-circle-check" style="color: var(--corp-primary);"></i> {step}</li>')
        elif i == active_idx:
            lines.append(f'                        <li class="active"><span class="pulse-dot"></span> {step}</li>')
        else:
            lines.append(f'                        <li><i class="fa-regular fa-circle"></i> {step}</li>')
    lines.append('                    </ul>')
    return '\n'.join(lines)

import glob
for filename in files_map.keys():
    filepath = os.path.join("/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion", filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}")
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # replace everything between <ul class="aurora-list"> and </ul>
    new_ul = generate_list(files_map[filename])
    new_content = re.sub(r'<ul class="aurora-list">.*?</ul>', new_ul, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")

