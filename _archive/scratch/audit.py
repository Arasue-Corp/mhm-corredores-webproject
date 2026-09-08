import os
import glob
import re

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

patterns = ['cotizacion-asistencia-ciclista-*.html', 'cotizacion-asistencia-hogar-*.html', 'cotizacion-escolar-*.html', 'cotizacion-mascota-*.html', 'cotizacion-vehicular-*.html']
files = []
for p in patterns:
    files.extend(glob.glob(os.path.join(base_dir, p)))
files.sort()

with open('scratch/audit_report.md', 'w') as out:
    for filepath in files:
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # extract h1 inside title-group
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        h1 = h1_match.group(1).strip() if h1_match else "NO H1"
        
        # extract ruta de contratacion active step
        active_match = re.search(r'<li class="active">.*?</span>(.*?)</li>', content, re.IGNORECASE | re.DOTALL)
        active_step = active_match.group(1).strip() if active_match else "NO ACTIVE STEP"
        
        # extract all steps in ruta
        steps_match = re.findall(r'<li[^>]*>.*?</li>', content, re.IGNORECASE | re.DOTALL)
        # simplistic parsing for ruta
        ruta_steps = []
        in_ruta = False
        for line in content.split('\n'):
            if 'Ruta de Contratación' in line or '<ul class="aurora-list"' in line:
                in_ruta = True
            elif in_ruta and '</ul>' in line:
                in_ruta = False
                break
            elif in_ruta and '<li' in line:
                clean_li = re.sub(r'<[^>]+>', '', line).strip()
                ruta_steps.append(clean_li)
                
        out.write(f"### {filename}\n")
        out.write(f"- **H1:** {h1}\n")
        out.write(f"- **Active Step:** {active_step}\n")
        out.write(f"- **Ruta:** {', '.join(ruta_steps)}\n\n")

print("Audit script finished.")
