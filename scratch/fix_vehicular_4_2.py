import re

with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the form fields layout in the JS template
old_form_part = '''<div class="harmonic-card">
            <div class="form-grid-2">
                <div class="form-grid-2">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Patente (Ej: ABCD12)">
<input type="number" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Año (Ej: 2020)">
</div>

<div class="form-grid-2">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Marca (Ej: Toyota)">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Modelo (Ej: Yaris)">
</div>

<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Número de Motor (Opcional)">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Número de Chasis (Opcional)">

            
            <input type="tel" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Teléfono">
            <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Dirección">
            
            <div class="harmonic-input-wrapper">
                <select onchange="validatePetsForm()" class="pet-input harmonic-input" required>
                    <option value="" disabled selected>Comuna   Selecciona la comuna...</option>
                    <option value="Santiago">Santiago</option>
                    <option value="Providencia">Providencia</option>
                    <option value="Las Condes">Las Condes</option>
                </select>
            </div>
            
            <div style="display: flex; align-items: center; margin: 20px 0 20px; width: 100%;">
                <input type="checkbox" id="chkPetsCorrect" class="custom-chk" onchange="validatePetsForm()">
                <label for="chkPetsCorrect" style="margin-left: 10px; font-size: 0.85rem; font-weight: 500; color: #475569; cursor: pointer; user-select: none;">Todos los datos registrados son correctos.</label>
            </div>

            <button type="button" id="btn-finish" onclick="finishFlow()" style="background: #1C4E5E; color: white; border: none; width: 100%; padding: 14px; border-radius: 8px; font-size: 1.1rem; font-weight: 700; cursor: pointer; opacity: 0.5; pointer-events: none; transition: 0.3s; box-shadow: 0 4px 15px rgba(28, 78, 94, 0.3);">
                Registrar
            </button>
        </div>'''

new_form_part = '''<div class="harmonic-card" style="max-width: 100%;">
            <div class="form-grid-2">
                <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Patente (Ej: ABCD12)">
                <input type="number" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Año (Ej: 2020)">
            </div>
            <div class="form-grid-2">
                <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Marca (Ej: Toyota)">
                <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Modelo (Ej: Yaris)">
            </div>
            <div class="form-grid-2">
                <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Número de Motor (Opcional)">
                <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Número de Chasis (Opcional)">
            </div>

            <div style="display: flex; align-items: center; margin: 20px 0 20px; width: 100%;">
                <input type="checkbox" id="chkPetsCorrect" class="custom-chk" onchange="validatePetsForm()">
                <label for="chkPetsCorrect" style="margin-left: 10px; font-size: 0.85rem; font-weight: 500; color: #475569; cursor: pointer; user-select: none;">Todos los datos registrados son correctos.</label>
            </div>

            <button type="button" id="btn-finish" onclick="finishFlow()" style="background: #1C4E5E; color: white; border: none; width: 100%; padding: 14px; border-radius: 8px; font-size: 1.1rem; font-weight: 700; cursor: pointer; opacity: 0.5; pointer-events: none; transition: 0.3s; box-shadow: 0 4px 15px rgba(28, 78, 94, 0.3);">
                Registrar
            </button>
        </div>'''

html = html.replace(old_form_part, new_form_part)

# 2. Fix the fa-user-graduate icon
html = html.replace('fa-user-graduate', 'fa-car')

with open('cotizacion/cotizacion-vehicular-4.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed vehicular-4 layout and icon.")
