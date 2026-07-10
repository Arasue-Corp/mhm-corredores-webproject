import re

with open('cotizacion/cotizacion-escolar-5.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the specs-layout-grid
start_tag = '<div class="specs-layout-grid">'
end_tag = '</div>\n    </div>\n\n<script>'

start_idx = content.find(start_tag)
end_idx = content.find(end_tag)

if start_idx != -1 and end_idx != -1:
    new_html = """
        <style>
            .success-clean-content {
                background: #fff;
                padding: 40px;
                margin: 0 auto 40px;
                max-width: 800px;
                font-size: 1.05rem;
                color: #1C4E5E;
                font-weight: 500;
                line-height: 1.6;
            }
            .success-clean-content h3 {
                color: #1C4E5E;
                font-weight: 800;
                font-size: 1.15rem;
                margin-top: 25px;
                margin-bottom: 15px;
            }
            .success-clean-content ul {
                list-style-type: disc;
                margin-left: 25px;
                margin-bottom: 25px;
                color: #1C4E5E;
            }
            .success-clean-content ul li {
                margin-bottom: 8px;
            }
            .success-clean-content ul li strong {
                font-weight: 800;
            }
            .success-clean-content a {
                color: #1C4E5E;
                text-decoration: underline;
                font-weight: 800;
            }
            
            .cross-sell-section {
                text-align: center;
                margin-bottom: 60px;
                padding: 0 20px;
            }
            .cross-sell-section h2 {
                color: #1C4E5E;
                font-weight: 900;
                font-size: 1.5rem;
                margin-bottom: 10px;
            }
            .cross-sell-section p {
                color: #475569;
                font-size: 1.05rem;
                margin-bottom: 30px;
                font-weight: 500;
            }
            .cross-sell-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
                max-width: 900px;
                margin: 0 auto;
            }
            .cs-card {
                background: #F8FAFC;
                border-radius: 16px;
                padding: 30px 20px;
                text-align: center;
                transition: transform 0.3s ease;
                text-decoration: none;
                display: block;
            }
            .cs-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0,0,0,0.05);
            }
            .cs-icon-circle {
                width: 120px;
                height: 120px;
                background: #1C4E5E;
                border-radius: 50%;
                margin: 0 auto 20px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 3rem;
            }
            .cs-card h4 {
                color: #1C4E5E;
                font-weight: 800;
                font-size: 1.25rem;
                margin-bottom: 5px;
                text-decoration: underline;
            }
            .cs-card span {
                color: #1C4E5E;
                font-size: 0.85rem;
                font-weight: 800;
            }
            @media (max-width: 768px) {
                .cross-sell-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        
        <div class="container">
            <div class="success-clean-content anim-entry delay-2">
                <h3 style="margin-top: 0;">-Detalle de contratación:</h3>
                <ul>
                    <li><strong>Nº de contrato:</strong> <span id="contractNumber">1234567</span></li>
                    <li><strong>Fecha de activación:</strong> <span id="activationDate">Cargando...</span></li>
                    <li><strong>Medio de pago:</strong> Tarjeta de débito terminada en *******4539</li>
                    <li><strong>Total mensual:</strong> <span id="totalMonthly">Cargando...</span></li>
                </ul>

                <h3>-Documentación enviada</h3>
                <p style="margin-bottom: 25px;">Te enviamos una copia de tu contrato a <span id="ownerEmail">contacto@mhmseguros.cl</span></p>

                <h3>-Acciones disponibles:</h3>
                <ul>
                    <li><a href="#">Descargar PDF</a></li>
                    <li>Conocer <a href="#">detalle de asistencia</a> o <a href="#">condicionado.</a></li>
                </ul>
            </div>

            <div class="cross-sell-section anim-entry delay-3">
                <h2>CUIDAR LO QUE QUIERES NO TERMINA AQUÍ 💚</h2>
                <p>Descubre otras asistencias que pueden ayudarte en tu día a día:</p>

                <div class="cross-sell-grid">
                    <a href="../cotizacion-hogar/index.html" class="cs-card">
                        <div class="cs-icon-circle">
                            <i class="fa-solid fa-house-chimney"></i>
                        </div>
                        <h4>HOGAR</h4>
                        <span>DESDE $7.990</span>
                    </a>
                    <a href="../funnel-auto/index.html" class="cs-card">
                        <div class="cs-icon-circle">
                            <i class="fa-solid fa-car-side"></i>
                        </div>
                        <h4>MOVILIDAD</h4>
                        <span>DESDE $3.200</span>
                    </a>
                    <a href="../cotizacion/cotizacion.html" class="cs-card">
                        <div class="cs-icon-circle">
                            <i class="fa-solid fa-paw"></i>
                        </div>
                        <h4>MASCOTAS</h4>
                        <span>DESDE $9.490</span>
                    </a>
                </div>
            </div>
        </div>
"""
    content = content[:start_idx] + new_html + content[end_idx:]

# Let's also remove the unnecessary successModal at the bottom
modal_start = content.find('<!-- Success Modal -->')
modal_end = content.find('<style>', modal_start)
if modal_start != -1 and modal_end != -1:
    content = content[:modal_start] + content[modal_end:]

with open('cotizacion/cotizacion-escolar-5.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done rewrite")
