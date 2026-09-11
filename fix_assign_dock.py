import re

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for assignCard
css_block = """
    <style>
        .assign-card-wrapper {
            margin-top: 40px;
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
            transition: all 0.4s ease;
            opacity: 0;
            transform: translateY(20px);
            display: none;
        }
        .assign-card-wrapper.visible {
            display: block;
            opacity: 1;
            transform: translateY(0);
        }
        .assign-card-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #0F172A;
            margin-bottom: 20px;
            border-bottom: 1px solid #E2E8F0;
            padding-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .assign-pets-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 25px;
        }
        .assign-pet-item {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 15px;
        }
        .assign-pet-item label {
            display: block;
            font-weight: 600;
            color: #334155;
            margin-bottom: 10px;
            font-size: 0.95rem;
        }
        .assign-pet-item select {
            width: 100%;
            padding: 10px;
            border: 1px solid #CBD5E1;
            border-radius: 8px;
            font-size: 14px;
            background: white;
            cursor: pointer;
        }
        .assign-pet-item select:focus {
            outline: none;
            border-color: #0F766E;
            box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.1);
        }
    </style>
"""
if '.assign-card-wrapper {' not in content:
    content = content.replace('</head>', css_block + '</head>')

# 2. Replace FLOATING ASSIGN DOCK with a static assign card
old_assign_dock = r'<!-- FLOATING ASSIGN DOCK -->.*?</div>\s*</div>\s*</div>'
new_assign_dock = """<!-- ASSIGNMENT CARD -->
            <div class="assign-card-wrapper" id="assignDock">
                <div class="assign-card-title">
                    <i class="fa-solid fa-list-check" style="color: #0F766E;"></i>
                    Asigna un plan a tus mascotas para continuar
                </div>
                <div class="assign-pets-grid" id="assignPetsContainer">
                    <!-- Dynamic assign dropdowns go here -->
                </div>
                <div style="display: flex; justify-content: flex-end;">
                    <button type="button" class="btn-primary-premium" id="btnContinuarResumen" onclick="irAResumen()" style="padding: 12px 30px; opacity: 0.5; pointer-events: none; border-radius: 12px; font-weight: 600;">
                        <span>Continuar a Resumen</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>"""
content = re.sub(old_assign_dock, new_assign_dock, content, flags=re.DOTALL)

# 3. Update the JS `renderAssignDock()` to show this block and inject items correctly
js_render_assign = r'function renderAssignDock\(\) \{.*?\n        \}'
new_js_render_assign = """function renderAssignDock() {
            const container = document.getElementById('assignPetsContainer');
            const dock = document.getElementById('assignDock');
            if(!container || !dock) return;

            // Render select for each pet
            container.innerHTML = petsData.map((p, i) => `
                <div class="assign-pet-item">
                    <label><i class="fa-solid ${p.type === 'gato' ? 'fa-cat' : 'fa-dog'}" style="color: #64748B; margin-right: 5px;"></i> ${p.name || 'Mascota ' + (i+1)}</label>
                    <select class="pet-plan-select" data-petid="${p.id}" onchange="checkAssigns()">
                        <option value="">Selecciona un plan...</option>
                        <option value="basico">Asistencia Mascota ($9.490/mes)</option>
                        <option value="pro">Asistencia Mascota Pro ($12.490/mes)</option>
                        <option value="senior">Asistencia Mascota Senior ($16.490/mes)</option>
                    </select>
                </div>
            `).join('');

            dock.classList.add('visible');
        }"""
content = re.sub(js_render_assign, new_js_render_assign, content, flags=re.DOTALL)

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied static assign card fix successfully.")
