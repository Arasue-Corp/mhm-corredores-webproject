import re

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add compareCheckRow to the template in renderPlans
old_actions_row = r'(<div class="policyActionsRow">.*?</div>)'
new_actions_row = r'''\1
                            <div class="compareCheckRow">
                                <label class="custom-compare-label">
                                    <input type="checkbox" class="compare-checkbox" ${isCompared ? 'checked' : ''} onchange="handleCompareChange('${p.id}', this.checked)">
                                    <span>Agregar a comparación</span>
                                </label>
                            </div>'''
# Only do this if we haven't already
if 'compareCheckRow' not in content:
    content = re.sub(old_actions_row, new_actions_row, content, flags=re.DOTALL)

# 2. Add Floating Dock and Modal HTML before </section> (the one closing healthResults)
html_to_inject = """
            <!-- Floating Compare Dock -->
            <div class="compareFloatingDock" id="compareDock">
                <div class="compareDockInner">
                    <div class="compareDockInfo">
                        <i class="fa-solid fa-code-compare"></i>
                        <span id="compareDockText">2 planes seleccionados para comparar</span>
                    </div>
                    <div class="compareDockActions">
                        <button type="button" class="btn-view-compare" onclick="openCompareModal()">
                            <span>Ver comparativa frente a frente</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                        <button type="button" class="btn-clear-compare" onclick="clearComparison()" title="Limpiar comparación">
                            <i class="fa-solid fa-xmark"></i>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Compare Modal -->
            <div class="compareModalOverlay" id="compareModal" onclick="closeCompareModal(event)">
                <div class="compareModalBox" style="max-width: 900px;">
                    <button type="button" class="compareModalClose" onclick="closeCompareModal()"><i class="fa-solid fa-xmark"></i></button>
                    <div class="compareModalHead">
                        <span class="compareModalTag">COMPARATIVA EXCLUSIVA</span>
                        <h3>Seguros de Mascotas</h3>
                        <p>Compara directamente las coberturas, asistencias y tarifas para decidir con total claridad.</p>
                    </div>
                    <div class="compareModalTableWrapper" id="compareTableContent">
                        <!-- Dynamic table rendered here -->
                    </div>
                </div>
            </div>
"""

if 'compareFloatingDock' not in content:
    # Find the closing tag of healthResults
    content = content.replace('</section>\n    </main>', html_to_inject + '\n        </section>\n    </main>')

