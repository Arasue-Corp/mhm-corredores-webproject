import os

with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the form HTML in the JS template
old_form = '''<div class="harmonic-input-wrapper row-layout" style="margin-bottom: 0;">
<strong style="color: #334155; font-size: 15px; margin-right: 12px;">Rut</strong>
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input" placeholder="12345678-9">
</div>
<div class="harmonic-input-wrapper" style="margin-bottom: 0; position: relative;">
<span class="harmonic-label">Fecha de cumpleaños</span>
<input type="text" onchange="validatePetsForm()" onfocus="(this.type='date')" onblur="(this.value === '' ? this.type='text' : null)" class="pet-input harmonic-input" placeholder="dd/mm/aaaa">
</div>
</div>

<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Nombre">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Apellidos">

<div class="form-grid-2" style="grid-template-columns: 1fr; margin-bottom:0;">
<input type="number" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Edad">
</div>

<input type="email" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Email">

<div class="harmonic-input-wrapper">
<select onchange="validatePetsForm()" class="pet-input harmonic-input" required>
<option value="" disabled selected>Previsión</option>
<option value="Fonasa">Fonasa</option>
<option value="Isapre">Isapre</option>
</select>
</div>'''

new_form = '''<div class="harmonic-input-wrapper" style="margin-bottom: 0; position: relative;">
<span class="harmonic-label">Rut del beneficiario</span>
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input" placeholder="12345678-9">
</div>
<div class="harmonic-input-wrapper" style="margin-bottom: 0; position: relative;">
<span class="harmonic-label">Fecha de cumpleaños</span>
<input type="text" onchange="validatePetsForm()" onfocus="(this.type='date')" onblur="(this.value === '' ? this.type='text' : null)" class="pet-input harmonic-input" placeholder="dd/mm/aaaa">
</div>
</div>

<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Nombre">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Apellidos">

<input type="email" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Email">
<input type="tel" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Teléfono">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Dirección">

<div class="harmonic-input-wrapper">
<select onchange="validatePetsForm()" class="pet-input harmonic-input" required>
<option value="" disabled selected>Comuna Selecciona la comuna...</option>
<option value="Providencia">Providencia</option>
<option value="Las Condes">Las Condes</option>
<option value="Santiago">Santiago</option>
</select>
</div>'''

if old_form in html:
    html = html.replace(old_form, new_form)
else:
    print("WARNING: Old form not found for replacement!")

with open('cotizacion/cotizacion-vehicular-4.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated cotizacion-vehicular-4.html")
