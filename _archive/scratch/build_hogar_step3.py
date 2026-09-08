import os

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'
src = os.path.join(base_dir, 'cotizacion-escolar-4.html')
dst = os.path.join(base_dir, 'cotizacion-asistencia-hogar-3.html')

with open(src, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace texts for Asistencia Hogar
html = html.replace('Asistencia Escolar', 'Asistencia Hogar')
html = html.replace('Asistencia Protección Escolar', 'Asistencia Hogar')
html = html.replace('fa-school', 'fa-house-chimney')
html = html.replace('mhmEscolarCart', 'mhmHogarCart')
html = html.replace('mhmEscolarClient', 'mhmHogarClient')
html = html.replace('mhmPetCart', 'mhmHogarCart') # Just in case

# Replace navigation links
html = html.replace('cotizacion-escolar-3.html', 'cotizacion-asistencia-hogar-2.html') # Back button goes to 2
html = html.replace('cotizacion-escolar-4.html', 'cotizacion-asistencia-hogar-3.html') # Self reference
html = html.replace('cotizacion-escolar-5.html', 'cotizacion-asistencia-hogar-4.html') # Next button goes to 4 (Success)

# Update sidebar summary text
old_list = """                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Urgencia médica por accidente.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Descuento en farmacias.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Consulta médica general y Telemedicina.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Orientación médica telefónica.
                            </li>"""

new_list = """                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Protección y coberturas 100%.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Eventos disponibles todo el año.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Usa tu Asistencia Integral Pro en el centro médico que desees, estamos en todo Chile.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Reembolso rápido y fácil.
                            </li>"""
html = html.replace(old_list, new_list)

# Update the form fields in renderPetsForm
# We need to remove Edad, change Previsión to Tipo de inmueble
# And add the green header "Datos del beneficiario" to the top of harmonic-card

old_form_inputs = """            <div class="form-grid-2" style="grid-template-columns: 1fr; margin-bottom:0;">
                 <input type="number" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Edad">
            </div>

            <input type="email" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Email">
            
            <div class="harmonic-input-wrapper">
                <select onchange="validatePetsForm()" class="pet-input harmonic-input" required>
                    <option value="" disabled selected>Previsión</option>
                    <option value="Fonasa">Fonasa</option>
                    <option value="Isapre">Isapre</option>
                </select>
            </div>"""

new_form_inputs = """            <input type="email" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Email">
            
            <div class="harmonic-input-wrapper">
                <select onchange="validatePetsForm()" class="pet-input harmonic-input" required>
                    <option value="" disabled selected>Tipo de inmueble</option>
                    <option value="Casa">Casa</option>
                    <option value="Departamento">Departamento</option>
                </select>
            </div>"""
html = html.replace(old_form_inputs, new_form_inputs)

# Add the green header inside harmonic-card
old_card_start = """<div class="harmonic-card">
            <div class="form-grid-2">"""

new_card_start = """<div class="harmonic-card" style="padding-top: 0; overflow: hidden;">
            <div style="background: #A3D80E; margin: 0 -20px 20px -20px; padding: 15px 20px; text-align: left; display: flex; justify-content: space-between; align-items: center;">
                <h3 style="color: white; margin: 0; font-size: 1.25rem; font-weight: 700;">Datos del beneficiario</h3>
                <span style="background: white; padding: 4px 10px; border-radius: 4px; font-weight: 800; font-size: 1rem; color: #104C5C; display: flex; align-items: center; gap: 5px;"><i class="fa-solid fa-leaf" style="color: #A3D80E;"></i> Servi.click</span>
            </div>
            <div class="form-grid-2">"""
html = html.replace(old_card_start, new_card_start)

# Change Rut placeholder in the form
html = html.replace('<strong style="color: #334155; font-size: 15px; margin-right: 12px;">Rut</strong>', '<strong style="color: #334155; font-size: 12px; margin-right: 12px; line-height: 1.1;">Rut del<br>beneficiario</strong>')

# Change student icon to house icon in sidebar bottom message
html = html.replace('fa-user-graduate', 'fa-house-chimney')
html = html.replace('del estudiante', 'de la propiedad / beneficiario')

# Sidebar route of contracting (Steps)
# Escolar: Plan -> Datos -> Pago -> Beneficiarios
# Hogar: Plan -> Pago -> Beneficiarios
old_sidebar_route = """                    <ul class="aurora-list" style="margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px;">
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Selección de Plan</li>
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Datos del Contratante</li>
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Pago Seguro</li>
                        <li class="active"><span class="pulse-dot"></span> Registro Beneficiarios</li>
                    </ul>"""

new_sidebar_route = """                    <ul class="aurora-list" style="margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px;">
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Selección de Plan</li>
                        <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Pago Seguro</li>
                        <li class="active"><span class="pulse-dot"></span> Datos del Beneficiario</li>
                    </ul>"""
html = html.replace(old_sidebar_route, new_sidebar_route)

# Button text from Escolar (maybe it says Registrar already?)
# Yes, it says "Registrar". But let's check the button color. In escolar it is #1C4E5E. Let's leave it.

with open(dst, 'w', encoding='utf-8') as f:
    f.write(html)

print("Created cotizacion-asistencia-hogar-3.html with exactly the requested layout and fields.")
