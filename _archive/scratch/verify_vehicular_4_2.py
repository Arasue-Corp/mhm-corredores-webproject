with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Has fa-user-graduate?', 'fa-user-graduate' in html)
print('Has max-width: 100%?', 'max-width: 100%;' in html)
print('Has nested?', 'class="form-grid-2"\\n                <div class="form-grid-2"' in html)
