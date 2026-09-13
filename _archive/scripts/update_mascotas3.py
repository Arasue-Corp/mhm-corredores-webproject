import re

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Gender Selector (Use flex:1, high contrast active state)
old_gender = r'<div class="segmented" style="margin-top: 4px; width: 100%;">.*?</div>'
new_gender = """<div style="display: flex; gap: 10px; margin-top: 4px; width: 100%;">
                            <button type="button" style="flex: 1; padding: 10px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.2s; border: 2px solid ${p.gender==='Macho'?'#0F766E':'#CBD5E1'}; background: ${p.gender==='Macho'?'#F0FDF4':'#FFF'}; color: ${p.gender==='Macho'?'#0F766E':'#64748B'};" onclick="updatePanelPet(${p.id}, 'gender', 'Macho')"><i class="fa-solid fa-mars"></i> Macho</button>
                            <button type="button" style="flex: 1; padding: 10px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.2s; border: 2px solid ${p.gender==='Hembra'?'#0F766E':'#CBD5E1'}; background: ${p.gender==='Hembra'?'#F0FDF4':'#FFF'}; color: ${p.gender==='Hembra'?'#0F766E':'#64748B'};" onclick="updatePanelPet(${p.id}, 'gender', 'Hembra')"><i class="fa-solid fa-venus"></i> Hembra</button>
                        </div>"""
content = re.sub(old_gender, new_gender, content, flags=re.DOTALL)


# 2. Fix renderPlans() to match EXACLY the layout of salud.css
old_render_plans = r'function renderPlans\(\) \{.*?\}\s*function renderAssignDock'
new_render_plans = """function renderPlans() {
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
                const isCompared = false; // Mock for now
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
        
        function renderAssignDock"""
content = re.sub(old_render_plans, new_render_plans, content, flags=re.DOTALL)

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied fix 3 successfully.")
