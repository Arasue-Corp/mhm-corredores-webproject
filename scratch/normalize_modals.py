import re
import glob

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'
files = glob.glob(base_dir + '/*-1.html')

configs = {
    'cotizacion-asistencia-ciclista-1.html': {'icon': 'fa-person-biking', 'title': 'Coberturas: Asistencia al Ciclista'},
    'cotizacion-asistencia-hogar-1.html': {'icon': 'fa-house', 'title': 'Coberturas: Asistencia Hogar'},
    'cotizacion-escolar-1.html': {'icon': 'fa-graduation-cap', 'title': 'Coberturas: Asistencia Escolar'},
    'cotizacion-mascota-1.html': {'icon': 'fa-paw', 'title': 'Coberturas: Asistencia Mascotas'},
    'cotizacion-vehicular-1.html': {'icon': 'fa-car', 'title': 'Coberturas: Asistencia Vehicular'},
    'cotizacion-salud-1.html': {'icon': 'fa-heart-pulse', 'title': 'Coberturas: Asistencia de Salud'}
}

# The standard table header block we want everywhere
standard_thead = '''<thead>
                            <tr>
                                <th style="padding: 15px; font-weight: 700; border: 1px solid #E2E8F0;">SERVICIO</th>
                                <th style="padding: 15px; font-weight: 700; border: 1px solid #E2E8F0;">PROTECCIÓN</th>
                                <th style="padding: 15px; font-weight: 700; border: 1px solid #E2E8F0;">LÍMITE</th>
                                <th style="padding: 15px; font-weight: 700; border: 1px solid #E2E8F0;">MAX EVENTOS AL AÑO</th>
                            </tr>
                        </thead>'''

for filepath in files:
    filename = filepath.split('/')[-1]
    if filename not in configs:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    cfg = configs[filename]
    
    # 1. Fix Modal Header Icon and Title
    # It looks like:
    # <div class="header-icon-glass"><i class="fa-solid fa-graduation-cap"></i></div>
    # <div class="header-text-tech">
    #     <h3 class="tech-title text-gradient-corp" id="covModalTitle">Coberturas: Asistencia Hogar</h3>
    
    content = re.sub(
        r'<div class="header-icon-glass"><i class="[^"]*"></i></div>\s*<div class="header-text-tech">\s*<h3 class="tech-title text-gradient-corp" id="covModalTitle">.*?</h3>',
        f'<div class="header-icon-glass"><i class="fa-solid {cfg["icon"]}"></i></div>\n                <div class="header-text-tech">\n                    <h3 class="tech-title text-gradient-corp" id="covModalTitle">{cfg["title"]}</h3>',
        content, flags=re.IGNORECASE
    )
    
    # 2. Fix <thead> headers
    # We want to replace any <thead>...</thead> that looks like it's inside a table with the standard one, EXCEPT in salud where they might have 'Cobertura', 'Límite / Eventos' for something else?
    # Wait, in salud they have 4-column tables for the main coverages, but also maybe 2-column tables?
    # Let's replace ONLY if the thead has 4 ths.
    def replace_thead(match):
        inner = match.group(0)
        ths = re.findall(r'<th', inner, re.IGNORECASE)
        if len(ths) == 4:
            return standard_thead
        return inner
        
    content = re.sub(r'<thead[^>]*>.*?</thead>', replace_thead, content, flags=re.IGNORECASE | re.DOTALL)
    
    # 3. Fix Salud Javascript labels and THs
    if filename == 'cotizacion-salud-1.html':
        content = content.replace('data-label="Cobertura"', 'data-label="SERVICIO"')
        content = content.replace('data-label="Copago"', 'data-label="PROTECCIÓN"')
        content = content.replace('data-label="Monto Máximo"', 'data-label="LÍMite"')
        content = content.replace('data-label="Límite Anual"', 'data-label="MAX EVENTOS AL AÑO"')
        # Note: JavaScript generates headers too:
        content = content.replace('<th style="${thStyle}">Servicio</th>', '<th style="${thStyle}">SERVICIO</th>')
        content = content.replace('<th style="${thStyle}">Protección</th>', '<th style="${thStyle}">PROTECCIÓN</th>')
        content = content.replace('<th style="${thStyle}">Límite</th>', '<th style="${thStyle}">LÍMITE</th>')
        content = content.replace('<th style="${thStyle}">Max Eventos al Año</th>', '<th style="${thStyle}">MAX EVENTOS AL AÑO</th>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Normalized {filename}")

