import os

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

# Restore Screen 2 from Escolar-2
src2 = os.path.join(base_dir, 'cotizacion-escolar-2.html')
dst2 = os.path.join(base_dir, 'cotizacion-asistencia-hogar-2.html')

with open(src2, 'r', encoding='utf-8') as f:
    html2 = f.read()

html2 = html2.replace('Asistencia Escolar', 'Asistencia Hogar')
html2 = html2.replace('Asistencia Protección Escolar', 'Asistencia Hogar')
html2 = html2.replace('fa-school', 'fa-house-chimney')
html2 = html2.replace('cotizacion-escolar-', 'cotizacion-asistencia-hogar-')
html2 = html2.replace('mhmEscolarCart', 'mhmHogarCart')
html2 = html2.replace('mhmEscolarClient', 'mhmHogarClient')

# Clean up 'Alumno' in Screen 2
html2 = html2.replace('Información del Alumno', 'Información de la Propiedad')
html2 = html2.replace('del alumno beneficiario', 'de la propiedad asegurada')
html2 = html2.replace('al alumno', 'a la propiedad')

with open(dst2, 'w', encoding='utf-8') as f:
    f.write(html2)

# Fix Screen 3 (Payment) to have Transbank instead of Flow
dst3 = os.path.join(base_dir, 'cotizacion-asistencia-hogar-3.html')
with open(dst3, 'r', encoding='utf-8') as f:
    html3 = f.read()

html3 = html3.replace('Transacción respaldada por <strong>Flow</strong>', 'Transacción respaldada por <strong>Transbank</strong>')

with open(dst3, 'w', encoding='utf-8') as f:
    f.write(html3)

print("Flow perfectly restored. Screen 2 is Datos Personales, Screen 3 is Payment (Transbank).")
