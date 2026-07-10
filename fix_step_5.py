import os
import re

file_path = "cotizacion/cotizacion-salud-5.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix the top header (remove the top button, align text right)
old_top_div = """                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                                <button type="button" id="btn-add-top" onclick="openBeneficiaryModal()" style="background: #A3CC39; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: 0.3s;">
                                    Agregar Beneficiario
                                </button>
                                <span style="font-size: 0.85rem; color: #64748B;">Máximo <strong>2</strong> beneficiarios</span>
                            </div>"""

new_top_div = """                            <div style="display: flex; justify-content: flex-end; align-items: center; margin-bottom: 20px;">
                                <span style="font-size: 0.85rem; color: #64748B;">Máximo <strong>2</strong> beneficiarios</span>
                            </div>"""

content = content.replace(old_top_div, new_top_div)

# 2. Modify the empty state to remove its button, and put a central button below the list
old_empty = """                            <div id="empty-state-container" style="border: 1px dashed #CBD5E1; border-radius: 12px; padding: 50px 20px; text-align: center; background: #F8FAFC; margin-bottom: 30px;">
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
                            </div>"""

new_empty = """                            <div id="empty-state-container" style="border: 1px dashed #CBD5E1; border-radius: 12px; padding: 50px 20px; text-align: center; background: #F8FAFC; margin-bottom: 20px;">
                                <div style="font-size: 3rem; color: #94A3B8; margin-bottom: 15px;">
                                    <i class="fa-solid fa-users"></i>
                                </div>
                                <h4 style="color: #1E293B; font-size: 1.1rem; margin-bottom: 5px;">No hay beneficiarios agregados</h4>
                                <p style="color: #64748B; font-size: 0.9rem; margin-bottom: 0;">Comience agregando el primer beneficiario del seguro</p>
                            </div>

                            <div id="beneficiaries-list" style="display: none; margin-bottom: 20px;">
                                <!-- Cards will be injected here via JS -->
                            </div>
                            
                            <div style="text-align: center; margin-bottom: 30px;">
                                <button type="button" id="btn-add-main" onclick="openBeneficiaryModal()" style="background: white; border: 1px solid #A3CC39; color: #A3CC39; padding: 12px 30px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: 0.3s; display: inline-block;">
                                    Agregar primer beneficiario
                                </button>
                            </div>"""
content = content.replace(old_empty, new_empty)

# 3. Replace the entire script block explicitly
script_pattern = re.compile(r'<script>\s*function validateForm.*?<\/script>', re.DOTALL)
new_script = r"""<script>
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
                window.location.href = 'cotizacion-salud-6.html';
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
            const btnAddMain = document.getElementById('btn-add-main');
            
            if (beneficiaries.length === 0) {
                emptyState.style.display = 'block';
                listContainer.style.display = 'none';
                btnAddMain.innerText = 'Agregar primer beneficiario';
            } else {
                emptyState.style.display = 'none';
                listContainer.style.display = 'block';
                btnAddMain.innerText = 'Agregar otro beneficiario';
                
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
                btnAddMain.style.opacity = '0.5';
                btnAddMain.style.pointerEvents = 'none';
                btnAddMain.innerText = 'Límite de 2 alcanzado';
            } else {
                btnAddMain.style.opacity = '1';
                btnAddMain.style.pointerEvents = 'auto';
            }
        }
    </script>"""

content = script_pattern.sub(new_script.replace('\\', '\\\\'), content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Patch applied to step 5")
