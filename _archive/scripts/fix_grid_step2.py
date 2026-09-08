import re

with open("cotizacion/cotizacion-mascota-2.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Remove grid override
c = c.replace('.specs-layout-grid { display: block !important; }', '/* Grid enabled for step 2 */')
c = c.replace('<div class="main-spec-col" style="grid-column: 1 / -1;">', '<div class="main-spec-col">')

# 2. Insert aside after main-spec-col
# The main-spec-col ends where `<div id="quotesModal"` or footer used to be.
# Wait, let's find the closing div of main-spec-col.
# main-spec-col -> premium-white-card -> form.
# The form closes, then premium-white-card closes, then main-spec-col closes.
# Let's just find:
target_insertion = """</form>
                </div>
            </div>"""

if target_insertion in c:
    aside_html = """</form>
                </div>
            </div>

            <aside class="config-sidebar anim-entry delay-2">
                <div class="organic-panel" style="position: sticky; top: 100px;">
                    
                    <div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px;">
                        Ruta de Contratación
                    </div>
                    <ul class="aurora-list" style="margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px;">
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Selección de Plan</li>
                        <li class="active"><span class="pulse-dot"></span> Datos del Contratante</li>
                        <li><i class="fa-regular fa-circle"></i> Datos de la Mascota</li>
                        <li><i class="fa-regular fa-circle"></i> Pago y Emisión</li>
                    </ul>

                    <div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px; border-bottom: 1px solid #E2E8F0; padding-bottom: 15px;">
                        Resumen de Selección
                    </div>
                    
                    <div id="cart-summary-step2">
                        <!-- Javascript will render selected plans here -->
                    </div>

                    <div style="background: rgba(16, 185, 129, 0.05); border: 1px dashed #10B981; border-radius: 12px; padding: 15px; margin-top: 25px; text-align: center;">
                        <i class="fa-solid fa-shield-cat" style="font-size: 2rem; color: #10B981; margin-bottom: 10px;"></i>
                        <h4 style="margin: 0 0 5px 0; color: #0F172A; font-weight: 700; font-size: 1rem;">Protección Activa</h4>
                        <p style="margin: 0; font-size: 0.85rem; color: #64748B;">Estás a pocos pasos de asegurar a tu mascota.</p>
                    </div>
                </div>
            </aside>
"""
    c = c.replace(target_insertion, aside_html)
    print("ASIDE INSERTED.")
else:
    print("TARGET NOT FOUND FOR INSERTION.")

# Make sure modals are removed (just in case)
c = re.sub(r'<div id="quotesModal".*?(?=<footer class="footer-aurora">)', '', c, flags=re.DOTALL)
c = re.sub(r'<!-- Modal Leads -->.*?</div>\s*</div>\s*</div>', '', c, flags=re.DOTALL)

with open("cotizacion/cotizacion-mascota-2.html", "w", encoding="utf-8") as f:
    f.write(c)

