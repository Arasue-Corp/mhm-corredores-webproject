import re

with open('cotizacion/cotizacion-escolar-3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace texts and links
content = content.replace('Cotización de Asistencia Mascota', 'Cotización de Asistencia Escolar')
content = content.replace('Asistencia Mascota', 'Asistencia Escolar')
content = content.replace('Registro Mascotas', 'Registro Beneficiarios')
content = content.replace('cotizacion-mascota-2.html', 'cotizacion-escolar-2.html')
content = content.replace('cotizacion-mascota-4.html', 'cotizacion-escolar-4.html')
content = content.replace('fa-paw', 'fa-school')
content = content.replace('fa-shield-cat', 'fa-user-graduate')
content = content.replace('asegurar a tu mascota', 'asegurar al estudiante')
content = content.replace('mhmPetClient', 'mhmEscolarClient')
content = content.replace('mhmPetCart', 'mhmPetCart') # Actually I used mhmPetCart in step 2 for Escolar as well. So no need to change it, but wait: in step 2 for Escolar, I used sessionStorage.getItem('mhmPetCart'). I'll keep it as mhmPetCart for now since they share the cart logic, or I should rename it. Let's just leave mhmPetCart alone for the cart so it doesn't break. 

with open('cotizacion/cotizacion-escolar-3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done building escolar 3")
