import re

with open('cotizacion/cotizacion-mascota-4.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div class="page-wrapper">')
if start_idx == -1:
    print("Could not find page-wrapper in step 4")
    exit(1)

script_idx = content.find('<script>', start_idx)

head_content = content[:start_idx]
footer_content = content[script_idx:]

new_html = """
    <div class="page-wrapper">

        <div class="wizard-container">
            <div class="wizard-top">
                <div class="wizard-title" style="color: #10B981;"><i class="fa-solid fa-circle-check"></i>¡Todo Listo!</div>
                <div class="wizard-title"><i class="fa-solid fa-flag-checkered"></i></div>
            </div>
            <div class="progress-track"><div class="progress-fill" style="width: 100%; background: #10B981;"></div></div>
            <div class="header-split"></div>
            <header class="brand-page-header">
                <div class="title-group">
                    <h1 style="color: #0F172A; font-weight: 900; font-size: 2.2rem; letter-spacing: -0.5px;">¡TU ASISTENCIA YA ESTÁ ACTIVA!</h1>
                    <div class="aurora-line" style="background: #10B981;"></div> 
                </div>
                <p>Tu mascota ahora cuenta con la mejor protección. Revisa los detalles a continuación.</p>
            </header>
        </div>

        <div class="specs-layout-grid">
            <div class="main-spec-col">
                
                <style>
                    .harmonic-card { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); overflow: hidden; }
                    .harmonic-header { background: #F8FAFC; padding: 15px 20px; border-bottom: 1px solid #E2E8F0; font-weight: 800; color: #104C5C; font-size: 1.1rem; display: flex; align-items: center; gap: 10px; }
                    .harmonic-body { padding: 20px; display: flex; flex-direction: column; gap: 15px; }
                    .detail-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 15px; background: #F1F5F9; border-radius: 8px; font-size: 0.95rem; }
                    .detail-row strong { color: #104C5C; font-weight: 800; display: flex; align-items: center; gap: 8px; }
                    .detail-row span { color: #475569; font-weight: 600; }
                    
                    .action-link { display: flex; align-items: center; justify-content: space-between; padding: 15px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; text-decoration: none; color: #1E293B; font-weight: 700; transition: all 0.2s; }
                    .action-link:hover { border-color: #2ED9C3; background: #FFFFFF; box-shadow: 0 4px 10px rgba(46, 217, 195, 0.1); transform: translateY(-2px); }
                    .action-link i { color: #2ED9C3; font-size: 1.2rem; }
                    
                    .cross-sell-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 10px; }
                    .cross-sell-card { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px 10px; text-align: center; cursor: pointer; transition: all 0.3s; text-decoration: none; display: block; }
                    .cross-sell-card:hover { border-color: #104C5C; transform: translateY(-4px); box-shadow: 0 10px 20px rgba(16, 76, 92, 0.08); }
                    .cross-sell-icon { width: 50px; height: 50px; border-radius: 50%; background: #F1F5F9; color: #104C5C; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin: 0 auto 15px; }
                    .cross-sell-card:hover .cross-sell-icon { background: #104C5C; color: white; }
                    
                    @media (max-width: 600px) {
                        .cross-sell-grid { grid-template-columns: 1fr; }
                        .detail-row { flex-direction: column; align-items: flex-start; gap: 5px; }
                    }
                </style>
                
                <!-- Confetti animation layer -->
                <div class="success-graphic" style="margin: 20px auto 40px;">
                    <div class="success-bg"></div>
                    <i class="fa-solid fa-check success-icon"></i>
                </div>

                <div class="harmonic-card">
                    <div class="harmonic-header">
                        <i class="fa-solid fa-file-invoice"></i> Detalle de contratación
                    </div>
                    <div class="harmonic-body">
                        <div class="detail-row">
                            <strong><i class="fa-solid fa-file-contract" style="color: #64748B;"></i> Nº de contrato:</strong>
                            <span id="contractNumber">1234567</span>
                        </div>
                        <div class="detail-row">
                            <strong><i class="fa-solid fa-calendar-check" style="color: #64748B;"></i> Fecha de activación:</strong>
                            <span id="activationDate">Cargando...</span>
                        </div>
                        <div class="detail-row">
                            <strong><i class="fa-solid fa-credit-card" style="color: #64748B;"></i> Medio de pago:</strong>
                            <span>Débito terminada en *****4539</span>
                        </div>
                        <div class="detail-row" style="background: #ECFDF5; border: 1px solid #A7F3D0;">
                            <strong style="color: #065F46;"><i class="fa-solid fa-sack-dollar" style="color: #10B981;"></i> Total mensual:</strong>
                            <span id="totalMonthly" style="color: #065F46; font-size: 1.1rem; font-weight: 800;">Cargando...</span>
                        </div>
                    </div>
                </div>

                <div class="harmonic-card">
                    <div class="harmonic-header">
                        <i class="fa-solid fa-layer-group"></i> Acciones disponibles
                    </div>
                    <div class="harmonic-body">
                        <a href="#" class="action-link">
                            <div style="display: flex; flex-direction: column; gap: 4px;">
                                <span>Descargar copia del contrato</span>
                                <span style="font-size: 0.8rem; color: #64748B; font-weight: 500;">O revisa tu correo <span id="ownerEmail" style="color: #104C5C; font-weight: 700;"></span></span>
                            </div>
                            <i class="fa-solid fa-download"></i>
                        </a>
                        
                        <a href="#" class="action-link">
                            <div style="display: flex; flex-direction: column; gap: 4px;">
                                <span>Ver detalle legal de asistencia</span>
                                <span style="font-size: 0.8rem; color: #64748B; font-weight: 500;">Términos, condiciones y exclusiones</span>
                            </div>
                            <i class="fa-solid fa-scale-balanced"></i>
                        </a>
                        <p style="font-size: 0.8rem; color: #94A3B8; text-align: center; margin: 0;">*Los documentos pueden tardar hasta 24 hrs en estar disponibles.</p>
                    </div>
                </div>

                <div class="harmonic-card" style="border-color: #2ED9C3; background: #FAFAFA;">
                    <div class="harmonic-header" style="background: #2ED9C3; color: white; border: none; justify-content: center; font-size: 1.2rem;">
                        CUIDAR LO QUE QUIERES NO TERMINA AQUÍ <i class="fa-solid fa-heart"></i>
                    </div>
                    <div class="harmonic-body" style="padding: 25px 20px;">
                        <p style="color: #475569; text-align: center; font-weight: 600; margin-bottom: 5px;">Descubre otras asistencias para tu día a día:</p>
                        
                        <div class="cross-sell-grid">
                            <a href="../cotizacion-hogar/index.html" class="cross-sell-card">
                                <div class="cross-sell-icon"><i class="fa-solid fa-house"></i></div>
                                <div style="color: #104C5C; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">Hogar</div>
                                <div style="color: #64748B; font-size: 0.8rem; font-weight: 600;">Desde <strong style="color: #2ED9C3; font-size: 1rem;">$7.990</strong></div>
                            </a>
                            
                            <a href="../funnel-auto/index.html" class="cross-sell-card">
                                <div class="cross-sell-icon"><i class="fa-solid fa-car-side"></i></div>
                                <div style="color: #104C5C; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">Movilidad</div>
                                <div style="color: #64748B; font-size: 0.8rem; font-weight: 600;">Desde <strong style="color: #2ED9C3; font-size: 1rem;">$3.200</strong></div>
                            </a>
                            
                            <a href="../seguro-complementario-salud/index.html" class="cross-sell-card">
                                <div class="cross-sell-icon"><i class="fa-solid fa-hand-holding-medical"></i></div>
                                <div style="color: #104C5C; font-weight: 900; text-transform: uppercase; margin-bottom: 4px;">Salud</div>
                                <div style="color: #64748B; font-size: 0.8rem; font-weight: 600;">Desde <strong style="color: #2ED9C3; font-size: 1rem;">$3.780</strong></div>
                            </a>
                        </div>
                    </div>
                </div>

                <a href="../index.html" class="btn-aurora-gradient" style="display: flex; margin: 30px auto; width: max-content; padding: 15px 40px;">
                    <span>Volver al Inicio</span>
                    <i class="fa-solid fa-arrow-right-long btn-icon-anim"></i>
                </a>

            </div>
        </div>
    </div>
"""

with open('cotizacion/cotizacion-mascota-5.html', 'w', encoding='utf-8') as f:
    f.write(head_content + new_html + footer_content)

print("Created beautiful step 5")
