import os
import re

with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the bullet points in the right panel summary
old_bullets = '''<li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Urgencia médica por accidente.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Descuento en farmacias.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Consulta médica general y Telemedicina.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Orientación médica telefónica.
                            </li>'''

new_bullets = '''<li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Protección y coberturas 100%.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Eventos disponibles todo el año.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Usa tu Asistencia Integral Pro en el centro médico que desees, estamos en todo Chile.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Reembolso rápido y fácil.
                            </li>'''

if old_bullets in html:
    html = html.replace(old_bullets, new_bullets)
    print("Bullets replaced using direct string match")
else:
    # Try Regex
    pattern = re.compile(r'<li style="display: flex; align-items: start; margin-bottom: 10px;">.*?Orientaci[ó\xcc\x81\xc3\xb3]n.*?</li>', re.DOTALL)
    if pattern.search(html):
        html = pattern.sub(new_bullets, html)
        print("Bullets replaced using regex")
    else:
        print("WARNING: Could not find bullets")

with open('cotizacion/cotizacion-vehicular-4.html', 'w', encoding='utf-8') as f:
    f.write(html)
