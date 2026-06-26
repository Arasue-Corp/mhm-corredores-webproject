import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

pet_cards_new = """
    <style>
        .pet-feature-list {
            list-style: none;
            padding: 0;
            margin: 10px 0 0 0;
            font-size: 0.85rem;
            color: #64748B;
        }
        .pet-feature-list li {
            margin-bottom: 5px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .pet-feature-list li i {
            color: #2ED9C3;
            font-size: 0.8rem;
        }
        .pro-card .pet-feature-list li i {
            color: #2563EB;
        }
        .plan-price {
            font-size: 1.1rem;
            font-weight: 800;
            color: #0F172A;
            margin-top: 10px;
        }
        .pro-card .plan-price {
            color: #2563EB;
        }
        .vt-info {
            width: 100%;
        }
    </style>
    <div class="veh-type-grid">
        <div class="veh-type-card" onclick="selectType('basico', this)">
            <div class="vt-icon"><i class="fa-solid fa-dog"></i></div>
            <div class="vt-info">
                <h4>Asistencia Mascota</h4>
                <div class="plan-price">$5.555 / mes</div>
                <ul class="pet-feature-list">
                    <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                    <li><i class="fa-solid fa-check"></i> Asistencia 24/7</li>
                    <li><i class="fa-solid fa-check"></i> Ingreso: 0 hasta 9 años con 365 días</li>
                    <li><i class="fa-solid fa-check"></i> Descuento en farmacia y beneficios</li>
                    <li><i class="fa-solid fa-check"></i> Libre elección en todo Chile</li>
                </ul>
            </div>
            <input type="radio" name="vehType" class="vt-radio" value="basico">
        </div>

        <div class="veh-type-card pro-card" onclick="selectType('pro', this)" style="border-color: #2563EB; background: rgba(37, 99, 235, 0.05);">
            <div class="vt-icon" style="background: #2563EB; color: white;"><i class="fa-solid fa-shield-dog"></i></div>
            <div class="vt-info">
                <h4 style="color: #2563EB;">Asistencia Mascota Pro <span style="font-size: 0.7em; background: #2563EB; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;">Recomendado</span></h4>
                <div class="plan-price">$5.555 / mes</div>
                <ul class="pet-feature-list">
                    <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                    <li><i class="fa-solid fa-check"></i> Asistencia 24/7</li>
                    <li><i class="fa-solid fa-check"></i> Ingreso: 0 hasta 9 años con 365 días</li>
                    <li><i class="fa-solid fa-check"></i> Descuento, mayor cobertura y beneficios</li>
                    <li><i class="fa-solid fa-check"></i> Libre elección en todo Chile</li>
                </ul>
            </div>
            <input type="radio" name="vehType" class="vt-radio" value="pro">
        </div>

        <div class="veh-type-card" onclick="selectType('senior', this)">
            <div class="vt-icon"><i class="fa-solid fa-bone"></i></div>
            <div class="vt-info">
                <h4>Asistencia Senior</h4>
                <div class="plan-price">$5.555 / mes</div>
                <ul class="pet-feature-list">
                    <li><i class="fa-solid fa-check"></i> ¡Reembolso rápido y simple!</li>
                    <li><i class="fa-solid fa-check"></i> Asistencia 24/7</li>
                    <li><i class="fa-solid fa-check"></i> Ingreso: 7 hasta 13 años con 365 días</li>
                    <li><i class="fa-solid fa-check"></i> Exámenes, mayor cobertura</li>
                    <li><i class="fa-solid fa-check"></i> Descuento en farmacia y beneficios</li>
                </ul>
            </div>
            <input type="radio" name="vehType" class="vt-radio" value="senior">
        </div>
    </div>
"""

grid_pattern = re.compile(r'<div class="veh-type-grid">.*?</div>\s*</div>\s*</div>', re.DOTALL)
c = grid_pattern.sub(pet_cards_new.strip(), c, count=1)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Updated cotizacion-mascota-1.html with rich features")
