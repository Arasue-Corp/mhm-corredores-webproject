import re
with open('cotizacion/cotizacion.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace modal HTML
old_modal_html = '''<div class="modal-image-panel">
<div class="modal-image-placeholder">
<i class="fa-regular fa-image" id="modal-icon-big"></i>
<span id="modal-image-text">Imagen</span>
</div>
</div>'''
new_modal_html = '''<div class="modal-image-panel">
<img id="modal-image-big" src="" alt="" style="width:100%; height:100%; object-fit:cover; border-top-left-radius: 20px; border-bottom-left-radius: 20px;">
</div>'''

content = content.replace(old_modal_html, new_modal_html)

# Also fix the border radius on mobile
content = content.replace('    .modal-image-panel { width: 100%; height: 150px; }', '    .modal-image-panel { width: 100%; height: 200px; }\n    .modal-image-panel img { border-bottom-left-radius: 0 !important; border-top-right-radius: 20px; }')

# Replace JS
old_js = '''        document.getElementById('modal-icon-big').className = `fa-solid ${icon}`;
        document.getElementById('modal-image-text').textContent = title;'''
new_js = '''        const img = element.getAttribute('data-img');
        if (img) {
            document.getElementById('modal-image-big').src = img;
            document.getElementById('modal-image-big').alt = title;
        }'''
content = content.replace(old_js, new_js)

# Update hub cards to add data-img
replacements = [
    ('data-title="Seguro Automotriz"', 'data-title="Seguro Automotriz" data-img="../assets/img/vehicular.svg"'),
    ('data-title="Asistencia de Salud"', 'data-title="Asistencia de Salud" data-img="../assets/img/salud.svg"'),
    ('data-title="Asistencia Veterinaria"', 'data-title="Asistencia Veterinaria" data-img="../assets/img/veterinaria.svg"'),
    ('data-title="Asistencia Protección Escolar"', 'data-title="Asistencia Protección Escolar" data-img="../assets/img/escolar.svg"'),
    ('data-title="Asistencia Vehicular"', 'data-title="Asistencia Vehicular" data-img="../assets/img/vehicular.svg"'),
    ('data-title="Asistencia Hogar"', 'data-title="Asistencia Hogar" data-img="../assets/img/hogar.svg"'),
    ('data-title="Asistencia al Ciclista"', 'data-title="Asistencia al Ciclista" data-img="../assets/img/ciclista.svg"')
]

for old, new in replacements:
    content = content.replace(old, new)

with open('cotizacion/cotizacion.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated modals with SVG images')
