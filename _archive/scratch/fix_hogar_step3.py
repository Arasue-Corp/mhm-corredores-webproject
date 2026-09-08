import os

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-hogar-3.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('cotizacion-mascota-1.html', 'cotizacion-asistencia-hogar-1.html')
html = html.replace('cotizacion-mascota-4.html', 'cotizacion-asistencia-hogar-4.html')
html = html.replace('TUS MASCOTAS', 'LA PROPIEDAD')
html = html.replace('mhmPetClient', 'mhmHogarClient')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed!")
