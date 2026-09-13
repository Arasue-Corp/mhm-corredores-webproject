                <a href="../index.html">Volver to Home <i class="fa-solid fa-arrow-right"></i></a>
            </div>
        </div>
        <button class="floating-menu-btn js-toggle-mega-menu" aria-label="Open menu">
            <i class="fa-regular fa-compass"></i>
        </button>
    </div>

    <div id="floating-chat-container">
        <div class="alex-chat-window" id="chatWindow">
            <div class="chat-header">
                <div class="agent-info">
                    <div class="agent-avatar"><i class="fa-solid fa-robot"></i><div class="status-dot"></div></div>
                    <div class="agent-text">
                        <span class="name">Asistente MHM</span>
                        <span class="status">Tiempo de respuesta: Inmediato</span>
                    </div>
                </div>
                <button class="close-chat-btn js-close-chat"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <div class="chat-body">
                <div class="chat-timestamp">Hoy, 17:00</div>
                
                <div class="msg-row bot">
                    <div class="msg-bubble">
                        ¡Hola! Veo que estás cotizando. ¿Tienes alguna pregunta sobre el <strong>Deducible</strong> o las coberturas? 🚗
                    </div>
                </div>
                
                <div class="chat-suggestions">
                    <button>Explicar Deducibles</button>
                    <button>Hablar con Ejecutivo</button>
                </div>
            </div>
            
            <div class="chat-footer">
                <input type="text" placeholder="Escribe tu pregunta..." class="chat-input">
                <button class="send-btn"><i class="fa-solid fa-paper-plane"></i></button>
            </div>
        </div>

        <button class="chat-avatar-btn js-trigger-chat" aria-label="Chat with support">
            <i class="fa-solid fa-comment-dots"></i>
            <span class="online-badge"></span>
        </button>
    </div>

    <script src="../js/script.js?v=6"></script>
    

    

                <!-- Modal Leads -->
<div class="lead-modal-overlay" id="leadModal">
    

    <div class="lead-modal">
        <button class="lead-close" onclick="closeLeadModal()"><i class="fa-solid fa-xmark"></i></button>
        
        <div id="leadContent">
            <div class="lead-header">
                <img src="../assets/img/logo-mhm-color.png" alt="MHM Corredores de Seguros, corredora de seguros en Chile especializada en seguros para personas y empresas." class="lead-logo">
                <h3>Diseñemos tu seguro</h3>
                <p>Déjanos tus datos y un Agente especialista de MHM te contactará con una propuesta a medida.</p>
            </div>
            
            <div class="lead-form-group">
                <input type="text" class="lead-input validate-req" placeholder=" " id="leadName">
                <label class="floating-label">Nombre Completo</label>
            </div>
            <div class="lead-form-group">
                <input type="email" class="lead-input validate-req" placeholder=" " id="leadEmail">
                <label class="floating-label">Correo Electrónico</label>
            </div>
            <div class="lead-form-group">
                <input type="tel" class="lead-input validate-req" placeholder=" " id="leadPhone">
                <label class="floating-label">Teléfono</label>
            </div>
            
            <button class="lead-submit" onclick="submitLead()">Enviar Solicitud <i class="fa-solid fa-paper-plane"></i></button>
        </div>
        
        <div class="lead-success" id="leadSuccess">
            <div class="success-graphic">
                <div class="success-bg"></div>
                <div class="success-icon"><i class="fa-solid fa-circle-check"></i></div>
            </div>
            <h3>¡Todo listo!</h3>
            <p>Hemos recibido tus datos correctamente. Un ejecutivo de MHM Seguros se contactará contigo a la brevedad para asesorarte y ofrecerte la mejor tarifa.</p>
            <button class="lead-submit" onclick="window.location.href='cotizacion.html'" style="margin-top: 30px;">Volver a Productos</button>
        </div>
    </div>
