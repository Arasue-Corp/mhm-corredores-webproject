import os
import glob

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'
files = glob.glob(os.path.join(base_dir, 'cotizacion-asistencia-ciclista-*.html'))

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix graduate icon
    content = content.replace('fa-user-graduate', 'fa-person-biking')
    
    # Fix "Información del Alumno"
    content = content.replace('Información del Alumno', 'Información del Ciclista')
    content = content.replace('del alumno beneficiario.', 'del ciclista beneficiario.')
    
    # Fix bad icon
    content = content.replace('fa-person-biking-circle-check', 'fa-shield-halved')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed icons and texts successfully")
