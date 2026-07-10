import os
import re
import shutil

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

# 1. Update cotizacion.html
cot_html_path = os.path.join(base_dir, 'cotizacion.html')
with open(cot_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_card = """<div class="hub-card" data-covers="['Plomería', 'Electricidad', 'Cerrajería', 'Vidriería', 'Instalación de cortinas']" data-desc="Asistencia rápida y confiable para los imprevistos de tu hogar, incluyendo servicios de plomería, electricidad y cerrajería." data-icon="fa-house-chimney" data-link="cotizacion-asistencia-hogar-1.html" data-tag="Hogar" data-title="Asistencia Hogar" onclick="openModal(this)" onmouseenter="showCustomPopover(this)" onmouseleave="hideCustomPopover()">
<div class="hub-icon"><i class="fa-solid fa-house-chimney"></i></div>
<h3>Asistencia Hogar</h3>
<p>Protección y asistencia experta para los imprevistos de tu hogar.</p>
</div>
"""

# Insert before the closing div of tab-asistencias if not already there
if 'Asistencia Hogar' not in content:
    content = content.replace('</div>\n</div>\n</div>\n</main>', new_card + '</div>\n</div>\n</div>\n</main>')
    with open(cot_html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added card to cotizacion.html")


# 2. Duplicate and modify Escolar flow
for i in range(1, 6):
    src = os.path.join(base_dir, f'cotizacion-escolar-{i}.html')
    dst = os.path.join(base_dir, f'cotizacion-asistencia-hogar-{i}.html')
    
    if os.path.exists(src):
        with open(src, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # General replacements
        html = html.replace('Asistencia Escolar', 'Asistencia Hogar')
        html = html.replace('Asistencia Protección Escolar', 'Asistencia Hogar')
        html = html.replace('fa-school', 'fa-house-chimney')
        html = html.replace('cotizacion-escolar-', 'cotizacion-asistencia-hogar-')
        html = html.replace('mhmEscolarCart', 'mhmHogarCart')
        html = html.replace('mhmEscolarClient', 'mhmHogarClient')
        
        # Step 1 specific replacements
        if i == 1:
            html = html.replace("['Urgencia médica por accidente', 'Descuento en farmacias', 'Consulta médica general', 'Telemedicina', 'Orientación médica telefónica']", "['Plomería', 'Electricidad', 'Cerrajería', 'Vidriería', 'Instalación de cortinas']")
            
            html = re.sub(r'<li><i class="fa-solid fa-check"></i>.*?</li>', '', html) # clear old bullets
            
            bullets = """
            <li><i class="fa-solid fa-check"></i> Plomería</li>
            <li><i class="fa-solid fa-check"></i> Electricidad</li>
            <li><i class="fa-solid fa-check"></i> Cerrajería</li>
            <li><i class="fa-solid fa-check"></i> Vidriería</li>
            <li><i class="fa-solid fa-check"></i> Instalación de cortinas</li>
            """
            html = html.replace('<ul class="pet-feature-list">', '<ul class="pet-feature-list">' + bullets)
            
            # Update JS prices/keys if necessary
            html = html.replace("'escolar': { name: 'Asistencia Hogar'", "'hogar': { name: 'Asistencia Hogar'")
            html = html.replace("updateQty('escolar',", "updateQty('hogar',")
            html = html.replace("id=\"qty-escolar\"", "id=\"qty-hogar\"")
            html = html.replace("openCoverageModal('escolar')", "openCoverageModal('hogar')")
            html = html.replace("id=\"img-escolar\"", "id=\"img-hogar\"")
            html = html.replace("id=\"table-escolar\"", "id=\"table-hogar\"")
            html = html.replace("id=\"toggle-escolar\"", "id=\"toggle-hogar\"")
            html = html.replace("for=\"toggle-escolar\"", "for=\"toggle-hogar\"")
            
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Created {dst}")
