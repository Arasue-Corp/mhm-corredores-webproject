import re

with open('cotizacion/cotizacion-escolar-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the form body layout (remove bubble, center fields)
form_body_start = content.find('        <!-- Body -->')
form_body_end = content.find('        </div>\n    </div>', form_body_start)

if form_body_start != -1 and form_body_end != -1:
    new_body = """        <!-- Body -->
        <div style="padding: 40px; background: white; max-width: 500px; margin: 0 auto;">
            <!-- Form Fields -->
            <div style="display: flex; flex-direction: column; gap: 15px; border: 1px solid #E2E8F0; border-radius: 12px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.02);">
                
                <div style="display: flex; border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden; background: #F8FAFC;">
                    <div style="padding: 12px 15px; font-weight: 700; color: #334155; border-right: 1px solid #E2E8F0; display: flex; align-items: center; width: 85px;">Rut</div>
                    <input type="text" id="rutInput" onkeyup="validateForm()" placeholder="12345678-9" style="width: 100%; border: none; background: transparent; padding: 12px 15px; font-size: 1rem; color: #0F172A; outline: none;" required>
                </div>
                
                <div style="display: flex; border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden; background: #F8FAFC;">
                    <div style="padding: 12px 15px; font-weight: 700; color: #334155; border-right: 1px solid #E2E8F0; display: flex; align-items: center; width: 85px;">Nombre</div>
                    <input type="text" id="nameInput" onkeyup="validateForm()" style="width: 100%; border: none; background: transparent; padding: 12px 15px; font-size: 1rem; color: #0F172A; outline: none;" required>
                </div>
                
                <div style="display: flex; border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden; background: #F8FAFC;">
                    <div style="padding: 12px 15px; font-weight: 700; color: #334155; border-right: 1px solid #E2E8F0; display: flex; align-items: center; width: 85px;">Email</div>
                    <input type="email" id="emailInput" onkeyup="validateForm()" style="width: 100%; border: none; background: transparent; padding: 12px 15px; font-size: 1rem; color: #0F172A; outline: none;" required>
                </div>

                <button type="submit" id="btn-continue" style="margin-top: 10px; width: 100%; padding: 12px; border-radius: 8px; background: #1C4E5E; color: white; font-weight: 700; border: none; cursor: pointer; transition: 0.3s; opacity: 0.5; pointer-events: none; font-size: 1rem;">
                    Continuar
                </button>
            </div>
"""
    content = content[:form_body_start] + new_body + content[form_body_end:]

# 2. Update 'Registro Mascotas' to 'Registro Beneficiarios'
content = content.replace('Registro Mascotas', 'Registro Beneficiarios')

# 3. Update 'Protección Activa' text
content = content.replace(
    '<p style="margin: 0; font-size: 0.85rem; color: #64748B;">Estás a pocos pasos de asegurar a tu mascota.</p>',
    '<p style="margin: 0; font-size: 0.85rem; color: #64748B; margin-top: 10px;">Si eres <strong style="font-weight: 700; color: #0F172A;">contratante y beneficiario</strong> a la vez, continúa completando los formularios con tus datos.</p>'
)

# 4. Update modal text for 'Mascota'
content = content.replace('<h4>Información de la Mascota</h4>', '<h4>Información del Alumno</h4>')
content = content.replace('<p>Nombre, especie, raza y edad de tu mascota.</p>', '<p>Nombre, rut y fecha de nacimiento del alumno beneficiario.</p>')

with open('cotizacion/cotizacion-escolar-2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done with fix_escolar3")
