import re

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS to be minimalist and premium
old_css_regex = r'\.assign-card-wrapper \{.*?\@media \(max-width: 768px\) \{.*?\}'
new_css = """
        .assign-card-wrapper {
            margin-top: 60px;
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.4);
            border-radius: 32px;
            padding: 40px;
            box-shadow: 0 10px 40px -10px rgba(0, 0, 0, 0.05);
            display: none;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
        }
        .assign-card-wrapper.visible {
            display: block;
            opacity: 1;
            transform: translateY(0);
        }
        .assign-card-title {
            font-size: 1.4rem;
            font-weight: 400;
            color: #334155;
            margin-bottom: 35px;
            display: flex;
            align-items: center;
            gap: 12px;
            letter-spacing: -0.02em;
        }
        .assign-card-title strong {
            font-weight: 700;
            color: #0F172A;
        }
        .assign-card-title-icon {
            color: #0F766E;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
        }
        .assign-pets-grid {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 40px;
        }
        .assign-pet-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            padding: 16px 24px;
            transition: all 0.3s ease;
            box-shadow: 0 2px 10px rgba(0,0,0,0.02);
            border: 1px solid rgba(0,0,0,0.03);
        }
        .assign-pet-row:hover, .assign-pet-row:focus-within {
            background: #FFFFFF;
            box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.06);
            transform: translateY(-2px);
        }
        .assign-pet-info {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        .assign-pet-avatar {
            width: 48px;
            height: 48px;
            border-radius: 16px;
            background: #F8FAFC;
            color: #94A3B8;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
        }
        .assign-pet-name {
            font-size: 1.1rem;
            font-weight: 600;
            color: #1E293B;
            margin-bottom: 2px;
        }
        .assign-pet-type {
            font-size: 0.75rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 600;
        }
        .assign-pet-control {
            flex: 0 0 380px;
        }
        .premium-select {
            width: 100%;
            appearance: none;
            background: #F8FAFC url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%2394A3B8%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%226%209%2012%2015%2018%209%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E") no-repeat right 15px center;
            background-size: 16px;
            border: 1px solid transparent;
            border-radius: 14px;
            padding: 14px 20px;
            font-size: 0.95rem;
            font-weight: 500;
            color: #334155;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .premium-select:focus, .premium-select:hover {
            outline: none;
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        }
        .btn-minimal-submit {
            background: #0F172A;
            color: white;
            padding: 16px 40px;
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
        .btn-minimal-submit:hover {
            background: #1E293B;
            transform: scale(1.02);
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.2);
        }
        @media (max-width: 768px) {
            .assign-card-wrapper {
                padding: 30px 20px;
                border-radius: 24px;
            }
            .assign-pet-row {
                flex-direction: column;
                align-items: flex-start;
                gap: 20px;
                padding: 20px;
            }
            .assign-pet-control {
                flex: unset;
                width: 100%;
            }
        }
"""
content = re.sub(old_css_regex, new_css.strip(), content, flags=re.DOTALL)


# 2. Update the HTML for the card title and button
old_assign_html = r'<!-- ASSIGNMENT CARD -->.*?</div>\s*</div>\s*</div>'
new_assign_html = """<!-- ASSIGNMENT CARD -->
            <div class="assign-card-wrapper" id="assignDock">
                <div class="assign-card-title">
                    <div class="assign-card-title-icon"><i class="fa-solid fa-sparkles"></i></div>
                    <span>Configura tu <strong>seguro a medida</strong></span>
                </div>
                <div class="assign-pets-grid" id="assignPetsContainer">
                    <!-- Dynamic assign dropdowns go here -->
                </div>
                <div style="display: flex; justify-content: flex-end; align-items: center; padding-top: 10px;">
                    <div style="margin-right: 24px; color: #94A3B8; font-size: 0.9rem; display: none;" id="assignHint">
                        Selecciona un plan para cada mascota
                    </div>
                    <button type="button" class="btn-minimal-submit" id="btnContinuarResumen" onclick="irAResumen()">
                        <span>Ir a Resumen</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>"""
content = re.sub(old_assign_html, new_assign_html, content, flags=re.DOTALL)


# 3. Update the renderAssignDock and checkAssigns to fix logic
old_js = r'function renderAssignDock\(\) \{.*?\}\n        \};\n'
new_js = """function renderAssignDock() {
            const container = document.getElementById('assignPetsContainer');
            const dock = document.getElementById('assignDock');
            const hint = document.getElementById('assignHint');
            if(!container || !dock) return;

            container.innerHTML = petsData.map((p, i) => {
                const isCat = p.type === 'gato';
                const name = p.name || 'Mascota ' + (i+1);
                return `
                <div class="assign-pet-row">
                    <div class="assign-pet-info">
                        <div class="assign-pet-avatar" style="color: ${isCat ? '#8B5CF6' : '#F59E0B'}; background: ${isCat ? '#F5F3FF' : '#FEF3C7'};">
                            <i class="fa-solid ${isCat ? 'fa-cat' : 'fa-dog'}"></i>
                        </div>
                        <div>
                            <div class="assign-pet-name">${name}</div>
                            <div class="assign-pet-type">${isCat ? 'Gato' : 'Perro'}</div>
                        </div>
                    </div>
                    <div class="assign-pet-control">
                        <select class="premium-select pet-plan-select" data-petid="${p.id}" onchange="checkAssigns(this)">
                            <option value="">Elegir plan...</option>
                            <option value="basico">Asistencia Mascota ($9.490/mes)</option>
                            <option value="pro">Asistencia Mascota Pro ($12.490/mes)</option>
                            <option value="senior">Asistencia Mascota Senior ($16.490/mes)</option>
                        </select>
                    </div>
                </div>
                `;
            }).join('');

            dock.classList.add('visible');
            if(hint) hint.style.display = 'block';
        }

        window.checkAssigns = function(selectElem) {
            // Fix logic: Assign to petsData
            if (selectElem) {
                const petId = parseInt(selectElem.getAttribute('data-petid'), 10);
                const p = petsData.find(x => x.id === petId);
                if (p) p.plan = selectElem.value;
            }

            let allAssigned = true;
            document.querySelectorAll('.pet-plan-select').forEach(sel => {
                if (!sel.value) allAssigned = false;
            });
            const btn = document.getElementById('btnContinuarResumen');
            const hint = document.getElementById('assignHint');
            if (allAssigned) {
                btn.style.opacity = '1';
                btn.style.pointerEvents = 'auto';
                if(hint) hint.style.display = 'none';
            } else {
                btn.style.opacity = '0.5';
                btn.style.pointerEvents = 'none';
                if(hint) hint.style.display = 'block';
            }
        };
"""
content = re.sub(old_js, new_js, content, flags=re.DOTALL)

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied minimal premium assign module and fixed logic.")
