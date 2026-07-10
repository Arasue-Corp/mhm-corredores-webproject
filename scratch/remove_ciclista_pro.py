import os
import re

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-ciclista-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The second card starts with `<div class="veh-type-card">` and contains `Asistencia al Ciclista Pro`
# We will use regex to find and remove it.

pattern = r'<div class="veh-type-card">\s*<div class="vt-image"><img src="\.\./assets/img/article-3\.webp" alt="Asistencia al Ciclista" id="img-ciclista-pro">.*?</div>\s*</div>'

content = re.sub(pattern, '', content, flags=re.DOTALL)

# Also update the price of the first one to $3.200 / mes just in case it didn't update before
content = content.replace('<div class="plan-price">$7.990 / mes</div>', '<div class="plan-price">$3.200 / mes</div>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed Ciclista Pro card and updated price successfully.")
