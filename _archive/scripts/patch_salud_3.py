import os

file_path = "cotizacion/cotizacion-salud-3.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Back button
content = content.replace(
    '<a href="cotizacion-salud-1.html" class="nav-back-btn"><div class="icon-circle"><i class="fa-solid fa-arrow-left"></i></div><span> Volver a Selección de Plan</span></a>',
    '<a href="cotizacion-salud-2.html" class="nav-back-btn"><div class="icon-circle"><i class="fa-solid fa-arrow-left"></i></div><span> Volver a Datos del Contratante</span></a>'
)

# 2. Header and Title
content = content.replace(
    '<p>Ingresa los datos del comprador para continuar con la contratación.</p>',
    '<p>Ingresa los datos del titular principal de la póliza.</p>'
)
content = content.replace(
    '<h2 style="font-size: 1.5rem; color: #0F172A; margin-bottom: 30px; font-weight: 800;">Datos del Comprador</h2>',
    '<h2 style="font-size: 1.5rem; color: #0F172A; margin-bottom: 20px; font-weight: 800;">Datos del Titular</h2>'
)

# 3. Insert same-as-contractor button right after the form starts
form_start = '<form id="compradorForm" onsubmit="event.preventDefault(); goToNextStep();">'
banner = """<form id="titularForm" onsubmit="event.preventDefault(); goToNextStep();">
                            <div class="same-as-contractor" style="background: #EEF2FF; border: 1px dashed #796bfc; padding: 15px; border-radius: 12px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                                <div>
                                    <h4 style="margin: 0; color: #4F46E5; font-size: 0.95rem;">¿El titular es el mismo contratante?</h4>
                                    <p style="margin: 0; font-size: 0.8rem; color: #64748B;">Autocompleta usando los datos del paso anterior.</p>
                                </div>
                                <button type="button" onclick="fillWithContractorData()" class="btn-pill-outline" style="background: white; border-color: #796bfc; color: #796bfc;">Sí, usar mis datos</button>
                            </div>"""
content = content.replace(form_start, banner)

# 4. Modify Rut input to include DOB alongside it
rut_input_block = """                            <div class="input-group-modern" style="margin-bottom: 25px;">
                                <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Rut *</label>
                                <div class="input-with-icon" style="position: relative;"><i class="fa-solid fa-id-card" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
<input type="text" id="rutInput" onkeyup="validateForm()" class="rich-input" placeholder="Ej: 12.345.678-9" style="width: 100%; max-width: 300px; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
</div>
                            </div>"""

rut_and_dob_block = """                            <div class="form-grid" style="margin-bottom: 25px;">
                                <div class="input-group-modern">
                                    <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Rut *</label>
                                    <div class="input-with-icon" style="position: relative;"><i class="fa-solid fa-id-card" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                    <input type="text" id="rutInput" onkeyup="validateForm()" class="rich-input" placeholder="Ej: 12.345.678-9" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                                    </div>
                                </div>
                                <div class="input-group-modern">
                                    <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Fecha de Nacimiento *</label>
                                    <div class="input-with-icon" style="position: relative;"><i class="fa-solid fa-calendar-days" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                    <input type="date" id="dobInput" onchange="validateForm()" class="rich-input" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #E2E8F0; background: #F8FAFC; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                                    </div>
                                </div>
                            </div>"""
content = content.replace(rut_input_block, rut_and_dob_block)

# 5. Sidebar active state
sidebar_old = """                            <li class="active"><span class="pulse-dot"></span> Datos del Contratante</li>
                            <li><i class="fa-regular fa-circle"></i> Titular</li>"""
sidebar_new = """                            <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Datos del Contratante</li>
                            <li class="active"><span class="pulse-dot"></span> Titular</li>"""
content = content.replace(sidebar_old, sidebar_new)

