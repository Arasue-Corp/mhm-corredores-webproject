import os
import re

def adapt_file(source_file, target_file, replacements):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

# Replacements common to all
common_replacements = [
    ('Asistencia Escolar', 'Asistencia Hogar'),
    ('cotizacion-escolar-', 'cotizacion-asistencia-hogar-'),
    ('mhmEscolarCart', 'mhmHogarCart'),
    ('mhmEscolarClient', 'mhmHogarClient'),
    ('fa-school', 'fa-house-chimney'),
    ('al estudiante', 'tu propiedad'),
    ('fa-user-graduate', 'fa-house-chimney'),
]

# Step 2: Datos (Clone from escolar-2)
step2_replacements = common_replacements + [
    ("cotizacion-escolar-3.html", "cotizacion-asistencia-hogar-3.html"),
    ('<li><i class="fa-regular fa-circle"></i> Registro Beneficiarios</li>', '') # Remove beneficiarios step from sidebar
]
adapt_file(os.path.join(base_dir, 'cotizacion-escolar-2.html'), 
           os.path.join(base_dir, 'cotizacion-asistencia-hogar-2.html'), 
           step2_replacements)

# Step 3: Pago (Clone from escolar-3)
step3_replacements = common_replacements + [
    ("cotizacion-escolar-4.html", "cotizacion-asistencia-hogar-4.html"), # After payment, go to success (step 4)
    ('<li><i class="fa-regular fa-circle"></i> Registro Beneficiarios</li>', ''), # Remove from sidebar
    ('Transacción respaldada por <strong>Flow</strong>', 'Transacción respaldada por <strong>Transbank</strong>'),
    ('https://www.flow.cl/terminos-y-condiciones.php', '#')
]
adapt_file(os.path.join(base_dir, 'cotizacion-escolar-3.html'), 
           os.path.join(base_dir, 'cotizacion-asistencia-hogar-3.html'), 
           step3_replacements)

# Step 4: Success (Clone from escolar-5, since there's no step 4 in Hogar)
step4_replacements = common_replacements + [
    ('<li><i class="fa-regular fa-circle"></i> Registro Beneficiarios</li>', ''), # Remove from sidebar
    ('<li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Registro Beneficiarios</li>', ''), # Remove from sidebar (checked state)
    ('¡Alumno Protegido!', '¡Propiedad Protegida!'),
    ('fa-user-graduate', 'fa-house-chimney')
]
adapt_file(os.path.join(base_dir, 'cotizacion-escolar-5.html'), 
           os.path.join(base_dir, 'cotizacion-asistencia-hogar-4.html'), 
           step4_replacements)

print("Flow fixed.")
