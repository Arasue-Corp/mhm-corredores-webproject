import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Update the header
c = c.replace(
    '<h1 class="text-gradient-corp">Datos Principales</h1>',
    '<h1 class="text-gradient-corp">Planes de Asistencia</h1>'
)
c = c.replace(
    '<p>Indícanos qué tipo de seguro de auto buscas para guiarte en el proceso.</p>',
    '<p>Elige el plan de Asistencia Veterinaria que mejor se adapte a tu mascota.</p>'
)

# 2. Replace the vehicle type grid with the pet cards
pet_cards = """
    <div class="veh-type-grid">
        <div class="veh-type-card" onclick="selectType('basico', this)">
            <div class="vt-icon"><i class="fa-solid fa-dog"></i></div>
            <div class="vt-info">
                <h4>Asistencia Mascota</h4>
                <p>Urgencias médicas, vacunas y más.</p>
            </div>
            <input type="radio" name="vehType" class="vt-radio" value="basico">
        </div>

        <div class="veh-type-card" onclick="selectType('pro', this)" style="border-color: #2563EB; background: rgba(37, 99, 235, 0.05);">
            <div class="vt-icon" style="background: #2563EB; color: white;"><i class="fa-solid fa-shield-dog"></i></div>
            <div class="vt-info">
                <h4 style="color: #2563EB;">Asistencia Mascota Pro <span style="font-size: 0.7em; background: #2563EB; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;">Recomendado</span></h4>
                <p>Telemedicina, descuentos y consultas generales.</p>
            </div>
            <input type="radio" name="vehType" class="vt-radio" value="pro">
        </div>

        <div class="veh-type-card" onclick="selectType('senior', this)">
            <div class="vt-icon"><i class="fa-solid fa-bone"></i></div>
            <div class="vt-info">
                <h4>Asistencia Senior</h4>
                <p>Para mascotas mayores a 7 años.</p>
            </div>
            <input type="radio" name="vehType" class="vt-radio" value="senior">
        </div>
    </div>
"""

# Replace the specific grid HTML
# We can find <div class="veh-type-grid"> until </div></div></div> (end of grid)
grid_pattern = re.compile(r'<div class="veh-type-grid">.*?</div>\s*</div>\s*</div>', re.DOTALL)
c = grid_pattern.sub(pet_cards.strip(), c, count=1)

# Fix the JavaScript selectType function inside the form
js_pattern = re.compile(r"if\(type === 'liviano'\) {.*?else if \(type === 'pesado' \|\| type === 'km'\)", re.DOTALL)
new_js = """if(type === 'basico' || type === 'pro' || type === 'senior') {
                // Add a subtle transition effect before redirecting
                document.body.style.opacity = '0';
                document.body.style.transition = 'opacity 0.3s ease';
                setTimeout(() => {
                    window.location.href = 'cotizacion-mascota-2.html';
                }, 300);
            } else if (false)"""
c = js_pattern.sub(new_js, c)

c = c.replace(
    '<p>Al continuar, confirmas que has elegido correctamente la categoría de tu vehículo para que MHM Corredores pueda brindarte la mejor opción disponible.</p>',
    '<p>Al continuar, confirmas que has elegido el plan adecuado para tu mascota.</p>'
)

# 3. Update the onboarding modal
# Replace "Cotizando Asistencia Mascota"
c = c.replace(
    '<h2 class="c-title">Bienvenido a <br><span class="shimmer-text">MHM Seguros</span></h2>',
    '<h2 class="c-title">Cotizando <br><span class="shimmer-text">Asistencia Mascotas</span></h2>'
)

# Replace "Requisitos de Cotización"
# Change icons and texts for Pet requirements
req_pattern = re.compile(r'<div class="info-group">.*?</div>\s*</div>\s*<div class="c-slide" data-step="2">', re.DOTALL)
pet_reqs = """<div class="info-group">
                        
                        <div class="info-card-row">
                            <div class="ic-icon"><i class="fa-solid fa-user"></i></div>
                            <div class="ic-content">
                                <h4>Datos del Dueño</h4>
                                <p>Tu nombre, RUT, teléfono y correo electrónico.</p>
                            </div>
                        </div>

                        <div class="info-card-row" style="border-color: #2ED9C333; background: #f0f9ff;">
                            <div class="ic-icon" style="background:white; color:#2ED9C3;"><i class="fa-solid fa-paw"></i></div>
                            <div class="ic-content">
                                <h4>Información de la Mascota</h4>
                                <p>Nombre, especie, raza y edad de tu mascota.</p>
                            </div>
                        </div>

                        <div class="info-card-row">
                            <div class="ic-icon"><i class="fa-solid fa-shield-dog"></i></div>
                            <div class="ic-content">
                                <h4>Plan Deseado</h4>
                                <p>Elige entre Básico, Pro o Senior según sus necesidades.</p>
                            </div>
                        </div>

                    </div>
                </div>

                <div class="c-slide" data-step="2">"""
c = req_pattern.sub(pet_reqs, c)


with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)
    
print("Updated cotizacion-mascota-1.html")
