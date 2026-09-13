import re

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Gender Selection
old_gender = """<div style="display:flex; gap: 10px; margin-top:3px;">
                            <button class="stepper" style="border: 1px solid ${p.gender==='Macho'?'#0F766E':'#CBD5E1'}; background:${p.gender==='Macho'?'#F0FDF4':'#F8FAFC'}; color:#0F172A; border-radius: 6px; padding: 4px 10px; cursor:pointer;" onclick="updatePanelPet(${p.id}, 'gender', 'Macho')">Macho</button>
                            <button class="stepper" style="border: 1px solid ${p.gender==='Hembra'?'#0F766E':'#CBD5E1'}; background:${p.gender==='Hembra'?'#F0FDF4':'#F8FAFC'}; color:#0F172A; border-radius: 6px; padding: 4px 10px; cursor:pointer;" onclick="updatePanelPet(${p.id}, 'gender', 'Hembra')">Hembra</button>
                        </div>"""
new_gender = """<div class="segmented" style="margin-top: 4px; width: 100%;">
                            <button type="button" class="filterHealth ${p.gender==='Macho'?'active':''}" onclick="updatePanelPet(${p.id}, 'gender', 'Macho')">Macho</button>
                            <button type="button" class="filterHealth ${p.gender==='Hembra'?'active':''}" onclick="updatePanelPet(${p.id}, 'gender', 'Hembra')">Hembra</button>
                        </div>"""

content = content.replace(old_gender, new_gender)

# 2. Inject Filters Sidebar and restore resultsLayout
old_results_layout = r'<div class="veh-type-grid" id="policyList" style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(280px, 1fr\)\); gap: 20px; width: 100%; margin-bottom: 30px;">.*?</div>\s*<!-- Commercial Legal Disclaimer -->'
new_results_layout = """<div class="resultsLayout">
                    <!-- Left Sidebar Filters -->
                    <aside class="healthFilters is-collapsed" id="healthFilters">
                        <div class="filterHead" id="filterHeadToggle" onclick="toggleMobileFilters()">
                            <div class="filterHeadText">
                                <h3><i class="fa-solid fa-sliders filterIconTitle"></i> Refina tus resultados</h3>
                                <p>Los cambios se aplican al instante</p>
                            </div>
                            <button type="button" class="mobileFilterToggleBtn" aria-label="Mostrar u ocultar filtros">
                                <span class="mobileToggleText">Mostrar</span>
                                <i class="fa-solid fa-chevron-down toggleChevron"></i>
                            </button>
                        </div>

                        <div class="filterBody" id="filterBody">
                            <!-- Tipo de Mascota -->
                            <fieldset class="filterFieldset">
                                <legend>Especie Permitida</legend>
                                <div class="segmented">
                                    <button type="button" class="filterHealth active">Perros y Gatos</button>
                                </div>
                            </fieldset>

                            <!-- Prioridad -->
                            <fieldset class="filterFieldset">
                                <legend>Nivel de Cobertura</legend>
                                <div class="radioGroup">
                                    <label class="customRadio">
                                        <input type="radio" name="priorityRadio" value="all" checked>
                                        <span class="radioDot"></span>
                                        <span class="radioLabel">Equilibrio (Básico)</span>
                                    </label>
                                    <label class="customRadio">
                                        <input type="radio" name="priorityRadio" value="benefits">
                                        <span class="radioDot"></span>
                                        <span class="radioLabel">Reembolsos & Cirugías (Pro)</span>
                                    </label>
                                    <label class="customRadio">
                                        <input type="radio" name="priorityRadio" value="senior">
                                        <span class="radioDot"></span>
                                        <span class="radioLabel">Senior (Mascotas Mayores)</span>
                                    </label>
                                </div>
                            </fieldset>

                            <!-- Edad de Ingreso -->
                            <fieldset class="filterFieldset">
                                <legend>Edad de Ingreso</legend>
                                <div class="selectWrapper">
                                    <select class="customSelect">
                                        <option value="all">Cualquier edad</option>
                                        <option value="young">0 a 9 años</option>
                                        <option value="old">Más de 10 años</option>
                                    </select>
                                    <i class="fa-solid fa-chevron-down selectIcon"></i>
                                </div>
                            </fieldset>
                            
                            <div class="advisorMiniCard">
                                <div class="advisorIcon"><i class="fa-solid fa-headset"></i></div>
                                <div class="advisorText">
                                    <b>¿Dudas con tu plan?</b>
                                    <p>Un especialista de MHM te asesora gratis.</p>
                                </div>
                                <button type="button" class="btn-advisor-mini" onclick="window.location.href='../contacto/index.html'">
                                    Hablar con asesor
                                </button>
                            </div>
                        </div>
                    </aside>
                    
                    <!-- Policy Cards Column -->
                    <div class="healthPolicyList" id="policyList">
                        <!-- Planes inyectados via JS -->
                    </div>
                </div>

                <!-- Commercial Legal Disclaimer -->"""

