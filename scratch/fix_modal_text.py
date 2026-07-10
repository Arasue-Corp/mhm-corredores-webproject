import os

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-ciclista-3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the text
content = content.replace(
    'Importante, debes completar tus datos y los del beneficiario aquí.',
    'Importante, debes completar tus datos.'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modal text updated successfully.")
