import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

new_main_content = """<div class="main-spec-col">
                <div class="premium-white-card" id="quoteFormStep1">
                    
<form id="startForm" onsubmit="event.preventDefault();">
    <style>
        .veh-type-grid {
            display: grid; grid-template-columns: 1fr; gap: 15px; margin-bottom: 30px;
        }
        .veh-type-card {
            border: 1px solid #E2E8F0; border-radius: 20px; padding: 25px;
            display: flex; align-items: center; gap: 25px;
            background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(10px);
            position: relative; overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.02);
            transition: all 0.3s ease;
        }
        .veh-type-card:hover { 
            border-color: #2ED9C3; transform: translateY(-3px); 
            box-shadow: 0 10px 25px rgba(46, 217, 195, 0.1); 
            background: white;
        }
        
        .vt-icon {
            width: 65px; height: 65px; border-radius: 16px;
            background: linear-gradient(135deg, #F8FAFC, #E2E8F0);
            color: #2ED9C3; font-size: 2rem;
            display: flex; justify-content: center; align-items: center;
            flex-shrink: 0; box-shadow: inset 0 2px 4px white, 0 4px 10px rgba(0,0,0,0.05);
            transition: 0.4s; position: relative; z-index: 2;
        }
        
        .vt-info { position: relative; z-index: 2; width: 100%; }
        .vt-info h4 { margin: 0 0 6px 0; color: #0F172A; font-size: 1.25rem; font-weight: 800; letter-spacing: -0.5px; }
        .vt-info p { margin: 0; font-size: 0.9rem; color: #64748B; font-weight: 500; }
        
        .pet-feature-list {
            list-style: none; padding: 0; margin: 10px 0 0 0; font-size: 0.85rem; color: #64748B;
        }
        .pet-feature-list li { margin-bottom: 5px; display: flex; align-items: center; gap: 6px; }
        .pet-feature-list li i { color: #2ED9C3; font-size: 0.8rem; }
        .pro-card .pet-feature-list li i { color: #2563EB; }
        
        .plan-price { font-size: 1.1rem; font-weight: 800; color: #0F172A; margin-top: 10px; }
        .pro-card .plan-price { color: #2563EB; }
        
        /* Quantity Controls */
        .qty-controls {
            display: flex;
            align-items: center;
            background: #F1F5F9;
            border-radius: 12px;
            overflow: hidden;
            margin-top: 15px;
            width: fit-content;
        }
        .qty-btn {
            background: transparent;
            border: none;
            color: #475569;
            width: 36px;
            height: 36px;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            transition: all 0.2s;
        }
        .qty-btn:hover { background: #E2E8F0; color: #0F172A; }
        .qty-value {
            width: 40px;
            text-align: center;
            font-weight: 700;
            color: #0F172A;
            font-size: 1rem;
        }
    </style>

    <div class="veh-type-grid">
        <div class="veh-type-card">
            <div class="vt-icon"><i class="fa-solid fa-dog"></i></div>
            <div class="vt-info">
                <h4>Asistencia Mascota</h4>
                <div class="plan-price">$5.555 / mes</div>
                <ul class="pet-feature-list">
                    <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                    <li><i class="fa-solid fa-check"></i> Asistencia 24/7</li>
                    <li><i class="fa-solid fa-check"></i> Ingreso: 0 hasta 9 años con 365 días</li>
                    <li><i class="fa-solid fa-check"></i> Descuento en farmacia y beneficios</li>
                    <li><i class="fa-solid fa-check"></i> Libre elección en todo Chile</li>
                </ul>
                <div class="qty-controls">
                    <button type="button" class="qty-btn" onclick="updateQty('basico', -1)"><i class="fa-solid fa-minus"></i></button>
                    <span class="qty-value" id="qty-basico">0</span>
                    <button type="button" class="qty-btn" onclick="updateQty('basico', 1)"><i class="fa-solid fa-plus"></i></button>
                </div>
            </div>
        </div>

        <div class="veh-type-card pro-card" style="border-color: #2563EB; background: rgba(37, 99, 235, 0.03);">
            <div class="vt-icon" style="background: #2563EB; color: white;"><i class="fa-solid fa-shield-dog"></i></div>
            <div class="vt-info">
                <h4 style="color: #2563EB;">Asistencia Mascota Pro <span style="font-size: 0.7em; background: #2563EB; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;">Recomendado</span></h4>
                <div class="plan-price">$5.555 / mes</div>
                <ul class="pet-feature-list">
                    <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                    <li><i class="fa-solid fa-check"></i> Asistencia 24/7</li>
                    <li><i class="fa-solid fa-check"></i> Ingreso: 0 hasta 9 años con 365 días</li>
                    <li><i class="fa-solid fa-check"></i> Descuento, mayor cobertura y beneficios</li>
                    <li><i class="fa-solid fa-check"></i> Libre elección en todo Chile</li>
                </ul>
                <div class="qty-controls">
                    <button type="button" class="qty-btn" onclick="updateQty('pro', -1)"><i class="fa-solid fa-minus"></i></button>
                    <span class="qty-value" id="qty-pro">0</span>
                    <button type="button" class="qty-btn" onclick="updateQty('pro', 1)"><i class="fa-solid fa-plus"></i></button>
                </div>
            </div>
        </div>

        <div class="veh-type-card">
            <div class="vt-icon"><i class="fa-solid fa-bone"></i></div>
            <div class="vt-info">
                <h4>Asistencia Senior</h4>
                <div class="plan-price">$5.555 / mes</div>
                <ul class="pet-feature-list">
                    <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                    <li><i class="fa-solid fa-check"></i> Asistencia 24/7</li>
                    <li><i class="fa-solid fa-check"></i> Ingreso: 7 hasta 13 años con 365 días</li>
                    <li><i class="fa-solid fa-check"></i> Exámenes, mayor cobertura</li>
                    <li><i class="fa-solid fa-check"></i> Descuento en farmacia y beneficios</li>
                </ul>
                <div class="qty-controls">
                    <button type="button" class="qty-btn" onclick="updateQty('senior', -1)"><i class="fa-solid fa-minus"></i></button>
                    <span class="qty-value" id="qty-senior">0</span>
                    <button type="button" class="qty-btn" onclick="updateQty('senior', 1)"><i class="fa-solid fa-plus"></i></button>
                </div>
            </div>
        </div>
    </div>
    
    <div class="legal-checks" style="margin-top: 30px; padding: 25px; background: rgba(255,255,255,0.7); border-radius: 16px; border: 1px solid #E2E8F0;">
        <label class="custom-checkbox-row" style="display: flex; align-items: center; gap: 12px; cursor: pointer; margin-bottom: 15px;">
            <input type="checkbox" id="chk-terms" onchange="validateForm()" style="width: 20px; height: 20px; accent-color: #2ED9C3;">
            <span style="font-size: 0.95rem; color: #334155;">He leído y acepto los <a href="../terminos-condiciones/index.html" target="_blank" style="color: #2563EB; font-weight: 600; text-decoration: underline;">Términos y condiciones</a>.</span>
        </label>
        <label class="custom-checkbox-row" style="display: flex; align-items: center; gap: 12px; cursor: pointer;">
            <input type="checkbox" id="chk-legal" onchange="validateForm()" style="width: 20px; height: 20px; accent-color: #2ED9C3;">
            <span style="font-size: 0.95rem; color: #334155;">Comprendo y acepto el <a href="../politica-privacidad/index.html" target="_blank" style="color: #2563EB; font-weight: 600; text-decoration: underline;">Detalle legal de servicio</a>.</span>
        </label>
    </div>

    <button type="button" id="btn-continue" class="btn-primary-shimmer" style="margin-top: 25px; width: 100%; opacity: 0.5; pointer-events: none;" onclick="goToNextStep()">
        Continuar a Siguiente Paso <i class="fa-solid fa-arrow-right"></i>
    </button>
    
</form>

<script>
    const plans = {
        'basico': { name: 'Asistencia Mascota', price: 5555, qty: 0 },
        'pro': { name: 'Asistencia Mascota Pro', price: 5555, qty: 0 },
        'senior': { name: 'Asistencia Senior', price: 5555, qty: 0 }
    };

    function updateQty(id, delta) {
        plans[id].qty += delta;
        if(plans[id].qty < 0) plans[id].qty = 0;
        
        // Max limit to prevent absurd numbers? Let's say 10
        if(plans[id].qty > 10) plans[id].qty = 10;
        
        document.getElementById('qty-' + id).innerText = plans[id].qty;
        
        renderSummary();
        validateForm();
    }

    function renderSummary() {
        const summaryDiv = document.getElementById('cart-summary');
        if(!summaryDiv) return;
        
        let html = '';
        let total = 0;
        let itemsCount = 0;

        for(let id in plans) {
            if(plans[id].qty > 0) {
                itemsCount += plans[id].qty;
                const subtotal = plans[id].qty * plans[id].price;
                total += subtotal;
                html += `<div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 0.95rem; color: #334155;">
                    <span><i class="fa-solid fa-paw" style="color: #CBD5E1; margin-right: 8px;"></i> ${plans[id].name} <strong style="color: #0F172A;">x ${plans[id].qty}</strong></span>
                    <strong style="color: #0F172A;">$${subtotal.toLocaleString('es-CL')}</strong>
                </div>`;
            }
        }

        if(itemsCount === 0) {
            html = '<div style="color: #94A3B8; font-size: 0.9rem; text-align: center; padding: 20px 0;"><i class="fa-solid fa-basket-shopping" style="font-size: 2rem; margin-bottom: 10px; opacity: 0.5;"></i><br>Aún no has seleccionado ningún plan.</div>';
        } else {
            html += `<div style="border-top: 2px dashed #E2E8F0; margin-top: 15px; padding-top: 15px; display: flex; justify-content: space-between; font-size: 1.2rem; color: #0F172A;">
                <strong>Total Estimado:</strong>
                <strong style="color: #2ED9C3;">$${total.toLocaleString('es-CL')}</strong>
            </div>`;
        }
        summaryDiv.innerHTML = html;
    }

    function validateForm() {
        const chkTerms = document.getElementById('chk-terms').checked;
        const chkLegal = document.getElementById('chk-legal').checked;
        const btn = document.getElementById('btn-continue');
        
        let hasItems = false;
        for(let id in plans) {
            if(plans[id].qty > 0) hasItems = true;
        }

        if(chkTerms && chkLegal && hasItems) {
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
            btn.style.transform = 'translateY(0)';
        } else {
            btn.style.opacity = '0.5';
            btn.style.pointerEvents = 'none';
            btn.style.transform = 'translateY(0)'; // reset any hover effect
        }
    }

    function goToNextStep() {
        // Save state to sessionStorage so it can be passed to following steps
        sessionStorage.setItem('mhmPetCart', JSON.stringify(plans));
        
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.3s ease';
        setTimeout(() => {
            window.location.href = 'cotizacion-mascota-2.html';
        }, 300);
    }
    
    // Initialize empty summary
    document.addEventListener('DOMContentLoaded', () => {
        renderSummary();
    });
</script>

                </div>
            </div>

            <aside class="config-sidebar anim-entry delay-2">
                <div class="organic-panel">
                    
                    <div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px;">
                        Resumen de Selección
                    </div>
                    
                    <div id="cart-summary" style="margin-bottom: 40px; background: white; border-radius: 16px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); border: 1px solid #F1F5F9;">
                        <!-- JS injected -->
                    </div>

                    <style>
                    /* Premium Feature Cards */
                    .mhm-premium-features {
                        display: flex;
                        flex-direction: column;
                        gap: 16px;
                        margin-top: 15px;
                    }

                    .mhm-feature-card {
                        position: relative;
                        padding: 18px 16px;
                        border-radius: 16px;
                        background: linear-gradient(145deg, rgba(255,255,255,1) 0%, rgba(248,250,252,0.6) 100%);
                        border: 1px solid rgba(226, 232, 240, 0.8);
                        display: flex;
                        gap: 16px;
                        align-items: flex-start;
                        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                        overflow: hidden;
                        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
                        cursor: default;
                    }

                    .mhm-feature-card:hover {
                        transform: translateY(-4px) scale(1.02);
                        border-color: rgba(45, 212, 191, 0.4);
                        box-shadow: 0 12px 25px rgba(45, 212, 191, 0.15);
                        background: linear-gradient(145deg, rgba(255,255,255,1) 0%, rgba(240,253,250,0.9) 100%);
                    }

                    .mhm-feature-icon {
                        width: 44px;
                        height: 44px;
                        border-radius: 12px;
                        background: linear-gradient(135deg, rgba(45, 212, 191, 0.15) 0%, rgba(16, 185, 129, 0.05) 100%);
                        color: var(--brand-green, #10B981);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 1.25rem;
                        flex-shrink: 0;
                        position: relative;
                        z-index: 2;
                        transition: all 0.4s ease;
                        border: 1px solid rgba(45, 212, 191, 0.2);
                    }

                    .mhm-feature-card:hover .mhm-feature-icon {
                        background: linear-gradient(135deg, var(--brand-green, #10B981) 0%, #059669 100%);
                        color: #ffffff;
                        box-shadow: 0 6px 15px rgba(16, 185, 129, 0.35);
                        transform: rotate(-8deg) scale(1.1);
                        border-color: transparent;
                    }

                    .mhm-feature-content {
                        position: relative;
                        z-index: 2;
                        padding-top: 2px;
                    }

                    .mhm-feature-title {
                        margin: 0 0 5px 0;
                        font-size: 1rem;
                        color: #0F172A;
                        font-weight: 800;
                        letter-spacing: -0.3px;
                        transition: color 0.3s ease;
                    }

                    .mhm-feature-card:hover .mhm-feature-title {
                        color: var(--brand-green, #10B981);
                    }

                    .mhm-feature-desc {
                        margin: 0;
                        font-size: 0.85rem;
                        color: #64748B;
                        line-height: 1.45;
                        font-weight: 500;
                    }
                    </style>

                    <div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px;">
                        ¿Por qué cotizar con MHM?
                    </div>

                    <div class="mhm-premium-features">
                        <div class="mhm-feature-card">
                            <div class="mhm-feature-icon"><i class="fa-solid fa-shield-halved"></i></div>
                            <div class="mhm-feature-content">
                                <h4 class="mhm-feature-title">Seguridad y Confianza</h4>
                                <p class="mhm-feature-desc">Trabajamos con las aseguradoras más prestigiosas y sólidas de Chile.</p>
                            </div>
                        </div>
                        
                        <div class="mhm-feature-card">
                            <div class="mhm-feature-icon"><i class="fa-solid fa-headset"></i></div>
                            <div class="mhm-feature-content">
                                <h4 class="mhm-feature-title">Asesoría 360°</h4>
                                <p class="mhm-feature-desc">Acompañamiento experto en la elección y gestión 24/7 de siniestros.</p>
                            </div>
                        </div>
                        
                        <div class="mhm-feature-card">
                            <div class="mhm-feature-icon"><i class="fa-solid fa-bolt"></i></div>
                            <div class="mhm-feature-content">
                                <h4 class="mhm-feature-title">Eficiencia Digital</h4>
                                <p class="mhm-feature-desc">Proceso 100% online, ultra rápido y sin papeleos innecesarios.</p>
                            </div>
                        </div>
                    </div>

                </div>
            </aside>"""

pattern = re.compile(r'<div class="main-spec-col">.*?</aside>', re.DOTALL)
c = pattern.sub(new_main_content.strip(), c, count=1)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Shopping cart integrated successfully!")
