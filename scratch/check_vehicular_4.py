with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
if re.search(r'Todos los datos registrados', html):
    print("Checkbox found")
else:
    print("Checkbox NOT found")

if re.search(r'¡Excelente elección!', html):
    print("Excelente eleccion found")
