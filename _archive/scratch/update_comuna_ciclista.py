import os

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-ciclista-4.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<option value="" disabled selected>Comuna</option>',
    '<option value="" disabled selected>Selecciona la comuna...</option>'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Comuna updated successfully.")