# We need to remove the whole <div class="veh-type-grid"... block.
content = re.sub(old_results_layout, new_results_layout, content, flags=re.DOTALL)

# 3. Add openDetailsState map in JS and toggle function if they don't exist
if 'const openDetailsState = {};' not in content:
    content = content.replace('let petsData = [', 'const openDetailsState = {};\n        let petsData = [')

js_toggle_func = """
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
"""
if 'function togglePlanDetails' not in content:
    content = content.replace('// --- RESULTS AND PLANS LOGIC ---', js_toggle_func + '\n        // --- RESULTS AND PLANS LOGIC ---')

# 4. Rewrite renderPlans to output healthPolicyCard 
old_render_plans = r'function renderPlans\(\) \{.*?\}'
new_render_plans = """function renderPlans() {
            const list = document.getElementById('policyList');
            const plans = [
                {
                    id: 'basico',
                    planType: 'basico',
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
                    planType: 'pro',
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
                    planType: 'senior',
                    tier: 'PLAN SENIOR',
                    badgeSub: 'Para +10 años',
                    bandTheme: 'band-individual',
                    capitalUF: 'Senior',
                    capitalLabel: 'Especial mascotas mayores',
                    insurer: 'MHM · SEGURO DE MASCOTAS',
                    title: 'Asistencia Mascota Senior',
                    lead: 'Especialmente diseñado para perros y gatos de mayor edad, sin restricciones de ingreso por vejez.',
                    priceMonth: '$16.490/mes',
                    priceYear: '$197.880 anual',
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
                return `
                <article class="healthPolicyCard ${p.isRecommended ? 'recommended' : ''}">
                    ${p.isRecommended ? '<div class="policyRecommendBadge">PLAN MÁS SELECCIONADO</div>' : ''}
                    
                    <div class="policyMainRow">
                        <!-- Left Band -->
                        <div class="healthPolicyBrand ${p.bandTheme}">
                            <div class="brandLogoWrap">
                                <img src="../assets/img/logo-mhm-color.png" alt="MHM">
                            </div>
                            <b class="bandCapital">${p.capitalUF}</b>
                            <small class="bandSub"><strong>${p.badgeSub}</strong><br>${p.capitalLabel}</small>
                        </div>

                        <!-- Right Policy Content -->
                        <div class="healthPolicyContent">
                            <div class="policyMeta">
                                <span class="insurerTag">${p.insurer}</span>
                                <div class="metaBadges">
                                    ${p.isRecommended ? `<span class="badge-best-match"><i class="fa-solid fa-star" style="color: #2ED9C3; margin-right: 4px;"></i>MEJOR COINCIDENCIA</span>` : ''}
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
                                <div class="priceBox" style="text-align: right;">
                                    <div style="font-size: 1.3rem; font-weight: 900; color: #0F172A;">${p.priceMonth}</div>
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
                                        <h5>Coberturas principales</h5>
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
                                        <h5>Exclusiones importantes</h5>
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
        }"""

content = re.sub(old_render_plans, new_render_plans, content, flags=re.DOTALL)

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script executed successfully.")
