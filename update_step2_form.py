import re

with open("cotizacion/cotizacion-mascota-2.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Replace Stepper
old_stepper_pattern = r'<ul class="aurora-list".*?</ul>'
new_stepper = """<ul class="aurora-list" style="margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px;">
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Selección de Plan</li>
                        <li class="active"><span class="pulse-dot"></span> Datos del Contratante</li>
                        <li><i class="fa-regular fa-circle"></i> Pago Seguro</li>
                        <li><i class="fa-regular fa-circle"></i> Registro Mascotas</li>
                    </ul>"""
c = re.sub(old_stepper_pattern, new_stepper, c, flags=re.DOTALL)

# Also rename the Resumen de Selección title to just leave it blank or remove the label, 
# because the summary is going to take up the whole box and looks like a standalone block.
# I'll leave the title "Resumen de Selección" but maybe remove the generic protection box.
# Add ID to generic box to easily hide it:
c = c.replace('<div style="background: rgba(16, 185, 129, 0.05);', '<div id="generic-protection-box" style="background: rgba(16, 185, 129, 0.05);')

# 2. Replace Form
form_start_pattern = r'<form id="startForm" onsubmit="event.preventDefault(); goToNextStep\(\);">.*?</form>'
new_form = """<form id="startForm" onsubmit="event.preventDefault(); goToNextStep();">
    <div style="padding: 10px 5px;">
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px;">
            <div class="input-group-modern">
                <label style="display: block; margin-bottom: 8px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Rut</label>
                <div class="input-with-icon" style="position: relative;">
                    <input type="text" id="rutInput" onkeyup="validateForm()" class="rich-input" placeholder="12345678-9" style="width: 100%; padding: 14px 15px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                </div>
            </div>
            <div class="input-group-modern">
                <label style="display: block; margin-bottom: 8px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Fecha de cumpleaños</label>
                <div class="input-with-icon" style="position: relative;">
                    <input type="date" id="dobInput" onchange="validateForm()" class="rich-input" style="width: 100%; padding: 14px 15px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                </div>
            </div>
        </div>

        <div class="input-group-modern" style="margin-bottom: 20px;">
            <label style="display: block; margin-bottom: 8px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Nombre</label>
            <input type="text" id="nameInput" onkeyup="validateForm()" class="rich-input" placeholder="Nombre" style="width: 100%; padding: 14px 15px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
        </div>

        <div class="input-group-modern" style="margin-bottom: 20px;">
            <label style="display: block; margin-bottom: 8px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Apellidos</label>
            <input type="text" id="lastNameInput" onkeyup="validateForm()" class="rich-input" placeholder="Apellidos" style="width: 100%; padding: 14px 15px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
        </div>

        <div class="input-group-modern" style="margin-bottom: 20px;">
            <label style="display: block; margin-bottom: 8px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Email</label>
            <input type="email" id="emailInput" onkeyup="validateForm()" class="rich-input" placeholder="Email" style="width: 100%; padding: 14px 15px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
        </div>

        <div class="input-group-modern" style="margin-bottom: 20px;">
            <label style="display: block; margin-bottom: 8px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Teléfono</label>
            <input type="tel" id="phoneInput" onkeyup="validateForm()" class="rich-input" placeholder="Teléfono" style="width: 100%; padding: 14px 15px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
        </div>

        <div class="input-group-modern" style="margin-bottom: 20px;">
            <label style="display: block; margin-bottom: 8px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Dirección</label>
            <input type="text" id="addressInput" onkeyup="validateForm()" class="rich-input" placeholder="Dirección" style="width: 100%; padding: 14px 15px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
        </div>

        <div class="input-group-modern" style="margin-bottom: 30px;">
            <label style="display: block; margin-bottom: 8px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Comuna</label>
            <select id="comunaInput" onchange="validateForm()" class="rich-input" style="width: 100%; padding: 14px 15px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                <option value="" disabled selected>Selecciona la comuna...</option>
                <option value="Providencia">Providencia</option>
                <option value="Las Condes">Las Condes</option>
                <option value="Santiago Centro">Santiago Centro</option>
                <option value="Ñuñoa">Ñuñoa</option>
                <option value="Maipú">Maipú</option>
            </select>
        </div>

        <div style="display: flex; align-items: center; margin-bottom: 30px;">
            <input type="checkbox" id="chkCorrect" class="custom-chk" onchange="validateForm()">
            <label for="chkCorrect" style="margin-left: 10px; font-size: 0.95rem; font-weight: 500; color: #475569; cursor: pointer; user-select: none;">Todos los datos registrados son correctos.</label>
        </div>

        <button type="submit" id="btn-continue" style="background: #104C5C; color: white; border: none; width: 100%; padding: 18px; border-radius: 12px; font-size: 1.15rem; font-weight: 700; cursor: pointer; opacity: 0.5; pointer-events: none; transition: 0.3s; box-shadow: 0 4px 15px rgba(16, 76, 92, 0.3);" onmouseover="if(this.style.opacity=='1'){this.style.background='#0A323D';}" onmouseout="if(this.style.opacity=='1'){this.style.background='#104C5C';}">
            Registrar
        </button>
    </div>
</form>"""
c = re.sub(form_start_pattern, new_form, c, flags=re.DOTALL)


# 3. Replace the script tags JS part
js_pattern = r'function renderSummaryStep2\(\) \{.*?\n    \}\n\n    document\.addEventListener'
new_js = """function renderSummaryStep2() {
        const summaryDiv = document.getElementById('cart-summary-step2');
        if(!summaryDiv) return;
        
        let html = '';
        let hasItems = false;
        
        const cartStr = sessionStorage.getItem('mhmPetCart');
        if (cartStr) {
            const plans = JSON.parse(cartStr);
            for(let id in plans) {
                if(plans[id].qty > 0) {
                    hasItems = true;
                    html += `
                    <div style="margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px dashed #E2E8F0;">
                        <h4 style="color: #104C5C; font-size: 1.15rem; font-weight: 800; margin-bottom: 15px; line-height: 1.3;">
                            ¡Excelente elección!<br>
                            Contrataste ${plans[id].name}
                        </h4>
                        
                        <ul style="list-style: none; padding: 0; margin: 0 0 20px 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Protección y coberturas 100%.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Eventos disponibles todo el año.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Usa tu asistencia en la veterinaria que desees, estamos en todo Chile.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Reembolso rápido y fácil.
                            </li>
                        </ul>

                        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; text-align: center;">
                            <div>
                                <div style="background: #A3D80E; color: white; width: 45px; height: 45px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 1.3rem;">
                                    <i class="fa-regular fa-star"></i>
                                </div>
                                <span style="font-size: 0.75rem; color: #104C5C; line-height: 1.2; display: block; font-weight: 600;">Valores accesibles.</span>
                            </div>
                            <div>
                                <div style="background: #A3D80E; color: white; width: 45px; height: 45px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 1.3rem;">
                                    <i class="fa-solid fa-lock"></i>
                                </div>
                                <span style="font-size: 0.75rem; color: #104C5C; line-height: 1.2; display: block; font-weight: 600;">Sin trámites complejos.</span>
                            </div>
                            <div>
                                <div style="background: #A3D80E; color: white; width: 45px; height: 45px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-size: 1.3rem;">
                                    <i class="fa-solid fa-dollar-sign"></i>
                                </div>
                                <span style="font-size: 0.75rem; color: #104C5C; line-height: 1.2; display: block; font-weight: 600;">+ Protección,<br>+ Tranquilidad.</span>
                            </div>
                        </div>
                    </div>`;
                }
            }
        }
        
        if (!hasItems) {
            window.location.href = 'cotizacion-mascota-1.html';
            return;
        }

        summaryDiv.innerHTML = html;
        
        const genericBox = document.getElementById('generic-protection-box');
        if(genericBox) genericBox.style.display = 'none';
        
        // Let's remove the Resumen title since the block looks self-contained now.
        const headerTitle = document.getElementById('resumen-title-header');
        if(headerTitle) headerTitle.style.display = 'none';
    }

    function validateRut(rut) {
        return /^[0-9]+-[0-9kK]{1}$/.test(rut);
    }
    
    function validateEmail(email) {
        return /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/.test(email);
    }

    function validateForm() {
        const rut = document.getElementById('rutInput') ? document.getElementById('rutInput').value.trim() : '';
        const name = document.getElementById('nameInput') ? document.getElementById('nameInput').value.trim() : '';
        const lastName = document.getElementById('lastNameInput') ? document.getElementById('lastNameInput').value.trim() : '';
        const email = document.getElementById('emailInput') ? document.getElementById('emailInput').value.trim() : '';
        const phone = document.getElementById('phoneInput') ? document.getElementById('phoneInput').value.trim() : '';
        const address = document.getElementById('addressInput') ? document.getElementById('addressInput').value.trim() : '';
        const comuna = document.getElementById('comunaInput') ? document.getElementById('comunaInput').value : '';
        const chk = document.getElementById('chkCorrect') ? document.getElementById('chkCorrect').checked : false;
        
        const btn = document.getElementById('btn-continue');
        if(!btn) return;
        
        if (rut.length > 5 && name.length > 2 && lastName.length > 2 && validateEmail(email) && phone.length > 5 && address.length > 3 && comuna && chk) {
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
        const lastName = document.getElementById('lastNameInput').value.trim();
        const email = document.getElementById('emailInput').value.trim();
        const phone = document.getElementById('phoneInput').value.trim();
        const address = document.getElementById('addressInput').value.trim();
        const comuna = document.getElementById('comunaInput').value;
        
        sessionStorage.setItem('mhmPetClient', JSON.stringify({rut, name, lastName, email, phone, address, comuna}));
        
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.3s ease';
        setTimeout(() => {
            window.location.href = 'cotizacion-mascota-3.html';
        }, 300);
    }

    document.addEventListener"""
c = re.sub(js_pattern, new_js, c, flags=re.DOTALL)

# Add id to the title so we can hide it
c = c.replace('<div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px; border-bottom: 1px solid #E2E8F0; padding-bottom: 15px;">\n                        Resumen de Selección\n                    </div>', '<div id="resumen-title-header" class="sidebar-title text-gradient-corp" style="display: none; font-size: 1.25rem; font-weight: 800; margin-bottom: 20px; border-bottom: 1px solid #E2E8F0; padding-bottom: 15px;">\n                        Resumen de Selección\n                    </div>')

with open("cotizacion/cotizacion-mascota-2.html", "w", encoding="utf-8") as f:
    f.write(c)
