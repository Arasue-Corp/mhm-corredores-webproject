import os
import re

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'
src = os.path.join(base_dir, 'cotizacion-escolar-5.html')
dst = os.path.join(base_dir, 'cotizacion-asistencia-hogar-4.html')

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace texts
content = content.replace('Asistencia Escolar', 'Asistencia Hogar')
content = content.replace('Estudiante Protegido', 'Propiedad Protegida')
content = content.replace('fa-user-graduate', 'fa-house-chimney')
content = content.replace('fa-graduation-cap', 'fa-house')
content = content.replace('El estudiante ahora', 'La propiedad ahora')
content = content.replace('mhmEscolarCart', 'mhmHogarCart')

# The header title might be '¡Asistencia Escolar Activa!' -> '¡Asistencia Hogar Activa!'

with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Created {dst} successfully.")
