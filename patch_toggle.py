import re

html_path = "cotizacion/cotizacion-7-1.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace tabs with aurora-toggle-segment
tabs_pattern = re.compile(r'<div class="car-tabs-integrated" id="entityTabs" style="margin-bottom: 2rem;">.*?</div>', re.DOTALL)

toggle_html = """
                <div class="row-switch-container mb-4" style="justify-content: center; background: transparent; border: none; padding: 0;">
                    <div class="aurora-toggle-segment" style="transform: scale(1.1); margin: 0 auto;">
                        <input type="radio" name="entityTypeToggle" id="togglePersona" value="persona" checked onchange="switchEntityToggle('persona')">
                        <label for="togglePersona" style="padding: 10px 30px;"><i class="fa-solid fa-user"></i> Persona</label>
                        
                        <input type="radio" name="entityTypeToggle" id="toggleEmpresa" value="empresa" onchange="switchEntityToggle('empresa')">
                        <label for="toggleEmpresa" style="padding: 10px 30px;"><i class="fa-solid fa-building"></i> Empresa</label>
                        <div class="segment-highlight"></div>
                    </div>
                </div>
"""
content = tabs_pattern.sub(toggle_html, content)

# Replace JS function
js_pattern = re.compile(r'function switchEntityTab\(entityType, btn\) \{.*?\}', re.DOTALL)
new_js = """
function switchEntityToggle(entityType) {
    const panelPersona = document.getElementById('panel-persona');
    const panelEmpresa = document.getElementById('panel-empresa');
    const sideIndicator = document.getElementById('sideEntityIndicator');

    if (entityType === 'persona') {
        panelPersona.style.display = 'block';
        panelEmpresa.style.display = 'none';
        if (sideIndicator) sideIndicator.innerText = "Contratante Persona";
    } else {
        panelPersona.style.display = 'none';
        panelEmpresa.style.display = 'block';
        if (sideIndicator) sideIndicator.innerText = "Contratante Empresa";
    }
}
"""
content = js_pattern.sub(new_js, content)

# Also update the sidebar to have the sideIndicator ID
sidebar_pattern = re.compile(r'<div class="sl-sub">Confirmación de Identidad</div>')
content = sidebar_pattern.sub(r'<div class="sl-sub" id="sideEntityIndicator">Contratante Persona</div>', content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Toggle successfully added")
