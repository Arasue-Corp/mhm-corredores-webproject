import re

with open('cotizacion/cotizacion-mascota-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need everything up to <div class="page-wrapper">
header_match = re.search(r'([\s\S]*?<div class="page-wrapper">\s*)', content)
header = header_match.group(1)

# We need the footer part. It starts around <footer class="footer-aurora">
# Let's find the end of page-wrapper. Actually, let's just find footer.
footer_match = re.search(r'(\s*<footer class="footer-aurora">[\s\S]*)', content)
footer = footer_match.group(1)

body = """
        <div class="wizard-container">
            <div class="wizard-top">
                <div class="wizard-title"><i class="fa-solid fa-paw"></i> Calcula tu seguro ideal</div>
                <div class="wizard-title"><i class="fa-solid fa-shield-halved"></i> MHM Mascotas</div>
            </div>
            <div class="progress-track"><div class="progress-fill" style="width: 25%;"></div></div>
            <div class="header-split"></div>
            <header class="brand-page-header">
                <div class="title-group">
                    <h1 class="text-gradient-corp">Seguro de Mascotas a tu Medida</h1>
                    <div class="aurora-line"></div> 
                </div>
                <p>Ingresa la información de tus mascotas para mostrarte las mejores opciones.</p>
            </header>
        </div>

        <div class="specs-layout-grid" id="recomendador">
            <div class="main-spec-col" style="grid-column: 1 / -1;">
                <div class="premium-white-card" style="max-width: 800px; margin: 0 auto; padding: 40px 30px;">
                    <div style="margin-bottom: 25px; text-align: center;">
                        <h2 style="font-size: 1.5rem; color: #0F172A; font-weight: 800; margin-bottom: 10px;">¿Cuántas mascotas deseas asegurar?</h2>
                        <select id="petQuantity" style="padding: 12px 20px; font-size: 1.1rem; border: 2px solid #E2E8F0; border-radius: 12px; width: 120px; text-align: center; font-weight: 600; color: #334155; outline: none; background: #F8FAFC; cursor: pointer; transition: border-color 0.3s ease;">
                            <option value="1" selected>1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select>
                    </div>

                    <div id="petFormsContainer" style="display: flex; flex-direction: column; gap: 20px;">
                        <!-- Dynamic pet forms will be injected here -->
                    </div>

                    <div style="margin-top: 30px; text-align: center;">
                        <button id="btnCotizarAhora" class="btn-primary-premium" style="max-width: 300px; margin: 0 auto; font-size: 1.1rem; padding: 16px;">
                            <span>Cotizar ahora</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- RESULTADOS (HIDDEN INITIALLY) -->
        <div id="resultados" style="opacity: 0; visibility: hidden; transition: all 0.5s ease; padding-top: 40px; margin-bottom: 80px;">
            <div style="text-align: center; margin-bottom: 40px;">
                <h2 style="font-size: 2rem; color: #0F172A; font-weight: 800;">Planes Disponibles</h2>
                <p style="color: #64748B; font-size: 1.1rem;">Selecciona el plan ideal para cada una de tus mascotas.</p>
            </div>

            <div class="veh-type-grid" id="policyList">
                <!-- PLANS -->
                <!-- Plan 1 -->
                <div class="veh-type-card" id="plan-basico">
                    <div class="vt-image">
                        <img src="../assets/img/asistencias/asistencia-mascota.png" alt="Asistencia Mascota">
                    </div>
                    <div class="vt-info">
                        <h4>Asistencia Mascota</h4>
                        <div class="plan-price">$9.490 / mes</div>
                        <ul class="pet-feature-list">
                            <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                            <li><i class="fa-solid fa-check"></i> Asistencia 24/7</li>
                            <li><i class="fa-solid fa-check"></i> Ingreso: 0 hasta 9 años con 365 días</li>
                        </ul>
                    </div>
                </div>

                <!-- Plan 2 -->
                <div class="veh-type-card pro-card" id="plan-pro">
                    <div class="card-aurora-top"></div>
                    <div class="vt-image">
                        <img src="../assets/img/asistencias/asistencia-mascota-pro.png" alt="Asistencia Mascota Pro">
                    </div>
                    <div class="vt-info">
                        <span class="badge-recomendado" style="margin-bottom: 10px;">Recomendado</span>
                        <h4>Asistencia Mascota Pro</h4>
                        <div class="plan-price">$12.490 / mes</div>
                        <ul class="pet-feature-list">
                            <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                            <li><i class="fa-solid fa-check"></i> Asistencia 24/7</li>
                            <li><i class="fa-solid fa-check"></i> Coberturas ampliadas (Gastos, cirugías)</li>
                        </ul>
                    </div>
                </div>

                <!-- Plan 3 -->
                <div class="veh-type-card" id="plan-senior">
                    <div class="vt-image">
                        <img src="../assets/img/asistencias/asistencia-mascota-senior.png" alt="Asistencia Mascota Senior">
                    </div>
                    <div class="vt-info">
                        <h4>Asistencia Mascota Senior</h4>
                        <div class="plan-price">$16.490 / mes</div>
                        <ul class="pet-feature-list">
                            <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                            <li><i class="fa-solid fa-check"></i> Asistencia 24/7</li>
                            <li><i class="fa-solid fa-check"></i> Ingreso: +10 años con 365 días</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div> <!-- Close page wrapper -->

    <!-- FLOATING ASSIGN DOCK -->
    <div class="compareFloatingDock" id="assignDock" style="padding: 15px 20px; background: white; border-top: 2px solid #E2E8F0; z-index: 100;">
        <div class="container" style="display: flex; flex-direction: column; gap: 15px;">
            <div style="font-weight: 700; color: #0F172A; text-align: center; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px;">
                Asigna un plan a tus mascotas
            </div>
            <div id="assignPetsContainer" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; width: 100%;">
                <!-- Dynamic assign dropdowns go here -->
            </div>
            <div style="display: flex; justify-content: center; margin-top: 10px;">
                <button type="button" class="btn-primary-premium" id="btnContinuarResumen" onclick="irAResumen()" style="width: auto; padding: 12px 30px; opacity: 0.5; pointer-events: none;">
                    <span>Continuar a Resumen</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>
    </div>
"""

scripts = """
<script>
    const dogBreeds = ["Mestizo", "Pastor Alemán", "Bulldog", "Poodle", "Labrador", "Golden Retriever", "Chihuahua", "Pug", "Otro"];
    const catBreeds = ["Mestizo", "Persa", "Siamés", "Maine Coon", "Esfinge", "Bengalí", "Angora", "Otro"];

    let petsData = [];

    function renderPetForms() {
        const qty = parseInt(document.getElementById('petQuantity').value) || 1;
        const container = document.getElementById('petFormsContainer');
        container.innerHTML = '';
        petsData = [];

        for (let i = 1; i <= qty; i++) {
            petsData.push({ id: i, name: '', type: 'perro', breed: '', age: '', gender: 'Macho', plan: '' });

            const div = document.createElement('div');
            div.style.border = '1px solid #E2E8F0';
            div.style.borderRadius = '12px';
            div.style.padding = '20px';
            div.style.background = '#FFFFFF';
            div.style.boxShadow = '0 2px 8px rgba(0,0,0,0.02)';

            div.innerHTML = `
                <div style="font-weight: 700; color: #796bfc; margin-bottom: 15px; font-size: 1.1rem; border-bottom: 1px dashed #E2E8F0; padding-bottom: 10px;">
                    <i class="fa-solid fa-paw"></i> Mascota ${i}
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                    
                    <div style="display: flex; flex-direction: column; gap: 5px;">
                        <label style="font-size: 0.9rem; font-weight: 600; color: #475569;">Nombre</label>
                        <input type="text" id="petName_${i}" placeholder="Ej. Firulais" onchange="updatePetData(${i})"
                               style="padding: 10px; border: 1px solid #CBD5E1; border-radius: 8px; font-size: 0.95rem;">
                    </div>

                    <div style="display: flex; flex-direction: column; gap: 5px;">
                        <label style="font-size: 0.9rem; font-weight: 600; color: #475569;">Tipo</label>
                        <select id="petType_${i}" onchange="updatePetType(${i})"
                                style="padding: 10px; border: 1px solid #CBD5E1; border-radius: 8px; font-size: 0.95rem; background: #fff;">
                            <option value="perro">Perro</option>
                            <option value="gato">Gato</option>
                        </select>
                    </div>

                    <div style="display: flex; flex-direction: column; gap: 5px;">
                        <label style="font-size: 0.9rem; font-weight: 600; color: #475569;">Raza</label>
                        <select id="petBreed_${i}" onchange="updatePetData(${i})"
                                style="padding: 10px; border: 1px solid #CBD5E1; border-radius: 8px; font-size: 0.95rem; background: #fff;">
                            ${dogBreeds.map(b => `<option value="${b}">${b}</option>`).join('')}
                        </select>
                    </div>

                    <div style="display: flex; flex-direction: column; gap: 5px;">
                        <label style="font-size: 0.9rem; font-weight: 600; color: #475569;">Edad (años)</label>
                        <input type="number" min="0" max="25" id="petAge_${i}" placeholder="Ej. 3" onchange="updatePetData(${i})"
                               style="padding: 10px; border: 1px solid #CBD5E1; border-radius: 8px; font-size: 0.95rem;">
                    </div>

                    <div style="display: flex; flex-direction: column; gap: 5px;">
                        <label style="font-size: 0.9rem; font-weight: 600; color: #475569;">Sexo</label>
                        <select id="petGender_${i}" onchange="updatePetData(${i})"
                                style="padding: 10px; border: 1px solid #CBD5E1; border-radius: 8px; font-size: 0.95rem; background: #fff;">
                            <option value="Macho">Macho</option>
                            <option value="Hembra">Hembra</option>
                        </select>
                    </div>
                </div>
            `;
            container.appendChild(div);
        }
    }

    function updatePetType(index) {
        const typeSelect = document.getElementById(`petType_${index}`);
        const breedSelect = document.getElementById(`petBreed_${index}`);
        const type = typeSelect.value;
        const breeds = type === 'gato' ? catBreeds : dogBreeds;
        
        breedSelect.innerHTML = breeds.map(b => `<option value="${b}">${b}</option>`).join('');
        updatePetData(index);
    }

    function updatePetData(index) {
        const p = petsData.find(x => x.id === index);
        if(p) {
            p.name = document.getElementById(`petName_${index}`).value;
            p.type = document.getElementById(`petType_${index}`).value;
            p.breed = document.getElementById(`petBreed_${index}`).value;
            p.age = document.getElementById(`petAge_${index}`).value;
            p.gender = document.getElementById(`petGender_${index}`).value;
        }
    }

    document.getElementById('petQuantity').addEventListener('change', renderPetForms);

    document.getElementById('btnCotizarAhora').addEventListener('click', () => {
        // Validation basic
        let valid = true;
        petsData.forEach(p => {
            if(!p.name || !p.age) valid = false;
        });

        if(!valid) {
            alert('Por favor, completa el nombre y edad de todas las mascotas.');
            return;
        }

        const res = document.getElementById('resultados');
        res.style.opacity = '1';
        res.style.visibility = 'visible';
        
        renderAssignDock();
        
        const dock = document.getElementById('assignDock');
        dock.classList.add('visible');

        setTimeout(() => {
            res.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
    });

    function renderAssignDock() {
        const container = document.getElementById('assignPetsContainer');
        container.innerHTML = '';

        petsData.forEach((p, idx) => {
            const div = document.createElement('div');
            div.style.display = 'flex';
            div.style.flexDirection = 'column';
            div.style.gap = '5px';
            div.style.padding = '10px';
            div.style.background = '#F8FAFC';
            div.style.borderRadius = '8px';
            div.style.border = '1px solid #E2E8F0';

            const name = p.name || `Mascota ${p.id}`;
            const icon = p.type === 'gato' ? '<i class="fa-solid fa-cat"></i>' : '<i class="fa-solid fa-dog"></i>';

            div.innerHTML = `
                <span style="font-size: 0.9rem; font-weight: 700; color: #334155;">${icon} ${name}</span>
                <select id="assignPlan_${p.id}" onchange="assignPlan(${p.id}, this.value)" style="padding: 6px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 0.85rem; background: white;">
                    <option value="" disabled selected>Selecciona un plan...</option>
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
        } else {
            btn.style.opacity = '0.5';
            btn.style.pointerEvents = 'none';
        }
    }

    function irAResumen() {
        sessionStorage.setItem('mhm_mascotas_data', JSON.stringify(petsData));
        window.location.href = 'cotizacion-mascota-nueva-resumen.html';
    }

    document.addEventListener('DOMContentLoaded', () => {
        renderPetForms();
    });
</script>
"""

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'w', encoding='utf-8') as f:
    f.write(header + body + footer + scripts)

print("Generated cotizacion-mascota-nueva-1.html")
