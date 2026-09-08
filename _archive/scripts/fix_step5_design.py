import re

with open('cotizacion/cotizacion-mascota-5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace everything inside the page-wrapper.
# First, let's find the closing tag of <div class="page-wrapper"
start_idx = content.find('<div class="page-wrapper"')
if start_idx == -1:
    print("Could not find page-wrapper")
    exit(1)

# we know the script tag comes after the page-wrapper div closes, but we also have our injected script there
# let's just find the start of the previous page-wrapper and the start of the script tag
script_idx = content.find('<script>', start_idx)

if script_idx == -1:
    print("Could not find script tag")
    exit(1)

head_content = content[:start_idx]
footer_content = content[script_idx:]

new_html = """
    <div class="page-wrapper" style="background: transparent; min-height: 80vh; display: flex; align-items: center; justify-content: center; position: relative; padding: 20px;">
        <!-- Confetti Background (CSS based) -->
        <div class="confetti-container" style="position: absolute; top:0; left:0; width:100%; height:100%; overflow:hidden; z-index:0; pointer-events:none;">
            <!-- Simple dots via CSS background -->
        </div>
        
        <div class="premium-white-card anim-entry" style="position: relative; z-index: 1; max-width: 800px; width: 100%; padding: 0; overflow: hidden; display: flex; flex-direction: column;">
            
            <div style="background: var(--primary, #104C5C); color: white; text-align: center; padding: 25px 20px; font-size: 1.25rem; font-weight: 800; letter-spacing: 1px; display: flex; align-items: center; justify-content: center; gap: 10px;">
                <i class="fa-solid fa-circle-check" style="font-size: 1.7rem; color: var(--accent, #A3D80E);"></i>
                ¡TU ASISTENCIA YA ESTÁ ACTIVA!
            </div>
            
            <div style="padding: 40px 30px;">
                <h3 class="text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 25px; display: flex; align-items: center; gap: 10px;">
                    <i class="fa-solid fa-file-invoice" style="color: var(--primary, #104C5C); font-size: 1.1rem;"></i>
                    Detalle de contratación:
                </h3>
                <ul style="list-style: none; padding: 0; margin: 0 0 40px 15px; color: var(--text-dark, #1E293B); line-height: 1.8; font-size: 1.05rem;">
                    <li style="display: flex; gap: 12px; margin-bottom: 15px; align-items: flex-start;">
                        <i class="fa-solid fa-file-contract" style="color: var(--accent, #A3D80E); margin-top: 4px;"></i>
                        <div><strong style="color: var(--primary, #104C5C);">Nº de contrato:</strong> <span id="contractNumber">1234567</span></div>
                    </li>
                    <li style="display: flex; gap: 12px; margin-bottom: 15px; align-items: flex-start;">
                        <i class="fa-solid fa-calendar-check" style="color: var(--accent, #A3D80E); margin-top: 4px;"></i>
                        <div><strong style="color: var(--primary, #104C5C);">Fecha de activación:</strong> <span id="activationDate">Cargando...</span></div>
                    </li>
                    <li style="display: flex; gap: 12px; margin-bottom: 15px; align-items: flex-start;">
                        <i class="fa-solid fa-credit-card" style="color: var(--accent, #A3D80E); margin-top: 4px;"></i>
                        <div><strong style="color: var(--primary, #104C5C);">Medio de pago:</strong> Tarjeta terminada en *****4539</div>
                    </li>
                    <li style="display: flex; gap: 12px; margin-bottom: 15px; align-items: flex-start;">
                        <i class="fa-solid fa-sack-dollar" style="color: var(--accent, #A3D80E); margin-top: 4px;"></i>
                        <div><strong style="color: var(--primary, #104C5C);">Total mensual:</strong> <span id="totalMonthly" style="font-weight: 800;">Cargando...</span></div>
                    </li>
                </ul>
                
                <h3 class="text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 25px; display: flex; align-items: center; gap: 10px;">
                    <i class="fa-solid fa-layer-group" style="color: var(--primary, #104C5C); font-size: 1.1rem;"></i>
                    Acciones disponibles:
                </h3>
                <ul style="padding: 0; margin: 0 0 40px 15px; list-style: none; color: var(--text-dark, #1E293B); line-height: 1.8; font-size: 1.05rem;">
                    <li style="display: flex; gap: 12px; margin-bottom: 15px; align-items: flex-start;">
                        <i class="fa-solid fa-envelope-circle-check" style="color: var(--accent, #A3D80E); margin-top: 4px;"></i>
                        <div>Te enviamos una copia de tu contrato a <strong id="ownerEmail" style="color: var(--primary, #104C5C);">tu correo</strong> o <a href="#" style="color: var(--accent, #A3D80E); font-weight: 800; text-decoration: none;">descárgala aquí</a>.<br><span style="font-size: 0.85rem; color: #64748B;">*Revisar por contrato después de 24 hrs.</span></div>
                    </li>
                    <li style="display: flex; gap: 12px; margin-bottom: 15px; align-items: flex-start;">
                        <i class="fa-solid fa-scale-balanced" style="color: var(--accent, #A3D80E); margin-top: 4px;"></i>
                        <div>Conoce el <a href="#" style="color: var(--accent, #A3D80E); font-weight: 800; text-decoration: none;">detalle legal de tu asistencia</a>.</div>
                    </li>
                </ul>
                
                <div style="text-align: center; margin-top: 50px; border-top: 1px dashed #CBD5E1; padding-top: 40px;">
                    <h2 class="text-gradient-corp" style="font-size: 1.4rem; font-weight: 900; margin-bottom: 10px; text-transform: uppercase;">
                        CUIDAR LO QUE QUIERES NO TERMINA AQUÍ 
                        <i class="fa-solid fa-heart" style="color: var(--accent, #A3D80E);"></i>
                    </h2>
                    <p style="color: #64748B; font-size: 1rem; margin-bottom: 30px; max-width: 600px; margin-left: auto; margin-right: auto; font-weight: 500;">
                        Descubre otras asistencias que pueden ayudarte en tu día a día:
                    </p>
                    
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
                        <!-- Hogar -->
                        <div class="card-hover-effect" style="background: #F8FAFC; border-radius: 16px; padding: 30px 20px; text-align: center; border: 1px solid #E2E8F0; cursor: pointer; transition: 0.3s;" onmouseover="this.style.borderColor='var(--accent, #A3D80E)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.borderColor='#E2E8F0'; this.style.transform='translateY(0)';">
                            <div style="background: var(--primary, #104C5C); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; color: white; font-size: 2rem; box-shadow: 0 10px 20px rgba(16,76,92,0.15);">
                                <i class="fa-solid fa-house"></i>
                            </div>
                            <h4 class="text-gradient-corp" style="font-size: 1.15rem; font-weight: 800; margin-bottom: 5px; text-transform: uppercase;">Hogar</h4>
                            <span style="color: #64748B; font-size: 0.85rem; font-weight: 700;">DESDE <strong style="color: var(--primary, #104C5C); font-size: 1.15rem;">$7.990</strong></span>
                        </div>
                        
                        <!-- Movilidad -->
                        <div class="card-hover-effect" style="background: #F8FAFC; border-radius: 16px; padding: 30px 20px; text-align: center; border: 1px solid #E2E8F0; cursor: pointer; transition: 0.3s;" onmouseover="this.style.borderColor='var(--accent, #A3D80E)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.borderColor='#E2E8F0'; this.style.transform='translateY(0)';">
                            <div style="background: var(--primary, #104C5C); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; color: white; font-size: 2rem; box-shadow: 0 10px 20px rgba(16,76,92,0.15);">
                                <i class="fa-solid fa-car-side"></i>
                            </div>
                            <h4 class="text-gradient-corp" style="font-size: 1.15rem; font-weight: 800; margin-bottom: 5px; text-transform: uppercase;">Movilidad</h4>
                            <span style="color: #64748B; font-size: 0.85rem; font-weight: 700;">DESDE <strong style="color: var(--primary, #104C5C); font-size: 1.15rem;">$3.200</strong></span>
                        </div>
                        
                        <!-- Salud -->
                        <div class="card-hover-effect" style="background: #F8FAFC; border-radius: 16px; padding: 30px 20px; text-align: center; border: 1px solid #E2E8F0; cursor: pointer; transition: 0.3s;" onmouseover="this.style.borderColor='var(--accent, #A3D80E)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.borderColor='#E2E8F0'; this.style.transform='translateY(0)';">
                            <div style="background: var(--primary, #104C5C); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; color: white; font-size: 2rem; box-shadow: 0 10px 20px rgba(16,76,92,0.15);">
                                <i class="fa-solid fa-hand-holding-medical"></i>
                            </div>
                            <h4 class="text-gradient-corp" style="font-size: 1.15rem; font-weight: 800; margin-bottom: 5px; text-transform: uppercase;">Salud</h4>
                            <span style="color: #64748B; font-size: 0.85rem; font-weight: 700;">DESDE <strong style="color: var(--primary, #104C5C); font-size: 1.15rem;">$3.780</strong></span>
                        </div>
                    </div>
                </div>
                
                <!-- Botón Volver al Inicio -->
                <div style="text-align: center; margin-top: 40px;">
                    <a href="../index.html" class="btn-primary" style="display: inline-block; padding: 15px 40px; font-weight: 800; font-size: 1.1rem; text-decoration: none; border-radius: 30px; box-shadow: 0 10px 20px rgba(16,76,92,0.2);">
                        Volver al Inicio
                    </a>
                </div>
            </div>
        </div>
    </div>
"""

with open('cotizacion/cotizacion-mascota-5.html', 'w', encoding='utf-8') as f:
    f.write(head_content + new_html + footer_content)

print("Updated cotizacion-mascota-5.html with MHM design system")
