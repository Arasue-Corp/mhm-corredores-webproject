import re

with open("cotizacion/cotizacion-8-1.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Headings
content = content.replace("Contrato 100% Digital", "Carga tu documento y valida tu 0Km")
content = content.replace("Verifica los datos del contratante antes de emitir tu póliza.", "Verifica que tu vehículo es nuevo subiendo la documentación requerida.")

# 2. Update Sidebar
old_sidebar = """<ul class="aurora-list">
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Cotización</li>
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Selección de Plan</li>
                        <li class="active"><span class="pulse-dot"></span> Verificación de Datos</li>
                        <li><i class="fa-regular fa-circle"></i> Opciones de Pago</li>
                        <li><i class="fa-regular fa-circle"></i> Emisión Final</li>
                    </ul>"""
new_sidebar = """<ul class="aurora-list">
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Cotización</li>
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Selección de Plan</li>
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Verificación de Datos</li>
                        <li class="active"><span class="pulse-dot"></span> Validación 0Km</li>
                        <li><i class="fa-regular fa-circle"></i> Opciones de Pago</li>
                        <li><i class="fa-regular fa-circle"></i> Emisión Final</li>
                    </ul>"""
content = content.replace(old_sidebar, new_sidebar)

# 3. Update the form body
new_body = """
                <div class="premium-white-card" id="quoteFormStep8">
                    <div class="info-banner-warning mb-4" style="background: #FFFBEB; border: 1px solid #FEF08A; color: #B45309; padding: 15px 20px; border-radius: 12px; display: flex; align-items: flex-start; gap: 12px;">
                        <div class="banner-icon" style="color: #F59E0B; margin-top:2px;"><i class="fa-solid fa-clock-rotate-left"></i></div>
                        <div><strong>Atención:</strong> La factura o Guía de despacho no debe superar las 48 horas desde la emisión.</div>
                    </div>
                    
                    <div class="grid-2-tight mb-4">
                        <div class="inp-rich-group">
                            <label>RUT del emisor de la factura</label>
                            <div class="input-rich-wrapper compact-premium theme-blue">
                                <div class="icon-slot"><i class="fa-solid fa-building"></i></div>
                                <input type="text" class="rich-input" placeholder="Ej: 76.123.456-7" id="rutEmisor">
                            </div>
                        </div>
                        <div class="inp-rich-group">
                            <label>Número de factura</label>
                            <div class="input-rich-wrapper compact-premium theme-blue">
                                <div class="icon-slot"><i class="fa-solid fa-file-invoice"></i></div>
                                <input type="text" class="rich-input" placeholder="Ej: 125678" id="numFactura">
                            </div>
                        </div>
                    </div>

                    <div class="inp-rich-group mb-5">
                        <label>Favor de seleccionar fecha de emisión <i class="fa-solid fa-calendar-days" style="color: var(--quote-primary); margin-left:5px;"></i></label>
                        <div class="date-boxes-container">
                            <div class="input-rich-wrapper compact-premium theme-purple date-box">
                                <div class="icon-slot" style="font-size:0.75rem; font-weight:700;">DD</div>
                                <input type="number" class="rich-input text-center" placeholder="01" min="1" max="31" id="dateDD" oninput="checkFormCompletion()">
                            </div>
                            <span class="date-separator">/</span>
                            <div class="input-rich-wrapper compact-premium theme-purple date-box">
                                <div class="icon-slot" style="font-size:0.75rem; font-weight:700;">MM</div>
                                <input type="number" class="rich-input text-center" placeholder="12" min="1" max="12" id="dateMM" oninput="checkFormCompletion()">
                            </div>
                            <span class="date-separator">/</span>
                            <div class="input-rich-wrapper compact-premium theme-purple date-box year-box">
                                <div class="icon-slot" style="font-size:0.75rem; font-weight:700;">YYYY</div>
                                <input type="number" class="rich-input text-center" placeholder="2026" min="2020" max="2030" id="dateYYYY" oninput="checkFormCompletion()">
                            </div>
                        </div>
                    </div>
                    
                    <div class="pg-header">
                        <div class="pg-header-badge teal">
                            <i class="fa-solid fa-cloud-arrow-up"></i> CARGA DE DOCUMENTO
                        </div>
                        <div class="pg-header-line"></div>
                    </div>
                    
                    <div class="upload-area-container mb-2">
                        <input type="file" id="fileUpload" class="hidden-file-input" accept="application/pdf" onchange="handleFileUpload(event)">
                        
                        <div class="upload-drop-zone" id="dropZone" onclick="document.getElementById('fileUpload').click()">
                            <div class="upload-icon-wrapper">
                                <i class="fa-solid fa-file-pdf"></i>
                            </div>
                            <h3 class="upload-title">Adjunta PDF</h3>
                            <p class="upload-desc">Arrastra y suelta tu archivo aquí, o haz clic para explorar</p>
                            <div class="upload-btn-fake">Seleccionar Archivo</div>
                        </div>
                        
                        <div class="document-preview-card" id="docPreview" style="display: none;">
                            <div class="doc-icon"><i class="fa-solid fa-file-pdf" style="color: #EF4444;"></i></div>
                            <div class="doc-info">
                                <div class="doc-name" id="docName">factura.pdf</div>
                                <div class="doc-size" id="docSize">-- • Carga completada</div>
                            </div>
                            <button class="doc-remove-btn" onclick="removeDocument(event)"><i class="fa-solid fa-xmark"></i></button>
                        </div>
                    </div>
"""

# Replace between specs-layout-grid and hero-action-area
pattern = re.compile(r'<div class="row-switch-container mb-4".*?<div class="hero-action-area mt-5"', re.DOTALL)
content = pattern.sub(new_body + '\n                    <div class="hero-action-area mt-5"', content)

# 4. Update Next button target to cotizacion-9.html
content = content.replace('href="cotizacion-8-1.html"', 'href="cotizacion-9.html"')

# 5. Remove switchEntityToggle and toggleContinueBtn JS scripts
script_pattern = re.compile(r'<script>.*?</script>', re.DOTALL)
new_scripts = """<script>
    function handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
            document.getElementById('dropZone').style.display = 'none';
            document.getElementById('docPreview').style.display = 'flex';
            document.getElementById('docName').innerText = file.name;
            const sizeInMB = (file.size / (1024*1024)).toFixed(2);
            document.getElementById('docSize').innerText = sizeInMB + " MB • Carga completada";
            checkFormCompletion();
        }
    }

    function removeDocument(event) {
        event.stopPropagation();
        document.getElementById('fileUpload').value = "";
        document.getElementById('docPreview').style.display = 'none';
        document.getElementById('dropZone').style.display = 'flex';
        checkFormCompletion();
    }
    
    function checkFormCompletion() {
        // Logic to enable continue button if file is loaded
        const btnNext = document.getElementById('btnNext');
        const linkNext = document.getElementById('linkNext');
        const fileVal = document.getElementById('fileUpload').value;
        const rut = document.getElementById('rutEmisor').value;
        const num = document.getElementById('numFactura').value;
        
        // For prototype, just checking if a file is uploaded to enable button
        if (fileVal !== "") {
            btnNext.disabled = false;
            btnNext.classList.remove('disabled');
            btnNext.style.cursor = 'pointer';
            btnNext.style.opacity = '1';
            linkNext.style.pointerEvents = 'auto';
        } else {
            btnNext.disabled = true;
            btnNext.classList.add('disabled');
            btnNext.style.cursor = 'not-allowed';
            btnNext.style.opacity = '0.5';
            linkNext.style.pointerEvents = 'none';
        }
    }
    
    // Drag and drop visuals
    const dropZone = document.getElementById('dropZone');
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = 'var(--quote-primary)';
        dropZone.style.background = '#EFF6FF';
    });
    dropZone.addEventListener('dragleave', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = '#CBD5E1';
        dropZone.style.background = '#F8FAFC';
    });
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        if (e.dataTransfer.files.length) {
            document.getElementById('fileUpload').files = e.dataTransfer.files;
            // Manually trigger change event
            const event = new Event('change');
            document.getElementById('fileUpload').dispatchEvent(event);
        }
    });

    // Make inputs trigger checkFormCompletion
    document.getElementById('rutEmisor').addEventListener('input', checkFormCompletion);
    document.getElementById('numFactura').addEventListener('input', checkFormCompletion);
</script>"""

content = script_pattern.sub(new_scripts, content)

with open("cotizacion/cotizacion-8-1.html", "w", encoding="utf-8") as f:
    f.write(content)

print("cotizacion-8-1.html generated")
