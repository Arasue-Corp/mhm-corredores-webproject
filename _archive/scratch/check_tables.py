import re

files = [
    '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-salud-1.html',
    '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-hogar-1.html'
]

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        tables = re.findall(r'<table[^>]*>', content)
        table_wrappers = re.findall(r'<div[^>]*table[^>]*>', content, re.IGNORECASE)
        print(f"--- {filepath.split('/')[-1]} ---")
        print("Tables:", tables)
        print("Table Wrappers:", [w for w in table_wrappers if 'table-responsive' in w or 'table' in w.lower()])
    except FileNotFoundError:
        print(f"File not found: {filepath}")
