import re

with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the inner div of successModal
modal_start = html.find('<div id="successModal"')
if modal_start != -1:
    modal_inner_start = html.find('<div style="background: white;', modal_start)
    modal_end = html.find('</div>\n    </div>', modal_inner_start)
    
    if modal_inner_start != -1 and modal_end != -1:
        # We replace from modal_inner_start to modal_end
        new_modal_content = '''<div style="background: white; border-radius: 8px; width: 90%; max-width: 400px; padding: 40px 30px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); position: relative; animation: modalPop 0.3s ease-out; margin: 0 auto;">
            
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
            </button>'''
        
        html = html[:modal_inner_start] + new_modal_content + html[modal_end:]

with open('cotizacion/cotizacion-vehicular-4.html', 'w', encoding='utf-8') as f:
    f.write(html)
