import os

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-hogar-4.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('mhmPetClient', 'mhmHogarClient')
content = content.replace('mhmPetCart', 'mhmHogarCart')
content = content.replace('mhmEscolarClient', 'mhmHogarClient')
content = content.replace('mhmEscolarCart', 'mhmHogarCart')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed {filepath} successfully.")
