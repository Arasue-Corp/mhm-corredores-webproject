import re
import os

files = [
    "/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-1.html",
    "/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-2.html"
]

target_str = '<div class="sidebar-title" style="font-size: 1.25rem; font-weight: 800; background: linear-gradient(90deg, #0F172A, #334155); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 20px;">'
new_str = '<div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px;">'

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content.replace(target_str, new_str)
        
        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Patched Title in {os.path.basename(fpath)}")
        else:
            print(f"No changes in {os.path.basename(fpath)}")

