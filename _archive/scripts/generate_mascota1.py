import re

with open('cotizacion/cotizacion-salud-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Title, Tags, etc.
content = content.replace('<title>Seguro de Salud | MHM Corredores</title>', '<title>Seguro de Mascotas | MHM Corredores</title>')
content = content.replace('seguro salud, salud complementaria, seguro médico, seguro hospitalario', 'seguro mascotas, seguro veterinario, seguro perro gato')

# Replace Hero section
hero_salud = """<section class="healthLanding" id="inicio">
            <div class="healthPhoto"></div>
            <div class="container healthIntro-wrap">
                <div class="healthIntro">
                    <span class="healthKicker-badge"><i class="fa-solid fa-shield-heart"></i> SEGUROS PARA PERSONAS, FAMILIAS Y EMPRESAS</span>
                    <h1>Protege lo que estás <em>construyendo.</em></h1>
                    <p>Una familia que crece, un negocio que avanza, una salud que quieres cuidar.<br/>En MHM encontramos el seguro que acompaña lo que estás construyendo.</p>
                </div>
            </div>"""

hero_mascotas = """<section class="healthLanding" id="inicio" style="background-image: radial-gradient(circle at 85% 15%, rgba(46, 217, 195, 0.08) 0%, transparent 45%);">
            <div class="healthPhoto"></div>
            <div class="container healthIntro-wrap">
                <div class="healthIntro">
                    <span class="healthKicker-badge" style="color: #0F766E; background: rgba(46, 217, 195, 0.15); border-color: rgba(46, 217, 195, 0.3);"><i class="fa-solid fa-paw"></i> ENCUENTRA TU PROTECCIÓN IDEAL</span>
                    <h1>Protege a tu <em>mejor amigo.</em></h1>
                    <p>Un paseo seguro, travesuras sin miedo y su salud siempre cuidada.<br/>En MHM encontramos el seguro que protege a tu mascota.</p>
                </div>
            </div>"""

content = content.replace(hero_salud, hero_mascotas)

# Replace finderFields
finder_salud_regex = r'<div class="finderFields">.*?(?=</section>\s*</section>)'
finder_mascota = """<div class="finderFields">
                    <!-- Campo Nombre -->
                    <div class="finder-field-col">
                        <div class="finder-tile">
                            <label class="finder-label" for="petName_1">
                                <i class="fa-solid fa-tag"></i> NOMBRE
                            </label>
                            <input type="text" id="petName_1" class="finder-input" placeholder="Ej. Firulais" onchange="updateMainPet()" />
                        </div>
                    </div>

                    <!-- Campo Tipo -->
                    <div class="finder-field-col">
                        <div class="finder-tile select-tile">
                            <label class="finder-label" for="petType_1">
                                <i class="fa-solid fa-dog"></i> TIPO
                            </label>
                            <select id="petType_1" class="finder-select" onchange="updateMainPetType()">
                                <option value="perro" selected>Perro</option>
                                <option value="gato">Gato</option>
                            </select>
                            <i class="fa-solid fa-chevron-down select-arrow"></i>
                        </div>
                    </div>

                    <!-- Campo Edad -->
                    <div class="finder-field-col">
                        <div class="finder-tile">
                            <label class="finder-label" for="petAge_1">
                                <i class="fa-solid fa-cake-candles"></i> EDAD
                            </label>
                            <input type="number" min="0" max="25" id="petAge_1" class="finder-input" placeholder="Años (ej. 3)" onchange="updateMainPet()" />
                        </div>
                    </div>

                    <!-- Panel Mas Detalles / Más Mascotas -->
                    <div class="finder-field-col assured-col-wrapper">
                        <div class="assured-wrapper">
                            <button class="finder-tile assuredField" id="btnAssuredOpen" type="button" aria-expanded="false" aria-controls="assuredPanel">
                                <div class="assuredField-content">
                                    <span class="finder-label"><i class="fa-solid fa-circle-plus"></i> DETALLES & MÁS MASCOTAS</span>
                                    <strong class="assured-value" id="assuredSummary">1 mascota</strong>
                                </div>
                                <span class="assured-badge-icon" id="assuredToggle">
                                    <i class="fa-solid fa-paw"></i>
                                </span>
                            </button>

                            <div class="assuredPanel" id="assuredPanel" style="display: none;">
                                <div class="assuredPanel-header">
                                    <strong><i class="fa-solid fa-list"></i> Completa los datos</strong>
                                    <p>Indica la raza y sexo de tu mascota, y agrega más si lo necesitas.</p>
                                </div>
                                
                                <div class="assuredPanel-body" id="petsPanelBody">
                                    <!-- Pet 1 extra details injected here by JS -->
                                </div>

                                <div class="assuredPanel-footer" style="display: flex; flex-direction: column; gap: 10px;">
                                    <button type="button" class="btn-partner-toggle" style="width: 100%; justify-content: center;" onclick="addPet()">
                                        <i class="fa-solid fa-plus"></i> <span class="partner-label">Añadir otra mascota</span>
                                    </button>
                                    <button type="button" id="btnAssuredDone" class="btn-assured-done">
                                        <i class="fa-solid fa-check"></i> Aplicar al cálculo
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Botón Cotizar Ahora (Aurora CTA) -->
                    <div class="finder-field-col submit-col">
                        <button class="finderSubmit" id="btnRecommend" disabled type="button">
                            <span>Cotizar ahora</span>
                            <div class="submit-icon-circle">
                                <i class="fa-solid fa-arrow-right"></i>
                            </div>
                        </button>
                    </div>
                </div>
                
                <div class="healthProof">
                    <span><i class="fa-solid fa-shield-halved"></i> Cotización sin costo ni compromiso</span>
                    <span>• Planes detallados y transparentes</span>
                    <span>• Atención veterinaria 24/7</span>
                </div>
            </section>
        </section>"""

content = re.sub(finder_salud_regex, finder_mascota, content, flags=re.DOTALL)

# Replace Results Banner
results_banner_salud = """<div class="resultsBanner">
                <div class="container">
                    <span class="resultsKicker"><i class="fa-solid fa-shield-halved"></i> COTIZACIÓN DE SEGUROS DE SALUD</span>
                    <h2>Opciones pensadas para ti</h2>
                    <p>Compara coberturas, asistencias y beneficios para elegir la mejor protección para ti o tu familia.</p>
                </div>
            </div>"""

results_banner_mascotas = """<div class="resultsBanner" style="background: linear-gradient(135deg, #0A0E1A 0%, #0F3836 50%, #082928 100%) !important;">
                <div class="container">
                    <span class="resultsKicker"><i class="fa-solid fa-paw"></i> COTIZACIÓN DE SEGUROS DE MASCOTAS</span>
                    <h2>Opciones pensadas para tus peludos</h2>
                    <p>Compara coberturas, asistencias y beneficios para elegir la mejor protección para ellos.</p>
                </div>
            </div>"""

content = content.replace(results_banner_salud, results_banner_mascotas)

# Replace resultTools
content = re.sub(r'<div class="resultTools">.*?</div>\s*</div>', '<div class="resultTools"><div class="toolsTitleGroup"><b id="availablePlansCount">3 planes disponibles</b><small>Elige el mejor plan para cada mascota y asígnalo abajo</small></div></div>', content, flags=re.DOTALL)

# Replace Left Sidebar Filters with a simpler or hidden one, or just hide it
content = re.sub(r'<aside class="healthFilters is-collapsed" id="healthFilters">.*?</aside>', '', content, flags=re.DOTALL)

# Change policy list layout class so it spans full width since we removed filters
content = content.replace('<div class="healthPolicyList" id="policyList">', '<div class="veh-type-grid" id="policyList" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; width: 100%; margin-bottom: 30px;">')

# Replace commercial note
content = content.replace('Productos sujetos a condiciones de asegurabilidad, límites, exclusiones y condiciones particulares de la póliza. La información presentada es un resumen comercial.', 'Productos sujetos a condiciones de asegurabilidad (edad máxima de ingreso) y condiciones particulares. El precio mostrado es por mascota individual.')

# Add Floating compare dock for pets (Assign plans)
dock_regex = r'<!-- Floating Compare Dock -->.*?</div>\s*</div>'
dock_mascota = """<!-- FLOATING ASSIGN DOCK -->
            <div class="compareFloatingDock" id="assignDock" style="padding: 15px 20px; background: white; border-top: 2px solid #E2E8F0; z-index: 100; transform: translateY(150%);">
                <div class="container" style="display: flex; flex-direction: column; gap: 15px;">
                    <div style="font-weight: 700; color: #0F172A; text-align: center; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px;">
                        Asigna un plan a tus mascotas
                    </div>
                    <div id="assignPetsContainer" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; width: 100%;">
                        <!-- Dynamic assign dropdowns go here -->
                    </div>
                    <div style="display: flex; justify-content: center; margin-top: 10px;">
                        <button type="button" class="btn-primary-premium" id="btnContinuarResumen" onclick="irAResumen()" style="width: auto; padding: 12px 30px; opacity: 0.5; pointer-events: none; border-radius: 12px;">
                            <span>Continuar a Resumen</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>"""

content = re.sub(dock_regex, dock_mascota, content, flags=re.DOTALL)

# Strip out Compare Modal
content = re.sub(r'<!-- Compare Modal -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

# Strip out FAQ (optional, or we can leave it). I'll leave the FAQ but change titles.
content = content.replace('FAQ SALUD', 'FAQ MASCOTAS')
content = content.replace('seguro de salud o complementario', 'seguro de mascotas')
content = content.replace('¿Este seguro reemplaza a Fonasa o Isapre?', '¿Para qué sirve este seguro?')
content = content.replace('No lo reemplaza, sino que <strong>lo complementa y potencia</strong>. El seguro complementario de salud financia el copago que queda después de la bonificación de Fonasa o tu Isapre, reduciendo drásticamente tus gastos de bolsillo en hospitalizaciones, cirugías, consultas y medicamentos.', 'Te ayuda a costear los gastos imprevistos por accidentes, enfermedades o emergencias veterinarias de tus perros y gatos, con asistencias 24/7 y cobertura de responsabilidad civil.')

# Strip JS script tag from the bottom and add ours
content = re.sub(r'<!-- Custom Logic for the form -->\s*<script>.*?</script>', '', content, flags=re.DOTALL)

js_script = """
    <!-- Custom Logic for the form Mascotas -->
    <script>
        const dogBreeds = ["Mestizo", "Pastor Alemán", "Bulldog", "Poodle", "Labrador", "Golden Retriever", "Chihuahua", "Pug", "Otro"];
        const catBreeds = ["Mestizo", "Persa", "Siamés", "Maine Coon", "Esfinge", "Bengalí", "Angora", "Otro"];

        let petsData = [
            { id: 1, name: '', type: 'perro', breed: 'Mestizo', age: '', gender: 'Macho', plan: '' }
        ];

        // Panel Toggle
        const btnAssuredOpen = document.getElementById('btnAssuredOpen');
        const assuredPanel = document.getElementById('assuredPanel');
        const btnAssuredDone = document.getElementById('btnAssuredDone');

        btnAssuredOpen.addEventListener('click', (e) => {
            e.stopPropagation();
            const isExpanded = btnAssuredOpen.getAttribute('aria-expanded') === 'true';
            if (isExpanded) {
                closePanel();
            } else {
                openPanel();
            }
        });

        function openPanel() {
            btnAssuredOpen.setAttribute('aria-expanded', 'true');
            btnAssuredOpen.classList.add('active');
            assuredPanel.style.display = 'flex';
        }

        function closePanel() {
            btnAssuredOpen.setAttribute('aria-expanded', 'false');
            btnAssuredOpen.classList.remove('active');
            assuredPanel.style.display = 'none';
            validateForm();
        }

        btnAssuredDone.addEventListener('click', closePanel);

        document.addEventListener('click', (e) => {
            if (!btnAssuredOpen.contains(e.target) && !assuredPanel.contains(e.target)) {
                closePanel();
            }
        });

        function renderPetsPanel() {
            const container = document.getElementById('petsPanelBody');
            container.innerHTML = '';

            petsData.forEach((p, idx) => {
                const isMain = idx === 0;
                const div = document.createElement('div');
                div.style.borderBottom = idx < petsData.length - 1 ? '1px solid #F1F5F9' : 'none';
                div.style.padding = '10px 0';
                div.style.display = 'flex';
                div.style.flexDirection = 'column';
                div.style.gap = '8px';

                const title = isMain ? 'Detalles Mascota 1' : `Mascota ${idx + 1}`;
                const breeds = p.type === 'gato' ? catBreeds : dogBreeds;
                
                let extraInputs = '';
                if (!isMain) {
                    extraInputs = `
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                            <div>
                                <label style="font-size: 11px; color:#64748B;">NOMBRE</label>
                                <input type="text" value="${p.name}" onchange="updatePanelPet(${p.id}, 'name', this.value)" style="width:100%; padding: 6px; border: 1px solid #CBD5E1; border-radius: 6px; font-size:13px;">
                            </div>
                            <div>
                                <label style="font-size: 11px; color:#64748B;">EDAD</label>
                                <input type="number" min="0" value="${p.age}" onchange="updatePanelPet(${p.id}, 'age', this.value)" style="width:100%; padding: 6px; border: 1px solid #CBD5E1; border-radius: 6px; font-size:13px;">
                            </div>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                            <div>
                                <label style="font-size: 11px; color:#64748B;">TIPO</label>
                                <select onchange="updatePanelPetType(${p.id}, this.value)" style="width:100%; padding: 6px; border: 1px solid #CBD5E1; border-radius: 6px; font-size:13px; background:white;">
                                    <option value="perro" ${p.type==='perro'?'selected':''}>Perro</option>
                                    <option value="gato" ${p.type==='gato'?'selected':''}>Gato</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-size: 11px; color:#64748B;">RAZA</label>
                                <select onchange="updatePanelPet(${p.id}, 'breed', this.value)" style="width:100%; padding: 6px; border: 1px solid #CBD5E1; border-radius: 6px; font-size:13px; background:white;">
                                    ${breeds.map(b => `<option value="${b}" ${b===p.breed?'selected':''}>${b}</option>`).join('')}
                                </select>
                            </div>
                        </div>
                    `;
                } else {
                    extraInputs = `
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                            <div>
                                <label style="font-size: 11px; color:#64748B;">RAZA</label>
                                <select onchange="updatePanelPet(${p.id}, 'breed', this.value)" style="width:100%; padding: 6px; border: 1px solid #CBD5E1; border-radius: 6px; font-size:13px; background:white;">
                                    ${breeds.map(b => `<option value="${b}" ${b===p.breed?'selected':''}>${b}</option>`).join('')}
                                </select>
                            </div>
                        </div>
                    `;
                }

                div.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: 700; font-size: 13px; color: #0F172A;"><i class="fa-solid fa-paw" style="color: #0F766E;"></i> ${title}</span>
                        ${!isMain ? `<button onclick="removePet(${p.id})" style="background:none; border:none; color:#E11D48; cursor:pointer;"><i class="fa-solid fa-trash"></i></button>` : ''}
                    </div>
                    ${extraInputs}
                    <div>
                        <label style="font-size: 11px; color:#64748B;">SEXO</label>
                        <div style="display:flex; gap: 10px; margin-top:3px;">
                            <button class="stepper" style="border: 1px solid ${p.gender==='Macho'?'#0F766E':'#CBD5E1'}; background:${p.gender==='Macho'?'#F0FDF4':'#F8FAFC'}; color:#0F172A; border-radius: 6px; padding: 4px 10px; cursor:pointer;" onclick="updatePanelPet(${p.id}, 'gender', 'Macho')">Macho</button>
                            <button class="stepper" style="border: 1px solid ${p.gender==='Hembra'?'#0F766E':'#CBD5E1'}; background:${p.gender==='Hembra'?'#F0FDF4':'#F8FAFC'}; color:#0F172A; border-radius: 6px; padding: 4px 10px; cursor:pointer;" onclick="updatePanelPet(${p.id}, 'gender', 'Hembra')">Hembra</button>
                        </div>
                    </div>
                `;
                container.appendChild(div);
            });

            document.getElementById('assuredSummary').innerText = `${petsData.length} mascota${petsData.length > 1 ? 's' : ''}`;
        }

        function addPet() {
            if (petsData.length >= 5) {
                alert('Máximo 5 mascotas permitidas por póliza online.');
                return;
            }
            const newId = Date.now();
            petsData.push({ id: newId, name: '', type: 'perro', breed: 'Mestizo', age: '', gender: 'Macho', plan: '' });
            renderPetsPanel();
            validateForm();
        }

        function removePet(id) {
            petsData = petsData.filter(p => p.id !== id);
            renderPetsPanel();
            validateForm();
        }

        function updateMainPetType() {
            const t = document.getElementById('petType_1').value;
            petsData[0].type = t;
            petsData[0].breed = t === 'gato' ? 'Mestizo' : 'Mestizo';
            updateMainPet();
            renderPetsPanel();
        }

        function updateMainPet() {
            petsData[0].name = document.getElementById('petName_1').value;
            petsData[0].age = document.getElementById('petAge_1').value;
            validateForm();
        }

        function updatePanelPet(id, field, value) {
            const p = petsData.find(x => x.id === id);
            if(p) p[field] = value;
            if(id === petsData[0].id) {
                if(field === 'name') document.getElementById('petName_1').value = value;
                if(field === 'age') document.getElementById('petAge_1').value = value;
            }
            if(field === 'gender') renderPetsPanel();
            validateForm();
        }

        function updatePanelPetType(id, val) {
            const p = petsData.find(x => x.id === id);
            if(p) {
                p.type = val;
                p.breed = val === 'gato' ? 'Mestizo' : 'Mestizo';
            }
            renderPetsPanel();
            validateForm();
        }

        function validateForm() {
            let valid = true;
            petsData.forEach(p => {
                if (!p.name || p.name.trim() === '' || !p.age || p.age.toString().trim() === '') {
                    valid = false;
                }
            });

            const btn = document.getElementById('btnRecommend');
            if (valid) {
                btn.removeAttribute('disabled');
            } else {
                btn.setAttribute('disabled', 'true');
            }
        }

        // --- RESULTS AND PLANS LOGIC ---
        document.getElementById('btnRecommend').addEventListener('click', () => {
            const results = document.getElementById('resultados');
            results.classList.add('visible');
            
            document.getElementById('resultTitle').innerText = `Cotización para ${petsData.length} mascota${petsData.length > 1 ? 's' : ''}`;
            const subt = petsData.map(p => p.name).join(', ');
            document.getElementById('resultSubtitle').innerText = subt;
            
            renderPlans();
            
            const dock = document.getElementById('assignDock');
            dock.style.transform = 'translateY(0)';
            renderAssignDock();

            setTimeout(() => {
                results.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        });

        function renderPlans() {
            const list = document.getElementById('policyList');
            list.innerHTML = `
                <!-- Plan Basico -->
                <div class="veh-type-card" style="border-radius:24px; padding:24px; background:white; border: 1px solid #E2E8F0; display:flex; flex-direction:column; justify-content:space-between; position:relative; overflow:hidden;">
                    <div>
                        <img src="../assets/img/asistencias/asistencia-mascota.png" alt="Asistencia Mascota" style="max-height:80px; margin-bottom:15px; border-radius:12px;">
                        <h4 style="font-weight: 800; font-size:1.1rem;">Asistencia Mascota</h4>
                        <div style="font-size:1.4rem; color: #796BFC; font-weight:900; margin-bottom:15px;">$9.490 <small style="font-size:0.8rem; color:#94A3B8;">/ mes</small></div>
                        <ul style="list-style:none; padding:0; font-size:0.9rem; color:#475569; display:flex; flex-direction:column; gap:8px;">
                            <li><i class="fa-solid fa-check" style="color:#10B981; margin-right:5px;"></i> Reembolso rápido</li>
                            <li><i class="fa-solid fa-check" style="color:#10B981; margin-right:5px;"></i> Asistencia veterinaria 24/7</li>
                        </ul>
                    </div>
                </div>

                <!-- Plan Pro -->
                <div class="veh-type-card" style="border-radius:24px; padding:24px; background:white; border: 2px solid #796BFC; display:flex; flex-direction:column; justify-content:space-between; position:relative; overflow:hidden; box-shadow:0 10px 25px rgba(121,107,252,0.15);">
                    <div style="position:absolute; top:0; left:0; right:0; height:4px; background:linear-gradient(90deg, #796BFC, #0F766E);"></div>
                    <div>
                        <span style="position:absolute; top:15px; right:15px; background:rgba(121,107,252,0.1); color:#796BFC; padding:4px 10px; border-radius:999px; font-size:10px; font-weight:800;">RECOMENDADO</span>
                        <img src="../assets/img/asistencias/asistencia-mascota-pro.png" alt="Asistencia Mascota Pro" style="max-height:80px; margin-bottom:15px; border-radius:12px;">
                        <h4 style="font-weight: 800; font-size:1.1rem;">Asistencia Mascota Pro</h4>
                        <div style="font-size:1.4rem; color: #796BFC; font-weight:900; margin-bottom:15px;">$12.490 <small style="font-size:0.8rem; color:#94A3B8;">/ mes</small></div>
                        <ul style="list-style:none; padding:0; font-size:0.9rem; color:#475569; display:flex; flex-direction:column; gap:8px;">
                            <li><i class="fa-solid fa-check" style="color:#10B981; margin-right:5px;"></i> Reembolso rápido</li>
                            <li><i class="fa-solid fa-check" style="color:#10B981; margin-right:5px;"></i> Asistencia veterinaria 24/7</li>
                            <li><i class="fa-solid fa-check" style="color:#10B981; margin-right:5px;"></i> Coberturas ampliadas (cirugías)</li>
                        </ul>
                    </div>
                </div>

                <!-- Plan Senior -->
                <div class="veh-type-card" style="border-radius:24px; padding:24px; background:white; border: 1px solid #E2E8F0; display:flex; flex-direction:column; justify-content:space-between; position:relative; overflow:hidden;">
                    <div>
                        <img src="../assets/img/asistencias/asistencia-mascota-senior.png" alt="Asistencia Mascota Senior" style="max-height:80px; margin-bottom:15px; border-radius:12px;">
                        <h4 style="font-weight: 800; font-size:1.1rem;">Asistencia Mascota Senior</h4>
                        <div style="font-size:1.4rem; color: #796BFC; font-weight:900; margin-bottom:15px;">$16.490 <small style="font-size:0.8rem; color:#94A3B8;">/ mes</small></div>
                        <ul style="list-style:none; padding:0; font-size:0.9rem; color:#475569; display:flex; flex-direction:column; gap:8px;">
                            <li><i class="fa-solid fa-check" style="color:#10B981; margin-right:5px;"></i> Ingreso: +10 años</li>
                            <li><i class="fa-solid fa-check" style="color:#10B981; margin-right:5px;"></i> Asistencia veterinaria 24/7</li>
                        </ul>
                    </div>
                </div>
            `;
        }

        function renderAssignDock() {
            const container = document.getElementById('assignPetsContainer');
            container.innerHTML = '';

            petsData.forEach((p) => {
                const div = document.createElement('div');
                div.style.display = 'flex';
                div.style.flexDirection = 'column';
                div.style.gap = '5px';
                div.style.padding = '10px';
                div.style.background = '#F8FAFC';
                div.style.borderRadius = '8px';
                div.style.border = '1px solid #E2E8F0';

                const name = p.name || `Mascota ${p.id}`;
                const icon = p.type === 'gato' ? '<i class="fa-solid fa-cat" style="color:#796BFC;"></i>' : '<i class="fa-solid fa-dog" style="color:#796BFC;"></i>';

                div.innerHTML = `
                    <span style="font-size: 0.9rem; font-weight: 700; color: #0F172A;">${icon} ${name}</span>
                    <select onchange="assignPlan(${p.id}, this.value)" style="padding: 8px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 0.85rem; background: white; outline:none;">
                        <option value="" disabled selected>Asignar un plan...</option>
                        <option value="basico">Asistencia Mascota ($9.490)</option>
                        <option value="pro">Asistencia Mascota Pro ($12.490)</option>
                        <option value="senior">Asistencia Mascota Senior ($16.490)</option>
                    </select>
                `;
                container.appendChild(div);
            });
            checkContinueBtn();
        }

        function assignPlan(petId, planValue) {
            const p = petsData.find(x => x.id === petId);
            if(p) p.plan = planValue;
            checkContinueBtn();
        }

        function checkContinueBtn() {
            const btn = document.getElementById('btnContinuarResumen');
            const allAssigned = petsData.every(p => p.plan && p.plan !== '');
            if(allAssigned) {
                btn.style.opacity = '1';
                btn.style.pointerEvents = 'auto';
                btn.style.background = 'linear-gradient(135deg, #10B981 0%, #0F766E 100%)';
            } else {
                btn.style.opacity = '0.5';
                btn.style.pointerEvents = 'none';
                btn.style.background = '';
            }
        }

        function irAResumen() {
            sessionStorage.setItem('mhm_mascotas_data', JSON.stringify(petsData));
            window.location.href = 'cotizacion-mascota-nueva-resumen.html';
        }

        document.addEventListener('DOMContentLoaded', () => {
            renderPetsPanel();
            validateForm();
        });
    </script>
</body>
"""

content = content.replace('</body>', js_script)

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated new Mascotas HTML based perfectly on Salud template.")
