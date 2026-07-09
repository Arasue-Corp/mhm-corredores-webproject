import re

with open('cotizacion/cotizacion-vehicular-5.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the Registrar button link to cotizacion-vehicular-6.html
html = html.replace("window.location.href='index.html'", "window.location.href='cotizacion-vehicular-6.html'")

with open('cotizacion/cotizacion-vehicular-5.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated cotizacion-vehicular-5.html to link to page 6")
