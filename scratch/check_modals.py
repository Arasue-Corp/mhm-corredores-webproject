import glob
import re

files = glob.glob('/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/*-1.html')
valid_files = [f for f in files if any(x in f for x in ['ciclista', 'hogar', 'escolar', 'mascota', 'vehicular', 'salud'])]

for filepath in valid_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"=== {filepath.split('/')[-1]} ===")
    
    # Check modal header
    modal_headers = re.findall(r'<div class="modal-header">(.*?)</div>', content, re.IGNORECASE | re.DOTALL)
    if modal_headers:
        for mh in modal_headers:
            icon = re.search(r'<i class="([^"]*)">', mh)
            title = re.search(r'<h2>(.*?)</h2>', mh, re.IGNORECASE | re.DOTALL)
            print(f"Modal Icon: {icon.group(1) if icon else 'NONE'}")
            # print title but remove inner tags
            print(f"Modal Title: {re.sub('<[^>]+>', '', title.group(1)).strip() if title else 'NONE'}")
            
    # Check table headers
    theads = re.findall(r'<thead[^>]*>(.*?)</thead>', content, re.IGNORECASE | re.DOTALL)
    if theads:
        for th in theads:
            cols = re.findall(r'<th[^>]*>(.*?)</th>', th, re.IGNORECASE | re.DOTALL)
            print(f"Table Headers: {cols}")
    
    # Check JS table headers if any (for salud)
    js_ths = re.findall(r'<th style="\$\{thStyle\}">(.*?)</th>', content)
    if js_ths:
        print(f"JS Table Headers: {js_ths}")
