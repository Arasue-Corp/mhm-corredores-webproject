import re

with open('cotizacion/cotizacion-salud-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Grab header up to <div class="specs-layout-grid">
header_match = re.search(r'([\s\S]*?<div class="specs-layout-grid">\s*)', content)
header = header_match.group(1)

# Grab footer
footer_match = re.search(r'(\s*</div\s*>\s*</div\s*>\s*<script>[\s\S]*)', content)
footer = footer_match.group(1)
# we actually want to strip the <script> part and write our own.
footer = re.sub(r'<script>[\s\S]*', '', footer)
# Re-add the closing tags that might have been lost
footer += "\n    </div>\n"
# Actually, let's grab footer starting from <footer class="footer-aurora"> or just re-use the footer from the previous script?
# cotizacion-salud-2.html doesn't have footer-aurora? It does have <div class="specs-layout-grid">. Let's close it manually.

body = """
                <div class="main-spec-col anim-entry delay-1">
                    <div class="premium-white-card" style="padding: 36px 32px;">
                        
                        <form id="compradorForm" onsubmit="event.preventDefault(); goToNextStep();">

                            <!-- DATOS PERSONALES DEL CONTRATANTE -->
                            <h2 style="font-size: 1.3rem; color: #0F172A; margin-bottom: 22px; font-weight: 800;">
                                <i class="fa-solid fa-id-card-clip" style="color: #796bfc; margin-right: 8px;"></i> Datos del Responsable (Dueño)
                            </h2>
                            
                            <div class="input-group-modern" style="margin-bottom: 25px;">
                                <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">RUT *</label>
                                <div class="input-with-icon" style="position: relative;">
                                    <i class="fa-solid fa-id-card" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                    <input type="text" id="rutInput" onkeyup="validateForm()" class="rich-input" placeholder="Ej: 12.345.678-9" style="width: 100%; max-width: 320px; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #CBD5E1; background: #FFFFFF; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                                </div>
                            </div>

                            <div class="input-group-modern" style="margin-bottom: 25px;">
                                <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Nombres *</label>
                                <div class="input-with-icon" style="position: relative;">
                                    <i class="fa-solid fa-user" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                    <input type="text" id="nameInput" onkeyup="validateForm()" class="rich-input" placeholder="Ingrese nombres completos" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #CBD5E1; background: #FFFFFF; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                                </div>
                            </div>

                            <div class="form-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                                <div class="input-group-modern" style="margin-bottom: 25px;">
                                    <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Apellido Paterno *</label>
                                    <div class="input-with-icon" style="position: relative;">
                                        <i class="fa-solid fa-user-tag" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                        <input type="text" id="lastNameInput" onkeyup="validateForm()" class="rich-input" placeholder="Apellido paterno" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #CBD5E1; background: #FFFFFF; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                                    </div>
                                </div>
                                <div class="input-group-modern" style="margin-bottom: 25px;">
                                    <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Apellido Materno *</label>
                                    <div class="input-with-icon" style="position: relative;">
                                        <i class="fa-solid fa-user-tag" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                        <input type="text" id="secondLastNameInput" onkeyup="validateForm()" class="rich-input" placeholder="Apellido materno" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #CBD5E1; background: #FFFFFF; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                                    </div>
                                </div>
                            </div>

                            <div class="form-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                                <div class="input-group-modern" style="margin-bottom: 25px;">
                                    <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Correo Electrónico *</label>
                                    <div class="input-with-icon" style="position: relative;">
                                        <i class="fa-solid fa-envelope" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                        <input type="email" id="emailInput" onkeyup="validateForm()" class="rich-input" placeholder="correo@ejemplo.com" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #CBD5E1; background: #FFFFFF; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                                    </div>
                                </div>
                                <div class="input-group-modern" style="margin-bottom: 25px;">
                                    <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Teléfono Móvil *</label>
                                    <div class="input-with-icon" style="position: relative;">
                                        <i class="fa-solid fa-phone" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                        <input type="tel" id="phoneInput" onkeyup="validateForm()" class="rich-input" placeholder="+56 9 1234 5678" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #CBD5E1; background: #FFFFFF; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                                    </div>
                                </div>
                            </div>

                            <div class="input-group-modern" style="margin-bottom: 25px;">
                                <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Dirección Residencial *</label>
                                <div class="input-with-icon" style="position: relative;">
                                    <i class="fa-solid fa-location-dot" style="position: absolute; left: 16px; top: 16px; color: #94A3B8;"></i>
                                    <input type="text" id="addressInput" onkeyup="validateForm()" class="rich-input" placeholder="Av. Providencia 1234, depto 501" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #CBD5E1; background: #FFFFFF; transition: 0.3s; font-size: 1rem; color: #0F172A;" required>
                                </div>
                            </div>

                            <div class="input-group-modern" style="margin-bottom: 35px;">
                                <label style="display: block; margin-bottom: 10px; font-weight: 700; color: #1E293B; font-size: 0.95rem;">Comuna *</label>
                                <div class="input-with-icon" style="position: relative;">
                                    <i class="fa-solid fa-map-location-dot" style="position: absolute; left: 16px; top: 16px; color: #94A3B8; z-index: 10;"></i>
                                    <select id="comunaInput" onchange="validateForm()" class="rich-input" style="width: 100%; padding: 14px 15px 14px 45px; border-radius: 12px; border: 1px solid #CBD5E1; background: #FFFFFF; transition: 0.3s; font-size: 1rem; color: #0F172A; cursor: pointer; appearance: none;" required>
                                        <option value="" disabled selected>Selecciona tu comuna</option>
                                        <option value="santiago">Santiago Centro</option>
                                        <option value="providencia">Providencia</option>
                                        <option value="las_condes">Las Condes</option>
                                        <option value="nunoa">Ñuñoa</option>
                                        <option value="vitacura">Vitacura</option>
                                        <option value="lo_barnechea">Lo Barnechea</option>
                                        <option value="la_reina">La Reina</option>
                                        <option value="macul">Macul</option>
                                        <option value="florida">La Florida</option>
                                        <option value="maipu">Maipú</option>
                                        <option value="vina">Viña del Mar</option>
                                        <option value="concepcion">Concepción</option>
                                    </select>
                                    <i class="fa-solid fa-chevron-down" style="position: absolute; right: 15px; top: 18px; pointer-events: none; color: #94A3B8;"></i>
                                </div>
                            </div>

                            <div style="display: flex; justify-content: flex-end;">
                                <button type="submit" id="btn-continue" style="background: linear-gradient(135deg, #796BFC 0%, #5E4BF5 100%) !important; color: #FFFFFF !important; opacity: 0.5; pointer-events: none; transition: all 0.3s ease; padding: 16px 36px; border-radius: 14px; font-weight: 800; font-size: 1rem; border: none; cursor: pointer; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 8px 22px -3px rgba(121, 107, 252, 0.45);">
                                    <span>Continuar con el Pago</span>
                                    <i class="fa-solid fa-arrow-right"></i>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>

                <aside class="config-sidebar anim-entry delay-2">
                    <div class="organic-panel ruta-container" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px; padding: 24px; margin-bottom: 20px;">
                        <div class="sidebar-title text-gradient-corp" style="font-size: 1.15rem; font-weight: 800; margin-bottom: 18px;">
                            Ruta de Contratación
                        </div>
                        <ul class="aurora-list" style="margin-bottom: 0; padding-bottom: 0;">
                            <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Selección de Mascotas</li>
                            <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Resumen Mascotas</li>
                            <li class="active"><span class="pulse-dot"></span> Datos del Contratante</li>
                            <li><i class="fa-regular fa-circle"></i> Pago Seguro</li>
                        </ul>
                    </div>

                    <div class="organic-panel resumen-container" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px; padding: 24px;">
                        <div class="sidebar-title text-gradient-corp" style="font-size: 1.15rem; font-weight: 800; margin-bottom: 18px; border-bottom: 1px solid #E2E8F0; padding-bottom: 12px;">
                            Resumen de la Orden
                        </div>
                        
                        <div id="cart-summary-step2">
                            <div class="summary-item" style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 15px;">
                                <div>
                                    <span style="font-size: 10px; font-weight: 800; color: #796BFC; text-transform: uppercase; letter-spacing: 0.1em; display: block;">SEGURO MASCOTAS</span>
                                    <h4 style="margin: 3px 0 2px; color: #0F172A; font-weight: 800; font-size: 1.05rem;" id="mascotaCountText">Múltiples Planes</h4>
                                </div>
                                <div style="text-align: right;">
                                    <div id="dynamic-sidebar-price" style="color: #796bfc; font-weight: 900; font-size: 1.2rem;">$0</div>
                                    <div style="color: #94A3B8; font-size: 0.75rem;">/ mes</div>
                                </div>
                            </div>
                        </div>

                        <div style="background: rgba(46, 217, 195, 0.08); border: 1.5px dashed #2ED9C3; border-radius: 16px; padding: 16px; margin-top: 20px; text-align: center;">
                            <i class="fa-solid fa-paw" style="font-size: 1.8rem; color: #0F766E; margin-bottom: 8px;"></i>
                            <h4 style="margin: 0 0 4px 0; color: #0F172A; font-weight: 800; font-size: 0.95rem;">Mascotas Seguras</h4>
                            <p style="margin: 0; font-size: 0.8rem; color: #475569;">Atención veterinaria 24/7 de calidad.</p>
                        </div>
                    </div>
                </aside>
"""

js_script = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            initRegistrationForm();
        });

        const PLAN_PRICES = {
            'basico': 9490,
            'pro': 12490,
            'senior': 16490
        };

        function initRegistrationForm() {
            const dataStr = sessionStorage.getItem('mhm_mascotas_data');
            if (!dataStr) {
                window.location.href = 'cotizacion-mascota-nueva-1.html';
                return;
            }
            const petsData = JSON.parse(dataStr);
            let totalMensual = 0;
            petsData.forEach(p => {
                totalMensual += PLAN_PRICES[p.plan] || 0;
            });

            document.getElementById('mascotaCountText').innerText = `${petsData.length} mascota${petsData.length > 1 ? 's' : ''}`;
            document.getElementById('dynamic-sidebar-price').innerText = `$${totalMensual.toLocaleString('es-CL')}`;

            const prevContractor = sessionStorage.getItem('contratanteMascotaData');
            if (prevContractor) {
                try {
                    const c = JSON.parse(prevContractor);
                    if (c.rut) document.getElementById('rutInput').value = c.rut;
                    if (c.name) document.getElementById('nameInput').value = c.name;
                    if (c.lastName) document.getElementById('lastNameInput').value = c.lastName;
                    if (c.secondLastName) document.getElementById('secondLastNameInput').value = c.secondLastName;
                    if (c.email) document.getElementById('emailInput').value = c.email;
                    if (c.phone) document.getElementById('phoneInput').value = c.phone;
                    if (c.address) document.getElementById('addressInput').value = c.address;
                    if (c.comuna) document.getElementById('comunaInput').value = c.comuna;
                } catch(e){}
            }

            validateForm();
        }

        function validateEmail(email) {
            return /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/.test(email);
        }
        
        function validateRut(rut) {
            return rut.length >= 8;
        }

        function validateForm() {
            const rut = document.getElementById('rutInput')?.value.trim() || '';
            const name = document.getElementById('nameInput')?.value.trim() || '';
            const lastName = document.getElementById('lastNameInput')?.value.trim() || '';
            const secondLastName = document.getElementById('secondLastNameInput')?.value.trim() || '';
            const email = document.getElementById('emailInput')?.value.trim() || '';
            const phone = document.getElementById('phoneInput')?.value.trim() || '';
            const address = document.getElementById('addressInput')?.value.trim() || '';
            const comuna = document.getElementById('comunaInput')?.value || '';
            const btn = document.getElementById('btn-continue');
            if (!btn) return;
            
            const isValid = validateRut(rut) && 
                            name.length >= 2 && lastName.length >= 2 && secondLastName.length >= 2 && 
                            validateEmail(email) && phone.length >= 7 && address.length >= 4 && comuna !== "";

            if (isValid) {
                btn.style.opacity = '1';
                btn.style.pointerEvents = 'auto';
                btn.style.filter = 'none';
            } else {
                btn.style.opacity = '0.5';
                btn.style.pointerEvents = 'none';
            }
        }

        function goToNextStep() {
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
            sessionStorage.setItem('contratanteMascotaData', JSON.stringify(formData));

            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.3s ease';
            setTimeout(() => {
                alert('Cotización finalizada. Simulación de redirección al pago.');
                window.location.href = '../index.html';
            }, 300);
        }
    </script>
</body>
</html>
"""

# Let's fix up header
header = header.replace('cotizacion-salud-resumen.html', 'cotizacion-mascota-nueva-resumen.html')
header = header.replace('MAPFRE AP Salud 100 UF', 'Registro de Contratante')
header = header.replace('<title>Cotización de Asistencia de Salud | MHM Corredores</title>', '<title>Cotización Mascotas | MHM Corredores</title>')
header = header.replace('Paso 2: Registro de Contratación', 'Paso 3: Registro de Contratación')
header = header.replace('MAPFRE AP SALUD', 'SEGURO MASCOTAS')

with open('cotizacion/cotizacion-mascota-nueva-2.html', 'w', encoding='utf-8') as f:
    f.write(header + body + "\n    </div>\n" + js_script)

print("Generated cotizacion-mascota-nueva-2.html")
