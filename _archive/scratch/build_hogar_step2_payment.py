import os

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'
src = os.path.join(base_dir, 'cotizacion-escolar-3.html')
dst = os.path.join(base_dir, 'cotizacion-asistencia-hogar-2.html')

with open(src, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace texts for Asistencia Hogar
html = html.replace('Asistencia Escolar', 'Asistencia Hogar')
html = html.replace('Asistencia Protección Escolar', 'Asistencia Hogar')
html = html.replace('fa-school', 'fa-house-chimney')
html = html.replace('mhmEscolarCart', 'mhmHogarCart')
html = html.replace('mhmEscolarClient', 'mhmHogarClient')

# Replace navigation links
html = html.replace('cotizacion-escolar-1.html', 'cotizacion-asistencia-hogar-1.html')
html = html.replace('cotizacion-escolar-2.html', 'cotizacion-asistencia-hogar-1.html') # Back button goes to 1
html = html.replace('cotizacion-escolar-3.html', 'cotizacion-asistencia-hogar-2.html') # Self reference
html = html.replace('cotizacion-escolar-4.html', 'cotizacion-asistencia-hogar-3.html') # Next button goes to 3
html = html.replace('cotizacion-escolar-5.html', 'cotizacion-asistencia-hogar-3.html') 

# Fix Transbank texts according to the image provided by the user
html = html.replace('Transacción respaldada por <strong>Flow</strong>', 'Transacción respaldada por <strong>Transbank</strong>')
# Remove 'Datos Personales' from sidebar
html = html.replace('<li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Datos Personales</li>', '')

with open(dst, 'w', encoding='utf-8') as f:
    f.write(html)

print("Step 2 is now the payment screen (from escolar-3).")
