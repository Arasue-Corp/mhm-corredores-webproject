import os
import re

file_path = "cotizacion/cotizacion-salud-5.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Back button
content = content.replace(
    '<a href="cotizacion-salud-3.html" class="nav-back-btn"><div class="icon-circle"><i class="fa-solid fa-arrow-left"></i></div><span> Volver a Titular</span></a>',
    '<a href="cotizacion-salud-4.html" class="nav-back-btn"><div class="icon-circle"><i class="fa-solid fa-arrow-left"></i></div><span> Volver a Producto</span></a>'
)

# 2. Header and Title
content = content.replace(
    '<p>Por favor, completa los datos de previsión y convenio para aplicar las coberturas correctas.</p>',
    '<p>Puedes agregar hasta 2 beneficiarios a tu póliza de salud (Opcional).</p>'
)
content = content.replace(
    '<h2 style="font-size: 1.5rem; color: #0F172A; margin-bottom: 30px; font-weight: 800;">Datos del Producto</h2>',
    '<h2 style="font-size: 1.5rem; color: #0F172A; margin-bottom: 30px; font-weight: 800;">Beneficiarios</h2>'
)

# 3. Form Body (Replace the whole form with our new beneficiary UI)
new_content = """
                        <div id="beneficiarios-section">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                                <button type="button" id="btn-add-top" onclick="openBeneficiaryModal()" style="background: #A3CC39; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: 0.3s;">
                                    Agregar Beneficiario
                                </button>
                                <span style="font-size: 0.85rem; color: #64748B;">Máximo <strong>2</strong> beneficiarios</span>
                            </div>

                            <div id="empty-state-container" style="border: 1px dashed #CBD5E1; border-radius: 12px; padding: 50px 20px; text-align: center; background: #F8FAFC; margin-bottom: 30px;">
                                <div style="font-size: 3rem; color: #94A3B8; margin-bottom: 15px;">
                                    <i class="fa-solid fa-users"></i>
                                </div>
                                <h4 style="color: #1E293B; font-size: 1.1rem; margin-bottom: 5px;">No hay beneficiarios agregados</h4>
                                <p style="color: #64748B; font-size: 0.9rem; margin-bottom: 20px;">Comience agregando el primer beneficiario del seguro</p>
                                <button type="button" onclick="openBeneficiaryModal()" style="background: white; border: 1px solid #A3CC39; color: #A3CC39; padding: 10px 20px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: 0.3s;">
                                    Agregar primer beneficiario
                                </button>
                            </div>

                            <div id="beneficiaries-list" style="display: none; margin-bottom: 30px;">
                                <!-- Cards will be injected here via JS -->
                            </div>

                            <div style="display: flex; justify-content: flex-end;">
                                <button type="button" id="btn-continue" onclick="goToNextStep()" class="btn-primary-shimmer" style="background: linear-gradient(135deg, #3B82F6, #796bfc); opacity: 1; pointer-events: auto; transition: 0.3s; padding: 15px 30px;">
                                    Siguiente Paso <i class="fa-solid fa-arrow-right"></i>
                                </button>
                            </div>
                        </div>

                        <!-- Beneficiary Modal HTML -->
                        <div id="beneficiaryModal" class="modal-backdrop-aurora" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(15,23,42,0.6); z-index: 9999; justify-content: center; align-items: center; opacity: 0; transition: 0.3s;">
                            <div style="background: white; width: 100%; max-width: 600px; border-radius: 12px; overflow: hidden; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04); transform: translateY(20px); transition: 0.3s;" id="benModalContent">
                                <div style="display: flex; justify-content: space-between; align-items: center; padding: 20px; border-bottom: 1px solid #F1F5F9;">
                                    <h3 style="margin: 0; font-size: 1.25rem; color: #1E293B;">Agregar Nuevo Beneficiario</h3>
                                    <button onclick="closeBeneficiaryModal()" style="background: none; border: none; font-size: 1.2rem; color: #94A3B8; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
                                </div>
                                <div style="padding: 20px;">
                                    <form id="beneficiaryForm" onsubmit="event.preventDefault(); saveBeneficiary();">
                                        <div class="form-grid" style="margin-bottom: 15px;">
                                            <div>
                                                <input type="text" id="benRut" placeholder="Rut" onkeyup="validateBenForm()" class="rich-input" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #fff; font-size: 0.95rem;">
                                            </div>
                                            <div style="position: relative;">
                                                <input type="text" id="benDob" placeholder="Fecha nacimiento (dd/mm/yyyy)" maxlength="10" oninput="formatDate(this); validateBenForm()" class="rich-input" style="width: 100%; padding: 12px 15px 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #fff; font-size: 0.95rem;">
                                                <i class="fa-regular fa-calendar" style="position: absolute; right: 15px; top: 14px; color: #94A3B8; pointer-events: none;"></i>
                                            </div>
                                        </div>
                                        <div style="margin-bottom: 15px;">
                                            <input type="text" id="benNombre" placeholder="Nombre" onkeyup="validateBenForm()" class="rich-input" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #fff; font-size: 0.95rem;">
                                        </div>
                                        <div style="margin-bottom: 15px;">
                                            <input type="text" id="benPaterno" placeholder="Apellido Paterno" onkeyup="validateBenForm()" class="rich-input" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #fff; font-size: 0.95rem;">
                                        </div>
                                        <div style="margin-bottom: 15px;">
                                            <input type="text" id="benMaterno" placeholder="Apellido Materno" onkeyup="validateBenForm()" class="rich-input" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #fff; font-size: 0.95rem;">
                                        </div>
                                        <div style="margin-bottom: 25px; position: relative;">
                                            <select id="benParentesco" onchange="validateBenForm()" class="rich-input" style="width: 100%; padding: 12px 15px; border-radius: 8px; border: 1px solid #E2E8F0; background: #fff; font-size: 0.95rem; appearance: none;">
                                                <option value="" disabled selected>Parentesco</option>
                                                <option value="Conyuge">Cónyuge / Pareja</option>
                                                <option value="Hijo">Hijo(a)</option>
                                                <option value="PadreMadre">Padre / Madre</option>
                                                <option value="Otro">Otro</option>
                                            </select>
                                            <i class="fa-solid fa-chevron-down" style="position: absolute; right: 15px; top: 14px; color: #94A3B8; pointer-events: none;"></i>
                                        </div>
                                        
                                        <div style="display: flex; justify-content: center; gap: 15px;">
                                            <button type="button" onclick="closeBeneficiaryModal()" style="background: white; border: 1px solid #A3CC39; color: #A3CC39; padding: 10px 30px; border-radius: 8px; font-weight: 600; cursor: pointer;">Cancelar</button>
                                            <button type="submit" id="btn-save-ben" style="background: #A3CC39; border: none; color: white; padding: 10px 30px; border-radius: 8px; font-weight: 600; cursor: pointer; opacity: 0.5; pointer-events: none;">Guardar</button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
"""

