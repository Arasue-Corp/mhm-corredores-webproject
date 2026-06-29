import re
import shutil

# Copy step 2 to step 3 as a baseline
shutil.copy("cotizacion/cotizacion-mascota-2.html", "cotizacion/cotizacion-mascota-3.html")

with open("cotizacion/cotizacion-mascota-3.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Update Title and Progress
c = c.replace('<title>Cotización Mascota - Paso 2 | Seguros MHM</title>', '<title>Cotización Mascota - Pago | Seguros MHM</title>')
c = c.replace('<div class="progress-fill" style="width: 50%;"></div>', '<div class="progress-fill" style="width: 100%;"></div>')

# 2. Update Header Text
old_header = """<div class="title-group">
                    <h1 class="text-gradient-corp">Datos del Contratante</h1>
                    <div class="aurora-line"></div> 
                </div>
                <p>Ingresa tus datos personales para continuar con la cotización.</p>"""
new_header = """<div class="title-group">
                    <h1 class="text-gradient-corp">Confirmación y Pago</h1>
                    <div class="aurora-line"></div> 
                </div>
                <p>Estás a un paso de proteger a tu mascota. Selecciona tu medio de pago seguro.</p>"""
c = c.replace(old_header, new_header)

# 3. Replace the Form with the Flow Payment UI
form_start_pattern = r'<form id="startForm".*?</form>'

new_ui = """
<div id="paymentUI" style="display: flex; flex-direction: column; align-items: center; padding: 20px 10px; font-family: 'Inter', sans-serif;">
    
    <div style="text-align: center; margin-bottom: 30px;">
        <p style="color: #64748B; font-size: 1rem; margin-bottom: 15px; font-weight: 500;">Estás realizando el pago en:</p>
        <img src="../assets/img/logo-mhm-color.png" alt="MHM Corredores" style="max-height: 45px; object-fit: contain;">
    </div>

    <div style="width: 100%; max-width: 400px; margin-bottom: 40px;">
        <p style="color: #0F172A; font-weight: 700; font-size: 1.05rem; margin-bottom: 15px;">Selecciona tu medio de pago:</p>
        
        <a href="https://www.flow.cl/" target="_blank" style="display: flex; align-items: center; padding: 20px; border: 1px solid #E2E8F0; border-radius: 12px; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(0,0,0,0.02); background: white;" onmouseover="this.style.borderColor='#F97316'; this.style.boxShadow='0 10px 20px rgba(249, 115, 22, 0.1)';" onmouseout="this.style.borderColor='#E2E8F0'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.02)';">
            <div style="background: #FFF7ED; width: 50px; height: 50px; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 20px; flex-shrink: 0;">
                <i class="fa-solid fa-credit-card" style="font-size: 1.5rem; color: #F97316;"></i>
            </div>
            <div>
                <h4 style="margin: 0 0 5px 0; color: #0F172A; font-size: 1.15rem; font-weight: 700;">Plataforma Flow</h4>
                <p style="margin: 0; color: #64748B; font-size: 0.9rem;">Webpay, MACH, Servipag y más.</p>
            </div>
        </a>
    </div>

    <a href="cotizacion-mascota-2.html" style="color: #3B82F6; font-weight: 600; text-decoration: none; font-size: 0.95rem; transition: 0.3s;" onmouseover="this.style.textDecoration='underline';" onmouseout="this.style.textDecoration='none';">
        Abandonar y volver
    </a>

    <div style="margin-top: 50px; text-align: center; display: flex; align-items: center; justify-content: center; gap: 8px;">
        <i class="fa-solid fa-lock" style="color: #F59E0B; font-size: 1.1rem;"></i>
        <span style="color: #64748B; font-size: 0.85rem;">
            Transacción respaldada por <strong>Flow</strong>. Revisa las <a href="https://www.flow.cl/terminos-y-condiciones.php" target="_blank" style="color: #3B82F6; text-decoration: none; font-weight: 600;">Políticas de Seguridad y Privacidad</a>.
        </span>
    </div>

</div>
"""

c = re.sub(form_start_pattern, new_ui, c, flags=re.DOTALL)

# 4. Update the stepper in the right sidebar
# We'll just replace the whole UL to mark step 3 as active
new_stepper = """<ul class="aurora-list" style="margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px;">
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Selección de Plan</li>
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Datos del Contratante</li>
                        <li class="active"><span class="pulse-dot"></span> Pago y Emisión</li>
                    </ul>"""

old_stepper_pattern = r'<ul class="aurora-list".*?</ul>'
c = re.sub(old_stepper_pattern, new_stepper, c, flags=re.DOTALL)


# 5. Fix Javascript: change renderSummaryStep2 to renderSummaryStep3
c = c.replace('renderSummaryStep2()', 'renderSummaryStep3()')
c = c.replace('function renderSummaryStep2()', 'function renderSummaryStep3()')
c = c.replace("getElementById('cart-summary-step2')", "getElementById('cart-summary-step3')")

# Also change the id in the html
c = c.replace('id="cart-summary-step2"', 'id="cart-summary-step3"')

with open("cotizacion/cotizacion-mascota-3.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Generated cotizacion-mascota-3.html")
