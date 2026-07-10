import os
import re

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

# Rename files to make space for the new Step 2
os.rename(os.path.join(base_dir, 'cotizacion-asistencia-ciclista-4.html'), os.path.join(base_dir, 'cotizacion-asistencia-ciclista-5.html'))
os.rename(os.path.join(base_dir, 'cotizacion-asistencia-ciclista-3.html'), os.path.join(base_dir, 'cotizacion-asistencia-ciclista-4.html'))
os.rename(os.path.join(base_dir, 'cotizacion-asistencia-ciclista-2.html'), os.path.join(base_dir, 'cotizacion-asistencia-ciclista-3.html'))

# Now create cotizacion-asistencia-ciclista-2.html by cloning escolar-2 and adjusting for ciclista
escolar2 = os.path.join(base_dir, 'cotizacion-escolar-2.html')
with open(escolar2, 'r', encoding='utf-8') as f:
    content2 = f.read()

# Replace variables
content2 = content2.replace('cotizacion-escolar-', 'cotizacion-asistencia-ciclista-')
content2 = content2.replace('mhmPetCart', 'mhmCiclistaCart')
content2 = content2.replace('mhmPetClient', 'mhmCiclistaClient')
content2 = content2.replace('Escolar', 'Ciclista')
content2 = content2.replace('escolar', 'ciclista')
content2 = content2.replace('fa-school', 'fa-person-biking')

with open(os.path.join(base_dir, 'cotizacion-asistencia-ciclista-2.html'), 'w', encoding='utf-8') as f:
    f.write(content2)

# Update links inside the files
def replace_in_file(filename, replacements):
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    for old, new in replacements:
        c = c.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

# Fix step 1
replace_in_file('cotizacion-asistencia-ciclista-1.html', [
    ('cotizacion-asistencia-ciclista-2.html', 'cotizacion-asistencia-ciclista-2.html'), # this remains 2 (was going to payment, now goes to Datos)
])

# Fix step 3 (old 2, payment)
replace_in_file('cotizacion-asistencia-ciclista-3.html', [
    ('cotizacion-asistencia-ciclista-1.html', 'cotizacion-asistencia-ciclista-2.html'), # back button should go to 2
    ('cotizacion-asistencia-ciclista-2.html', 'cotizacion-asistencia-ciclista-3.html'), # any self links
    ('cotizacion-asistencia-ciclista-3.html', 'cotizacion-asistencia-ciclista-4.html'), # forward links to 4
    ('Datos del Contratante</li>\n                        <li class="active"><span class="pulse-dot"></span> Pago Seguro</li>\n                        <li><i class="fa-regular fa-circle"></i> Registro Beneficiarios', 'Datos del Contratante</li>\n                        <li class="active"><span class="pulse-dot"></span> Pago Seguro</li>\n                        <li><i class="fa-regular fa-circle"></i> Registro Beneficiarios')
])

# Also fix the sidebar in step 3 (old 2, payment) - wait, it already has "Datos del Contratante" in its sidebar? 
# Ah! My script earlier added "Datos del Contratante" to the sidebar for ciclista-2 but I didn't actually create the page!

# Fix step 4 (old 3, Beneficiarios)
replace_in_file('cotizacion-asistencia-ciclista-4.html', [
    ('cotizacion-asistencia-ciclista-2.html', 'cotizacion-asistencia-ciclista-3.html'), # back button to payment (3)
    ('cotizacion-asistencia-ciclista-4.html', 'cotizacion-asistencia-ciclista-5.html'), # forward to success (5)
])

# Fix step 5 (old 4, success)
replace_in_file('cotizacion-asistencia-ciclista-5.html', [
    ('cotizacion-asistencia-ciclista-4.html', 'cotizacion-asistencia-ciclista-5.html'), # self links
    ('cotizacion-asistencia-ciclista-3.html', 'cotizacion-asistencia-ciclista-4.html'), # back link if any
])

print("Reordered flow successfully")
