import re

with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find <div class="main-spec-col">
main_start = html.find('<div class="main-spec-col">')
# Find the start of the sidebar: <aside class="config-sidebar...
sidebar_start = html.find('<aside class="config-sidebar')

if main_start != -1 and sidebar_start != -1:
    # We will grab everything BEFORE main_spec_col,
    # replace it with the new page 5 content,
    # and then append everything AFTER sidebar_start (including the sidebar!)
    # But wait! We need to change titles and button links.
    
    # Let's do the title replacements on the whole HTML first.
    # Change the "Volver" button
    html = html.replace('href="cotizacion-vehicular-3.html"', 'href="cotizacion-vehicular-4.html"')
    html = html.replace('Volver a Pago Seguro', 'Volver a Registro Asistencia')
    
    # Change title
    html = html.replace('Registro de Asistencia', 'Datos del Vehículo')
    html = html.replace('Ingresa los detalles para la asistencia.', 'Ingresa los detalles de tu vehículo.')
    
    # Update progress bar to 100%
    html = html.replace('style="width: 90%;"', 'style="width: 100%;"')

    # Since we replaced the html string, the indices changed! Let's find them again.
    main_start = html.find('<div class="main-spec-col">')
    sidebar_start = html.find('<aside class="config-sidebar')
    
    new_main_content = '''<div class="main-spec-col">
        <div class="premium-white-card" style="display: flex; justify-content: center; align-items: center; padding: 60px 20px;">
            <div style="width: 100%; max-width: 320px; text-align: center;">
                
                <div style="margin-bottom: 25px; color: #104C5C;">
                    <i class="fa-solid fa-car" style="font-size: 4rem;"></i>
                </div>

                <style>
                    .vehicle-modal-input {
                        width: 100%;
                        padding: 12px 15px;
                        border: 1px solid #E2E8F0;
                        border-radius: 4px;
                        font-size: 0.95rem;
                        color: #1E293B;
                        margin-bottom: 15px;
                        background-color: #F8FAFC;
                        transition: all 0.3s ease;
                        outline: none;
                    }
                    .vehicle-modal-input:focus {
                        border-color: #104C5C;
                        background-color: white;
                    }
                    .vehicle-modal-select {
                        appearance: none;
                        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/200.svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23104C5C' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
                        background-repeat: no-repeat;
                        background-position: right 15px center;
                        background-size: 16px;
                    }
                </style>

                <input type="text" class="vehicle-modal-input" placeholder="Kilometraje del vehículo">
                
                <select class="vehicle-modal-input vehicle-modal-select">
                    <option value="" disabled selected>Tipo de vehículo</option>
                    <option value="Auto">Auto</option>
                    <option value="Camioneta">Camioneta</option>
                    <option value="SUV">SUV</option>
                    <option value="Moto">Moto</option>
                </select>
                
                <input type="text" class="vehicle-modal-input" placeholder="Patente">

                <!-- User screenshot shows a bright teal button. The class 'btn-aurora-gradient' gives a similar bright teal color, let's use that or explicitly a teal background. The screenshot button says Registrar with white text. Let's use #34d399 which is a common teal. -->
                <button onclick="window.location.href='index.html'" style="background: #34d399; color: white; border: none; width: 100%; padding: 12px; border-radius: 4px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: background 0.2s ease; margin-top: 10px;" onmouseover="this.style.background='#10b981';" onmouseout="this.style.background='#34d399';">
                    Registrar
                </button>
            </div>
        </div>
    </div>\n\n    '''
    
    final_html = html[:main_start] + new_main_content + html[sidebar_start:]
    
    with open('cotizacion/cotizacion-vehicular-5.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Created cotizacion-vehicular-5.html with sidebar")
else:
    print('Could not find markers', main_start, sidebar_start)
