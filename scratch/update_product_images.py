import os
import re

files_map = {
    'cotizacion-mascota-1.html': 'veterinaria.svg',
    'cotizacion-escolar-1.html': 'escolar.svg',
    'cotizacion-vehicular-1.html': 'vehicular.svg',
    'cotizacion-asistencia-hogar-1.html': 'hogar.svg',
    'cotizacion-asistencia-ciclista-1.html': 'ciclista.svg'
}

for file_name, new_img in files_map.items():
    path = os.path.join('cotizacion', file_name)
    if not os.path.exists(path):
        print(f"Skipping {file_name}, not found.")
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace `<img src="../assets/img/XXXXX.jpg" ...>` with `<img src="../assets/img/YYYYY.svg" ...>`
    # but only in the product cards. We can target `class="vt-image"><img src="..."`
    
    # Regex to match `<div class="vt-image"><img src="ANYTHING" alt="ANYTHING" id="ANYTHING"></div>`
    # Actually, we can just replace the `src` attribute of `<img>` tags immediately following `<div class="vt-image">`
    
    def replacer(match):
        # match.group(0) is `<div class="vt-image"><img src="old_url"`
        prefix = match.group(1) # `<div class="vt-image"><img ` or similar
        src_attr = f'src="../assets/img/{new_img}"'
        return f'{prefix}{src_attr}'

    new_content = re.sub(r'(<div class="vt-image">\s*<img\s+)src="[^"]+"', replacer, content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file_name} with {new_img}")
