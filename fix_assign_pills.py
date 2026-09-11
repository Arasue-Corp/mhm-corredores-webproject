import re

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS to include pet pills and sticky bar, and remove old assign CSS
new_css = """
        /* Pet Assignment Pills */
        .pet-assign-area {
            margin-top: 16px;
            padding-top: 16px;
            border-top: 1px solid #E2E8F0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .pet-pills-label {
            font-size: 0.85rem;
            color: #64748B;
            font-weight: 600;
        }
        .pet-pills-container {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        .pet-pill {
            background: #F1F5F9;
            border: 2px solid transparent;
            color: #475569;
            padding: 6px 14px;
            border-radius: 100px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .pet-pill:hover {
            background: #E2E8F0;
        }
        .pet-pill.active {
            background: #ECFDF5;
            border-color: #10B981;
            color: #047857;
        }

        /* Sticky Checkout Bar */
        .checkout-sticky-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-top: 1px solid #E2E8F0;
            padding: 15px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 -10px 30px rgba(0,0,0,0.05);
            z-index: 1000;
            transform: translateY(100%);
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .checkout-sticky-bar.visible {
            transform: translateY(0);
        }
        .checkout-status {
            display: flex;
            flex-direction: column;
        }
        .checkout-status-title {
            font-size: 1.1rem;
            font-weight: 700;
            color: #0F172A;
        }
        .checkout-status-sub {
            font-size: 0.85rem;
            color: #64748B;
        }
        .btn-checkout {
            background: #0F172A;
            color: white;
            padding: 12px 30px;
            border-radius: 100px;
            font-weight: 600;
            font-size: 1rem;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
            opacity: 0.5;
            pointer-events: none;
        }
        .btn-checkout.active {
            opacity: 1;
            pointer-events: auto;
            background: linear-gradient(135deg, #10B981 0%, #0F766E 100%);
        }
        .btn-checkout.active:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 20px rgba(16, 185, 129, 0.2);
        }
"""
# We will just append this CSS before </style>
content = content.replace('</style>', new_css + '\n</style>')

# 2. Modify the renderPlans function to inject the pills
old_actions_row = r'<div class="policyActionsRow">.*?</div>\s*</div>\s*</div>'
# We'll use a dynamic replacement for this block.
# Actually, it's safer to find the specific part of renderPlans and replace it.
def replacer(m):
    return """<div class="policyActionsRow">
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
                    </div>"""
content = re.sub(r'<div class="policyActionsRow">.*?</div>\s*</div>\s*</div>', replacer, content, flags=re.DOTALL)

# 3. Add the Sticky Bar to the HTML
sticky_bar_html = """
    <!-- STICKY CHECKOUT BAR -->
    <div class="checkout-sticky-bar" id="stickyCheckout">
        <div class="checkout-status">
            <span class="checkout-status-title" id="checkoutStatusTitle">0 de 1 mascota asignada</span>
            <span class="checkout-status-sub">Selecciona un plan para continuar</span>
        </div>
        <button type="button" class="btn-checkout" id="btnStickyCheckout" onclick="irAResumen()">
            <span>Continuar</span>
            <i class="fa-solid fa-arrow-right"></i>
        </button>
    </div>
"""
content = content.replace('</body>', sticky_bar_html + '\n</body>')

# 4. Remove old assign module
content = re.sub(r'<!-- ASSIGNMENT CARD -->.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

# 5. Update JS logic for assignPlanToPet and checkAssigns
# We need to replace renderAssignDock and checkAssigns.
old_js = r'function renderAssignDock\(\) \{.*?\}\n\n        window\.checkAssigns = function\(selectElem\) \{.*?\};'
new_js = """
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
"""
content = re.sub(old_js, new_js.strip(), content, flags=re.DOTALL)

# Also ensure renderPlans() calls checkAssigns() to keep sticky bar updated?
# Wait, checkAssigns() logic works. We just call it after rendering pets if pets>0.
# Let's hook it into validateForm (when "Cotizar" is clicked, we might want to show sticky bar).
content = content.replace("renderAssignDock();", "checkAssigns();")

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied inline pill assignment and sticky bar.")
