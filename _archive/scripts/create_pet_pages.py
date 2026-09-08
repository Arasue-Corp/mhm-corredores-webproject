import re

# 1. Create cotizacion-mascota-1.html based on cotizacion-1.html
with open("cotizacion/cotizacion-1.html", "r", encoding="utf-8") as f:
    c1 = f.read()

# Modify title
c1 = c1.replace("<title>Cotización de Seguro Automotriz | MHM Corredores</title>", "<title>Cotización de Asistencia Mascota | MHM Corredores</title>")

# Modify Welcome Modal title
c1 = c1.replace("Cotizando tu Vehículo", "Cotizando Asistencia Mascota")
c1 = c1.replace("Ingresa la patente de tu auto", "Conoce nuestras opciones de asistencia veterinaria")
c1 = c1.replace("Rápido, 100% online y con el respaldo de MHM Seguros.", "Rápido, 100% online y pensado en tus peludos.")

# Modify the progress header
c1 = c1.replace('<span>1</span>/<span>15</span>', '<span>1</span>/<span>3</span>')
c1 = c1.replace('Ingresa tu patente', 'Selecciona tu Plan')

# Modify the main content block to show 3 plans
# Looking for <h2 class="form-main-title">Ingresa la patente de tu auto</h2>
new_main_content = """
                    <h2 class="form-main-title">Nuestros Planes de Asistencia</h2>
                    <p class="form-desc" style="margin-bottom: 24px;">Selecciona el plan que mejor se adapte a las necesidades de tu mascota.</p>

                    <div class="plans-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 30px;">
                        <!-- Plan 1 -->
                        <div class="mhm-feature-card" style="flex-direction: column; cursor: pointer; border: 2px solid transparent;" onclick="selectPlan(this)">
                            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                                <div class="mhm-feature-icon" style="width: 50px; height: 50px;"><i class="fa-solid fa-paw"></i></div>
                                <div>
                                    <h4 class="mhm-feature-title" style="font-size: 1.1rem;">Asistencia Mascota</h4>
                                    <span style="font-size: 0.8rem; color: #64748B;">Plan Básico</span>
                                </div>
                            </div>
                            <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.9rem; color: #334155; line-height: 1.6;">
                                <li><i class="fa-solid fa-check" style="color: #10B981; margin-right: 8px;"></i> Urgencia médica veterinaria</li>
                                <li><i class="fa-solid fa-check" style="color: #10B981; margin-right: 8px;"></i> Consulta veterinaria (2 al año)</li>
                                <li><i class="fa-solid fa-check" style="color: #10B981; margin-right: 8px;"></i> Vacuna antirrábica</li>
                            </ul>
                        </div>
                        
                        <!-- Plan 2 -->
                        <div class="mhm-feature-card" style="flex-direction: column; cursor: pointer; border: 2px solid var(--brand-blue, #2563EB); position: relative;" onclick="selectPlan(this)">
                            <div style="position: absolute; top: -12px; right: 16px; background: var(--brand-blue, #2563EB); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700;">RECOMENDADO</div>
                            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                                <div class="mhm-feature-icon" style="width: 50px; height: 50px; background: linear-gradient(135deg, rgba(37, 99, 235, 0.15) 0%, rgba(37, 99, 235, 0.05) 100%); color: var(--brand-blue, #2563EB);"><i class="fa-solid fa-shield-dog"></i></div>
                                <div>
                                    <h4 class="mhm-feature-title" style="font-size: 1.1rem; color: var(--brand-blue, #2563EB);">Asistencia Mascota Pro</h4>
                                    <span style="font-size: 0.8rem; color: #64748B;">Plan Completo</span>
                                </div>
                            </div>
                            <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.9rem; color: #334155; line-height: 1.6;">
                                <li><i class="fa-solid fa-check" style="color: var(--brand-blue, #2563EB); margin-right: 8px;"></i> Urgencia médica veterinaria</li>
                                <li><i class="fa-solid fa-check" style="color: var(--brand-blue, #2563EB); margin-right: 8px;"></i> Consultas ilimitadas</li>
                                <li><i class="fa-solid fa-check" style="color: var(--brand-blue, #2563EB); margin-right: 8px;"></i> Descuentos en farmacias</li>
                                <li><i class="fa-solid fa-check" style="color: var(--brand-blue, #2563EB); margin-right: 8px;"></i> Telemedicina veterinaria</li>
                            </ul>
                        </div>

                        <!-- Plan 3 -->
                        <div class="mhm-feature-card" style="flex-direction: column; cursor: pointer; border: 2px solid transparent;" onclick="selectPlan(this)">
                            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                                <div class="mhm-feature-icon" style="width: 50px; height: 50px; background: linear-gradient(135deg, rgba(124, 58, 237, 0.15) 0%, rgba(124, 58, 237, 0.05) 100%); color: #7C3AED;"><i class="fa-solid fa-award"></i></div>
                                <div>
                                    <h4 class="mhm-feature-title" style="font-size: 1.1rem;">Asistencia Senior</h4>
                                    <span style="font-size: 0.8rem; color: #64748B;">Mascotas mayores de 7 años</span>
                                </div>
                            </div>
                            <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.9rem; color: #334155; line-height: 1.6;">
                                <li><i class="fa-solid fa-check" style="color: #7C3AED; margin-right: 8px;"></i> Cobertura especializada</li>
                                <li><i class="fa-solid fa-check" style="color: #7C3AED; margin-right: 8px;"></i> Exámenes geriátricos</li>
                                <li><i class="fa-solid fa-check" style="color: #7C3AED; margin-right: 8px;"></i> Asistencia 24/7</li>
                            </ul>
                        </div>
                    </div>

                    <div class="form-actions" style="margin-top: 30px;">
                        <a href="cotizacion-mascota-2.html" class="btn-aurora-gradient btn-continue" style="width: 100%; justify-content: center;">
                            <span>Continuar</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                    
                    <script>
                        function selectPlan(element) {
                            document.querySelectorAll('.plans-grid .mhm-feature-card').forEach(el => {
                                el.style.border = '2px solid transparent';
                            });
                            element.style.border = '2px solid var(--brand-blue, #2563EB)';
                        }
                    </script>
"""

# Replace the specific block of content where the form group resides
# I will use regex to find everything from <h2 class="form-main-title"> to <div class="form-actions"> ... </div> (and replace it)
pattern = re.compile(r'<h2 class="form-main-title">.*?<div class="form-actions">.*?</div>', re.DOTALL)
c1 = pattern.sub(new_main_content.strip(), c1)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c1)

print("Created cotizacion-mascota-1.html")

