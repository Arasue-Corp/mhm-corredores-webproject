import re
import os

files = [
    "/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-1.html",
    "/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-2.html"
]

replacement = """                    <div class="sidebar-title">¿Por qué elegir MHM?</div>
                    
                    <div style="display: flex; flex-direction: column; gap: 20px; margin-top: 25px;">
                        <div style="display: flex; gap: 15px; align-items: flex-start;">
                            <div style="background: rgba(46, 217, 195, 0.15); color: #059669; width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 1.2rem;">
                                <i class="fa-solid fa-shield-halved"></i>
                            </div>
                            <div>
                                <h4 style="margin: 0; font-size: 0.95rem; color: #0F172A; font-weight: 700;">Seguridad y Confianza</h4>
                                <p style="margin: 4px 0 0; font-size: 0.85rem; color: #475569; line-height: 1.4;">Trabajamos con las aseguradoras más prestigiosas de Chile.</p>
                            </div>
                        </div>

                        <div style="display: flex; gap: 15px; align-items: flex-start;">
                            <div style="background: rgba(46, 217, 195, 0.15); color: #059669; width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 1.2rem;">
                                <i class="fa-solid fa-headset"></i>
                            </div>
                            <div>
                                <h4 style="margin: 0; font-size: 0.95rem; color: #0F172A; font-weight: 700;">Asesoría Personalizada</h4>
                                <p style="margin: 4px 0 0; font-size: 0.85rem; color: #475569; line-height: 1.4;">Acompañamiento experto en la elección y ante cualquier siniestro.</p>
                            </div>
                        </div>

                        <div style="display: flex; gap: 15px; align-items: flex-start;">
                            <div style="background: rgba(46, 217, 195, 0.15); color: #059669; width: 38px; height: 38px; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 1.2rem;">
                                <i class="fa-solid fa-bolt"></i>
                            </div>
                            <div>
                                <h4 style="margin: 0; font-size: 0.95rem; color: #0F172A; font-weight: 700;">Cotización en Minutos</h4>
                                <p style="margin: 4px 0 0; font-size: 0.85rem; color: #475569; line-height: 1.4;">Proceso 100% digital, rápido y sin papeleos innecesarios.</p>
                            </div>
                        </div>
                    </div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Regex to find everything inside <div class="organic-panel"> ... </div>
        # and replace it if it contains "Ruta de Cotización"
        
        pattern = r'(<div class="organic-panel">)\s*<div class="sidebar-title">Ruta de Cotización</div>.*?</div>\s*</aside>'
        # wait, the closing </div> belongs to organic-panel.
        # it's better to match:
        pattern = r'(<div class="organic-panel">)\s*<div class="sidebar-title">Ruta de Cotización</div>.*?(\s*</div>\s*</aside>)'
        
        new_content = re.sub(pattern, r'\1\n' + replacement + r'\2', content, flags=re.DOTALL)
        
        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Patched {os.path.basename(fpath)}")
        else:
            print(f"No changes in {os.path.basename(fpath)}")

