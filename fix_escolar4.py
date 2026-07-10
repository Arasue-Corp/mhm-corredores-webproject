import re

with open('cotizacion/cotizacion-escolar-4.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Title and header
content = content.replace('Cotización de Asistencia Mascota', 'Cotización de Asistencia Escolar')
content = content.replace('Registro Mascotas', 'Registro Beneficiarios')
content = content.replace('Ingresa los detalles de cada una de tus mascotas aseguradas.', 'Ingresa los detalles del estudiante beneficiario.')
content = content.replace('cotizacion-mascota-3.html', 'cotizacion-escolar-3.html')
content = content.replace('cotizacion-mascota-5.html', 'cotizacion-escolar-5.html')

# Remove ownerSummaryContainer
content = re.sub(r'<!-- Owner Summary Flow -->.*?</div>\s*<!-- Pet Forms Flow -->', '<!-- Pet Forms Flow -->', content, flags=re.DOTALL)
content = content.replace("renderOwnerSummary();", "")

# Remove the default checkbox and button outside the container
content = re.sub(r'<div style="display: flex; align-items: center; margin-bottom: 30px; width: 100%;">.*?Registrar\s*</button>', '', content, flags=re.DOTALL)


# Update Javascript
old_js = """
    function renderPetsForm() {
        const container = document.getElementById('petsContainer');
        if(!container) return;
        
        const cartStr = sessionStorage.getItem('mhmPetCart');
        if (!cartStr) return;

        const plans = JSON.parse(cartStr);
        let html = '';
        let petCounter = 1;
        
        for(let id in plans) {
            for(let i=0; i<plans[id].qty; i++) {
                const uniqueId = id + '-' + i;
                
                html += `
                <div class="harmonic-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <h3 style="color: #0F172A; font-size: 1.1rem; font-weight: 700; margin: 0;">Mascota ${petCounter}</h3>
                        <span style="color: #10B981; font-size: 14px; font-weight: 600;">Plan: ${plans[id].name}</span>
                    </div>
                    
                    <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Nombre de la Mascota" required>
                    
                    <div class="harmonic-input-wrapper">
                        <span class="harmonic-label">Especie</span>
                        <select onchange="validatePetsForm()" class="pet-input harmonic-input" required>
                            <option value="" disabled selected>Selecciona...</option>
                            <option value="Perro">Perro</option>
                            <option value="Gato">Gato</option>
                        </select>
                    </div>
                    
                    <div class="harmonic-input-wrapper">
                        <span class="harmonic-label">Sexo</span>
                        <select onchange="validatePetsForm()" class="pet-input harmonic-input" required>
                            <option value="" disabled selected>Selecciona...</option>
                            <option value="Macho">Macho</option>
                            <option value="Hembra">Hembra</option>
                        </select>
                    </div>

                    <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Raza" required>
                    
                    <input type="number" onkeyup="validatePetsForm()" onchange="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Edad (Años)" min="0" max="30" style="margin-bottom: 0;" required>
                </div>`;
                petCounter++;
            }
        }
        
        container.innerHTML = html;
    }
"""

new_js = """
    function renderPetsForm() {
        const container = document.getElementById('petsContainer');
        if(!container) return;
        
        let html = `
        <style>
            .harmonic-card {
                background: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 12px;
                padding: 20px;
                margin: 0 auto 30px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
                max-width: 450px;
                width: 100%;
                box-sizing: border-box;
            }
            .form-grid-2 {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 12px;
                margin-bottom: 12px;
            }
            .harmonic-input-wrapper {
                background: #F8FAFC;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                padding: 6px 12px;
                box-sizing: border-box;
                display: flex;
                flex-direction: column;
                justify-content: center;
                min-height: 52px;
                margin-bottom: 12px;
            }
            .harmonic-input-wrapper.row-layout {
                flex-direction: row;
                align-items: center;
                justify-content: flex-start;
                padding: 0 12px;
            }
            .harmonic-label {
                font-size: 11px;
                color: #0F172A;
                font-weight: 500;
                margin-bottom: 2px;
            }
            .harmonic-input {
                border: none;
                background: transparent;
                outline: none;
                width: 100%;
                color: #0F172A;
                font-size: 15px;
                padding: 0;
                font-family: inherit;
            }
            .harmonic-input::placeholder {
                color: #94A3B8;
            }
            .harmonic-input.large {
                padding: 14px 12px;
                background: #F8FAFC;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                box-sizing: border-box;
                min-height: 52px;
                margin-bottom: 12px;
            }
            .harmonic-input:focus, .harmonic-input.large:focus, .harmonic-input-wrapper:focus-within {
                background: #FFFFFF;
                border-color: #10B981;
            }
            select.harmonic-input {
                color: #64748B;
            }
            .custom-chk {
                appearance: none;
                -webkit-appearance: none;
                width: 20px;
                height: 20px;
                border: 2px solid #CBD5E1;
                border-radius: 5px;
                background-color: white;
                cursor: pointer;
                position: relative;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                transition: all 0.2s ease;
                flex-shrink: 0;
                margin: 0;
            }
            .custom-chk:checked {
                background-color: #10B981;
                border-color: #10B981;
            }
            .custom-chk:checked::after {
                content: '';
                position: absolute;
                width: 5px;
                height: 10px;
                border: solid white;
                border-width: 0 2px 2px 0;
                transform: rotate(45deg);
                margin-top: -2px;
            }
        </style>
        
        <div class="harmonic-card">
            <div class="form-grid-2">
                <div class="harmonic-input-wrapper row-layout" style="margin-bottom: 0;">
                    <strong style="color: #334155; font-size: 15px; margin-right: 12px;">Rut</strong>
                    <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input" placeholder="12345678-9">
                </div>
                <div class="harmonic-input-wrapper" style="margin-bottom: 0;">
                    <span class="harmonic-label">Fecha de cumpleaños</span>
                    <input type="date" onchange="validatePetsForm()" class="pet-input harmonic-input">
                </div>
            </div>
            
            <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Nombre">
            <input type="text" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Apellidos">
            
            <div class="form-grid-2" style="grid-template-columns: 1fr; margin-bottom:0;">
                 <input type="number" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Edad   Máx. 24 años">
            </div>

            <input type="email" onkeyup="validatePetsForm()" class="pet-input harmonic-input large" placeholder="Email">
            
            <div class="harmonic-input-wrapper">
                <select onchange="validatePetsForm()" class="pet-input harmonic-input" required>
                    <option value="" disabled selected>Previsión</option>
                    <option value="Fonasa">Fonasa</option>
                    <option value="Isapre">Isapre</option>
                </select>
            </div>
            
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
        </div>`;
        
        container.innerHTML = html;
    }
"""

content = content.replace(old_js.strip(), new_js.strip())

# Clean up generic protection box text
content = content.replace('fa-shield-cat', 'fa-user-graduate')
content = content.replace('Estás a pocos pasos de asegurar a tu mascota.', 'Estás a un paso de completar el registro del estudiante.')

with open('cotizacion/cotizacion-escolar-4.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
