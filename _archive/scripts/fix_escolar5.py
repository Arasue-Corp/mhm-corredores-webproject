import re

with open('cotizacion/cotizacion-escolar-5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Text replacements
content = content.replace('Cotización de Asistencia Mascota', 'Cotización de Asistencia Escolar')
content = content.replace('Tu mascota ahora cuenta con la mejor protección.', 'El estudiante ahora cuenta con la mejor protección.')
content = content.replace('Tu mascota ya cuenta con el respaldo corporativo de MHM.', 'El estudiante ya cuenta con el respaldo corporativo de MHM.')
content = content.replace('TUS DATOS Y<br>LOS DE TUS MASCOTAS.', 'LOS DATOS DEL ESTUDIANTE.')
content = content.replace('cotizacion-mascota-4.html', 'cotizacion-escolar-4.html')

# Icon replacements
content = content.replace('fa-dog', 'fa-user-graduate')
content = content.replace('fa-shield-cat', 'fa-user-graduate')

# Color and button style replacements
# Previous success button in mascota was #796bfc
content = content.replace('#796bfc', '#1C4E5E')
content = content.replace('#cb6ce6', '#0A323D')

# In case the sidebar is there, replace mascota related text
content = content.replace('Registro Mascotas', 'Registro Beneficiarios')
content = content.replace('Estás a pocos pasos de asegurar a tu mascota.', 'Estás a un paso de completar el registro del estudiante.')

with open('cotizacion/cotizacion-escolar-5.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done step 5 replacements")
