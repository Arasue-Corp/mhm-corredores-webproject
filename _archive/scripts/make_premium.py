import re

with open('cotizacion/cotizacion-escolar-5.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = '<style>\n            .final-summary-container {'
end_tag = '</div>\n        </div>\n</div>\n        \n        <div class="aurora-border-glow"></div>'
start_idx = content.find(start_tag)
end_idx = content.find('<div class="aurora-border-glow"></div>')

if start_idx != -1 and end_idx != -1:
    new_html = """
        <style>
            /* Premium Base & Animations */
            .final-summary-container {
                max-width: 950px;
                margin: 0 auto 80px;
                padding: 0 20px;
                font-family: 'Inter', sans-serif;
                position: relative;
                z-index: 10;
            }
            
            @keyframes floatSmooth {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            @keyframes glowPulse {
                0%, 100% { box-shadow: 0 0 20px rgba(46, 217, 195, 0.2); }
                50% { box-shadow: 0 0 40px rgba(46, 217, 195, 0.6); }
            }

            /* Premium Glassmorphism Contract Card */
            .contract-premium-card {
                position: relative;
                margin-bottom: 70px;
                padding: 50px;
                background: rgba(255, 255, 255, 0.85);
                backdrop-filter: blur(20px);
                border-radius: 30px;
                box-shadow: 0 25px 60px rgba(16, 76, 92, 0.08), 
                            inset 0 0 0 1px rgba(255, 255, 255, 0.5);
                overflow: hidden;
            }
            .contract-premium-card::before {
                content: '';
                position: absolute;
                top: 0; left: 0; right: 0; height: 6px;
                background: linear-gradient(90deg, #104C5C, #2ED9C3, #104C5C);
                background-size: 200% 100%;
                animation: gradientMove 3s ease infinite;
            }
            @keyframes gradientMove {
                0% { background-position: 100% 0; }
                100% { background-position: -100% 0; }
            }
            
            /* Background Decoration inside card */
            .card-bg-deco {
                position: absolute;
                top: -50px; right: -50px;
                width: 250px; height: 250px;
                background: radial-gradient(circle, rgba(46, 217, 195, 0.15) 0%, transparent 70%);
                border-radius: 50%;
                z-index: 0;
                pointer-events: none;
            }

            .contract-content {
                position: relative;
                z-index: 2;
                display: flex;
                flex-direction: column;
                gap: 40px;
            }

            .premium-section-title {
                color: #104C5C;
                font-family: 'Poppins', sans-serif;
                font-weight: 800;
                font-size: 1.3rem;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 12px;
                letter-spacing: -0.5px;
            }
            .premium-section-title i {
                color: #2ED9C3;
                font-size: 1.5rem;
            }

            /* Detail Rows */
            .detail-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
            }
            .detail-item {
                background: #F8FAFC;
                padding: 20px;
                border-radius: 16px;
                border: 1px solid rgba(16, 76, 92, 0.05);
                transition: transform 0.3s, box-shadow 0.3s;
            }
            .detail-item:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 25px rgba(16, 76, 92, 0.06);
                border-color: rgba(46, 217, 195, 0.3);
            }
            .detail-label {
                color: #64748B;
                font-size: 0.85rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 1px;
                margin-bottom: 5px;
                display: block;
            }
            .detail-value {
                color: #104C5C;
                font-size: 1.2rem;
                font-weight: 800;
            }

            /* Action Buttons */
            .action-buttons-flex {
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
            }
            .premium-btn {
                display: inline-flex;
                align-items: center;
                gap: 12px;
                padding: 16px 28px;
                border-radius: 14px;
                font-weight: 700;
                font-size: 1.05rem;
                text-decoration: none;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }
            .btn-primary {
                background: #104C5C;
                color: #FFF;
                box-shadow: 0 10px 25px rgba(16, 76, 92, 0.2);
            }
            .btn-primary:hover {
                background: #0A323D;
                transform: translateY(-3px);
                box-shadow: 0 15px 35px rgba(16, 76, 92, 0.3);
            }
            .btn-secondary {
                background: #F1F5F9;
                color: #104C5C;
                border: 1px solid rgba(16, 76, 92, 0.1);
            }
            .btn-secondary:hover {
                background: #FFFFFF;
                border-color: #2ED9C3;
                color: #104C5C;
                transform: translateY(-3px);
                box-shadow: 0 10px 25px rgba(46, 217, 195, 0.15);
            }

            /* Cross-Sell Section */
            .cross-sell-wrapper {
                text-align: center;
                margin-top: 40px;
            }
            .cross-sell-header {
                display: inline-block;
                padding: 8px 20px;
                background: rgba(46, 217, 195, 0.1);
                color: #104C5C;
                font-weight: 800;
                border-radius: 30px;
                margin-bottom: 25px;
                font-size: 0.95rem;
                letter-spacing: 1px;
            }
            .cross-sell-title {
                color: #104C5C;
                font-family: 'Poppins', sans-serif;
                font-weight: 900;
                font-size: 2.2rem;
                margin-bottom: 15px;
                line-height: 1.2;
            }
            .cross-sell-title span {
                background: linear-gradient(135deg, #2ED9C3, #104C5C);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .cs-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 30px;
                margin-top: 40px;
            }
            .cs-premium-card {
                background: #FFFFFF;
                border-radius: 24px;
                padding: 40px 25px;
                text-align: center;
                text-decoration: none;
                transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                position: relative;
                overflow: hidden;
                border: 1px solid rgba(16, 76, 92, 0.05);
                box-shadow: 0 10px 30px rgba(0,0,0,0.03);
                z-index: 1;
            }
            .cs-premium-card::before {
                content: '';
                position: absolute;
                top: 0; left: 0; right: 0; bottom: 0;
                background: linear-gradient(135deg, rgba(46, 217, 195, 0.05), rgba(16, 76, 92, 0.05));
                opacity: 0;
                transition: opacity 0.4s;
                z-index: -1;
            }
            .cs-premium-card:hover {
                transform: translateY(-12px);
                border-color: rgba(46, 217, 195, 0.4);
                box-shadow: 0 25px 50px rgba(16, 76, 92, 0.12);
            }
            .cs-premium-card:hover::before {
                opacity: 1;
            }
            
            .cs-icon-ring {
                width: 110px;
                height: 110px;
                margin: 0 auto 25px;
                border-radius: 50%;
                background: #F8FAFC;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                transition: all 0.4s ease;
            }
            .cs-icon-ring::after {
                content: '';
                position: absolute;
                top: -5px; left: -5px; right: -5px; bottom: -5px;
                border-radius: 50%;
                border: 2px dashed rgba(16, 76, 92, 0.2);
                animation: spin 10s linear infinite;
                opacity: 0;
                transition: opacity 0.3s;
            }
            @keyframes spin { 100% { transform: rotate(360deg); } }
            
            .cs-premium-card:hover .cs-icon-ring {
                background: #104C5C;
                box-shadow: 0 15px 30px rgba(16, 76, 92, 0.25);
                transform: scale(1.1);
            }
            .cs-premium-card:hover .cs-icon-ring::after {
                opacity: 1;
                border-color: rgba(46, 217, 195, 0.6);
            }
            .cs-icon-ring i {
                font-size: 2.8rem;
                color: #104C5C;
                transition: color 0.4s;
            }
            .cs-premium-card:hover .cs-icon-ring i {
                color: #2ED9C3;
            }

            .cs-name {
                color: #104C5C;
                font-family: 'Poppins', sans-serif;
                font-weight: 800;
                font-size: 1.4rem;
                margin: 0 0 10px 0;
                transition: color 0.3s;
            }
            .cs-premium-card:hover .cs-name {
                color: #2ED9C3;
            }
            .cs-price-badge {
                display: inline-block;
                background: #F1F5F9;
                color: #104C5C;
                padding: 6px 15px;
                border-radius: 20px;
                font-size: 0.85rem;
                font-weight: 800;
                transition: all 0.3s;
            }
            .cs-premium-card:hover .cs-price-badge {
                background: #104C5C;
                color: #FFF;
            }
            
            @media (max-width: 768px) {
                .cs-grid {
                    grid-template-columns: 1fr;
                    gap: 20px;
                }
                .contract-premium-card {
                    padding: 30px 20px;
                }
                .cross-sell-title {
                    font-size: 1.8rem;
                }
            }
        </style>

        <div class="final-summary-container">
            
            <!-- Premium Contract Details Card -->
            <div class="contract-premium-card anim-entry delay-2" style="animation: floatSmooth 6s ease-in-out infinite;">
                <div class="card-bg-deco"></div>
                
                <div class="contract-content">
                    
                    <!-- Section 1 -->
                    <div>
                        <div class="premium-section-title">
                            <i class="fa-solid fa-file-signature"></i> Resumen de tu Póliza
                        </div>
                        <div class="detail-grid">
                            <div class="detail-item">
                                <span class="detail-label">Nº de Contrato</span>
                                <span class="detail-value" id="contractNumber">1234567</span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Activación</span>
                                <span class="detail-value" id="activationDate">Cargando...</span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Medio de Pago</span>
                                <span class="detail-value">Débito **** 4539</span>
                            </div>
                            <div class="detail-item" style="background: rgba(46, 217, 195, 0.1); border-color: rgba(46, 217, 195, 0.3);">
                                <span class="detail-label" style="color: #104C5C;">Total Mensual</span>
                                <span class="detail-value" id="totalMonthly" style="color: #2ED9C3; font-size: 1.4rem;">Cargando...</span>
                            </div>
                        </div>
                    </div>

                    <!-- Section 2 -->
                    <div style="border-top: 1px dashed rgba(16, 76, 92, 0.15); padding-top: 30px;">
                        <div class="premium-section-title">
                            <i class="fa-solid fa-paper-plane"></i> Documentación
                        </div>
                        <p style="color: #475569; font-size: 1.1rem; font-weight: 500; margin: 0 0 20px 0;">
                            Hemos enviado una copia digital respaldada de tu contrato a: <br>
                            <strong style="color: #104C5C; font-size: 1.2rem;" id="ownerEmail">contacto@mhmseguros.cl</strong>
                        </p>
                        
                        <div class="action-buttons-flex">
                            <a href="#" class="premium-btn btn-primary">
                                <i class="fa-solid fa-cloud-arrow-down"></i> Descargar Póliza PDF
                            </a>
                            <a href="#" class="premium-btn btn-secondary">
                                <i class="fa-solid fa-book-open-reader"></i> Ver Condicionado General
                            </a>
                        </div>
                    </div>

                </div>
            </div>

            <!-- Premium Cross-Sell Section -->
            <div class="cross-sell-wrapper anim-entry delay-3">
                <div class="cross-sell-header">MÁS PROTECCIÓN MHM</div>
                <h2 class="cross-sell-title">Cuidar lo que quieres <br><span>No termina aquí</span></h2>
                <p style="color: #64748B; font-size: 1.15rem; font-weight: 500; margin-bottom: 40px; max-width: 600px; margin-inline: auto;">
                    Potencia tu tranquilidad con condiciones preferenciales exclusivas. Descubre las asistencias diseñadas para tu día a día.
                </p>

                <div class="cs-grid">
                    <a href="../cotizacion-hogar/index.html" class="cs-premium-card">
                        <div class="cs-icon-ring">
                            <i class="fa-solid fa-house-chimney"></i>
                        </div>
                        <h4 class="cs-name">Hogar</h4>
                        <span class="cs-price-badge">Desde $7.990</span>
                    </a>
                    
                    <a href="../funnel-auto/index.html" class="cs-premium-card">
                        <div class="cs-icon-ring">
                            <i class="fa-solid fa-car-side"></i>
                        </div>
                        <h4 class="cs-name">Movilidad</h4>
                        <span class="cs-price-badge">Desde $3.200</span>
                    </a>
                    
                    <a href="../cotizacion/cotizacion.html" class="cs-premium-card">
                        <div class="cs-icon-ring">
                            <i class="fa-solid fa-paw"></i>
                        </div>
                        <h4 class="cs-name">Mascotas</h4>
                        <span class="cs-price-badge">Desde $9.490</span>
                    </a>
                </div>
            </div>

        </div>"""
    content = content[:start_idx] + new_html + content[end_idx:]
    with open('cotizacion/cotizacion-escolar-5.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Made it premium")
else:
    print("Could not find start/end")
