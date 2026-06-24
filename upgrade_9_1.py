import re

with open("cotizacion/cotizacion-9-1.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. UPGRADE THE MODAL
new_modal_html = """
    <!-- PREMIUM EMAIL VERIFICATION MODAL -->
    <div id="emailVerifyModal" class="zlight-overlay" style="display: flex; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); background: rgba(15, 23, 42, 0.4);">
        <div class="premium-modal-glass">
            
            <!-- STEP 1: Confirm Email -->
            <div id="emailStep1" class="modal-step-content active">
                <div class="modal-floating-icon blue-glow">
                    <i class="fa-solid fa-envelope-open-text"></i>
                </div>
                
                <h3 class="modal-premium-title">Verificación de Seguridad</h3>
                <p class="modal-premium-desc">
                    Para proteger tu transacción, enviaremos un PIN seguro a tu correo electrónico.
                </p>
                
                <div class="email-display-card">
                    <div class="ed-icon"><i class="fa-solid fa-at"></i></div>
                    <div class="ed-text">juan.perez@ejemplo.com</div>
                    <div class="ed-badge"><i class="fa-solid fa-check"></i> Listo</div>
                </div>
                
                <div class="modal-action-stack">
                    <button class="btn-hero-gradient w-100" style="padding: 14px; border-radius: 12px; font-size: 1.05rem;" onclick="goToModalStep2()">
                        Enviar PIN de Seguridad <i class="fa-solid fa-paper-plane" style="margin-left: 8px;"></i>
                    </button>
                    <button class="btn-ghost-premium w-100" onclick="alert('Funcionalidad de actualizar correo en desarrollo.')">
                        Actualizar Correo
                    </button>
                </div>
            </div>

            <!-- STEP 2: Enter PIN -->
            <div id="emailStep2" class="modal-step-content" style="display: none;">
                <div class="modal-floating-icon purple-glow">
                    <i class="fa-solid fa-shield-halved"></i>
                </div>
                
                <h3 class="modal-premium-title">Ingresa tu PIN</h3>
                <p class="modal-premium-desc">
                    Hemos enviado un código de 4 dígitos a <strong>juan.perez@ejemplo.com</strong>
                </p>
                
                <div class="pin-code-inputs">
                    <input type="text" maxlength="1" class="pin-box-premium" oninput="moveNext(this, 'pin2')" autofocus>
                    <input type="text" maxlength="1" class="pin-box-premium" id="pin2" oninput="moveNext(this, 'pin3')">
                    <input type="text" maxlength="1" class="pin-box-premium" id="pin3" oninput="moveNext(this, 'pin4')">
                    <input type="text" maxlength="1" class="pin-box-premium" id="pin4" oninput="verifyCode()">
                </div>
                
                <div class="resend-text">¿No recibiste el código? <span>Reenviar en 00:59</span></div>
                
                <button class="btn-hero-gradient w-100" id="btnVerifyPin" style="padding: 14px; border-radius: 12px; font-size: 1.05rem; opacity: 0.4; cursor: not-allowed; transition: all 0.3s ease;" disabled onclick="closeEmailModal()">
                    Verificar y Continuar <i class="fa-solid fa-unlock-keyhole" style="margin-left: 8px;"></i>
                </button>
            </div>

        </div>
    </div>
"""

content = re.sub(r'<!-- EMAIL VERIFICATION MODAL -->.*?</div>\s*</div>', new_modal_html, content, flags=re.DOTALL)


# 2. UPGRADE PLAN DE PAGO & DATOS PAGADOR
old_middle = r'<!-- PLAN DE PAGO SUMMARY -->.*?<!-- DATOS DEL PAGADOR -->.*?</label>\s*<div class="segment-highlight"></div>\s*</div>\s*</div>'

new_middle = """
                    <!-- PREMIUM SUMMARY DASHBOARD -->
                    <div class="dashboard-grid-main mb-5">
                        
                        <!-- Left Col: Plan de Pago -->
                        <div class="dashboard-card receipt-card">
                            <div class="dc-header">
                                <div class="dc-icon"><i class="fa-solid fa-file-invoice-dollar"></i></div>
                                <div class="dc-title">Plan de Pago</div>
                            </div>
                            
                            <div class="receipt-amount-big">
                                <span class="currency">UF</span> 38.70
                            </div>
                            
                            <div class="receipt-breakdown">
                                <div class="rb-row">
                                    <span class="rb-label">Modalidad</span>
                                    <span class="rb-value">1 Cuota</span>
                                </div>
                                <div class="rb-row">
                                    <span class="rb-label">Vigencia</span>
                                    <span class="rb-value">25 Días</span>
                                </div>
                                <div class="rb-divider"></div>
                                <div class="rb-row highlight">
                                    <span class="rb-label">Fecha de Cobro</span>
                                    <span class="rb-value">25-07-2026</span>
                                </div>
                            </div>
                        </div>

                        <!-- Right Col: Datos Pagador -->
                        <div class="dashboard-card payer-card">
                            <div class="dc-header">
                                <div class="dc-icon purple"><i class="fa-solid fa-user-check"></i></div>
                                <div class="dc-title">Datos del Pagador</div>
                            </div>
                            
                            <div class="payer-data-grid">
                                <div class="pd-item">
                                    <div class="pd-label">RUT</div>
                                    <div class="pd-value">10.042.595-5</div>
                                </div>
                                <div class="pd-item">
                                    <div class="pd-label">Nombre Completo</div>
                                    <div class="pd-value">Cristian Gonzalo Martinez Pardo</div>
                                </div>
                                <div class="pd-item">
                                    <div class="pd-label">Región</div>
                                    <div class="pd-value">De Los Ríos</div>
                                </div>
                                <div class="pd-item">
                                    <div class="pd-label">Comuna</div>
                                    <div class="pd-value">Valdivia</div>
                                </div>
                                <div class="pd-item full-width">
                                    <div class="pd-label">Dirección</div>
                                    <div class="pd-value">Martínez de Rozas 5523</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- MODERN TOGGLES -->
                    <div class="modern-toggle-box mb-4">
                        <div class="mtb-info">
                            <div class="mtb-icon"><i class="fa-solid fa-satellite-dish"></i></div>
                            <div class="mtb-text">
                                <div class="mtb-title">Requerimiento GPS</div>
                                <div class="mtb-desc">¿El vehículo requiere instalación de GPS?</div>
                            </div>
                        </div>
                        <div class="aurora-toggle-segment small-segment">
                            <input type="radio" name="gps" id="gps_yes" value="yes" checked>
                            <label for="gps_yes">Sí</label>
                            <input type="radio" name="gps" id="gps_no" value="no">
                            <label for="gps_no">No</label>
                            <div class="segment-highlight"></div>
                        </div>
                    </div>

                    <div class="modern-toggle-box highlight-box mb-5">
                        <div class="mtb-info">
                            <div class="mtb-icon teal"><i class="fa-solid fa-clipboard-check"></i></div>
                            <div class="mtb-text">
                                <div class="mtb-title">Confirmación de Datos</div>
                                <div class="mtb-desc">Confirmo que toda la información anterior es correcta.</div>
                            </div>
                        </div>
                        <div class="aurora-toggle-segment small-segment">
                            <input type="radio" name="datosCorrectos" id="dc_yes" value="yes" onchange="togglePACPATForm()">
                            <label for="dc_yes">Sí</label>
                            <input type="radio" name="datosCorrectos" id="dc_no" value="no" checked onchange="togglePACPATForm()">
                            <label for="dc_no">No</label>
                            <div class="segment-highlight"></div>
                        </div>
                    </div>
"""

content = re.sub(old_middle, new_middle, content, flags=re.DOTALL)


# 3. UPGRADE PAC/PAT TOGGLE AND FORM
old_pac_pat = r'<div class="payment-tabs-container mb-4">.*?</div>\s*<!-- PAC FORM -->'
new_pac_pat = """
                        <!-- APPLE STYLE SEGMENTED CONTROL -->
                        <div class="ios-segmented-control mb-4">
                            <button class="ios-segment active" id="tabPAC" onclick="switchPaymentTab('PAC')">
                                <i class="fa-solid fa-building-columns"></i> PAC (Cuenta)
                            </button>
                            <button class="ios-segment" id="tabPAT" onclick="switchPaymentTab('PAT')">
                                <i class="fa-regular fa-credit-card"></i> PAT (Tarjeta)
                            </button>
                            <div class="ios-segment-pill" id="iosPill"></div>
                        </div>

                        <!-- PAC FORM -->"""
content = re.sub(old_pac_pat, new_pac_pat, content, flags=re.DOTALL)

# Add logic for pill sliding
js_to_add = """
    function switchPaymentTab(type) {
        const tabPAC = document.getElementById('tabPAC');
        const tabPAT = document.getElementById('tabPAT');
        const formPAC = document.getElementById('formPAC');
        const formPAT = document.getElementById('formPAT');
        const pill = document.getElementById('iosPill');
        
        if (type === 'PAC') {
            tabPAC.classList.add('active');
            tabPAT.classList.remove('active');
            pill.style.transform = 'translateX(0)';
            
            formPAC.style.display = 'block';
            formPAT.style.display = 'none';
        } else {
            tabPAT.classList.add('active');
            tabPAC.classList.remove('active');
            pill.style.transform = 'translateX(100%)';
            
            formPAT.style.display = 'block';
            formPAC.style.display = 'none';
        }
    }
"""
content = re.sub(r'function switchPaymentTab.*?\}', js_to_add, content, flags=re.DOTALL)


with open("cotizacion/cotizacion-9-1.html", "w", encoding="utf-8") as f:
    f.write(content)


print("9-1 Premium HTML Updated!")
