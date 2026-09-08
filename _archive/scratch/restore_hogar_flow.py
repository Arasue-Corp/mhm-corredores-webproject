import os
import re

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

for i in range(2, 6):
    src = os.path.join(base_dir, f'cotizacion-escolar-{i}.html')
    dst = os.path.join(base_dir, f'cotizacion-asistencia-hogar-{i}.html')
    
    if os.path.exists(src):
        with open(src, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # General replacements
        html = html.replace('Asistencia Escolar', 'Asistencia Hogar')
        html = html.replace('Asistencia Protección Escolar', 'Asistencia Hogar')
        html = html.replace('fa-school', 'fa-house-chimney')
        html = html.replace('cotizacion-escolar-', 'cotizacion-asistencia-hogar-')
        html = html.replace('mhmEscolarCart', 'mhmHogarCart')
        html = html.replace('mhmEscolarClient', 'mhmHogarClient')
        
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Restored {dst}")
