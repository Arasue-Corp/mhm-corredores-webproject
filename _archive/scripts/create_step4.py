import shutil
import re

shutil.copy("cotizacion/cotizacion-mascota-3.html", "cotizacion/cotizacion-mascota-4.html")

with open("cotizacion/cotizacion-mascota-4.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Update Stepper sequence
stepper_pattern = r'<ul class="aurora-list".*?</ul>'
new_stepper = """<ul class="aurora-list" style="margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px;">
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Selección de Plan</li>
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Datos del Contratante</li>
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Pago Seguro</li>
                        <li class="active"><span class="pulse-dot"></span> Registro Mascotas</li>
                    </ul>"""
c = re.sub(stepper_pattern, new_stepper, c, flags=re.DOTALL)

# 2. Replace the payment container with the accordion container for pets
payment_pattern = r'<!-- Payment Flow -->(.*?)<!-- Start Side Summary -->'
pet_forms = """<!-- Pet Forms Flow -->
                    <div id="petsContainer" style="margin-bottom: 30px;">
                        <!-- dynamic accordions go here -->
                    </div>

                    <div style="display: flex; align-items: center; margin-bottom: 30px;">
                        <input type="checkbox" id="chkPetsCorrect" class="custom-chk" onchange="validatePetsForm()">
                        <label for="chkPetsCorrect" style="margin-left: 10px; font-size: 0.95rem; font-weight: 500; color: #475569; cursor: pointer; user-select: none;">Todos los datos registrados son correctos.</label>
                    </div>

                    <button type="button" id="btn-finish" onclick="finishFlow()" style="background: #104C5C; color: white; border: none; width: 100%; padding: 18px; border-radius: 12px; font-size: 1.15rem; font-weight: 700; cursor: pointer; opacity: 0.5; pointer-events: none; transition: 0.3s; box-shadow: 0 4px 15px rgba(16, 76, 92, 0.3);" onmouseover="if(this.style.opacity=='1'){this.style.background='#0A323D';}" onmouseout="if(this.style.opacity=='1'){this.style.background='#104C5C';}">
                        Registrar
                    </button>
                    """
c = re.sub(payment_pattern, pet_forms, c, flags=re.DOTALL)

# 3. Update the Javascript logic to generate the accordions
js_pattern = r'function goToNextStep\(\) \{.*?\n    \}'
new_js = """function toggleAccordion(id) {
        const content = document.getElementById('pet-content-' + id);
        const icon = document.getElementById('pet-icon-' + id);
        if (content.style.display === 'none') {
            content.style.display = 'block';
            icon.classList.remove('fa-chevron-down');
            icon.classList.add('fa-chevron-up');
        } else {
            content.style.display = 'none';
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
        }
    }

    function validatePetsForm() {
        const chk = document.getElementById('chkPetsCorrect').checked;
        const btn = document.getElementById('btn-finish');
        let allValid = true;
        
        // We could add deeper validation here to check each pet's input, but for now we'll require the checkbox and basic non-empty values
        const inputs = document.querySelectorAll('.pet-input');
        inputs.forEach(input => {
            if(!input.value.trim()) {
                allValid = false;
            }
        });

        if (chk && allValid) {
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
        } else {
            btn.style.opacity = '0.5';
            btn.style.pointerEvents = 'none';
        }
    }

    function renderPetsForm() {
        const container = document.getElementById('petsContainer');
        if(!container) return;
        
        const cartStr = sessionStorage.getItem('mhmPetCart');
        if (!cartStr) {
            window.location.href = 'cotizacion-mascota-1.html';
            return;
        }

        const plans = JSON.parse(cartStr);
        let html = '';
        let petCounter = 1;
        
        for(let id in plans) {
            for(let i=0; i<plans[id].qty; i++) {
                const uniqueId = id + '-' + i;
                const isOpen = petCounter === 1; // Only open the first one by default
                
                html += `
                <div style="border: 1px solid #E2E8F0; border-radius: 12px; margin-bottom: 15px; background: white; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">
                    <div onclick="toggleAccordion('${uniqueId}')" style="padding: 15px 20px; background: #F8FAFC; cursor: pointer; display: flex; justify-content: space-between; align-items: center; border-bottom: ${isOpen ? '1px solid #E2E8F0' : 'none'};">
                        <strong style="color: #0F172A; font-size: 1.05rem;">${petCounter}. ${plans[id].name}</strong>
                        <i id="pet-icon-${uniqueId}" class="fa-solid ${isOpen ? 'fa-chevron-up' : 'fa-chevron-down'}" style="color: #64748B;"></i>
                    </div>
                    <div id="pet-content-${uniqueId}" style="padding: 20px; display: ${isOpen ? 'block' : 'none'};">
                        
                        <div class="input-group-modern" style="margin-bottom: 15px;">
                            <label style="display: block; margin-bottom: 8px; font-weight: 600; color: #1E293B; font-size: 0.9rem;">Nombre de la Mascota</label>
                            <input type="text" onkeyup="validatePetsForm()" class="pet-input rich-input" placeholder="Ej: Firulais" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 0.95rem; color: #0F172A;" required>
                        </div>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                            <div class="input-group-modern">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: #1E293B; font-size: 0.9rem;">Especie</label>
                                <select onchange="validatePetsForm()" class="pet-input rich-input" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 0.95rem; color: #0F172A;" required>
                                    <option value="" disabled selected>Selecciona...</option>
                                    <option value="Perro">Perro</option>
                                    <option value="Gato">Gato</option>
                                </select>
                            </div>
                            <div class="input-group-modern">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: #1E293B; font-size: 0.9rem;">Sexo</label>
                                <select onchange="validatePetsForm()" class="pet-input rich-input" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 0.95rem; color: #0F172A;" required>
                                    <option value="" disabled selected>Selecciona...</option>
                                    <option value="Macho">Macho</option>
                                    <option value="Hembra">Hembra</option>
                                </select>
                            </div>
                        </div>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                            <div class="input-group-modern">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: #1E293B; font-size: 0.9rem;">Raza</label>
                                <input type="text" onkeyup="validatePetsForm()" class="pet-input rich-input" placeholder="Ej: Poodle" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 0.95rem; color: #0F172A;" required>
                            </div>
                            <div class="input-group-modern">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: #1E293B; font-size: 0.9rem;">Edad (Años)</label>
                                <input type="number" onkeyup="validatePetsForm()" onchange="validatePetsForm()" class="pet-input rich-input" placeholder="Ej: 3" min="0" max="30" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 0.95rem; color: #0F172A;" required>
                            </div>
                        </div>

                    </div>
                </div>`;
                petCounter++;
            }
        }
        
        container.innerHTML = html;
    }

    function finishFlow() {
        alert("¡Registro Exitoso! Serás redirigido.");
        window.location.href = '../index.html';
    }
    
    // Auto render on load
    document.addEventListener('DOMContentLoaded', function() {
        renderSummaryStep2();
        renderPetsForm();
    });"""
c = re.sub(js_pattern, new_js, c, flags=re.DOTALL)


# Ensure renderPetsForm gets called on DOM load instead of just renderSummaryStep2
# Since I replaced the end, I need to make sure the event listener is right
c = re.sub(r"document\.addEventListener\('DOMContentLoaded', function\(\) \{\n        renderSummaryStep2\(\);\n    \}\);", "", c, flags=re.DOTALL)


with open("cotizacion/cotizacion-mascota-4.html", "w", encoding="utf-8") as f:
    f.write(c)
