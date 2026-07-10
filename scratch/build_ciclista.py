import os
import re

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

for i in range(1, 5):
    src = os.path.join(base_dir, f'cotizacion-asistencia-hogar-{i}.html')
    dst = os.path.join(base_dir, f'cotizacion-asistencia-ciclista-{i}.html')
    
    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()

    # Basic replacements
    content = content.replace('Asistencia Hogar', 'Asistencia al Ciclista')
    content = content.replace('Hogar Pro', 'Ciclista Pro')
    content = content.replace('hogar-pro', 'ciclista-pro')
    content = content.replace('hogar', 'ciclista')
    content = content.replace('Hogar', 'Ciclista')
    
    content = content.replace('mhmHogarCart', 'mhmCiclistaCart')
    content = content.replace('mhmHogarClient', 'mhmCiclistaClient')
    
    content = content.replace('fa-house-chimney', 'fa-person-biking')
    content = content.replace('fa-house', 'fa-bicycle')
    
    content = content.replace('Propiedad Protegida', 'Ciclista Protegido')
    content = content.replace('La propiedad ahora', 'El ciclista ahora')
    content = content.replace('registro de la propiedad', 'registro del ciclista')

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(content)

print("Created Ciclista flow files successfully.")
