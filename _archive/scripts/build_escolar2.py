import re

with open('cotizacion/cotizacion-escolar-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update text and titles
content = content.replace('Cotización de Asistencia Mascota', 'Cotización de Asistencia Escolar')
content = content.replace('Asistencia Mascota', 'Asistencia Escolar')
content = content.replace('cotizacion-mascota-1.html', 'cotizacion-escolar-1.html')
content = content.replace('cotizacion-mascota-3.html', 'cotizacion-escolar-3.html')
content = content.replace('fa-paw', 'fa-school')
content = content.replace('fa-shield-dog', 'fa-school-circle-check')
content = content.replace('fa-shield-cat', 'fa-user-graduate')

# 2. Replace the form section
form_start = content.find('<form id="startForm"')
form_end = content.find('</form>')

if form_start != -1 and form_end != -1:
    new_form = """<form id="startForm" onsubmit="event.preventDefault(); goToNextStep();">
    <div style="border-radius: 12px; overflow: hidden; border: 1px solid #E2E8F0; margin-bottom: 20px;">
        <!-- Header -->
        <div style="display: flex; align-items: stretch;">
            <div style="background: #93C524; color: white; padding: 15px 30px; font-size: 1.25rem; font-weight: 800; display: flex; align-items: center; justify-content: center; flex: 1;">
                Datos del contratante
            </div>
            <div style="background: white; padding: 15px 30px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #1C4E5E; font-size: 1.25rem; border-left: 1px solid #E2E8F0; flex: 0.5;">
                <i class="fa-solid fa-leaf" style="color: #93C524; margin-right: 8px;"></i> Servi.click
            </div>
        </div>
        
        <!-- Body -->
        <div style="display: flex; padding: 40px; background: white; gap: 40px; align-items: center; flex-wrap: wrap;">
            
            <!-- Speech Bubble -->
            <div style="flex: 1; min-width: 250px;">
                <div style="border: 2px solid #93C524; border-radius: 8px; padding: 25px; position: relative; color: #1C4E5E; font-size: 0.95rem; line-height: 1.5; font-weight: 500;">
                    Si eres <strong style="font-weight: 700;">contratante y beneficiario</strong> a la vez, continúa completando los formularios con tus datos.
                    
                    <div style="position: absolute; top: 50%; left: -12px; transform: translateY(-50%); width: 0; height: 0; border-top: 10px solid transparent; border-bottom: 10px solid transparent; border-right: 10px solid #93C524;"></div>
                    <div style="position: absolute; top: 50%; left: -9px; transform: translateY(-50%); width: 0; height: 0; border-top: 9px solid transparent; border-bottom: 9px solid transparent; border-right: 9px solid white;"></div>
                </div>
            </div>

            <!-- Form Fields -->
            <div style="flex: 1; min-width: 280px; display: flex; flex-direction: column; gap: 15px; border: 1px solid #E2E8F0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.02);">
                
                <div style="display: flex; border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden; background: #F8FAFC;">
                    <div style="padding: 12px 15px; font-weight: 700; color: #334155; border-right: 1px solid #E2E8F0; display: flex; align-items: center;">Rut</div>
                    <input type="text" id="rutInput" onkeyup="validateForm()" placeholder="12345678-9" style="width: 100%; border: none; background: transparent; padding: 12px 15px; font-size: 1rem; color: #0F172A; outline: none;" required>
                </div>
                
                <div style="display: flex; border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden; background: #F8FAFC;">
                    <div style="padding: 12px 15px; font-weight: 700; color: #334155; border-right: 1px solid #E2E8F0; display: flex; align-items: center;">Nombre</div>
                    <input type="text" id="nameInput" onkeyup="validateForm()" style="width: 100%; border: none; background: transparent; padding: 12px 15px; font-size: 1rem; color: #0F172A; outline: none;" required>
                </div>
                
                <div style="display: flex; border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden; background: #F8FAFC;">
                    <div style="padding: 12px 15px; font-weight: 700; color: #334155; border-right: 1px solid #E2E8F0; display: flex; align-items: center;">Email</div>
                    <input type="email" id="emailInput" onkeyup="validateForm()" style="width: 100%; border: none; background: transparent; padding: 12px 15px; font-size: 1rem; color: #0F172A; outline: none;" required>
                </div>

                <button type="submit" id="btn-continue" style="margin-top: 10px; width: 100%; padding: 12px; border-radius: 8px; background: #1C4E5E; color: white; font-weight: 700; border: none; cursor: pointer; transition: 0.3s; opacity: 0.5; pointer-events: none; font-size: 1rem;">
                    Continuar
                </button>
            </div>
            
        </div>
    </div>"""
    content = content[:form_start] + new_form + content[form_end:]

# 3. Change cart rendering logic to reflect Asistencia Escolar instead of Mascotas
cart_js_start = content.find('function renderSummaryStep2() {')
cart_js_end = content.find('}', content.find('function validateRut'))

if cart_js_start != -1:
    new_cart_js = """function renderSummaryStep2() {
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
                        <span><i class="fa-solid fa-school" style="color: #CBD5E1; margin-right: 8px;"></i> ${plans[id].name} <strong style="color: #0F172A;">x ${plans[id].qty}</strong></span>
                        <strong style="color: #0F172A;">$${subtotal.toLocaleString('es-CL')}</strong>
                    </div>`;
                }
            }
        }
        
        if (!hasItems) {
            window.location.href = 'cotizacion-escolar-1.html';
            return;
        }

        html += `<div style="border-top: 2px dashed #E2E8F0; margin-top: 15px; padding-top: 20px; display: flex; justify-content: space-between; font-size: 1.3rem; color: #0F172A; align-items: baseline;">
            <strong>Total Estimado:</strong>
            <strong style="color: #2ED9C3;">$${total.toLocaleString('es-CL')}<span style="font-size: 0.9rem; color: #64748B; font-weight: normal; margin-left: 4px;">/mes</span></strong>
        </div>`;
        
        summaryDiv.innerHTML = html;
    }

    function validateRut(rut) {"""
    
    content = content[:cart_js_start] + new_cart_js + content[cart_js_end:]

with open('cotizacion/cotizacion-escolar-2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done building escolar 2")