# 3. Add Javascript logic
js_logic = """
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
                dock.classList.remove('visible');
            }
        }

        function clearComparison() {
            selectedForCompare.clear();
            updateCompareDock();
            document.querySelectorAll('.compare-checkbox').forEach(cb => cb.checked = false);
        }

        function getPlanData(id) {
            const plans = [
                {
                    id: 'basico',
                    planType: 'individual',
                    tier: 'PLAN BÁSICO',
                    title: 'Asistencia Mascota',
                    priceMonth: '$9.490',
                    priceYear: '($113.880/año)',
                    desc: 'Cobertura esencial con asistencias veterinarias.',
                    cols: [
                        { cat: 'Urgencias', val: 'Reembolso rápido por accidente' },
                        { cat: 'Cirugías', val: 'No cubre' },
                        { cat: 'Asistencia 24/7', val: 'Sí, Telefónica y Online' },
                        { cat: 'Edad Máxima', val: '9 años' }
                    ]
                },
                {
                    id: 'pro',
                    planType: 'familiar',
                    tier: 'PLAN PRO (RECOMENDADO)',
                    title: 'Asistencia Mascota Pro',
                    priceMonth: '$12.490',
                    priceYear: '($149.880/año)',
                    desc: 'El plan más completo que incluye cirugías.',
                    cols: [
                        { cat: 'Urgencias', val: 'Reembolso en consultas, exámenes' },
                        { cat: 'Cirugías', val: '<strong style="color:#0F766E">Sí, incluidas</strong>' },
                        { cat: 'Asistencia 24/7', val: 'Sí, Ilimitada' },
                        { cat: 'Edad Máxima', val: '9 años' }
                    ]
                },
                {
                    id: 'senior',
                    planType: 'individual',
                    tier: 'PLAN SENIOR',
                    title: 'Asistencia Mascota Senior',
                    priceMonth: '$16.490',
                    priceYear: '($197.880/año)',
                    desc: 'Diseñado para perros y gatos de mayor edad.',
                    cols: [
                        { cat: 'Urgencias', val: 'Reembolso de gastos urgentes' },
                        { cat: 'Cirugías', val: 'No cubre alta complejidad' },
                        { cat: 'Asistencia 24/7', val: 'Sí, Telefónica y Online' },
                        { cat: 'Edad Máxima', val: '+10 años (Exclusivo)' }
                    ]
                }
            ];
            return plans.find(p => p.id === id);
        }

        function openCompareModal() {
            const modal = document.getElementById('compareModal');
            const container = document.getElementById('compareTableContent');
            if (!modal || !container || selectedForCompare.size === 0) return;

            const selectedIds = Array.from(selectedForCompare);
            const plans = selectedIds.map(id => getPlanData(id));
            
            // Build Hero Cards
            const heroCardsHtml = plans.map(p => `
                <div class="compareHeroCard ${p.planType === 'individual' ? 'card-ind-hero' : 'card-fam-hero'}" style="flex: 1; min-width: 250px;">
                    <div class="compareHeroCardHead">
                        <div class="heroCardLogo">
                            <img src="../assets/img/logo-mhm-color.png" alt="MHM" style="width: 40px;">
                        </div>
                        <span class="heroCardTierBadge">${p.tier}</span>
                    </div>
                    <h4 class="heroCardTitle">${p.title}</h4>
                    <div class="heroCardPrice">
                        <strong>${p.priceMonth}</strong> <span>/ mes</span>
                        <small style="color: #64748B; margin-left: 8px;">${p.priceYear}</small>
                    </div>
                    <p style="font-size: 12px; color: #64748B; margin: 0;">${p.desc}</p>
                    <button type="button" class="btn-contratar-action" style="width: 100%; margin-top: 8px; font-size: 13px; padding: 10px 18px;" onclick="closeCompareModal(); alert('Contratando ' + '${p.title}');">
                        <span>Contratar</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            `).join('');

            // Build Table Rows
            const categories = [
                { id: 'Urgencias', icon: 'fa-truck-medical', color: 'var(--color-primary)', label: 'Atención de Urgencias' },
                { id: 'Cirugías', icon: 'fa-scalpel', color: '#10B981', label: 'Cirugías y Especialidades' },
                { id: 'Asistencia 24/7', icon: 'fa-phone', color: '#F59E0B', label: 'Asistencia y Telemedicina' },
                { id: 'Edad Máxima', icon: 'fa-calendar', color: '#64748B', label: 'Condiciones de Ingreso' }
            ];

            const rowsHtml = categories.map(cat => `
                <tr class="compareCategoryRow">
                    <th colspan="${plans.length + 1}"><i class="fa-solid ${cat.icon}" style="margin-right: 8px; color: ${cat.color};"></i> ${cat.label}</th>
                </tr>
                <tr>
                    <td style="font-weight: 600;">${cat.id}</td>
                    ${plans.map(p => {
                        const colData = p.cols.find(c => c.cat === cat.id);
                        return `<td>${colData ? colData.val : '-'}</td>`;
                    }).join('')}
                </tr>
            `).join('');

            container.innerHTML = `
            <div class="compareHeroCardsGrid" style="display: flex; gap: 20px; margin-bottom: 20px;">
                ${heroCardsHtml}
            </div>

            <div class="compareTableWrapper">
                <table class="compareTable">
                    <thead>
                        <tr>
                            <th style="width: 25%;">Característica / Cobertura</th>
                            ${plans.map(p => `<th style="width: ${(75/plans.length)}%;">${p.title}</th>`).join('')}
                        </tr>
                    </thead>
                    <tbody>
                        ${rowsHtml}
                    </tbody>
                </table>
            </div>
            `;

            modal.classList.add('active');
        }

        function closeCompareModal(e) {
            if (e && e.target && e.target !== document.getElementById('compareModal') && !e.target.closest('.compareModalClose')) {
                return;
            }
            const modal = document.getElementById('compareModal');
            if (modal) modal.classList.remove('active');
        }
"""

if 'function handleCompareChange' not in content:
    content = content.replace('</script>\n</body>', js_logic + '\n</script>\n</body>')

# 4. Make sure isCompared is actually defined in renderPlans.
# My update_mascotas3.py has `const isCompared = false; // Mock for now`
# We need to change that to `const isCompared = selectedForCompare.has(p.id);`
content = content.replace('const isCompared = false; // Mock for now', 'const isCompared = selectedForCompare.has(p.id);')

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added comparator successfully.")
