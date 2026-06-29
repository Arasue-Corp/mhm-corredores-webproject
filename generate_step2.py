import re
import os

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Update Title and Progress
c = c.replace('<title>Cotización Mascota | Seguros MHM</title>', '<title>Cotización Mascota - Paso 2 | Seguros MHM</title>')
c = c.replace('<div class="progress-fill" style="width: 25%;"></div>', '<div class="progress-fill" style="width: 50%;"></div>')

# 2. Update Header Text
old_header = """<div class="title-group">
                    <h1 class="text-gradient-corp">Elige el plan para tu mascota</h1>
                    <div class="aurora-line"></div> 
                </div>
                <p>Selecciona el nivel de protección que mejor se adapte a tu regalón.</p>"""
new_header = """<div class="title-group">
                    <h1 class="text-gradient-corp">Datos del Contratante</h1>
                    <div class="aurora-line"></div> 
                </div>
                <p>Ingresa tus datos personales para continuar con la cotización.</p>"""
c = c.replace(old_header, new_header)

# 3. Replace the Form
form_start_pattern = r'<form id="startForm" onsubmit="event.preventDefault\(\);">.*?</form>'
new_form = """<form id="startForm" onsubmit="event.preventDefault(); goToNextStep();">
    <div style="padding: 10px 5px;">
        <div class="input-group-modern" style="margin-bottom: 25px;">
            <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">RUT del contratante</label>
            <div class="input-with-icon" style="position: relative;">
                <i class="fa-solid fa-id-card" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                <input type="text" id="rutInput" onkeyup="validateForm()" class="rich-input" placeholder="Ej: 12.345.678-9" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
            </div>
        </div>

        <div class="input-group-modern" style="margin-bottom: 25px;">
            <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Nombre completo</label>
            <div class="input-with-icon" style="position: relative;">
                <i class="fa-solid fa-user" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                <input type="text" id="nameInput" onkeyup="validateForm()" class="rich-input" placeholder="Juan Pérez" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
            </div>
        </div>

        <div class="input-group-modern" style="margin-bottom: 35px;">
            <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Email</label>
            <div class="input-with-icon" style="position: relative;">
                <i class="fa-solid fa-envelope" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                <input type="email" id="emailInput" onkeyup="validateForm()" class="rich-input" placeholder="correo@ejemplo.com" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
            </div>
        </div>

        <button type="submit" id="btn-continue" class="btn-primary-shimmer" style="margin-top: 10px; width: 100%; opacity: 0.5; pointer-events: none; transition: 0.3s;">
            Continuar a Siguiente Paso <i class="fa-solid fa-arrow-right"></i>
        </button>
    </div>
</form>"""
c = re.sub(form_start_pattern, new_form, c, flags=re.DOTALL)


# 4. Replace the Sidebar (Right column)
sidebar_pattern = r'<aside class="config-sidebar anim-entry delay-2">.*?</aside>'
new_sidebar = """<aside class="config-sidebar anim-entry delay-2">
            <div class="organic-panel" style="position: sticky; top: 100px;">
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
        </aside>"""
c = re.sub(sidebar_pattern, new_sidebar, c, flags=re.DOTALL)


# 5. Replace Javascript Block
js_pattern = r'<script>\s*const plans.*?</script>'
new_js = """<script>
    function renderSummaryStep2() {
        const summaryDiv = document.getElementById('cart-summary-step2');
        if(!summaryDiv) return;
        
        let html = '';
        let total = 0;
        let hasItems = false;
        
        const cartStr = sessionStorage.getItem('mhmPetCart');
        if (cartStr) {
            const plans = JSON.parse(cartStr);
            for(let id in plans) {
                if(plans[id].qty > 0) {
                    hasItems = true;
                    const subtotal = plans[id].qty * plans[id].price;
                    total += subtotal;
                    html += `<div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 1.05rem; color: #334155;">
                        <span><i class="fa-solid fa-paw" style="color: #CBD5E1; margin-right: 8px;"></i> ${plans[id].name} <strong style="color: #0F172A;">x ${plans[id].qty}</strong></span>
                        <strong style="color: #0F172A;">$${subtotal.toLocaleString('es-CL')}</strong>
                    </div>`;
                }
            }
        }
        
        if (!hasItems) {
            window.location.href = 'cotizacion-mascota-1.html';
            return;
        }

        html += `<div style="border-top: 2px dashed #E2E8F0; margin-top: 15px; padding-top: 20px; display: flex; justify-content: space-between; font-size: 1.3rem; color: #0F172A; align-items: baseline;">
            <strong>Total Estimado:</strong>
            <strong style="color: #2ED9C3;">$${total.toLocaleString('es-CL')}<span style="font-size: 0.9rem; color: #64748B; font-weight: normal; margin-left: 4px;">/mes</span></strong>
        </div>`;
        
        summaryDiv.innerHTML = html;
    }

    function validateRut(rut) {
        // Basic naive regex check for now, enough for a demo
        return /^[0-9]+-[0-9kK]{1}$/.test(rut);
    }
    
    function validateEmail(email) {
        return /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/.test(email);
    }

    function validateForm() {
        const rut = document.getElementById('rutInput').value.trim();
        const name = document.getElementById('nameInput').value.trim();
        const email = document.getElementById('emailInput').value.trim();
        const btn = document.getElementById('btn-continue');
        
        if (rut.length > 5 && name.length > 2 && validateEmail(email)) {
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
        } else {
            btn.style.opacity = '0.5';
            btn.style.pointerEvents = 'none';
        }
    }

    function goToNextStep() {
        const rut = document.getElementById('rutInput').value.trim();
        const name = document.getElementById('nameInput').value.trim();
        const email = document.getElementById('emailInput').value.trim();
        
        sessionStorage.setItem('mhmPetClient', JSON.stringify({rut, name, email}));
        
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.3s ease';
        setTimeout(() => {
            window.location.href = 'cotizacion-mascota-3.html';
        }, 300);
    }
    
    document.addEventListener('DOMContentLoaded', () => {
        renderSummaryStep2();
    });
</script>"""
c = re.sub(js_pattern, new_js, c, flags=re.DOTALL)

with open("cotizacion/cotizacion-mascota-2.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Generated cotizacion-mascota-2.html")
