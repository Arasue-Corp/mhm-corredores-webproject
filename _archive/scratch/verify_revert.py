with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()
import re
match = re.search(r'<div class="harmonic-card" style="max-width: 100%;">.*?</div>\s*<button', html, re.DOTALL)
if match:
    print("Found form block")
else:
    print("Not found form block")
