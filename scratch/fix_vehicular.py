import os

# Fix cotizacion-vehicular-2.html
with open('cotizacion/cotizacion-vehicular-2.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

# Replace student icon in protection box
html2 = html2.replace('<i class="fa-solid fa-user-graduate" style="font-size: 2rem; color: #10B981; margin-bottom: 10px;"></i>', '<i class="fa-solid fa-car" style="font-size: 2rem; color: #10B981; margin-bottom: 10px;"></i>')

with open('cotizacion/cotizacion-vehicular-2.html', 'w', encoding='utf-8') as f:
    f.write(html2)

# Fix cotizacion-vehicular-3.html
with open('cotizacion/cotizacion-vehicular-3.html', 'r', encoding='utf-8') as f:
    html3 = f.read()

# Replace student icon in modal
html3 = html3.replace('<i class="fa-solid fa-user-graduate" style="font-size: 5rem; color: #104C5C; position: relative; z-index: 2;"></i>', '<i class="fa-solid fa-car" style="font-size: 5rem; color: #104C5C; position: relative; z-index: 2;"></i>')

# Replace text
html3 = html3.replace('LOS DATOS DEL ESTUDIANTE.', 'TUS DATOS Y<br>LOS DE TU VEHÍCULO.')

with open('cotizacion/cotizacion-vehicular-3.html', 'w', encoding='utf-8') as f:
    f.write(html3)

print("Files updated.")
