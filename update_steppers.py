import re
import os

files_to_update = {
    'cotizacion-3-1.html': 1, # Datos del Auto (index 1)
    'cotizacion-4-1.html': 1, # Datos del Auto
    'cotizacion-5-1.html': 2, # Datos Personales
    'cotizacion-7-1.html': 4, # Detalles de Contrato
    'cotizacion-8-1.html': 5, # Validación 0Km
    'cotizacion-9-1.html': 6  # Plan de Pago
}

steps = [
    "Tipo de Seguro",
    "Datos del Auto",
    "Datos Personales",
    "Coberturas",
    "Detalles de Contrato",
    "Validación 0Km",
    "Plan de Pago"
]

def generate_list(active_index):
    lines = ['                    <ul class="aurora-list">']
    for i, step in enumerate(steps):
        if i < active_index:
            lines.append(f'                        <li class="done"><i class="fa-solid fa-circle-check" style="color: var(--corp-primary);"></i> {step}</li>')
        elif i == active_index:
            lines.append(f'                        <li class="active"><span class="pulse-dot"></span> {step}</li>')
        else:
            lines.append(f'                        <li><i class="fa-regular fa-circle"></i> {step}</li>')
    lines.append('                    </ul>')
    return '\n'.join(lines)

for filename, active_idx in files_to_update.items():
    path = os.path.join('cotizacion', filename)
    with open(path, 'r') as f:
        content = f.read()
    
    new_list = generate_list(active_idx)
    new_content = re.sub(r'                    <ul class="aurora-list">.*?</ul>', new_list, content, flags=re.DOTALL)
    
    with open(path, 'w') as f:
        f.write(new_content)
        
print("Updated successfully")
