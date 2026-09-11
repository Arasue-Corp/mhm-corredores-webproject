import re

with open('cotizacion/cotizacion-salud-resumen.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Grab header (up to <main class="summaryMain"> and <div class="summaryGrid">)
header_match = re.search(r'([\s\S]*?<main class="summaryMain">\s*<div class="summaryGrid">\s*)', content)
header = header_match.group(1)

# Grab footer
footer_match = re.search(r'(\s*</div\s*>\s*</main\s*>[\s\S]*)', content)
footer = footer_match.group(1)

body = """
            <!-- LEFT MAIN CONTENT -->
            <section class="summaryFlow">
                
                <!-- HEADER SECTION -->
                <div style="margin-bottom: 24px;">
                    <div class="healthKicker-badge" style="margin-bottom: 8px;">
                        <i class="fa-solid fa-paw"></i>
                        <span>Resumen de Cotización · Seguro de Mascotas</span>
                    </div>
                    <h1 style="font-size: clamp(24px, 3.2vw, 34px); font-weight: 900; color: #0F172A; letter-spacing: -0.03em; margin: 4px 0 8px;">
                        Verifica tus mascotas aseguradas.
                    </h1>
                    <p style="font-size: 14.5px; color: #475569; margin: 0;">
                        Revisa los planes seleccionados para cada una de tus mascotas antes de proceder al registro.
                    </p>
                </div>

                <!-- CARD 1: MASCOTAS COTIZADAS -->
                <div class="summaryCard">
                    <div class="summaryCardHead">
                        <div class="summaryCardKicker">
                            <i class="fa-solid fa-list-check"></i>
                            <span>Mascotas y Planes Seleccionados</span>
                        </div>
                        <a href="cotizacion-mascota-nueva-1.html" class="btnModifyQuote">
                            <i class="fa-solid fa-pen-to-square"></i>
                            <span>Modificar datos</span>
                        </a>
                    </div>

                    <div id="petsSummaryList" style="display: flex; flex-direction: column; gap: 15px;">
                        <!-- Dynamic content via JS -->
                    </div>
                </div>

                <!-- CARD 2: CONDICIONES -->
                <div class="summaryCard">
                    <div class="summaryCardHead">
                        <div class="summaryCardKicker">
                            <i class="fa-solid fa-scale-balanced"></i>
                            <span>Condiciones Generales</span>
                        </div>
                    </div>

                    <ul class="legalList">
                        <li class="legalListItem">
                            <div class="legalListItemIcon success"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <strong>Vigencia:</strong> La cobertura inicia inmediatamente después del pago para consultas de telemedicina.
                            </div>
                        </li>
                        <li class="legalListItem">
                            <div class="legalListItemIcon info"><i class="fa-solid fa-notes-medical"></i></div>
                            <div>
                                <strong>Reembolsos:</strong> Los reembolsos por atención veterinaria están sujetos a los topes establecidos en cada plan.
                            </div>
                        </li>
                    </ul>

                    <!-- ACCEPTANCE CHECKBOX -->
                    <label class="termsAcceptanceCard" id="termsAcceptanceCard" for="termsAccept">
                        <input type="checkbox" id="termsAccept" class="termsCheckboxInput" onchange="toggleAcceptance(this.checked)">
                        <div>
                            <strong>He leído y acepto las condiciones generales del seguro de mascotas</strong>
                            <p>
                                Declaro que la información de mis mascotas es verdadera y autorizo el tratamiento de mis datos para la emisión de la póliza.
                            </p>
                        </div>
                    </label>
                </div>
            </section>

            <!-- RIGHT STICKY CHECKOUT SIDEBAR -->
            <aside class="summaryCheckoutSidebar">
                <div class="mhmCheckoutDarkCard">
                    
                    <div class="checkoutCardLogoRow">
                        <div class="checkoutMapfrePill">
                            <img src="../assets/img/logo-mhm-color.png" alt="MHM Mascotas">
                        </div>
                        <span class="checkoutPlanTierBadge" id="planTierBadge">SEGURO MASCOTAS</span>
                    </div>

                    <h2 class="checkoutPlanTitle" id="planTitleHeader">Resumen de Contratación</h2>
                    
                    <div class="checkoutCapitalChip" id="planCapitalChip">
                        <i class="fa-solid fa-paw"></i>
                        <span id="totalPetsCount">0 mascotas aseguradas</span>
                    </div>

                    <div class="checkoutPriceDivider"></div>

                    <div class="checkoutPriceLine">
                        <span style="color: #94A3B8;">Intermediación</span>
                        <strong style="color: #FFFFFF;">MHM Corredores</strong>
                    </div>

                    <div class="checkoutPriceLine total">
                        <div>
                            <span style="display: block; font-size: 11px; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700;">Total Mensual</span>
                            <span style="font-size: 12px; color: #CBD5E1;">IVA incluido</span>
                        </div>
                        <strong id="planPriceMonth">$0</strong>
                    </div>

                    <!-- TRUST SEALS -->
                    <div class="checkoutTrustSeals">
                        <div class="checkoutTrustItem">
                            <i class="fa-solid fa-circle-check"></i>
                            <span>Corredor Registrado ante la CMF</span>
                        </div>
                        <div class="checkoutTrustItem">
                            <i class="fa-solid fa-lock"></i>
                            <span>Conexión Encriptada SSL de 256 bits</span>
                        </div>
                    </div>

                    <!-- ACTIONS -->
                    <div class="checkoutActions">
                        <button type="button" class="btnProceedContract is-disabled" id="btnContinue" onclick="proceedToContractorStep()" role="button" aria-disabled="true">
                            <i class="fa-solid fa-lock btnLockIcon"></i>
                            <span id="btnContinueText">Acepta las condiciones</span>
                            <i class="fa-solid fa-arrow-right btnArrowIcon"></i>
                        </button>
                    </div>

                </div>
            </aside>
"""

# Replace the JS scripts entirely inside the footer or script tag area
js_script = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            initCheckoutData();
        });

        const PLAN_PRICES = {
            'basico': 9490,
            'pro': 12490,
            'senior': 16490
        };

        const PLAN_NAMES = {
            'basico': 'Asistencia Mascota',
            'pro': 'Asistencia Mascota Pro',
            'senior': 'Asistencia Mascota Senior'
        };

        function initCheckoutData() {
            const dataStr = sessionStorage.getItem('mhm_mascotas_data');
            if (!dataStr) {
                window.location.href = 'cotizacion-mascota-nueva-1.html';
                return;
            }

            const petsData = JSON.parse(dataStr);
            const listEl = document.getElementById('petsSummaryList');
            
            let html = '';
            let totalMensual = 0;

            petsData.forEach(p => {
                const planName = PLAN_NAMES[p.plan] || 'Plan Desconocido';
                const planPrice = PLAN_PRICES[p.plan] || 0;
                totalMensual += planPrice;

                const icon = p.type === 'gato' ? '<i class="fa-solid fa-cat"></i>' : '<i class="fa-solid fa-dog"></i>';

                html += `
                    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 15px; display: flex; justify-content: space-between; align-items: center;">
                        <div style="display: flex; gap: 15px; align-items: center;">
                            <div style="width: 45px; height: 45px; border-radius: 50%; background: #EEF2FF; color: #796bfc; display: grid; place-items: center; font-size: 1.2rem;">
                                ${icon}
                            </div>
                            <div>
                                <strong style="display: block; color: #0F172A; font-size: 1.1rem;">${p.name || 'Mascota'}</strong>
                                <span style="font-size: 0.85rem; color: #64748B;">${p.breed || 'Raza'}, ${p.age} años</span>
                                <span style="display: block; margin-top: 4px; font-size: 0.85rem; font-weight: 700; color: #10B981;">Plan: ${planName}</span>
                            </div>
                        </div>
                        <div style="font-weight: 800; color: #0F172A; font-size: 1.1rem;">
                            $${planPrice.toLocaleString('es-CL')}
                        </div>
                    </div>
                `;
            });

            listEl.innerHTML = html;

            document.getElementById('totalPetsCount').innerText = `${petsData.length} mascota${petsData.length > 1 ? 's' : ''} asegurada${petsData.length > 1 ? 's' : ''}`;
            document.getElementById('planPriceMonth').innerText = `$${totalMensual.toLocaleString('es-CL')}`;
        }

        function toggleAcceptance(accepted) {
            const btn = document.getElementById('btnContinue');
            const textEl = document.getElementById('btnContinueText');
            if (!btn) return;
            if (accepted) {
                btn.classList.add('enabled');
                btn.classList.remove('is-disabled');
                btn.setAttribute('aria-disabled', 'false');
                if (textEl) textEl.innerText = 'Continuar al Registro de Contratante';
            } else {
                btn.classList.remove('enabled');
                btn.classList.add('is-disabled');
                btn.setAttribute('aria-disabled', 'true');
                if (textEl) textEl.innerText = 'Acepta las condiciones';
            }
        }

        function proceedToContractorStep() {
            const check = document.getElementById('termsAccept');
            if (!check || !check.checked) {
                const termsCard = document.getElementById('termsAcceptanceCard') || check;
                if (termsCard) {
                    const navHeight = 110;
                    const rect = termsCard.getBoundingClientRect();
                    const targetScrollY = window.pageYOffset + rect.top - navHeight;
                    window.scrollTo({ top: targetScrollY, behavior: 'smooth' });
                    termsCard.classList.remove('attention-pulse');
                    void termsCard.offsetWidth;
                    termsCard.classList.add('attention-pulse');
                    setTimeout(() => { check.focus(); }, 400);
                }
                return;
            }
            window.location.href = 'cotizacion-mascota-nueva-2.html';
        }

        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            if (!menu) return;
            const isOpen = menu.classList.toggle('is-open');
            document.body.style.overflow = isOpen ? 'hidden' : '';
        }
    </script>
</body>
</html>
"""

# Strip out the old script from footer and append our new one
footer = re.sub(r'<script>[\s\S]*?</body>', '', footer)

# Fix back link
header = header.replace('cotizacion-salud-1.html', 'cotizacion-mascota-nueva-1.html')
header = header.replace('Catálogo de Salud', 'Selección de Mascotas')
header = header.replace('<title>Resumen de Solicitud | MAPFRE AP Salud | MHM Corredores</title>', '<title>Resumen Mascotas | MHM Corredores</title>')

with open('cotizacion/cotizacion-mascota-nueva-resumen.html', 'w', encoding='utf-8') as f:
    f.write(header + body + footer + js_script)

print("Generated cotizacion-mascota-nueva-resumen.html")
