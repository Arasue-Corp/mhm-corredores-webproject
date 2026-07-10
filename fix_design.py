import re

with open('cotizacion/cotizacion-escolar-5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the previous block we added
start_tag = '<style>\n            .success-clean-content {'
end_tag = '</div>\n        </div>'
start_idx = content.find(start_tag)
end_idx = content.find(end_tag) + len(end_tag)

if start_idx != -1 and content.find(end_tag) != -1:
    new_html = """
        <style>
            .final-summary-container {
                max-width: 900px;
                margin: 0 auto 60px;
                padding: 0 20px;
                font-family: 'Inter', sans-serif;
                position: relative;
                z-index: 2;
            }
            .contract-details-box {
                margin-bottom: 60px;
                padding: 40px;
                background: rgba(255, 255, 255, 0.8);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.02);
                border: 1px solid rgba(255,255,255,0.5);
            }
            .detail-section {
                margin-bottom: 30px;
            }
            .detail-section:last-child {
                margin-bottom: 0;
            }
            .detail-title {
                color: #104C5C;
                font-family: 'Poppins', sans-serif;
                font-weight: 800;
                font-size: 1.15rem;
                margin-bottom: 15px;
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .custom-list {
                list-style: none;
                padding: 0;
                margin: 0;
            }
            .custom-list li {
                position: relative;
                padding-left: 20px;
                margin-bottom: 10px;
                color: #104C5C;
                font-size: 1.05rem;
                font-weight: 500;
            }
            .custom-list li::before {
                content: '';
                position: absolute;
                left: 0;
                top: 10px;
                width: 6px;
                height: 6px;
                background-color: #104C5C;
                border-radius: 50%;
            }
            .custom-list li strong {
                font-weight: 700;
            }
            .detail-text {
                color: #104C5C;
                font-size: 1.05rem;
                font-weight: 500;
                margin: 0;
                line-height: 1.5;
            }
            .detail-link {
                color: #104C5C;
                font-weight: 700;
                text-decoration: underline;
                text-underline-offset: 4px;
                transition: color 0.3s;
            }
            .detail-link:hover {
                color: #2ED9C3;
            }

            .cross-sell-wrapper {
                text-align: center;
            }
            .cross-sell-title {
                color: #104C5C;
                font-family: 'Poppins', sans-serif;
                font-weight: 800;
                font-size: 1.6rem;
                margin-bottom: 10px;
                text-transform: uppercase;
                letter-spacing: -0.5px;
            }
            .cross-sell-subtitle {
                color: #475569;
                font-size: 1.1rem;
                margin-bottom: 40px;
                font-weight: 500;
            }
            .cs-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 25px;
            }
            .cs-card-item {
                background: #F8FAFC;
                border-radius: 24px;
                padding: 40px 20px;
                text-align: center;
                text-decoration: none;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                border: 1px solid transparent;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .cs-card-item:hover {
                transform: translateY(-8px);
                background: #FFFFFF;
                border-color: rgba(16, 76, 92, 0.1);
                box-shadow: 0 20px 40px rgba(16, 76, 92, 0.08);
            }
            .cs-circle {
                width: 130px;
                height: 130px;
                background: #104C5C;
                border-radius: 50%;
                margin-bottom: 25px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 3.5rem;
                transition: transform 0.3s ease;
            }
            .cs-card-item:hover .cs-circle {
                transform: scale(1.05);
            }
            .cs-name {
                color: #104C5C;
                font-family: 'Poppins', sans-serif;
                font-weight: 800;
                font-size: 1.3rem;
                margin: 0 0 8px 0;
                text-decoration: underline;
                text-underline-offset: 4px;
            }
            .cs-price {
                color: #104C5C;
                font-size: 0.9rem;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            @media (max-width: 768px) {
                .cs-grid {
                    grid-template-columns: 1fr;
                    gap: 15px;
                }
                .contract-details-box {
                    padding: 25px;
                }
            }
        </style>

        <div class="final-summary-container">
            <div class="contract-details-box anim-entry delay-2">
                
                <div class="detail-section">
                    <div class="detail-title">-Detalle de contratación:</div>
                    <ul class="custom-list">
                        <li><strong>Nº de contrato:</strong> <span id="contractNumber">1234567</span></li>
                        <li><strong>Fecha de activación:</strong> <span id="activationDate">Cargando...</span></li>
                        <li><strong>Medio de pago:</strong> Tarjeta de débito terminada en *******4539</li>
                        <li><strong>Total mensual:</strong> <span id="totalMonthly">Cargando...</span></li>
                    </ul>
                </div>

                <div class="detail-section">
                    <div class="detail-title">-Documentación enviada</div>
                    <p class="detail-text">Te enviamos una copia de tu contrato a <span id="ownerEmail" style="font-weight: 700;">contacto@mhmseguros.cl</span></p>
                </div>

                <div class="detail-section">
                    <div class="detail-title">-Acciones disponibles:</div>
                    <ul class="custom-list" style="margin-bottom: 0;">
                        <li><a href="#" class="detail-link">Descargar PDF</a></li>
                        <li>Conocer <a href="#" class="detail-link">detalle de asistencia</a> o <a href="#" class="detail-link">condicionado.</a></li>
                    </ul>
                </div>

            </div>

            <div class="cross-sell-wrapper anim-entry delay-3">
                <h2 class="cross-sell-title">CUIDAR LO QUE QUIERES NO TERMINA AQUÍ <span style="color: #2ED9C3;">💚</span></h2>
                <p class="cross-sell-subtitle">Descubre otras asistencias que pueden ayudarte en tu día a día:</p>

                <div class="cs-grid">
                    <a href="../cotizacion-hogar/index.html" class="cs-card-item">
                        <div class="cs-circle">
                            <i class="fa-solid fa-house-chimney"></i>
                        </div>
                        <h4 class="cs-name">HOGAR</h4>
                        <span class="cs-price">DESDE $7.990</span>
                    </a>
                    <a href="../funnel-auto/index.html" class="cs-card-item">
                        <div class="cs-circle">
                            <i class="fa-solid fa-car-side"></i>
                        </div>
                        <h4 class="cs-name">MOVILIDAD</h4>
                        <span class="cs-price">DESDE $3.200</span>
                    </a>
                    <a href="../cotizacion/cotizacion.html" class="cs-card-item">
                        <div class="cs-circle">
                            <i class="fa-solid fa-paw"></i>
                        </div>
                        <h4 class="cs-name">MASCOTAS</h4>
                        <span class="cs-price">DESDE $9.490</span>
                    </a>
                </div>
            </div>
        </div>"""
    
    content = content[:start_idx] + new_html + content[end_idx:]
    
    with open('cotizacion/cotizacion-escolar-5.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed layout")
else:
    print("Could not find layout to replace")
