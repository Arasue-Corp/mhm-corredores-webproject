import os
import re

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-ciclista-3.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the unused Success Modal
pattern = r'<!-- Success Modal -->.*?</div>\s*</div>\s*<style>\s*@keyframes modalPop.*?</style>'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# Fix remaining "propiedad" texts
content = content.replace('propiedad / beneficiario', 'beneficiario')
content = content.replace('detalles de la propiedad / beneficiario beneficiario', 'detalles del beneficiario')
content = content.replace('detalles del beneficiario beneficiario', 'detalles del beneficiario')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleaned up Step 3 successfully.")
