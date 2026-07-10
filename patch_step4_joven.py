import re

with open('cotizacion/cotizacion-salud-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the form with a dynamic container
new_form_content = """
                        <form id="productoForm" onsubmit="event.preventDefault(); goToNextStep();">
                            
                            <div id="fields-integral">
                                <div class="input-group-modern" style="margin-bottom: 25px;">
                                    <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Tipo de Previsión *</label>
                                    <div class="input-with-icon" style="position: relative;">
                                        <i class="fa-solid fa-stethoscope" style="position: absolute; left: 16px; top: 16px; color: #94A3B8; z-index: 10;"></i>
                                        <select id="previsionInput" onchange="validateForm()" class="rich-input" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A; cursor: pointer; appearance: none;">
                                            <option value="" disabled selected>Selecciona tipo de previsión</option>
                                            <option value="fonasa">FONASA</option>
                                            <option value="isapre">ISAPRE</option>
                                            <option value="capredena">CAPREDENA</option>
                                            <option value="dipreca">DIPRECA</option>
                                            <option value="particular">Particular / Sin previsión</option>
                                        </select>
                                        <i class="fa-solid fa-chevron-down" style="position: absolute; right: 15px; top: 16px; pointer-events: none; color: #94A3B8;"></i>
                                    </div>
                                </div>

                                <div class="input-group-modern" style="margin-bottom: 35px;">
                                    <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Convenio (Opcional)</label>
                                    <div class="input-with-icon" style="position: relative;">
                                        <i class="fa-solid fa-handshake" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                        <input type="text" id="convenioInput" class="rich-input" placeholder="Ej: Empresa X, Banco Y" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;">
                                    </div>
                                </div>
                            </div>
                            
                            <div id="fields-joven" style="display: none;">
                                <div class="input-group-modern" style="margin-bottom: 35px;">
                                    <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Tipo de Provisión *</label>
                                    <div class="input-with-icon" style="position: relative;">
                                        <i class="fa-solid fa-pen" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                        <input type="text" id="provisionInput" oninput="validateForm()" class="rich-input" placeholder="Ingresa tipo de provisión" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;">
                                    </div>
                                </div>
                            </div>

                            <div style="display: flex; justify-content: flex-end;">
                                <button type="submit" id="btn-continue" class="btn-primary-shimmer" style="background: linear-gradient(135deg, #3B82F6, #796bfc); opacity: 0.5; pointer-events: none; transition: 0.3s; padding: 15px 30px;">
                                    Siguiente Paso <i class="fa-solid fa-arrow-right"></i>
                                </button>
                            </div>
                        </form>
"""

# Find the form and replace it
form_start = html.find('<form id="productoForm"')
form_end = html.find('</form>', form_start) + len('</form>')
html = html[:form_start] + new_form_content + html[form_end:]

# Now replace the script
script_start = html.find('<script>')
script_end = html.find('</script>', script_start) + len('</script>')

new_script = """<script>
        let isJoven = false;
        document.addEventListener('DOMContentLoaded', () => {
            const planStr = sessionStorage.getItem('mhm_salud_plan');
            if (planStr) {
                const plan = JSON.parse(planStr);
                if (plan.id === 'joven') {
                    isJoven = true;
                }
                
                // Update sidebar details
                const titleEl = document.querySelector('#resumen-title-header + #cart-summary-step2 h4');
                const priceEl = document.querySelector('#cart-summary-step2 .plan-price');
                if (titleEl) titleEl.innerText = plan.name;
                if (priceEl) priceEl.innerText = '$' + plan.price.toLocaleString('es-CL');
            }

            // Adjust UI for Joven vs Integral
            if (isJoven) {
                document.getElementById('fields-integral').style.display = 'none';
                document.getElementById('fields-joven').style.display = 'block';
                
                // Hide Beneficiarios from sidebar
                const lis = document.querySelectorAll('.aurora-list li');
                lis.forEach(li => {
                    if (li.innerText.includes('Beneficiarios')) {
                        li.style.display = 'none';
                    }
                });
            }
        });

        function validateForm() {
            const btn = document.getElementById('btn-continue');
            let isValid = false;
            if (isJoven) {
                isValid = document.getElementById('provisionInput').value.trim() !== "";
            } else {
                isValid = document.getElementById('previsionInput').value !== "";
            }
            
            if (isValid) {
                btn.style.opacity = '1';
                btn.style.pointerEvents = 'auto';
            } else {
                btn.style.opacity = '0.5';
                btn.style.pointerEvents = 'none';
            }
        }
        
        function goToNextStep() {
            let formData = {};
            if (isJoven) {
                formData.provision = document.getElementById('provisionInput').value;
            } else {
                formData.prevision = document.getElementById('previsionInput').value;
                formData.convenio = document.getElementById('convenioInput').value;
            }
            sessionStorage.setItem('productoData', JSON.stringify(formData));

            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.3s ease';
            setTimeout(() => {
                if (isJoven) {
                    window.location.href = 'cotizacion-salud-6.html'; // Skip step 5
                } else {
                    window.location.href = 'cotizacion-salud-5.html'; 
                }
            }, 300);
        }

        function openCoverageModal(planId) {
            // ... omitting for brevity if not strictly needed in step 4, wait, it's used in the sidebar
            // Let's preserve the original openCoverageModal
        }
        function closeCoverageModal() {
            // ...
        }
"""

# I need to preserve the coverage modal logic from original script
orig_script = html[script_start:script_end]
modal_logic_start = orig_script.find('function openCoverageModal')
modal_logic = orig_script[modal_logic_start:]

html = html[:script_start] + new_script + modal_logic + html[script_end:]

with open('cotizacion/cotizacion-salud-4.html', 'w', encoding='utf-8') as f:
    f.write(html)