</div>


    <!-- Custom Logic for the form Mascotas -->
    <script>
        const dogBreeds = ["Mestizo", "Pastor Alemán", "Bulldog", "Poodle", "Labrador", "Golden Retriever", "Chihuahua", "Pug", "Otro"];
        const catBreeds = ["Mestizo", "Persa", "Siamés", "Maine Coon", "Esfinge", "Bengalí", "Angora", "Otro"];

        const openDetailsState = {};
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
            const path = e.composedPath();
            if (!path.includes(btnAssuredOpen) && !path.includes(assuredPanel)) {
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
                        <div style="display: flex; gap: 10px; margin-top: 4px; width: 100%;">
                            <button type="button" id="btn_macho_${p.id}" class="gender-btn ${p.gender==='Macho'?'active':''}" onclick="setGender(${p.id}, 'Macho')"><i class="fa-solid fa-mars"></i> Macho</button>
                            <button type="button" id="btn_hembra_${p.id}" class="gender-btn ${p.gender==='Hembra'?'active':''}" onclick="setGender(${p.id}, 'Hembra')"><i class="fa-solid fa-venus"></i> Hembra</button>
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

        
        function setGender(id, gender) {
            // Update data
            const p = petsData.find(x => x.id === id);
            if(p) p.gender = gender;
            
            // Update DOM directly without destroying panel
            const btnMacho = document.getElementById(`btn_macho_${id}`);
            const btnHembra = document.getElementById(`btn_hembra_${id}`);
            
            if (btnMacho && btnHembra) {
                if (gender === 'Macho') {
                    btnMacho.classList.add('active');
                    btnHembra.classList.remove('active');
                } else {
                    btnHembra.classList.add('active');
                    btnMacho.classList.remove('active');
                }
            }
        }

        function updatePanelPet(id, field, value) {
            const p = petsData.find(x => x.id === id);
            if(p) p[field] = value;
            if(id === petsData[0].id) {
                if(field === 'name') document.getElementById('petName_1').value = value;
                if(field === 'age') document.getElementById('petAge_1').value = value;
            }
            // gender is handled by setGender
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

        
        function togglePlanDetails(planId) {
            openDetailsState[planId] = !openDetailsState[planId];
            const drawer = document.getElementById(`details-${planId}`);
            const btn = document.getElementById(`btn-toggle-${planId}`);
            if (drawer && btn) {
                if (openDetailsState[planId]) {
                    drawer.classList.add('open');
                    btn.innerHTML = '<span>Cerrar detalles</span> <i class="fa-solid fa-chevron-up"></i>';
                } else {
                    drawer.classList.remove('open');
                    btn.innerHTML = '<span>Ver detalles</span> <i class="fa-solid fa-chevron-down"></i>';
                }
            }
        }
        
        function toggleMobileFilters() {
            const sidebar = document.getElementById('healthFilters');
            if(sidebar) sidebar.classList.toggle('is-collapsed');
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
            checkAssigns();

            setTimeout(() => {
                results.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        });

        function renderPlans() {
            const list = document.getElementById('policyList');
            const plans = [
                {
                    id: 'basico',
                    planType: 'individual',
                    tier: 'PLAN BÁSICO',
                    badgeSub: 'Para tu mascota',
                    bandTheme: 'band-individual',
                    capitalUF: 'Asistencia',
                    capitalLabel: 'Cobertura esencial',
                    insurer: 'MHM · SEGURO DE MASCOTAS',
                    title: 'Asistencia Mascota',
                    lead: 'Cobertura esencial con asistencias veterinarias y reembolsos rápidos.',
                    priceMonth: '$9.490/mes',
                    priceYear: '$113.880 anual',
                    bestMatchBadge: '',
                    match: '85',
                    isRecommended: false,
                    quickBenefits: [
                        'Reembolso rápido',
                        'Asistencia veterinaria 24/7'
                    ],
                    coberturas: [
                        'Asistencia veterinaria 24/7 (Telefónica y Online)',
                        'Reembolso rápido por gastos médicos por accidente (hasta topes)',
                        'Consulta veterinaria a domicilio (1 evento anual)'
                    ],
                    adicionales: [
                        'Descuentos en farmacias veterinarias adheridas',
                        'Orientación legal telefónica en caso de daños a terceros',
                        'Servicio de cremación (hasta 5 UF)'
                    ],
                    exclusiones: [
                        'No cubre enfermedades preexistentes.',
                        'Edad máxima de ingreso: 9 años.',
                        'No cubre vacunas ni tratamientos estéticos.'
                    ]
                },
                {
                    id: 'pro',
                    planType: 'familiar',
                    tier: 'PLAN PRO (RECOMENDADO)',
                    badgeSub: 'Máxima protección',
                    bandTheme: 'band-familiar',
                    capitalUF: 'Cirugías',
                    capitalLabel: 'Cobertura ampliada',
                    insurer: 'MHM · SEGURO DE MASCOTAS',
                    title: 'Asistencia Mascota Pro',
                    lead: 'El plan más completo que incluye cirugías y mayores topes de reembolso.',
                    priceMonth: '$12.490/mes',
                    priceYear: '$149.880 anual',
                    bestMatchBadge: 'MEJOR COINCIDENCIA',
                    match: '98',
                    isRecommended: true,
                    quickBenefits: [
                        'Reembolso rápido',
                        'Asistencia veterinaria 24/7',
                        'Coberturas ampliadas (cirugías)'
                    ],
                    coberturas: [
                        'Asistencia veterinaria 24/7 ilimitada',
                        'Reembolso en consultas, exámenes y cirugías por enfermedad/accidente',
                        'Responsabilidad civil por daños a terceros (hasta 10 UF)'
                    ],
                    adicionales: [
                        'Gastos de estadía en hotel para mascotas por hospitalización del dueño',
                        'Vacunación anual (1 evento)',
                        'Descuentos premium en farmacias veterinarias'
                    ],
                    exclusiones: [
                        'Carencia de 30 días para enfermedades generales.',
                        'Edad máxima de ingreso: 9 años.',
                        'Excluye cría y parto.'
                    ]
                },
                {
                    id: 'senior',
                    planType: 'individual',
                    tier: 'PLAN SENIOR',
                    badgeSub: 'Para +10 años',
                    bandTheme: 'band-individual',
                    capitalUF: 'Senior',
                    capitalLabel: 'Mascotas mayores',
                    insurer: 'MHM · SEGURO DE MASCOTAS',
                    title: 'Asistencia Mascota Senior',
                    lead: 'Especialmente diseñado para perros y gatos de mayor edad.',
                    priceMonth: '$16.490/mes',
                    priceYear: '$197.880 anual',
                    bestMatchBadge: '',
                    match: '90',
                    isRecommended: false,
                    quickBenefits: [
                        'Ingreso: +10 años',
                        'Asistencia veterinaria 24/7',
                        'Control geriátrico preventivo'
                    ],
                    coberturas: [
                        'Asistencia veterinaria 24/7',
                        'Reembolso de gastos médicos urgentes',
                        'Control geriátrico preventivo anual'
                    ],
                    adicionales: [
                        'Asistencia especial por fallecimiento',
                        'Descuentos en medicamentos de uso crónico',
                        'Consultas a domicilio preferenciales'
                    ],
                    exclusiones: [
                        'No cubre cirugías de alta complejidad.',
                        'Exclusivo para mascotas de 10 años o más.',
                        'Topes de reembolso reducidos frente a planes estándar.'
                    ]
                }
            ];

            list.innerHTML = plans.map(p => {
                const isDetailsOpen = !!openDetailsState[p.id];
                const isCompared = selectedForCompare.has(p.id);
                return `
                <article class="healthPolicyCard ${p.planType === 'individual' ? 'card-individual' : 'card-familiar'} ${p.isRecommended ? 'recommended' : ''}" id="card-${p.id}">
                    <div class="cardTopRow">
                        <!-- Left Side Ribbon Band -->
                        <div class="policyBand ${p.bandTheme}">
                            <span class="bandTier">${p.tier}</span>
                            <div class="healthMark" title="Aseguradora">
                                <img src="../assets/img/logo-mhm-color.png" alt="MHM" class="mapfreLogoImg" style="width: 40px;">
                            </div>
                            <b class="bandCapital">${p.capitalUF}</b>
                            <small class="bandSub"><strong>${p.badgeSub}</strong><br>${p.capitalLabel}</small>
                        </div>

                        <!-- Right Policy Content -->
                        <div class="healthPolicyContent">
                            <div class="policyMeta">
                                <span class="insurerTag">${p.insurer}</span>
                                <div class="metaBadges">
                                    ${p.bestMatchBadge ? `<span class="badge-best-match"><i class="fa-solid fa-star" style="color: #2ED9C3; margin-right: 4px;"></i>${p.bestMatchBadge}</span>` : ''}
                                    <span class="badge-affinity">${p.match}% afinidad</span>
                                </div>
                            </div>

                            <h3 class="planTitle">${p.title}</h3>
                            <p class="planLead">${p.lead}</p>

                            <div class="healthBenefitsGrid">
                                ${p.quickBenefits.map(b => `
                                    <div class="benefitItem">
                                        <i class="fa-solid fa-check"></i>
                                        <span>${b}</span>
                                    </div>
                                `).join('')}
                            </div>

                            <div class="policyActionsRow">
                                <button type="button" class="btn-details-toggle" id="btn-toggle-${p.id}" onclick="togglePlanDetails('${p.id}')">
                                    <span>${isDetailsOpen ? 'Cerrar detalles' : 'Ver detalles'}</span>
                                    <i class="fa-solid ${isDetailsOpen ? 'fa-chevron-up' : 'fa-chevron-down'}"></i>
                                </button>
                                <div style="display:flex; flex-direction:column; align-items:flex-end;">
                                    <span class="priceMetaLabel" style="font-size:10px; color:#64748B;">PRIMA MENSUAL</span>
                                    <div style="font-size: 1.5rem; font-weight: 800; color: #0F172A;">${p.priceMonth}</div>
                                    <div class="compareCheckRow" style="margin-top: 5px;">
                                        <label class="custom-compare-label">
                                            <input type="checkbox" class="compare-checkbox" ${isCompared ? 'checked' : ''} onchange="handleCompareChange('${p.id}', this.checked)">
                                            <span>Comparar</span>
                                        </label>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- PET ASSIGNMENT PILLS -->
                            <div class="pet-assign-area">
                                <span class="pet-pills-label">Asignar plan a:</span>
                                <div class="pet-pills-container">
                                    ${petsData.map(pet => {
                                        const isAssigned = pet.plan === p.id;
                                        return `<button type="button" class="pet-pill ${isAssigned ? 'active' : ''}" onclick="assignPlanToPet(${pet.id}, '${p.id}')">
                                                    <i class="fa-solid ${pet.type === 'gato' ? 'fa-cat' : 'fa-dog'}"></i>
                                                    ${pet.name || 'Mascota'}
                                                </button>`;
                                    }).join('')}
                                </div>
                            </div>
                        </div>
                    </div>
                        </div>
                    </div>

                    <!-- Expandable Nested Drawer -->
                    <div class="policyDetailsDrawer ${isDetailsOpen ? 'open' : ''}" id="details-${p.id}">
                        <div class="drawerInner">
                            <div class="drawerHeader">
                                <div class="drawerHeaderLeft">
                                    <span class="drawerTier">${p.tier}</span>
                                    <h4 class="drawerTitle">${p.title}</h4>
                                    <span class="drawerInsurer">${p.insurer}</span>
                                </div>
                                <div class="drawerHeaderRight">
                                    <span class="priceMetaLabel">PRIMA MENSUAL</span>
                                    <div class="priceMain">${p.priceMonth}</div>
                                    <small class="priceAnnual">${p.priceYear}</small>
                                </div>
                            </div>

                            <p class="drawerLead">${p.lead}</p>

                            <div class="detailsCols3">
                                <div class="detailCard detailCard-coberturas">
                                    <div class="detailCardHead">
                                        <i class="fa-solid fa-shield-halved"></i>
                                        <h5>Coberturas</h5>
                                    </div>
                                    <ul class="detailList checkList">
                                        ${p.coberturas.map(c => `
                                            <li><i class="fa-solid fa-check"></i> <span>${c}</span></li>
                                        `).join('')}
                                    </ul>
                                </div>

                                <div class="detailCard detailCard-asistencias">
                                    <div class="detailCardHead">
                                        <i class="fa-solid fa-plus"></i>
                                        <h5>Adicionales y asistencias</h5>
                                    </div>
                                    <ul class="detailList plusList">
                                        ${p.adicionales.map(a => `
                                            <li><i class="fa-solid fa-plus"></i> <span>${a}</span></li>
                                        `).join('')}
                                    </ul>
                                </div>

                                <div class="detailCard detailCard-exclusiones">
                                    <div class="detailCardHead">
                                        <i class="fa-solid fa-circle-info"></i>
                                        <h5>Exclusiones relevantes</h5>
                                    </div>
                                    <ul class="detailList bulletList">
                                        ${p.exclusiones.map(e => `
                                            <li><span>•</span> <span>${e}</span></li>
                                        `).join('')}
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </article>
                `;
            }).join('');
        }
        
        function assignPlanToPet(petId, planId) {
            const pet = petsData.find(p => p.id === petId);
            if(pet) {
                // Toggle off if already assigned to this plan
                if(pet.plan === planId) {
                    pet.plan = '';
                } else {
                    pet.plan = planId;
                }
            }
            // Re-render plans to update pills
            renderPlans();
            checkAssigns();
        }

        function checkAssigns() {
            const total = petsData.length;
            const assigned = petsData.filter(p => p.plan && p.plan !== '').length;
            
            const stickyBar = document.getElementById('stickyCheckout');
            const statusTitle = document.getElementById('checkoutStatusTitle');
            const btn = document.getElementById('btnStickyCheckout');
            
            if(stickyBar) stickyBar.classList.add('visible');
            
            if(statusTitle) {
                statusTitle.textContent = `${assigned} de ${total} mascota${total > 1 ? 's' : ''} asignada${total > 1 ? 's' : ''}`;
            }
            
            if(assigned === total && total > 0) {
                if(btn) btn.classList.add('active');
            } else {
                if(btn) btn.classList.remove('active');
            }
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
    
        const selectedForCompare = new Set();
        const MAX_COMPARE = 3;

        function handleCompareChange(planId, checked) {
            if (checked) {
                if (selectedForCompare.size >= MAX_COMPARE) {
                    alert(`Puedes comparar hasta ${MAX_COMPARE} planes a la vez.`);
                    renderPetsPanel(); // reset checkbox UI
                    return;
                }
                selectedForCompare.add(planId);
            } else {
                selectedForCompare.delete(planId);
            }
            updateCompareDock();
            
            // Re-render to ensure checkboxes stay in sync
            // Actually, we don't want to re-render the whole panel just for the checkbox, 
            // but we don't have petsData global for renderPlans outside of the function.
            // Wait, we can just let it be, the checkbox checked state is correct!
        }

        function updateCompareDock() {
            const dock = document.getElementById('compareDock');
            const text = document.getElementById('compareDockText');
            if (!dock) return;

            if (selectedForCompare.size > 0) {
                dock.classList.add('visible');
                text.innerText = selectedForCompare.size === 1 
                    ? '1 plan seleccionado para comparar' 
                    : `${selectedForCompare.size} planes seleccionados para comparar`;
            } else {
