import re

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the previous CSS for the assign card with a premium version
old_css_regex = r'<style>\s*\.assign-card-wrapper \{.*?\}'
new_css = """<style>
        .assign-card-wrapper {
            margin-top: 50px;
            background: linear-gradient(145deg, #ffffff 0%, #F8FAFC 100%);
            border: 1px solid rgba(255, 255, 255, 0.8);
            border-radius: 24px;
            padding: 40px;
            box-shadow: 0 20px 40px -10px rgba(15, 118, 110, 0.08), 0 1px 3px rgba(0,0,0,0.05);
            position: relative;
            overflow: hidden;
            display: none;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .assign-card-wrapper::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 6px;
            background: linear-gradient(90deg, #2ED9C3 0%, #0F766E 100%);
        }
        .assign-card-wrapper.visible {
            display: block;
            opacity: 1;
            transform: translateY(0);
        }
        .assign-card-title {
            font-size: 1.5rem;
            font-weight: 800;
            color: #0F172A;
            margin-bottom: 30px;
            display: flex;
            align-items: center;
            gap: 15px;
            border-bottom: 1px solid #E2E8F0;
            padding-bottom: 20px;
        }
        .assign-card-title-icon {
            background: #CCFBF1;
            color: #0F766E;
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            box-shadow: 0 4px 10px rgba(15, 118, 110, 0.1);
        }
        .assign-pets-grid {
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin-bottom: 35px;
        }
        .assign-pet-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #FFFFFF;
            border: 2px solid #E2E8F0;
            border-radius: 16px;
            padding: 20px 25px;
            transition: all 0.3s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        }
        .assign-pet-row:hover, .assign-pet-row:focus-within {
            border-color: #2ED9C3;
            box-shadow: 0 10px 25px -5px rgba(46, 217, 195, 0.15);
            transform: translateY(-2px);
        }
        .assign-pet-info {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .assign-pet-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: #F8FAFC;
            color: #64748B;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            border: 2px solid #E2E8F0;
        }
        .assign-pet-name {
            font-size: 1.15rem;
            font-weight: 700;
            color: #1E293B;
            margin-bottom: 4px;
        }
        .assign-pet-type {
            font-size: 0.8rem;
            color: #64748B;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 700;
        }
        .assign-pet-control {
            flex: 0 0 350px;
        }
        .premium-select {
            width: 100%;
            appearance: none;
            background: #F8FAFC url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2224%22%20height%3D%2224%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%230F766E%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%226%209%2012%2015%2018%209%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E") no-repeat right 15px center;
            background-size: 18px;
            border: 2px solid #E2E8F0;
            border-radius: 12px;
            padding: 14px 20px;
            font-size: 1rem;
            font-weight: 600;
            color: #0F172A;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .premium-select:focus, .premium-select:hover {
            outline: none;
            border-color: #0F766E;
            background-color: #FFFFFF;
            box-shadow: 0 0 0 4px rgba(15, 118, 110, 0.1);
        }
        @media (max-width: 768px) {
            .assign-card-wrapper {
                padding: 25px 20px;
            }
            .assign-pet-row {
                flex-direction: column;
                align-items: flex-start;
                gap: 15px;
                padding: 15px;
            }
            .assign-pet-control {
                flex: unset;
                width: 100%;
            }
        }
    }"""
content = re.sub(old_css_regex, new_css, content, flags=re.DOTALL)

# Also remove the trailing `}` that was left over in the css regex match
# Wait, I used a regex that matches `}` at the end of `.assign-card-wrapper {.*?}`
# Wait! My previous script did not have a closing `</style>` inside the block but at the end. Let me just replace the whole <style> block related to assign.
old_style_block = r'<style>\s*\.assign-card-wrapper \{.*?</style>'
new_style_block = new_css.replace('}\n    }', '}\n</style>')
content = re.sub(old_style_block, new_style_block, content, flags=re.DOTALL)


# Replace HTML
old_assign_html = r'<!-- ASSIGNMENT CARD -->.*?</div>\s*</div>\s*</div>'
new_assign_html = """<!-- ASSIGNMENT CARD -->
            <div class="assign-card-wrapper" id="assignDock">
                <div class="assign-card-title">
                    <div class="assign-card-title-icon"><i class="fa-solid fa-list-check"></i></div>
                    Configura tu seguro
                </div>
                <div class="assign-pets-grid" id="assignPetsContainer">
                    <!-- Dynamic assign dropdowns go here -->
                </div>
                <div style="display: flex; justify-content: flex-end; align-items: center; border-top: 1px solid #E2E8F0; padding-top: 25px; margin-top: 10px;">
                    <div style="margin-right: 20px; color: #64748B; font-size: 0.95rem; display: none;" id="assignHint">
                        Asigna un plan a todas las mascotas para continuar
                    </div>
                    <button type="button" class="btn-contratar-action" id="btnContinuarResumen" onclick="irAResumen()" style="padding: 14px 35px; opacity: 0.5; pointer-events: none; border-radius: 12px; font-weight: 700; font-size: 1.05rem;">
                        <span>Continuar a Resumen</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>"""
content = re.sub(old_assign_html, new_assign_html, content, flags=re.DOTALL)

# Update Javascript renderAssignDock
old_js = r'function renderAssignDock\(\) \{.*?\n        \}'
new_js = """function renderAssignDock() {
            const container = document.getElementById('assignPetsContainer');
            const dock = document.getElementById('assignDock');
            const hint = document.getElementById('assignHint');
            if(!container || !dock) return;

            // Render premium rows for each pet
            container.innerHTML = petsData.map((p, i) => {
                const isCat = p.type === 'gato';
                const name = p.name || 'Mascota ' + (i+1);
                return `
                <div class="assign-pet-row">
                    <div class="assign-pet-info">
                        <div class="assign-pet-avatar" style="color: ${isCat ? '#8B5CF6' : '#F59E0B'}; background: ${isCat ? '#F5F3FF' : '#FEF3C7'}; border-color: ${isCat ? '#EDE9FE' : '#FDE68A'};">
                            <i class="fa-solid ${isCat ? 'fa-cat' : 'fa-dog'}"></i>
                        </div>
                        <div>
                            <div class="assign-pet-name">${name}</div>
                            <div class="assign-pet-type">${isCat ? 'Gato' : 'Perro'}</div>
                        </div>
                    </div>
                    <div class="assign-pet-control">
                        <select class="premium-select pet-plan-select" data-petid="${p.id}" onchange="checkAssigns()">
                            <option value="">Selecciona el plan ideal...</option>
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

        // We also update checkAssigns to hide the hint when valid
        const originalCheckAssigns = checkAssigns;
        window.checkAssigns = function() {
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

print("Applied premium UI to assign module.")
