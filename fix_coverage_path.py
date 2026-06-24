import re
import os

configs = {
    "cotizacion-3-1.html": {
        "back_url": "cotizacion-1.html",
        "back_text": "Volver al inicio",
        "next_url": "cotizacion-4-1.html",
        "step_text": "Paso 1 de 7",
        "progress": "14",
        "tip": "¡Hola! Soy Alex. Ingresa los datos de tu auto 0km para buscar la cobertura ideal."
    },
    "cotizacion-4-1.html": {
        "back_url": "cotizacion-3-1.html",
        "back_text": "Volver a Datos de Auto",
        "next_url": "cotizacion-5-1.html",
        "step_text": "Paso 2 de 7",
        "progress": "28",
        "tip": "Ya casi. Necesito tus datos de contacto para enviarte las cotizaciones y avanzar."
    },
    "cotizacion-5-1.html": {
        "back_url": "cotizacion-4-1.html",
        "back_text": "Volver",
        "next_url": "cotizacion-6-1.html",
        "step_text": "Paso 3 de 7",
        "progress": "42",
        "tip": "Analizando cientos de opciones para encontrar el mejor precio..."
    },
    "cotizacion-6-1.html": {
        "back_url": "cotizacion-4-1.html",
        "back_text": "Volver a Datos",
        "next_url": "cotizacion-7-1.html",
        "step_text": "Paso 4 de 7",
        "progress": "57",
        "tip": "¡Encontré excelentes opciones! Compara los deducibles y elige la que más se ajuste a ti."
    },
    "cotizacion-7-1.html": {
        "back_url": "cotizacion-6-1.html",
        "back_text": "Volver a Resultados",
        "next_url": "cotizacion-8-1.html",
        "step_text": "Paso 5 de 7",
        "progress": "71",
        "tip": "Excelente elección. Revisa los detalles de la cobertura y asistencias antes de continuar."
    },
    "cotizacion-8-1.html": {
        "back_url": "cotizacion-7-1.html",
        "back_text": "Volver a Coberturas",
        "next_url": "cotizacion-9-1.html",
        "step_text": "Paso 6 de 7",
        "progress": "85",
        "tip": "Al ser un auto 0Km, necesitamos la factura o guía de despacho (con máximo 48 hrs de antigüedad) para validar."
    },
    "cotizacion-9-1.html": {
        "back_url": "cotizacion-8-1.html",
        "back_text": "Volver a Documentos",
        "next_url": "cotizacion-10-1-fid.html",
        "step_text": "Paso 7 de 7",
        "progress": "100",
        "tip": "¡Último paso! Confirma tus datos, elige cómo pagar (PAC/PAT) y tu seguro quedará emitido."
    }
}

base_path = "cotizacion/"

for filename, cfg in configs.items():
    filepath = os.path.join(base_path, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}, not found.")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Back link update
    # <a href="cotizacion-2.html" class="nav-back-btn"><div class="icon-circle"><i class="fa-solid fa-arrow-left"></i></div><span> Volver</span></a>
    content = re.sub(r'(<a href=")([^"]+)(" class="nav-back-btn">.*?<span>)\s*([^<]*)(</span>)', 
                     rf'\g<1>{cfg["back_url"]}\g<3>{cfg["back_text"]}\g<5>', 
                     content)
    
    # 2. Next link update
    # In forms, it might be <a href="..." id="linkNext"> or button onclick="window.location.href='...'"
    content = re.sub(r'(id="linkNext"[^>]*href=")([^"]+)(")', rf'\g<1>{cfg["next_url"]}\g<3>', content)
    content = re.sub(r'(onclick="window\.location\.href=\')([^\']+)(\'")', rf'\g<1>{cfg["next_url"]}\g<3>', content)
    
    # 5-1.html specific loading redirect
    if filename == "cotizacion-5-1.html":
        content = re.sub(r'(setTimeout\(\(\) => \{\n\s*window\.location\.href = \')([^\']+)(\';)', 
                         rf'\g<1>{cfg["next_url"]}\g<3>', content)
    
    # 3. Progress Bar Step Text
    content = re.sub(r'(<div class="step-text[^"]*">)Paso \d+ de \d+(</div>)', 
                     rf'\g<1>{cfg["step_text"]}\g<2>', content)
                     
    # 4. Progress Bar Width
    content = re.sub(r'(<div class="progress-bar-fill"[^>]*style="width: )\d+(%;"></div>)', 
                     rf'\g<1>{cfg["progress"]}\g<2>', content)
                     
    # 5. AI Tip Update
    # <p class="chatbot-message">...</p>
    content = re.sub(r'(<p class="chatbot-message"[^>]*>)(.*?)(</p>)', 
                     rf'\1{cfg["tip"]}\3', content, flags=re.DOTALL)
                     
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Processed {filename}")

# Fix 10-1-fid.html manually
try:
    with open("cotizacion/cotizacion-10-1-fid.html", "r", encoding="utf-8") as f:
        c10 = f.read()
    # remove back link entirely
    c10 = re.sub(r'<a href="[^"]+" class="nav-back-btn">.*?</a>', '', c10, flags=re.DOTALL)
    with open("cotizacion/cotizacion-10-1-fid.html", "w", encoding="utf-8") as f:
        f.write(c10)
    print("Processed cotizacion-10-1-fid.html")
except Exception as e:
    print(e)

