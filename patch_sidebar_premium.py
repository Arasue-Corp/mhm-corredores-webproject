import re
import os

files = [
    "/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-1.html",
    "/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-2.html"
]

premium_html = """
                    <style>
                    /* Premium Feature Cards */
                    .mhm-premium-features {
                        display: flex;
                        flex-direction: column;
                        gap: 16px;
                        margin-top: 15px;
                    }

                    .mhm-feature-card {
                        position: relative;
                        padding: 18px 16px;
                        border-radius: 16px;
                        background: linear-gradient(145deg, rgba(255,255,255,1) 0%, rgba(248,250,252,0.6) 100%);
                        border: 1px solid rgba(226, 232, 240, 0.8);
                        display: flex;
                        gap: 16px;
                        align-items: flex-start;
                        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                        overflow: hidden;
                        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
                        cursor: default;
                    }

                    .mhm-feature-card:hover {
                        transform: translateY(-4px) scale(1.02);
                        border-color: rgba(45, 212, 191, 0.4);
                        box-shadow: 0 12px 25px rgba(45, 212, 191, 0.15);
                        background: linear-gradient(145deg, rgba(255,255,255,1) 0%, rgba(240,253,250,0.9) 100%);
                    }

                    .mhm-feature-card::before {
                        content: '';
                        position: absolute;
                        top: 0; left: 0; right: 0; bottom: 0;
                        border-radius: 16px;
                        background: linear-gradient(135deg, transparent, rgba(45, 212, 191, 0.03));
                        pointer-events: none;
                    }

                    .mhm-feature-icon {
                        width: 44px;
                        height: 44px;
                        border-radius: 12px;
                        background: linear-gradient(135deg, rgba(45, 212, 191, 0.15) 0%, rgba(16, 185, 129, 0.05) 100%);
                        color: var(--brand-green, #10B981);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 1.25rem;
                        flex-shrink: 0;
                        position: relative;
                        z-index: 2;
                        transition: all 0.4s ease;
                        border: 1px solid rgba(45, 212, 191, 0.2);
                    }

                    .mhm-feature-card:hover .mhm-feature-icon {
                        background: linear-gradient(135deg, var(--brand-green, #10B981) 0%, #059669 100%);
                        color: #ffffff;
                        box-shadow: 0 6px 15px rgba(16, 185, 129, 0.35);
                        transform: rotate(-8deg) scale(1.1);
                        border-color: transparent;
                    }

                    .mhm-feature-content {
                        position: relative;
                        z-index: 2;
                        padding-top: 2px;
                    }

                    .mhm-feature-title {
                        margin: 0 0 5px 0;
                        font-size: 1rem;
                        color: #0F172A;
                        font-weight: 800;
                        letter-spacing: -0.3px;
                        transition: color 0.3s ease;
                    }

                    .mhm-feature-card:hover .mhm-feature-title {
                        color: var(--brand-green, #10B981);
                    }

                    .mhm-feature-desc {
                        margin: 0;
                        font-size: 0.85rem;
                        color: #64748B;
                        line-height: 1.45;
                        font-weight: 500;
                    }
                    </style>

                    <div class="sidebar-title" style="font-size: 1.25rem; font-weight: 800; background: linear-gradient(90deg, #0F172A, #334155); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 20px;">
                        ¿Por qué cotizar con MHM?
                    </div>

                    <div class="mhm-premium-features">
                        <div class="mhm-feature-card">
                            <div class="mhm-feature-icon"><i class="fa-solid fa-shield-halved"></i></div>
                            <div class="mhm-feature-content">
                                <h4 class="mhm-feature-title">Seguridad y Confianza</h4>
                                <p class="mhm-feature-desc">Trabajamos con las aseguradoras más prestigiosas y sólidas de Chile.</p>
                            </div>
                        </div>
                        
                        <div class="mhm-feature-card">
                            <div class="mhm-feature-icon"><i class="fa-solid fa-headset"></i></div>
                            <div class="mhm-feature-content">
                                <h4 class="mhm-feature-title">Asesoría 360°</h4>
                                <p class="mhm-feature-desc">Acompañamiento experto en la elección y gestión 24/7 de siniestros.</p>
                            </div>
                        </div>
                        
                        <div class="mhm-feature-card">
                            <div class="mhm-feature-icon"><i class="fa-solid fa-bolt"></i></div>
                            <div class="mhm-feature-content">
                                <h4 class="mhm-feature-title">Eficiencia Digital</h4>
                                <p class="mhm-feature-desc">Proceso 100% online, ultra rápido y sin papeleos innecesarios.</p>
                            </div>
                        </div>
                    </div>
"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # We need to replace everything from <div class="sidebar-title">¿Por qué elegir MHM?</div> 
        # down to the end of the organic-panel
        # Notice we matched <div class="organic-panel"> earlier.
        
        pattern = r'(<div class="organic-panel">)\s*<div class="sidebar-title">¿Por qué elegir MHM\?</div>.*?(\s*</div>\s*</aside>)'
        
        new_content = re.sub(pattern, r'\1\n' + premium_html + r'\2', content, flags=re.DOTALL)
        
        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Patched PREMIUM into {os.path.basename(fpath)}")
        else:
            print(f"No changes in {os.path.basename(fpath)}")

