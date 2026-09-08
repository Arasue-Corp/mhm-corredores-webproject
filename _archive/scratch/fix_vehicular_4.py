import re

with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Title and Subtitle
html = html.replace('Registro Beneficiarios', 'Datos del Vehículo')
html = html.replace('Ingresa los detalles del estudiante beneficiario.', 'Ingresa los detalles de tu vehículo.')
html = html.replace('Registro Beneficiario', 'Datos del Vehículo') # Just in case
html = html.replace('Registro de Beneficiarios', 'Datos del Vehículo')

# Fix bottom right box text and icon
html = html.replace('fa-graduation-cap', 'fa-car')
html = html.replace('registro del estudiante', 'registro de tu vehículo')
html = html.replace('Estudiante', 'Vehículo')
html = html.replace('estudiante', 'vehículo')

# Fix the narrow section (max-width: 450px)
html = html.replace('max-width: 450px;', 'max-width: 100%;')

# Fix the form fields for Vehicle
form_pattern = re.compile(r'<div class="harmonic-input-wrapper" style="margin-bottom: 0; position: relative;">\s*<span class="harmonic-label">Rut del beneficiario.*?Comuna Selecciona la comuna...</option>\s*<option value="Providencia">Providencia</option>\s*<option value="Las Condes">Las Condes</option>\s*<option value="Santiago">Santiago</option>\s*</select>\s*</div>', re.DOTALL)

vehicle_form = '''<div class="form-grid-2">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Patente (Ej: ABCD12)">
<input type="number" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Año (Ej: 2020)">
</div>

<div class="form-grid-2">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Marca (Ej: Toyota)">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Modelo (Ej: Yaris)">
</div>

<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Número de Motor (Opcional)">
<input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Número de Chasis (Opcional)">
'''

if form_pattern.search(html):
    html = form_pattern.sub(vehicle_form, html)
else:
    print("Could not find the form using regex to replace with vehicle fields.")

with open('cotizacion/cotizacion-vehicular-4.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated texts, icon, width and fields!")
