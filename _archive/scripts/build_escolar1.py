import re

with open('cotizacion/cotizacion-escolar-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace title
content = content.replace('Cotización de Asistencia Mascota', 'Cotización de Asistencia Escolar')
content = content.replace('Elige el plan de Asistencia Veterinaria que mejor se adapte a tu mascota.', 'Elige el plan de Asistencia Escolar que mejor se adapte a tus necesidades.')

# 2. Replace the grid
grid_start = content.find('<div class="veh-type-grid">')
grid_end = content.find('</div>\n    \n    <div style="display: grid;')

if grid_start != -1 and grid_end != -1:
    new_grid = """
    <style>
        .veh-type-grid { display: flex; justify-content: center; }
        .veh-type-card {
            max-width: 400px; width: 100%;
            border: 5px solid #93C524;
            border-radius: 20px; padding: 0;
            display: flex; flex-direction: column; align-items: center; text-align: center;
            background: #1C4E5E; color: white;
            position: relative; overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .vt-image {
            width: 100%; height: 200px;
            overflow: hidden; position: relative;
        }
        .vt-image img {
            width: 100%; height: 100%; object-fit: cover; opacity: 0.6;
        }
        .vt-image-overlay {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            display: flex; align-items: center; justify-content: center;
            background: rgba(28, 78, 94, 0.4);
        }
        .vt-image-overlay h4 {
            color: white; font-size: 2rem; font-weight: 800; text-transform: uppercase;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5); margin: 0; line-height: 1.1;
        }
        
        .vt-info { width: 100%; padding: 25px; box-sizing: border-box; }
        
        .pet-feature-list {
            list-style: none; padding: 0; margin: 0; font-size: 0.95rem; color: white;
            text-align: left; font-weight: 500;
        }
        .pet-feature-list li { margin-bottom: 12px; display: flex; align-items: flex-start; gap: 10px; }
        .pet-feature-list li i { color: white; font-size: 1.1rem; margin-top: 3px; }
        
        .plan-price { font-size: 2.5rem; font-weight: 800; color: white; margin-top: 20px; }
        
        /* Quantity Controls */
        .qty-controls {
            display: flex;
            align-items: center;
            justify-content: center;
            background: transparent;
            margin-top: 25px;
            width: 100%;
            gap: 15px;
        }
        .qty-btn {
            background: #E2E8F0; border: none; color: #0F172A;
            width: 35px; height: 35px; display: flex; justify-content: center; align-items: center;
            cursor: pointer; transition: all 0.2s; font-size: 1.1rem; border-radius: 50%;
        }
        .qty-btn:hover { background: #CBD5E1; }
        .qty-value { width: 40px; text-align: center; font-weight: 800; color: #0F172A; font-size: 1.2rem; }
    </style>

    <div class="veh-type-grid">
        <div class="veh-type-card">
            <div class="vt-image">
                <img src="../assets/img/article-3.webp" alt="Asistencia Escolar">
                <div class="vt-image-overlay">
                    <h4>ASISTENCIA<br>ESCOLAR</h4>
                </div>
            </div>
            <div class="vt-info">
                <ul class="pet-feature-list">
                    <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                    <li><i class="fa-solid fa-check"></i> Asistencia disponible para ti y tu familia 24/7.</li>
                    <li><i class="fa-solid fa-check"></i> Edad de ingreso: Para contratar debes ser mayor a 18 años y tener menos de 65 años.</li>
                    <li><i class="fa-solid fa-check"></i> Descuento en farmacia, mayor cobertura y beneficios exclusivos.</li>
                    <li><i class="fa-solid fa-check"></i> Libre elección en todo Chile.</li>
                </ul>
                
                <div class="plan-price">$3.780</div>
                
            </div>
        </div>
    </div>
    
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <div class="qty-controls" style="width: auto;">
            <button type="button" class="qty-btn" onclick="updateQty('escolar', -1)"><i class="fa-solid fa-minus"></i></button>
            <span class="qty-value" id="qty-escolar">0</span>
            <button type="button" class="qty-btn" onclick="updateQty('escolar', 1)"><i class="fa-solid fa-plus"></i></button>
        </div>
    </div>
"""
    content = content[:grid_start] + new_grid + content[grid_end+6:]

# 3. Replace JS logic
js_start = content.find('const plans = {')
js_end = content.find('};', js_start)

if js_start != -1 and js_end != -1:
    new_js = """const plans = {
        'escolar': { name: 'Asistencia Escolar', price: 3780, qty: 0 }
    };"""
    content = content[:js_start] + new_js + content[js_end+2:]

# Update rendering logic slightly if needed, specifically the icon
content = content.replace('fa-paw', 'fa-school')

# Change URL to go to next step
content = content.replace('cotizacion-mascota-2.html', 'cotizacion-escolar-2.html')

with open('cotizacion/cotizacion-escolar-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
