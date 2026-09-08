import re

with open('cotizacion/cotizacion-escolar-3.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('cotizacion-mascota-1.html', 'cotizacion-escolar-1.html')
content = content.replace('cotizacion-mascota-3.html', 'cotizacion-escolar-3.html')
content = content.replace('Información de la Mascota', 'Información del Alumno')
content = content.replace('Nombre, especie, raza y edad de tu mascota.', 'Nombre, rut y fecha de nacimiento del alumno beneficiario.')
content = content.replace('A continuación debes completar TUS DATOS Y<br>LOS DE TUS MASCOTAS.', 'A continuación debes completar TUS DATOS Y<br>LOS DEL BENEFICIARIO.')

with open('cotizacion/cotizacion-escolar-3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