# 6. JS functions (validateForm, goToNextStep, fillWithContractorData)
old_validate_func = """        function validateForm() {
            const rut = document.getElementById('rutInput').value.trim();
            const name = document.getElementById('nameInput').value.trim();
            const lastName = document.getElementById('lastNameInput').value.trim();
            const secondLastName = document.getElementById('secondLastNameInput').value.trim();
            const email = document.getElementById('emailInput').value.trim();
            const phone = document.getElementById('phoneInput').value.trim();
            const address = document.getElementById('addressInput').value.trim();
            const comuna = document.getElementById('comunaInput').value;
            const btn = document.getElementById('btn-continue');
            
            // All required fields must be somewhat filled
            if (validateRut(rut) && name.length > 2 && lastName.length > 2 && secondLastName.length > 2 && validateEmail(email) && phone.length > 7 && address.length > 5 && comuna !== "") {
                btn.style.opacity = '1';
                btn.style.pointerEvents = 'auto';
            } else {
                btn.style.opacity = '0.5';
                btn.style.pointerEvents = 'none';
            }
        }"""

new_validate_func = """        function validateForm() {
            const rut = document.getElementById('rutInput').value.trim();
            const dob = document.getElementById('dobInput').value;
            const name = document.getElementById('nameInput').value.trim();
            const lastName = document.getElementById('lastNameInput').value.trim();
            const secondLastName = document.getElementById('secondLastNameInput').value.trim();
            const email = document.getElementById('emailInput').value.trim();
            const phone = document.getElementById('phoneInput').value.trim();
            const address = document.getElementById('addressInput').value.trim();
            const comuna = document.getElementById('comunaInput').value;
            const btn = document.getElementById('btn-continue');
            
            if (validateRut(rut) && dob !== "" && name.length > 2 && lastName.length > 2 && secondLastName.length > 2 && validateEmail(email) && phone.length > 7 && address.length > 5 && comuna !== "") {
                btn.style.opacity = '1';
                btn.style.pointerEvents = 'auto';
            } else {
                btn.style.opacity = '0.5';
                btn.style.pointerEvents = 'none';
            }
        }
        
        function fillWithContractorData() {
            const data = sessionStorage.getItem('contratanteData');
            if(data) {
                const parsed = JSON.parse(data);
                document.getElementById('rutInput').value = parsed.rut || '';
                document.getElementById('nameInput').value = parsed.name || '';
                document.getElementById('lastNameInput').value = parsed.lastName || '';
                document.getElementById('secondLastNameInput').value = parsed.secondLastName || '';
                document.getElementById('emailInput').value = parsed.email || '';
                document.getElementById('phoneInput').value = parsed.phone || '';
                document.getElementById('addressInput').value = parsed.address || '';
                document.getElementById('comunaInput').value = parsed.comuna || '';
                validateForm();
            }
        }"""
content = content.replace(old_validate_func, new_validate_func)

old_go_func = """        function goToNextStep() {
            const formData = {
                rut: document.getElementById('rutInput').value,
                name: document.getElementById('nameInput').value,
                lastName: document.getElementById('lastNameInput').value,
                secondLastName: document.getElementById('secondLastNameInput').value,
                email: document.getElementById('emailInput').value,
                phone: document.getElementById('phoneInput').value,
                address: document.getElementById('addressInput').value,
                comuna: document.getElementById('comunaInput').value
            };
            sessionStorage.setItem('contratanteData', JSON.stringify(formData));

            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.3s ease';
            setTimeout(() => {
                window.location.href = 'cotizacion-salud-3.html';
            }, 300);
        }"""

new_go_func = """        function goToNextStep() {
            const formData = {
                rut: document.getElementById('rutInput').value,
                dob: document.getElementById('dobInput').value,
                name: document.getElementById('nameInput').value,
                lastName: document.getElementById('lastNameInput').value,
                secondLastName: document.getElementById('secondLastNameInput').value,
                email: document.getElementById('emailInput').value,
                phone: document.getElementById('phoneInput').value,
                address: document.getElementById('addressInput').value,
                comuna: document.getElementById('comunaInput').value
            };
            sessionStorage.setItem('titularData', JSON.stringify(formData));

            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.3s ease';
            setTimeout(() => {
                window.location.href = 'cotizacion-salud-4.html';
            }, 300);
        }"""
content = content.replace(old_go_func, new_go_func)


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Patch applied to cotizacion-salud-3.html")
