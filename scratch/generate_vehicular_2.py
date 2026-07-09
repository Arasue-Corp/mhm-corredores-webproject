import re
import os

with open('cotizacion/cotizacion-escolar-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Escolar to Vehicular
html = html.replace('cotizacion-escolar-', 'cotizacion-vehicular-')
html = html.replace('Asistencia Escolar', 'Asistencia Vehicular')
html = html.replace('ESCOLAR', 'VEHICULAR')

# We need to insert the tooltip next to the form.
# Look for: <div style="display: flex; flex-direction: column; gap: 15px; border: 1px solid #E2E8F0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.02);">
# Wait, let's wrap the form area in a flex container.

old_form_area = '''<div style="padding: 40px; background: white; max-width: 500px; margin: 0 auto;">
            <!-- Form Fields -->
            <div style="display: flex; flex-direction: column; gap: 15px; border: 1px solid #E2E8F0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.02);">'''

new_form_area = '''<div style="padding: 40px; background: white; max-width: 900px; margin: 0 auto; display: flex; align-items: center; justify-content: center; gap: 30px; flex-wrap: wrap;">
            
            <!-- Tooltip Message -->
            <div style="position: relative; border: 2px solid #a4c920; border-radius: 4px; padding: 20px 25px; background: #f8fafc; max-width: 320px; font-size: 0.95rem; color: #475569;">
                Si eres <strong>contratante y beneficiario</strong> a la vez, continúa completando los formularios con tus datos.
                <!-- Tooltip Arrow -->
                <div style="position: absolute; right: -12px; top: 50%; transform: translateY(-50%); width: 0; height: 0; border-top: 10px solid transparent; border-bottom: 10px solid transparent; border-left: 12px solid #a4c920;"></div>
                <div style="position: absolute; right: -9px; top: 50%; transform: translateY(-50%); width: 0; height: 0; border-top: 8px solid transparent; border-bottom: 8px solid transparent; border-left: 10px solid #f8fafc;"></div>
            </div>

            <!-- Form Fields -->
            <div style="display: flex; flex-direction: column; gap: 15px; border: 1px solid #E2E8F0; border-radius: 12px; padding: 35px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); min-width: 380px; background: white;">'''

if old_form_area in html:
    html = html.replace(old_form_area, new_form_area)
else:
    print("Warning: could not find old form area string.")

with open('cotizacion/cotizacion-vehicular-2.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Generated cotizacion-vehicular-2.html")
