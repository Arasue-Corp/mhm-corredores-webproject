import re

def extract_form(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'<div class="harmonic-card">(.*?)</div>', content, re.IGNORECASE | re.DOTALL)
    if match:
        print(f"--- {filepath} FORM ---")
        print(match.group(1))
    else:
        print(f"--- {filepath} NO FORM ---")

extract_form('/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-vehicular-4.html')
extract_form('/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-vehicular-5.html')
