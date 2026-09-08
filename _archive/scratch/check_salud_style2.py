with open('/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-salud-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
styles = re.findall(r'<style>(.*?)</style>', content, re.DOTALL)
print(styles[1])
