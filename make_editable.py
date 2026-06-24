import re

with open("cotizacion/cotizacion-9-1.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace static pd-value with inputs
old_grid = """<div class="payer-data-grid">
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
                            </div>"""

new_grid = """<div class="payer-data-grid">
                                <div class="pd-item">
                                    <div class="pd-label">RUT</div>
                                    <input type="text" class="pd-input" value="10.042.595-5">
                                </div>
                                <div class="pd-item">
                                    <div class="pd-label">Nombre Completo</div>
                                    <input type="text" class="pd-input" value="Cristian Gonzalo Martinez Pardo">
                                </div>
                                <div class="pd-item">
                                    <div class="pd-label">Región</div>
                                    <input type="text" class="pd-input" value="De Los Ríos">
                                </div>
                                <div class="pd-item">
                                    <div class="pd-label">Comuna</div>
                                    <input type="text" class="pd-input" value="Valdivia">
                                </div>
                                <div class="pd-item full-width">
                                    <div class="pd-label">Dirección</div>
                                    <input type="text" class="pd-input" value="Martínez de Rozas 5523">
                                </div>
                            </div>"""

content = content.replace(old_grid, new_grid)

# Update Javascript
old_js = """function togglePACPATForm() {
        const isYes = document.getElementById('dc_yes').checked;
        const section = document.getElementById('paymentOptionsSection');
        const btnNext = document.getElementById('btnNext');
        
        if (isYes) {"""

new_js = """function togglePACPATForm() {
        const isYes = document.getElementById('dc_yes').checked;
        const section = document.getElementById('paymentOptionsSection');
        const btnNext = document.getElementById('btnNext');
        const payerInputs = document.querySelectorAll('.pd-input');
        
        if (isYes) {
            // Lock inputs
            payerInputs.forEach(inp => {
                inp.setAttribute('readonly', true);
                inp.classList.add('locked');
            });
            """

content = content.replace(old_js, new_js)

old_js2 = """} else {
            section.style.opacity = '0';
            setTimeout(() => { section.style.display = 'none'; }, 400);"""

new_js2 = """} else {
            // Unlock inputs
            payerInputs.forEach(inp => {
                inp.removeAttribute('readonly');
                inp.classList.remove('locked');
            });
            
            section.style.opacity = '0';
            setTimeout(() => { section.style.display = 'none'; }, 400);"""

content = content.replace(old_js2, new_js2)

with open("cotizacion/cotizacion-9-1.html", "w", encoding="utf-8") as f:
    f.write(content)

# Append CSS for .pd-input
with open("css/style-quote.css", "a", encoding="utf-8") as f:
    f.write("""
/* Editable Payer Inputs */
.pd-input {
    width: 100%;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 0.95rem;
    font-weight: 600;
    color: #1E293B;
    background: #F8FAFC;
    outline: none;
    transition: all 0.2s ease;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
}
.pd-input:focus {
    border-color: #3B82F6;
    background: white;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
}
.pd-input.locked {
    border-color: transparent;
    background: transparent;
    box-shadow: none;
    padding-left: 0;
    pointer-events: none;
}
""")
