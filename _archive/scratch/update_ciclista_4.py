import os
import re

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-ciclista-4.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the "Asistencia Integral Pro" text in the right card
content = content.replace(
    'Usa tu Asistencia Integral Pro en el centro médico que desees',
    'Usa tu Asistencia al Ciclista en el centro médico que desees'
)

# Replace the Tipo de Bicicleta select with Previsión
old_select = '''<select id="tipoInmueble" class="pet-input harmonic-input" required onchange="validatePetsForm()">
                        <option value="" disabled selected>Tipo de bicicleta</option>
                        <option value="urbana">Bicicleta Urbana</option>
                        <option value="mtb">Mountain Bike (MTB)</option>
                        <option value="ruta">Bicicleta de Ruta</option>
                        <option value="electrica">Bicicleta Eléctrica</option>
                    </select>'''

new_select = '''<select id="prevision" class="pet-input harmonic-input" required onchange="validatePetsForm()">
                        <option value="" disabled selected>Previsión</option>
                        <option value="fonasa">Fonasa</option>
                        <option value="isapre">Isapre</option>
                        <option value="particular">Particular</option>
                    </select>'''

content = content.replace(old_select, new_select)

# Also check for "rut del beneficiario", currently it's "Rut", we can change the placeholder or label
content = content.replace('<strong style="color: #334155; font-size: 15px; margin-right: 12px;">Rut</strong>', '<strong style="color: #334155; font-size: 13px; margin-right: 12px;">Rut del beneficiario</strong>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Ciclista 4 updated successfully.")
