import re

# 1. Update link in 8-1
with open("cotizacion/cotizacion-8-1.html", "r", encoding="utf-8") as f:
    cot8_1 = f.read()
cot8_1 = cot8_1.replace("onclick=\"window.location.href='cotizacion-9.html'\"", "onclick=\"window.location.href='cotizacion-9-1.html'\"")
with open("cotizacion/cotizacion-8-1.html", "w", encoding="utf-8") as f:
    f.write(cot8_1)


# 2. Rewrite 9-1
with open("cotizacion/cotizacion-9-1.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add Modal right after <div class="noise-overlay"></div>
modal_html = """
    <!-- EMAIL VERIFICATION MODAL -->
    <div id="emailVerifyModal" class="zlight-overlay" style="display: flex;">
        <div class="zlight-card" style="max-width: 450px; text-align: center; padding: 40px 30px;">
            
            <!-- STEP 1: Confirm Email -->
            <div id="emailStep1">
                <div class="modal-icon-top mb-3" style="font-size: 3rem; color: var(--quote-primary);">
                    <i class="fa-regular fa-envelope"></i>
                </div>
                <h3 style="font-weight: 800; font-size: 1.5rem; margin-bottom: 10px; color: var(--quote-dark);">Verifica tu correo electrónico</h3>
                <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 25px;">
                    Te enviaremos un código de seguridad a tu correo para validar la transacción.
                </p>
                <div style="background: #f1f5f9; padding: 15px; border-radius: 8px; font-weight: 700; color: var(--quote-indigo); font-size: 1.1rem; margin-bottom: 25px;">
                    juan.perez@ejemplo.com
                </div>
                <div style="display: flex; gap: 15px; flex-direction: column;">
                    <button class="btn-hero-gradient" style="padding: 12px; border-radius: 50px; cursor: pointer; width: 100%; border: none;" onclick="goToModalStep2()">
                        Confirmar y Enviar Código
                    </button>
                    <button style="background: transparent; border: 1px solid #cbd5e1; color: #475569; padding: 12px; border-radius: 50px; cursor: pointer; width: 100%; font-weight: 600;" onclick="alert('Funcionalidad de actualizar correo en desarrollo.')">
                        Actualizar Correo
                    </button>
                </div>
            </div>

            <!-- STEP 2: Enter PIN -->
            <div id="emailStep2" style="display: none;">
                <div class="modal-icon-top mb-3" style="font-size: 3rem; color: #8b5cf6;">
                    <i class="fa-solid fa-shield-check"></i>
                </div>
                <h3 style="font-weight: 800; font-size: 1.5rem; margin-bottom: 10px; color: var(--quote-dark);">Ingresa tu código</h3>
                <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 25px;">
                    Ingresa el código de 4 dígitos que acabamos de enviar a tu correo.
                </p>
                <div class="pin-code-inputs" style="display: flex; justify-content: center; gap: 10px; margin-bottom: 25px;">
                    <input type="text" maxlength="1" class="pin-box" oninput="moveNext(this, 'pin2')">
                    <input type="text" maxlength="1" class="pin-box" id="pin2" oninput="moveNext(this, 'pin3')">
                    <input type="text" maxlength="1" class="pin-box" id="pin3" oninput="moveNext(this, 'pin4')">
                    <input type="text" maxlength="1" class="pin-box" id="pin4" oninput="verifyCode()">
                </div>
                <button class="btn-hero-gradient" id="btnVerifyPin" style="padding: 12px; border-radius: 50px; cursor: not-allowed; width: 100%; border: none; opacity: 0.5;" disabled onclick="closeEmailModal()">
                    Verificar Código
                </button>
            </div>

        </div>
    </div>
"""
content = content.replace('<div class="noise-overlay"></div>', '<div class="noise-overlay"></div>\n' + modal_html)

# Update Headings
content = content.replace("Carga tu documento y valida tu 0Km", "Opciones de Pago")
content = content.replace("Verifica que tu vehículo es nuevo subiendo la documentación requerida.", "Selecciona tu método de pago y finaliza compra.")

# Sidebar update
old_sidebar = """<ul class="aurora-list">
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Cotización</li>
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Selección de Plan</li>
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Verificación de Datos</li>
                        <li class="active"><span class="pulse-dot"></span> Validación 0Km</li>
                        <li><i class="fa-regular fa-circle"></i> Opciones de Pago</li>
                        <li><i class="fa-regular fa-circle"></i> Emisión Final</li>
                    </ul>"""
new_sidebar = """<ul class="aurora-list">
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Cotización</li>
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Selección de Plan</li>
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Verificación de Datos</li>
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Validación 0Km</li>
                        <li class="active"><span class="pulse-dot"></span> Opciones de Pago</li>
                        <li><i class="fa-regular fa-circle"></i> Emisión Final</li>
                    </ul>
                    
                    <div class="summary-vehicle-card mt-4" style="background: white; border-radius: 12px; padding: 15px; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 4px 15px rgba(0,0,0,0.02);">
                        <div style="font-size: 0.75rem; text-transform: uppercase; color: #94A3B8; font-weight: 700; letter-spacing: 1px; margin-bottom: 5px;">Vehículo y Contratante</div>
                        <div style="font-weight: 800; color: var(--quote-dark); font-size: 1rem; margin-bottom: 2px;">CHEVROLET AVEO 2026</div>
                        <div style="font-size: 0.85rem; color: #64748B; margin-bottom: 10px;">Sí, es 0Km</div>
                        <div style="height: 1px; background: #E2E8F0; margin: 10px 0;"></div>
                        <div style="font-size: 0.85rem; color: var(--quote-dark); display: flex; justify-content: space-between; margin-bottom: 4px;"><span>Edad:</span> <strong>45 años</strong></div>
                        <div style="font-size: 0.85rem; color: var(--quote-dark); display: flex; justify-content: space-between;"><span>RUT:</span> <strong>10.042.595-5</strong></div>
                    </div>
"""
content = content.replace(old_sidebar, new_sidebar)

# Form body replacement
new_body = """
                <div class="premium-white-card" id="quoteFormStep9">
                    
                    <!-- PLAN DE PAGO SUMMARY -->
                    <div class="pg-header">
                        <div class="pg-header-badge primary">
                            <i class="fa-solid fa-file-invoice-dollar"></i> PLAN DE PAGO
                        </div>
                        <div class="pg-header-line"></div>
                    </div>
                    
                    <div class="grid-3-tight mb-4" style="background: #F8FAFC; border-radius: 12px; padding: 20px; border: 1px solid #E2E8F0;">
                        <div>
                            <div style="font-size: 0.8rem; color: #64748b; font-weight: 600;">Monto a documentar UF</div>
                            <div style="font-size: 1.5rem; font-weight: 800; color: var(--quote-dark);">38.70</div>
                        </div>
                        <div>
                            <div style="font-size: 0.8rem; color: #64748b; font-weight: 600;">Cuotas</div>
                            <div style="font-size: 1.5rem; font-weight: 800; color: var(--quote-dark);">1</div>
                        </div>
                        <div>
                            <div style="font-size: 0.8rem; color: #64748b; font-weight: 600;">Días</div>
                            <div style="font-size: 1.5rem; font-weight: 800; color: var(--quote-dark);">25</div>
                        </div>
                    </div>
                    
                    <table class="aurora-table mb-5" style="width: 100%; border-collapse: collapse; text-align: left; background: white; border-radius: 8px; overflow: hidden; border: 1px solid #E2E8F0;">
                        <thead style="background: #F1F5F9; color: #475569; font-size: 0.85rem;">
                            <tr><th style="padding: 10px 15px;">Cuota</th><th style="padding: 10px 15px;">Fecha</th><th style="padding: 10px 15px;">Monto (UF)</th></tr>
                        </thead>
                        <tbody style="font-size: 0.95rem; font-weight: 600; color: var(--quote-dark);">
                            <tr><td style="padding: 10px 15px; border-top: 1px solid #E2E8F0;">1</td><td style="padding: 10px 15px; border-top: 1px solid #E2E8F0;">25-07-2026</td><td style="padding: 10px 15px; border-top: 1px solid #E2E8F0;">38.70</td></tr>
                        </tbody>
                    </table>

                    <!-- DATOS DEL PAGADOR -->
                    <div class="pg-header">
                        <div class="pg-header-badge purple">
                            <i class="fa-solid fa-user-check"></i> DATOS DEL PAGADOR
                        </div>
                        <div class="pg-header-line"></div>
                    </div>

                    <div class="grid-2-tight mb-4">
                        <div class="inp-rich-group">
                            <label>RUT</label>
                            <input type="text" class="rich-input" value="10.042.595-5" disabled style="background: #F8FAFC; color: #94A3B8;">
                        </div>
                        <div class="inp-rich-group">
                            <label>Nombre</label>
                            <input type="text" class="rich-input" value="Cristian Gonzalo Martinez Pardo" disabled style="background: #F8FAFC; color: #94A3B8;">
                        </div>
                        <div class="inp-rich-group">
                            <label>Región</label>
                            <input type="text" class="rich-input" value="DE LOS RÍOS" disabled style="background: #F8FAFC; color: #94A3B8;">
                        </div>
                        <div class="inp-rich-group">
                            <label>Comuna</label>
                            <input type="text" class="rich-input" value="VALDIVIA" disabled style="background: #F8FAFC; color: #94A3B8;">
                        </div>
                        <div class="inp-rich-group" style="grid-column: span 2;">
                            <label>Dirección</label>
                            <input type="text" class="rich-input" value="Martínez de Rozas 5523" disabled style="background: #F8FAFC; color: #94A3B8;">
                        </div>
                    </div>

                    <div style="background: #EFF6FF; border: 1px solid #BFDBFE; padding: 15px; border-radius: 12px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: 700; color: var(--quote-indigo);">Requiere GPS</span>
                        <div class="aurora-toggle-segment" style="margin: 0; background: white;">
                            <input type="radio" name="gps" id="gps_yes" value="yes" checked>
                            <label for="gps_yes">Sí</label>
                            <input type="radio" name="gps" id="gps_no" value="no">
                            <label for="gps_no">No</label>
                            <div class="segment-highlight"></div>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #E2E8F0; padding-top: 20px; margin-bottom: 30px;">
                        <span style="font-weight: 700; font-size: 1.1rem; color: var(--quote-dark);">¿Los datos están correctos?</span>
                        <div class="aurora-toggle-segment">
                            <input type="radio" name="datosCorrectos" id="dc_yes" value="yes" onchange="togglePACPATForm()">
                            <label for="dc_yes">Sí</label>
                            <input type="radio" name="datosCorrectos" id="dc_no" value="no" checked onchange="togglePACPATForm()">
                            <label for="dc_no">No</label>
                            <div class="segment-highlight"></div>
                        </div>
                    </div>

                    <!-- PAC / PAT TABS (HIDDEN UNTIL SÍ IS CHECKED) -->
                    <div id="paymentOptionsSection" style="display: none; opacity: 0; transition: opacity 0.4s ease;">
                        <div class="pg-header">
                            <div class="pg-header-badge teal">
                                <i class="fa-solid fa-credit-card"></i> OPCIONES DE PAGO: PAC O PAT
                            </div>
                            <div class="pg-header-line"></div>
                        </div>

                        <div class="payment-tabs-container mb-4">
                            <button class="payment-tab active" id="tabPAC" onclick="switchPaymentTab('PAC')">
                                <i class="fa-solid fa-building-columns"></i> PAC (Cuenta)
                            </button>
                            <button class="payment-tab" id="tabPAT" onclick="switchPaymentTab('PAT')">
                                <i class="fa-regular fa-credit-card"></i> PAT (Tarjeta)
                            </button>
                        </div>

                        <!-- PAC FORM -->
                        <div id="formPAC" class="payment-form-box">
                            <h4 style="font-size: 1.1rem; font-weight: 800; color: var(--quote-dark); margin-bottom: 15px;">PAC: Datos de la cuenta</h4>
                            <div class="grid-2-tight">
                                <div class="inp-rich-group">
                                    <label>Banco</label>
                                    <div class="input-rich-wrapper compact-premium theme-blue">
                                        <div class="icon-slot"><i class="fa-solid fa-building-columns"></i></div>
                                        <select class="rich-input" style="background: transparent; border: none; width: 100%; outline: none;">
                                            <option value="">Selecciona Banco</option>
                                            <option value="bch">Banco de Chile</option>
                                            <option value="santander">Banco Santander</option>
                                            <option value="bci">BCI</option>
                                            <option value="estado">BancoEstado</option>
                                            <option value="itau">Itaú</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Nº de cuenta</label>
                                    <div class="input-rich-wrapper compact-premium theme-blue">
                                        <div class="icon-slot"><i class="fa-solid fa-hashtag"></i></div>
                                        <input type="text" class="rich-input" placeholder="0-000-00-00000-0">
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- PAT FORM -->
                        <div id="formPAT" class="payment-form-box" style="display: none;">
                            <h4 style="font-size: 1.1rem; font-weight: 800; color: var(--quote-dark); margin-bottom: 15px;">PAT: Datos de la tarjeta</h4>
                            <div class="grid-2-tight">
                                <div class="inp-rich-group">
                                    <label>Tipo de tarjeta</label>
                                    <div class="input-rich-wrapper compact-premium theme-purple">
                                        <div class="icon-slot"><i class="fa-brands fa-cc-visa"></i></div>
                                        <select class="rich-input" style="background: transparent; border: none; width: 100%; outline: none;">
                                            <option value="">Selecciona Tipo</option>
                                            <option value="visa">Visa</option>
                                            <option value="mastercard">MasterCard</option>
                                            <option value="amex">American Express</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Nº de tarjeta</label>
                                    <div class="input-rich-wrapper compact-premium theme-purple">
                                        <div class="icon-slot"><i class="fa-regular fa-credit-card"></i></div>
                                        <input type="text" class="rich-input" placeholder="0000-0000-0000-0000" maxlength="19">
                                    </div>
                                </div>
                            </div>
                            
                            <div class="grid-3-tight mt-3">
                                <div class="inp-rich-group">
                                    <label>MM</label>
                                    <input type="text" class="rich-input" placeholder="12" maxlength="2">
                                </div>
                                <div class="inp-rich-group">
                                    <label>YYYY</label>
                                    <input type="text" class="rich-input" placeholder="2028" maxlength="4">
                                </div>
                                <div class="inp-rich-group">
                                    <label>Banco Emisor</label>
                                    <input type="text" class="rich-input" placeholder="Ej: Santander">
                                </div>
                            </div>
                        </div>

                    </div>

"""

pattern = re.compile(r'<div class="premium-white-card" id="quoteFormStep8">.*?</script>', re.DOTALL)
# Extract the javascript logic we need to keep/replace.
# Wait, let's just do a manual replace of the body area down to <div class="hero-action-area mt-5"
body_pattern = re.compile(r'<div class="premium-white-card" id="quoteFormStep8">.*?<div class="hero-action-area mt-5"', re.DOTALL)
content = body_pattern.sub(new_body + '\n                    <div class="hero-action-area mt-5"', content)

# Update Next button target to cotizacion-10-1.html
content = content.replace("onclick=\"window.location.href='cotizacion-8-1.html'\"", "onclick=\"window.location.href='cotizacion-10-1.html'\"")
content = content.replace("onclick=\"window.location.href='cotizacion-9.html'\"", "onclick=\"window.location.href='cotizacion-10-1.html'\"")

# Add custom javascript to handle modal and form
new_scripts = """<script>
    // Modal Logic
    function goToModalStep2() {
        document.getElementById('emailStep1').style.display = 'none';
        document.getElementById('emailStep2').style.display = 'block';
        setTimeout(() => { document.querySelector('.pin-box').focus(); }, 100);
    }
    
    function moveNext(elem, nextId) {
        if(elem.value.length >= 1) {
            const nextElem = document.getElementById(nextId);
            if(nextElem) {
                nextElem.focus();
            } else {
                verifyCode();
            }
        }
    }
    
    function verifyCode() {
        const p1 = document.querySelector('.pin-box').value;
        const p2 = document.getElementById('pin2').value;
        const p3 = document.getElementById('pin3').value;
        const p4 = document.getElementById('pin4').value;
        
        if (p1 && p2 && p3 && p4) {
            const btn = document.getElementById('btnVerifyPin');
            btn.disabled = false;
            btn.style.opacity = '1';
            btn.style.cursor = 'pointer';
        }
    }
    
    function closeEmailModal() {
        document.getElementById('emailVerifyModal').style.display = 'none';
        document.body.style.overflow = 'auto'; // restore scroll
    }

    // PAC/PAT Form logic
    function togglePACPATForm() {
        const isYes = document.getElementById('dc_yes').checked;
        const section = document.getElementById('paymentOptionsSection');
        const btnNext = document.getElementById('btnNext');
        
        if (isYes) {
            section.style.display = 'block';
            setTimeout(() => { section.style.opacity = '1'; }, 10);
            
            // Enable next button when they confirm
            btnNext.disabled = false;
            btnNext.classList.remove('disabled');
            btnNext.style.cursor = 'pointer';
            btnNext.style.opacity = '1';
        } else {
            section.style.opacity = '0';
            setTimeout(() => { section.style.display = 'none'; }, 400);
            
            btnNext.disabled = true;
            btnNext.classList.add('disabled');
            btnNext.style.cursor = 'not-allowed';
            btnNext.style.opacity = '0.5';
        }
    }
    
    function switchPaymentTab(type) {
        const tabPAC = document.getElementById('tabPAC');
        const tabPAT = document.getElementById('tabPAT');
        const formPAC = document.getElementById('formPAC');
        const formPAT = document.getElementById('formPAT');
        
        if (type === 'PAC') {
            tabPAC.classList.add('active');
            tabPAT.classList.remove('active');
            formPAC.style.display = 'block';
            formPAT.style.display = 'none';
        } else {
            tabPAT.classList.add('active');
            tabPAC.classList.remove('active');
            formPAT.style.display = 'block';
            formPAC.style.display = 'none';
        }
    }
    
    // On load, disable body scroll until modal is closed
    document.addEventListener("DOMContentLoaded", () => {
        document.body.style.overflow = 'hidden';
    });
</script>"""

script_pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
content = script_pattern.sub(new_scripts, content)

with open("cotizacion/cotizacion-9-1.html", "w", encoding="utf-8") as f:
    f.write(content)

print("cotizacion-9-1.html successfully generated!")
