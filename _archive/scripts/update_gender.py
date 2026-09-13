import re

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for the gender buttons
css_block = """
    <style>
        .gender-btn {
            flex: 1;
            padding: 10px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 2px solid #CBD5E1;
            background: #FFF;
            color: #64748B;
        }
        .gender-btn.active {
            border: 2px solid #0F766E;
            background: #F0FDF4;
            color: #0F766E;
        }
    </style>
"""
if '.gender-btn {' not in content:
    content = content.replace('</head>', css_block + '</head>')

# 2. Update renderPetsPanel to use gender-btn classes and direct DOM updates
old_gender = r'<div style="display: flex; gap: 10px; margin-top: 4px; width: 100%;">.*?</div>'
new_gender = """<div style="display: flex; gap: 10px; margin-top: 4px; width: 100%;">
                            <button type="button" id="btn_macho_${p.id}" class="gender-btn ${p.gender==='Macho'?'active':''}" onclick="setGender(${p.id}, 'Macho')"><i class="fa-solid fa-mars"></i> Macho</button>
                            <button type="button" id="btn_hembra_${p.id}" class="gender-btn ${p.gender==='Hembra'?'active':''}" onclick="setGender(${p.id}, 'Hembra')"><i class="fa-solid fa-venus"></i> Hembra</button>
                        </div>"""

content = re.sub(old_gender, new_gender, content, flags=re.DOTALL)

# 3. Modify updatePanelPet so it DOES NOT call renderPetsPanel for gender, but instead modifies classes locally
old_update_panel_pet = r"if\(field === 'gender'\) renderPetsPanel\(\);"
new_update_panel_pet = r"// gender is handled by setGender"
content = re.sub(old_update_panel_pet, new_update_panel_pet, content)

# 4. Add setGender function
js_set_gender = """
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
"""
if 'function setGender(' not in content:
    content = content.replace('function updatePanelPet(', js_set_gender + '\n        function updatePanelPet(')

with open('cotizacion/cotizacion-mascota-nueva-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Gender fix applied.")
