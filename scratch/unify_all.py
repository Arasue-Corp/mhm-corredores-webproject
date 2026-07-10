import os
import re

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

flows = {
    'escolar': {
        'prefix': 'cotizacion-escolar',
        'title': 'Asistencia Escolar',
        'var': 'mhmEscolarCart',
        'client': 'mhmEscolarClient',
        'icon': 'fa-user-graduate',
        'rut_label': 'Rut del beneficiario',
        'step4_title': 'Registro Beneficiarios',
        'step4_custom_fields': '''
            <div class="harmonic-input-wrapper">
                <div class="row-layout">
                    <select id="prevision" class="pet-input harmonic-input" required onchange="validatePetsForm()">
                        <option value="" disabled selected>Previsión</option>
                        <option value="fonasa">Fonasa</option>
                        <option value="isapre">Isapre</option>
                        <option value="particular">Particular</option>
                    </select>
                </div>
            </div>
        '''
    },
    'hogar': {
        'prefix': 'cotizacion-asistencia-hogar',
        'title': 'Asistencia Hogar',
        'var': 'mhmHogarCart',
        'client': 'mhmHogarClient',
        'icon': 'fa-house',
        'rut_label': 'Rut del propietario',
        'step4_title': 'Registro del Hogar',
        'step4_custom_fields': '''
            <div class="harmonic-input-wrapper">
                <div class="row-layout">
                    <select id="tipoVivienda" class="pet-input harmonic-input" required onchange="validatePetsForm()">
                        <option value="" disabled selected>Tipo de vivienda</option>
                        <option value="casa">Casa</option>
                        <option value="departamento">Departamento</option>
                    </select>
                </div>
            </div>
        '''
    },
    'mascota': {
        'prefix': 'cotizacion-mascota',
        'title': 'Asistencia Mascotas',
        'var': 'mhmMascotaCart',
        'client': 'mhmMascotaClient',
        'icon': 'fa-paw',
        'rut_label': 'Rut del dueño',
        'step4_title': 'Registro Mascotas',
        'step4_custom_fields': '''
            <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Nombre de la mascota">
            <div class="harmonic-input-wrapper">
                <div class="row-layout">
                    <select id="tipoMascota" class="pet-input harmonic-input" required onchange="validatePetsForm()">
                        <option value="" disabled selected>Tipo de mascota</option>
                        <option value="perro">Perro</option>
                        <option value="gato">Gato</option>
                        <option value="exotica">Exótica</option>
                    </select>
                </div>
            </div>
        '''
    },
    'vehicular': {
        'prefix': 'cotizacion-vehicular',
        'title': 'Asistencia Vehicular',
        'var': 'mhmVehicularCart',
        'client': 'mhmVehicularClient',
        'icon': 'fa-car',
        'rut_label': 'Rut del contratante',
        'step4_title': 'Registro Vehículo',
        'step4_custom_fields': '''
            <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Patente (Ej: ABCD12)">
            <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Marca (Ej: Toyota)">
            <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Modelo (Ej: Yaris)">
            <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Año (Ej: 2023)">
        '''
    }
}

template_ciclista = {
    'prefix': 'cotizacion-asistencia-ciclista',
    'title': 'Asistencia al Ciclista',
    'var': 'mhmCiclistaCart',
    'client': 'mhmCiclistaClient',
    'icon': 'fa-person-biking',
    'rut_label': 'Rut del beneficiario',
    'step4_title': 'Registro Beneficiarios',
    'step4_custom_fields': '''
            <div class="harmonic-input-wrapper">
                <div class="row-layout">
                    <select id="prevision" class="pet-input harmonic-input" required onchange="validatePetsForm()">
                        <option value="" disabled selected>Previsión</option>
                        <option value="fonasa">Fonasa</option>
                        <option value="isapre">Isapre</option>
                        <option value="particular">Particular</option>
                    </select>
                </div>
            </div>
        '''
}

def clean_custom_fields(fields):
    return re.sub(r'\s+', '', fields)

# Generate files based on templates
for step in [2, 3, 4, 5]:
    tpl_path = os.path.join(base_dir, f"{template_ciclista['prefix']}-{step}.html")
    with open(tpl_path, 'r', encoding='utf-8') as f:
        tpl_content = f.read()

    for flow_id, flow_data in flows.items():
        content = tpl_content
        
        # Replacements
        content = content.replace(template_ciclista['title'], flow_data['title'])
        content = content.replace(template_ciclista['var'], flow_data['var'])
        content = content.replace(template_ciclista['client'], flow_data['client'])
        content = content.replace(template_ciclista['icon'], flow_data['icon'])
        content = content.replace(template_ciclista['prefix'], flow_data['prefix'])
        
        if step == 4:
            content = content.replace(template_ciclista['rut_label'], flow_data['rut_label'])
            content = content.replace(template_ciclista['step4_title'], flow_data['step4_title'])
            
            # Replace custom fields exactly using regex or string match
            # To be safe, we will replace the exact HTML block
            old_block = '''<div class="harmonic-input-wrapper">
                <div class="row-layout">
                    <select id="prevision" class="pet-input harmonic-input" required onchange="validatePetsForm()">
                        <option value="" disabled selected>Previsión</option>
                        <option value="fonasa">Fonasa</option>
                        <option value="isapre">Isapre</option>
                        <option value="particular">Particular</option>
                    </select>
                </div>
            </div>'''
            
            content = content.replace(old_block, flow_data['step4_custom_fields'].strip())
            
            # Sidebar texts
            content = content.replace('del ciclista / beneficiario', 'del ' + flow_data['title'].lower().replace('asistencia ', ''))

        if step == 5:
            content = content.replace('El ciclista ahora cuenta', 'El beneficiario ahora cuenta')
            # Specifically for step 5, cross sell keeps Ciclista/Movilidad/Mascotas or we don't care much.
            pass

        out_path = os.path.join(base_dir, f"{flow_data['prefix']}-{step}.html")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated {out_path}")

print("Done unifying templates.")
