import os

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

def fix_has_items(filename):
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # In step 3, !hasItems goes to 2 (my previous replacement). It should go to 1.
    if filename == 'cotizacion-asistencia-ciclista-3.html':
        content = content.replace("if (!hasItems) {\n            window.location.href = 'cotizacion-asistencia-ciclista-2.html';\n            return;\n        }", "if (!hasItems) {\n            window.location.href = 'cotizacion-asistencia-ciclista-1.html';\n            return;\n        }")
        content = content.replace("if (!hasItems) {\n            window.location.href = 'cotizacion-asistencia-ciclista-4.html';\n            return;\n        }", "if (!hasItems) {\n            window.location.href = 'cotizacion-asistencia-ciclista-1.html';\n            return;\n        }")
    
    if filename == 'cotizacion-asistencia-ciclista-2.html':
        content = content.replace("window.location.href = 'cotizacion-escolar-1.html';", "window.location.href = 'cotizacion-asistencia-ciclista-1.html';")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_has_items('cotizacion-asistencia-ciclista-2.html')
fix_has_items('cotizacion-asistencia-ciclista-3.html')
