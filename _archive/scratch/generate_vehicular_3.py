import re
import os

with open('cotizacion/cotizacion-escolar-3.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Escolar to Vehicular
html = html.replace('cotizacion-escolar-', 'cotizacion-vehicular-')
html = html.replace('Asistencia Escolar', 'Asistencia Vehicular')
html = html.replace('ESCOLAR', 'VEHICULAR')

with open('cotizacion/cotizacion-vehicular-3.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Generated cotizacion-vehicular-3.html")
