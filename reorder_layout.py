import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# We'll completely replace the contents of specs-layout-grid
new_layout = """<div class="main-spec-col" style="grid-column: 1 / -1;">
                <div class="premium-white-card" id="quoteFormStep1" style="padding: 40px;">
                    
<form id="startForm" onsubmit="event.preventDefault();">
    <style>
        .specs-layout-grid { display: block !important; }
        
        .veh-type-grid {
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
            gap: 25px; 
            margin-bottom: 40px;
        }
        .veh-type-card {
            border: 1px solid #E2E8F0; border-radius: 20px; padding: 25px;
            display: flex; flex-direction: column; align-items: center; text-align: center; gap: 15px;
            background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(10px);
            position: relative; overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.02);
            transition: all 0.3s ease;
        }
        .veh-type-card:hover { 
            border-color: #2ED9C3; transform: translateY(-5px); 
            box-shadow: 0 15px 35px rgba(46, 217, 195, 0.15); 
            background: white;
        }
        
        .vt-image {
            width: 100%; height: 180px; border-radius: 16px;
            overflow: hidden; margin-bottom: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        .vt-image img {
            width: 100%; height: 100%; object-fit: cover;
            transition: transform 0.5s ease;
        }
        .veh-type-card:hover .vt-image img { transform: scale(1.05); }
        
        .vt-info { width: 100%; }
        .vt-info h4 { margin: 0 0 6px 0; color: #0F172A; font-size: 1.4rem; font-weight: 800; letter-spacing: -0.5px; }
        
        .pet-feature-list {
            list-style: none; padding: 0; margin: 15px 0 0 0; font-size: 0.9rem; color: #64748B;
            text-align: left;
        }
        .pet-feature-list li { margin-bottom: 8px; display: flex; align-items: flex-start; gap: 8px; }
        .pet-feature-list li i { color: #2ED9C3; font-size: 0.9rem; margin-top: 3px; }
        .pro-card .pet-feature-list li i { color: #2563EB; }
        
        .plan-price { font-size: 1.2rem; font-weight: 800; color: #0F172A; margin-top: 5px; }
        .pro-card .plan-price { color: #2563EB; }
        
        /* Quantity Controls */
        .qty-controls {
            display: flex;
            align-items: center;
            justify-content: center;
            background: #F1F5F9;
            border-radius: 12px;
            overflow: hidden;
            margin-top: 20px;
            width: 100%;
        }
        .qty-btn {
            background: transparent; border: none; color: #475569;
            width: 45px; height: 45px; display: flex; justify-content: center; align-items: center;
            cursor: pointer; transition: all 0.2s; font-size: 1.1rem;
        }
        .qty-btn:hover { background: #E2E8F0; color: #0F172A; }
        .qty-value { width: 50px; text-align: center; font-weight: 700; color: #0F172A; font-size: 1.1rem; }
    </style>

    <div class="veh-type-grid">
        <div class="veh-type-card">
            <div class="vt-image"><img src="../assets/img/seguro-auto.jpg" alt="Mascota Basico" id="img-basico"></div>
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
            <div class="vt-image"><img src="../assets/img/seguro-salud.jpg" alt="Mascota Pro" id="img-pro"></div>
            <div class="vt-info">
                <h4 style="color: #2563EB;">Asistencia Mascota Pro <br><span style="font-size: 0.6em; background: #2563EB; color: white; padding: 4px 8px; border-radius: 6px; vertical-align: middle; display: inline-block; margin-top: 5px;">Recomendado</span></h4>
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
            <div class="vt-image"><img src="../assets/img/seguro-pymes.jpg" alt="Mascota Senior" id="img-senior"></div>
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
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 40px;" class="bottom-section-grid">
        <style>
            @media (max-width: 768px) {
                .bottom-section-grid { grid-template-columns: 1fr !important; }
            }
        </style>
        
        <div class="cart-summary-container">
            <div class="sidebar-title text-gradient-corp" style="font-size: 1.4rem; font-weight: 800; margin-bottom: 20px;">
                Resumen de Selección
            </div>
            <div id="cart-summary" style="background: white; border-radius: 16px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); border: 1px solid #E2E8F0;">
                <!-- JS injected -->
            </div>
            
            <div class="legal-checks" style="margin-top: 25px; padding: 20px; background: rgba(248,250,252,0.8); border-radius: 16px; border: 1px solid #E2E8F0;">
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
        </div>
        
        <div class="why-mhm-container">
            <div class="sidebar-title text-gradient-corp" style="font-size: 1.4rem; font-weight: 800; margin-bottom: 20px;">
                ¿Por qué cotizar con MHM?
            </div>
            <div class="mhm-premium-features" style="display: flex; flex-direction: column; gap: 16px;">
                <div class="mhm-feature-card" style="padding: 18px; border-radius: 16px; background: white; border: 1px solid #E2E8F0; display: flex; gap: 16px; align-items: center; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);">
                    <div class="mhm-feature-icon" style="width: 48px; height: 48px; border-radius: 12px; background: rgba(16, 185, 129, 0.1); color: #10B981; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0;"><i class="fa-solid fa-shield-halved"></i></div>
                    <div class="mhm-feature-content">
                        <h4 style="margin: 0 0 4px 0; font-size: 1.05rem; color: #0F172A; font-weight: 800;">Seguridad y Confianza</h4>
                        <p style="margin: 0; font-size: 0.9rem; color: #64748B;">Trabajamos con las aseguradoras más prestigiosas de Chile.</p>
                    </div>
                </div>
                
                <div class="mhm-feature-card" style="padding: 18px; border-radius: 16px; background: white; border: 1px solid #E2E8F0; display: flex; gap: 16px; align-items: center; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);">
                    <div class="mhm-feature-icon" style="width: 48px; height: 48px; border-radius: 12px; background: rgba(16, 185, 129, 0.1); color: #10B981; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0;"><i class="fa-solid fa-headset"></i></div>
                    <div class="mhm-feature-content">
                        <h4 style="margin: 0 0 4px 0; font-size: 1.05rem; color: #0F172A; font-weight: 800;">Asesoría 360°</h4>
                        <p style="margin: 0; font-size: 0.9rem; color: #64748B;">Acompañamiento experto en la elección y gestión 24/7.</p>
                    </div>
                </div>
                
                <div class="mhm-feature-card" style="padding: 18px; border-radius: 16px; background: white; border: 1px solid #E2E8F0; display: flex; gap: 16px; align-items: center; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);">
                    <div class="mhm-feature-icon" style="width: 48px; height: 48px; border-radius: 12px; background: rgba(16, 185, 129, 0.1); color: #10B981; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0;"><i class="fa-solid fa-bolt"></i></div>
                    <div class="mhm-feature-content">
                        <h4 style="margin: 0 0 4px 0; font-size: 1.05rem; color: #0F172A; font-weight: 800;">Eficiencia Digital</h4>
                        <p style="margin: 0; font-size: 0.9rem; color: #64748B;">Proceso 100% online, ultra rápido y sin papeleos.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
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
                html += `<div style="display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 1.05rem; color: #334155;">
                    <span><i class="fa-solid fa-paw" style="color: #CBD5E1; margin-right: 8px;"></i> ${plans[id].name} <strong style="color: #0F172A;">x ${plans[id].qty}</strong></span>
                    <strong style="color: #0F172A;">$${subtotal.toLocaleString('es-CL')}</strong>
                </div>`;
            }
        }

        if(itemsCount === 0) {
            html = '<div style="color: #94A3B8; font-size: 1rem; text-align: center; padding: 20px 0;"><i class="fa-solid fa-basket-shopping" style="font-size: 2.5rem; margin-bottom: 15px; opacity: 0.3;"></i><br>Aún no has seleccionado ningún plan.</div>';
        } else {
            html += `<div style="border-top: 2px dashed #E2E8F0; margin-top: 15px; padding-top: 20px; display: flex; justify-content: space-between; font-size: 1.3rem; color: #0F172A;">
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
            btn.style.transform = 'translateY(0)';
        }
    }

    function goToNextStep() {
        sessionStorage.setItem('mhmPetCart', JSON.stringify(plans));
        
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.3s ease';
        setTimeout(() => {
            window.location.href = 'cotizacion-mascota-2.html';
        }, 300);
    }
    
    document.addEventListener('DOMContentLoaded', () => {
        renderSummary();
    });
</script>

                </div>
            </div>"""

pattern = re.compile(r'<div class="main-spec-col">.*?</aside>', re.DOTALL)
c = pattern.sub(new_layout.strip(), c, count=1)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Reordered layout successfully!")
