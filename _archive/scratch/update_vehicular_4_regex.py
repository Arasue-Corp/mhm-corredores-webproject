import re
with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace using regex between the form-grid-2 and the end of the form
pattern = re.compile(r'<div class="harmonic-input-wrapper row-layout".*?<option value="Isapre">Isapre</option>\s*</select>\s*</div>', re.DOTALL)
if pattern.search(html):
    print('Pattern found!')
    
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

<div class="harmonic-input-wrapper" style="margin-bottom: 15px;">
<select onchange="validatePetsForm()" class="pet-input harmonic-input" required>
<option value="" disabled selected>Comuna Selecciona la comuna...</option>
<option value="Providencia">Providencia</option>
<option value="Las Condes">Las Condes</option>
<option value="Santiago">Santiago</option>
</select>
</div>'''

    html = pattern.sub(new_form, html)
    with open('cotizacion/cotizacion-vehicular-4.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Replaced form')
else:
    print('Pattern NOT found')
