import re

with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

content_start = html.find('<div class="quote-container">')
footer_start = html.find('<!-- Footer -->')

if content_start != -1 and footer_start != -1:
    new_content = '''<div class="quote-container" style="display: flex; justify-content: center; align-items: center; min-height: 60vh;">
        <div class="harmonic-card" style="width: 100%; max-width: 400px; padding: 40px 30px; text-align: center; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            
            <div style="margin-bottom: 25px; color: #104C5C;">
                <i class="fa-solid fa-car" style="font-size: 5rem;"></i>
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

            <button onclick="window.location.href='index.html'" style="background: #104C5C; color: white; border: none; width: 100%; padding: 14px; border-radius: 6px; font-size: 1.1rem; font-weight: 600; cursor: pointer; transition: background 0.2s ease; margin-top: 10px;" onmouseover="this.style.background='#0A323D';" onmouseout="this.style.background='#104C5C';">
                Registrar
            </button>
        </div>
    </div>\n    '''
    
    final_html = html[:content_start] + new_content + html[footer_start:]
    
    # We should also modify the "Registrar" button on page 4 to redirect to page 5!
    with open('cotizacion/cotizacion-vehicular-5.html', 'w', encoding='utf-8') as f2:
        f2.write(final_html)
    print('Created cotizacion-vehicular-5.html')
else:
    print('Could not find markers')
