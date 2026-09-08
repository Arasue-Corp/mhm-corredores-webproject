import re
import os

files_to_update = [
    'cotizacion/cotizacion-escolar-2.html',
    'cotizacion/cotizacion-escolar-3.html',
    'cotizacion/cotizacion-escolar-4.html'
]

new_list = """
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
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
                            </li>
"""

# Regex to match the ul containing the old list
ul_pattern = re.compile(r'<ul style="list-style: none; padding: 0; margin: 0 0 20px 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">.*?</ul>', re.DOTALL)

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_ul = '<ul style="list-style: none; padding: 0; margin: 0 0 20px 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">' + new_list + '                        </ul>'
    
    content = ul_pattern.sub(new_ul, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done updating summaries")
