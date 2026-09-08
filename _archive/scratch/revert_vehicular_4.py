import re

with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace the form grid back to the person fields.
form_part = '''<div class="harmonic-card" style="max-width: 100%;">
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
            </div>'''

correct_form_part = '''<div class="harmonic-card" style="max-width: 100%;">
            <div class="form-grid-2">
                <div class="harmonic-input-wrapper" style="margin-bottom: 0; position: relative;">
                    <span class="harmonic-label">Rut</span>
                    <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input" placeholder="12345678-9">
                </div>
                <div class="harmonic-input-wrapper" style="margin-bottom: 0; position: relative;">
                    <span class="harmonic-label">Fecha de cumpleaños</span>
                    <input type="text" onchange="validatePetsForm()" onfocus="(this.type='date')" onblur="(this.value === '' ? this.type='text' : null)" class="pet-input harmonic-input" placeholder="dd/mm/aaaa">
                </div>
            </div>

            <div class="form-grid-2">
                <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Nombre">
                <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Apellidos">
            </div>

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

html = html.replace(form_part, correct_form_part)

# Also fix "Datos del Vehículo" if it should be something else.
# The user said "Revisa los textos, estos no son beneficiarios, ni estudiantes"
# So keeping "Datos del Vehículo" or "Registro" might be fine, or maybe just "Datos de la Asistencia".
# Let's change "Datos del Vehículo" to "Datos del Conductor" just in case, or maybe keep it "Datos del Vehículo" but the person driving it?
# The image said "Registro Beneficiarios". Let's change it to "Registro de Asistencia" and "Ingresa los detalles para la asistencia."
html = html.replace('Datos del Vehículo', 'Registro de Asistencia')
html = html.replace('Ingresa los detalles de tu vehículo.', 'Ingresa los detalles para la asistencia.')
html = html.replace('registro de tu vehículo', 'registro de asistencia')

with open('cotizacion/cotizacion-vehicular-4.html', 'w', encoding='utf-8') as f:
    f.write(html)