# Find the form start and the button end
pattern = re.compile(r'<form id="productoForm".*?</form>', re.DOTALL)
content = pattern.sub(new_content, content)


# 4. Sidebar active state
sidebar_old = """                            <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Titular</li>
                            <li class="active"><span class="pulse-dot"></span> Producto</li>
                            <li><i class="fa-regular fa-circle"></i> Beneficiarios</li>"""

sidebar_new = """                            <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Titular</li>
                            <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Producto</li>
                            <li class="active"><span class="pulse-dot"></span> Beneficiarios</li>"""
content = content.replace(sidebar_old, sidebar_new)


# 5. JS functions 
script_pattern = re.compile(r'<script>\s*function validateForm.*?function closeCoverageModal\(\) \{.*?\}.*?\}<\/script>', re.DOTALL)

new_script = """<script>
        let beneficiaries = [];

        function formatDate(input) {
            let v = input.value.replace(/\D/g, ''); // keep only numbers
            if (v.match(/^\d{2}$/) !== null) {
                input.value = v + '/';
            } else if (v.match(/^\d{2}\/\d{2}$/) !== null) {
                input.value = v + '/';
            } else if (v.length >= 4) {
                input.value = v.substring(0,2) + '/' + v.substring(2,4) + '/' + v.substring(4,8);
            }
        }
        
        function goToNextStep() {
            sessionStorage.setItem('beneficiariesData', JSON.stringify(beneficiaries));
            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.3s ease';
            setTimeout(() => {
                window.location.href = 'cotizacion-salud-6.html'; // Assuming Resumen is step 6
            }, 300);
        }

        function openBeneficiaryModal() {
            if(beneficiaries.length >= 2) return;
            document.getElementById('beneficiaryForm').reset();
            document.getElementById('btn-save-ben').style.opacity = '0.5';
            document.getElementById('btn-save-ben').style.pointerEvents = 'none';
            
            const modal = document.getElementById('beneficiaryModal');
            modal.style.display = 'flex';
            setTimeout(() => {
                modal.style.opacity = '1';
                document.getElementById('benModalContent').style.transform = 'translateY(0)';
            }, 10);
        }

        function closeBeneficiaryModal() {
            const modal = document.getElementById('beneficiaryModal');
            modal.style.opacity = '0';
            document.getElementById('benModalContent').style.transform = 'translateY(20px)';
            setTimeout(() => {
                modal.style.display = 'none';
            }, 300);
        }

        function validateBenForm() {
            const rut = document.getElementById('benRut').value;
            const dob = document.getElementById('benDob').value;
            const nom = document.getElementById('benNombre').value;
            const pat = document.getElementById('benPaterno').value;
            const mat = document.getElementById('benMaterno').value;
            const par = document.getElementById('benParentesco').value;
            
            const btn = document.getElementById('btn-save-ben');
            
            if (rut.length > 7 && dob.length === 10 && nom.length > 1 && pat.length > 1 && mat.length > 1 && par !== "") {
                btn.style.opacity = '1';
                btn.style.pointerEvents = 'auto';
            } else {
                btn.style.opacity = '0.5';
                btn.style.pointerEvents = 'none';
            }
        }

        function saveBeneficiary() {
            const ben = {
                rut: document.getElementById('benRut').value,
                dob: document.getElementById('benDob').value,
                nombre: document.getElementById('benNombre').value,
                paterno: document.getElementById('benPaterno').value,
                materno: document.getElementById('benMaterno').value,
                parentesco: document.getElementById('benParentesco').value
            };
            
            beneficiaries.push(ben);
            closeBeneficiaryModal();
            renderBeneficiaries();
        }

        function removeBeneficiary(index) {
            beneficiaries.splice(index, 1);
            renderBeneficiaries();
        }

        function renderBeneficiaries() {
            const emptyState = document.getElementById('empty-state-container');
            const listContainer = document.getElementById('beneficiaries-list');
            const btnAddTop = document.getElementById('btn-add-top');
            
            if (beneficiaries.length === 0) {
                emptyState.style.display = 'block';
                listContainer.style.display = 'none';
            } else {
                emptyState.style.display = 'none';
                listContainer.style.display = 'block';
                
                let html = '';
                beneficiaries.forEach((b, i) => {
                    html += `
                        <div style="border: 1px solid #E2E8F0; border-radius: 12px; padding: 15px 20px; background: white; display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <div>
                                <div style="font-weight: 700; color: #1E293B; margin-bottom: 4px;">${b.nombre} ${b.paterno} ${b.materno}</div>
                                <div style="font-size: 0.85rem; color: #64748B;">Rut: ${b.rut} | Parentesco: ${b.parentesco}</div>
                            </div>
                            <button onclick="removeBeneficiary(${i})" style="background: none; border: none; color: #EF4444; font-size: 1.2rem; cursor: pointer;" title="Eliminar"><i class="fa-regular fa-trash-can"></i></button>
                        </div>
                    `;
                });
                listContainer.innerHTML = html;
            }
            
            if (beneficiaries.length >= 2) {
                btnAddTop.style.opacity = '0.5';
                btnAddTop.style.pointerEvents = 'none';
            } else {
                btnAddTop.style.opacity = '1';
                btnAddTop.style.pointerEvents = 'auto';
            }
        }
    </script>"""

content = script_pattern.sub(new_script.replace('\\', '\\\\'), content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
