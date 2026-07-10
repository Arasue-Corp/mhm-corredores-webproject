with open('/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-salud-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
styles = re.findall(r'<style>(.*?)</style>', content, re.DOTALL)
for i, s in enumerate(styles):
    if 'table' in s.lower() or 'cov-' in s.lower() or 'responsive' in s.lower():
        print(f"--- Style Block {i+1} ---")
        print(s[:500]) # Print first 500 chars to see what it is
