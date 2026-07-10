import os
import re

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-ciclista-1.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Javascript products dictionary
content = re.sub(
    r"const products = \{[^\}]+\};",
    "const products = {\n        'ciclista': { name: 'Asistencia al Ciclista', price: 3200, qty: 0 }\n    };",
    content
)

# 2. Update the coverage modal HTML
modal_table = """
                        <div class="table-responsive">
                            <table class="c-table">
                                <thead>
                                    <tr>
                                        <th>SERVICIO</th>
                                        <th>PROTECCIÓN</th>
                                        <th>LÍMITE</th>
                                        <th>MAX EVENTOS AL AÑO</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td class="cov-label"><i class="fa-solid fa-heart-pulse cov-icon"></i> URGENCIA MÉDICA POR ACCIDENTE EN BICICLETA</td>
                                        <td class="cov-val"><span class="highlight-cov">100% ISAPRE Y FONASA / 50% FONASA A</span></td>
                                        <td class="cov-val">$90.000</td>
                                        <td class="cov-val">2</td>
                                    </tr>
                                    <tr>
                                        <td class="cov-label"><i class="fa-solid fa-money-bill-wave cov-icon"></i> DESCUENTO EN FARMACIAS</td>
                                        <td class="cov-val"><span class="highlight-cov">50% DE LA BOLETA</span></td>
                                        <td class="cov-val">$10.000</td>
                                        <td class="cov-val">12</td>
                                    </tr>
                                    <tr>
                                        <td class="cov-label"><i class="fa-solid fa-user-doctor cov-icon"></i> TELEMEDICINA</td>
                                        <td class="cov-val"><span class="highlight-cov">100%</span></td>
                                        <td class="cov-val">2 UF</td>
                                        <td class="cov-val">2</td>
                                    </tr>
                                    <tr>
                                        <td class="cov-label"><i class="fa-solid fa-phone-volume cov-icon"></i> ORIENTACIÓN MÉDICA TELEFÓNICA</td>
                                        <td class="cov-val"><span class="highlight-cov">100%</span></td>
                                        <td class="cov-val">2 UF</td>
                                        <td class="cov-val">4</td>
                                    </tr>
                                    <tr>
                                        <td class="cov-label"><i class="fa-solid fa-scale-balanced cov-icon"></i> ASISTENCIA LEGAL TELEFÓNICA</td>
                                        <td class="cov-val"><span class="highlight-cov">100%</span></td>
                                        <td class="cov-val">2 UF</td>
                                        <td class="cov-val">4</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="info-statement-box mt-4">
                            <p>Los descuentos y beneficios de salud son entregados en línea a través de i-Med o a través de red de prestadores propios.</p>
                        </div>
"""

# Find the existing modal content and replace it
# We know the modal content is inside `<div id="covModalContent">`
content = re.sub(
    r'<div id="covModalContent">.*?</div>\s*</div>\s*</div>',
    f'<div id="covModalContent">\n{modal_table}\n</div>\n                </div>\n            </div>',
    content,
    flags=re.DOTALL
)

# 3. Update the single plan card and remove the second plan
# The cards are in `<div class="marketplace-grid">`
# We will just replace everything between `<div class="marketplace-grid">` and `</section>` (excluding section tag)
new_grid = """<div class="marketplace-grid">
            
            <div class="offer-card organic-panel anim-entry delay-1" id="card-ciclista">
                <div class="vt-image"><img src="../assets/img/article-3.webp" alt="Asistencia al Ciclista" id="img-ciclista"></div>
                <div class="offer-content">
                    <div class="offer-header">
                        <h4>Asistencia al Ciclista</h4>
                    </div>
                    <ul class="offer-features">
                        <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                        <li><i class="fa-solid fa-check"></i> Asistencia disponible para ti.</li>
                        <li><i class="fa-solid fa-check"></i> Edad de ingreso: Para contratar debes ser mayor a 18 años y tener menos de 65 años.</li>
                        <li><i class="fa-solid fa-check"></i> Descuento en farmacia, mayor cobertura y beneficios exclusivos.</li>
                        <li><i class="fa-solid fa-check"></i> Libre elección en todo Chile.</li>
                    </ul>
                    
                    <button type="button" class="btn-text" onclick="showCoverage('ciclista')">Ver Coberturas <i class="fa-solid fa-arrow-right"></i></button>

                    <div class="price-action">
                        <div class="price-val">$3.200 <span style="font-size: 0.8rem; color: #94A3B8; font-weight: normal;">/mes</span></div>
                        
                        <div class="qty-control" id="qty-control-ciclista" style="display: none;">
                            <button type="button" onclick="updateQty('ciclista', -1)"><i class="fa-solid fa-minus"></i></button>
                            <span id="qty-ciclista">0</span>
                            <button type="button" onclick="updateQty('ciclista', 1)"><i class="fa-solid fa-plus"></i></button>
                        </div>
                        <button type="button" class="btn-primary" id="btn-add-ciclista" onclick="updateQty('ciclista', 1)">Agregar</button>
                    </div>
                </div>
            </div>

        </div>
        
    </div>
"""

content = re.sub(
    r'<div class="marketplace-grid">.*?</div>\s*</div>\s*</section>',
    f'{new_grid}</section>',
    content,
    flags=re.DOTALL
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Ciclista step 1 successfully.")
