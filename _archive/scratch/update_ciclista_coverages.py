import os
import re

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-ciclista-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the coverages list in JS
content = re.sub(
    r"const baseCoverages = \[.*?\];", 
    """const baseCoverages = [
            { icon: '<i class=\"fa-solid fa-heart-pulse\"></i>', text: 'URGENCIA MÉDICA POR ACCIDENTE EN BICICLETA' },
            { icon: '<i class=\"fa-solid fa-money-bill-wave\"></i>', text: 'DESCUENTO EN FARMACIAS' },
            { icon: '<i class=\"fa-solid fa-user-doctor\"></i>', text: 'TELEMEDICINA' },
            { icon: '<i class=\"fa-solid fa-phone-volume\"></i>', text: 'ORIENTACIÓN MÉDICA TELEFÓNICA' },
            { icon: '<i class=\"fa-solid fa-scale-balanced\"></i>', text: 'ASISTENCIA LEGAL TELEFÓNICA' }
        ];""", 
    content, flags=re.DOTALL
)

content = re.sub(
    r"const proCoverages = \[.*?\];", 
    """const proCoverages = [
            { icon: '<i class=\"fa-solid fa-heart-pulse\"></i>', text: 'URGENCIA MÉDICA POR ACCIDENTE EN BICICLETA (Tope Alto)' },
            { icon: '<i class=\"fa-solid fa-money-bill-wave\"></i>', text: 'DESCUENTO EN FARMACIAS' },
            { icon: '<i class=\"fa-solid fa-user-doctor\"></i>', text: 'TELEMEDICINA ILIMITADA' },
            { icon: '<i class=\"fa-solid fa-phone-volume\"></i>', text: 'ORIENTACIÓN MÉDICA TELEFÓNICA' },
            { icon: '<i class=\"fa-solid fa-scale-balanced\"></i>', text: 'ASISTENCIA LEGAL TELEFÓNICA' }
        ];""", 
    content, flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Ciclista coverages successfully.")
