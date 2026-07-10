import os
import glob

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

mappings = {
    'cotizacion-escolar-1.html': 'mhmEscolarCart',
    'cotizacion-mascota-1.html': 'mhmMascotaCart',
    'cotizacion-asistencia-hogar-1.html': 'mhmHogarCart',
    'cotizacion-vehicular-1.html': 'mhmVehicularCart',
    'cotizacion-asistencia-ciclista-1.html': 'mhmCiclistaCart'
}

for filename, var_name in mappings.items():
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We need to replace mhmPetCart with var_name in these files
        content = content.replace('mhmPetCart', var_name)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

# Remove vehicular-6.html
v6 = os.path.join(base_dir, 'cotizacion-vehicular-6.html')
if os.path.exists(v6):
    os.remove(v6)
    print("Removed cotizacion-vehicular-6.html")

