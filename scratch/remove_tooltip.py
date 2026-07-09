import re

with open('cotizacion/cotizacion-vehicular-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the tooltip we just added
# Find: <!-- Tooltip Message --> ... <!-- Form Fields -->
tooltip_regex = r'<!-- Tooltip Message -->.*?<!-- Form Fields -->'
html = re.sub(tooltip_regex, '<!-- Form Fields -->', html, flags=re.DOTALL)

# Remove the student icon from the right panel
# The user's image shows "Protección Activa" with an icon above it. Let's find "Protección Activa"
# and look for an icon nearby, like fa-graduation-cap or fa-school
html = html.replace('<i class="fa-solid fa-graduation-cap" style="color: #2ED9C3;"></i>', '')
html = html.replace('<i class="fa-solid fa-graduation-cap"></i>', '')
html = html.replace('<i class="fa-solid fa-school" style="color: #2ED9C3;"></i>', '')
html = html.replace('<i class="fa-solid fa-school"></i>', '')
# Let's just remove any i tag with graduation-cap or school near "Protección Activa"
# But maybe we want a car icon instead? "Quita el icono de estudiante"
# I will just replace any student icon in the file with a generic car or remove it. Let's just replace it with fa-car. No, the user said "Quita el icono". I'll remove it. Wait, the image shows it has NO icon, wait! The user's image SHOWS the student icon and they said "Quita el icono de estudiante". Okay, so I will remove it.

# Let's find exactly the line to remove.
# We will use regex to remove it if it's near "Protección Activa".
def remove_icon(match):
    return ""

# Remove any icon before Protección Activa
html = re.sub(r'<div[^>]*><i class="fa-solid fa-graduation-cap"[^>]*></i></div>\s*(?=<h4[^>]*>Protección Activa)', '', html, flags=re.IGNORECASE)
html = re.sub(r'<i class="fa-solid fa-graduation-cap"[^>]*></i>', '', html, flags=re.IGNORECASE)
html = re.sub(r'<div[^>]*><i class="fa-solid fa-school"[^>]*></i></div>\s*(?=<h4[^>]*>Protección Activa)', '', html, flags=re.IGNORECASE)
html = re.sub(r'<i class="fa-solid fa-school"[^>]*></i>', '', html, flags=re.IGNORECASE)

with open('cotizacion/cotizacion-vehicular-2.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated cotizacion-vehicular-2.html")
