import re

with open("cotizacion/cotizacion-2.html", "r", encoding="utf-8") as f:
    c2 = f.read()

# Modify title
c2 = c2.replace("<title>Cotización de Seguro Automotriz | MHM Corredores</title>", "<title>Cotización de Asistencia Mascota | MHM Corredores</title>")

# Modify the progress header
c2 = c2.replace('<span>2</span>/<span>15</span>', '<span>2</span>/<span>3</span>')
c2 = c2.replace('Datos del vehículo', 'Datos del dueño')
c2 = c2.replace('href="cotizacion-1.html"', 'href="cotizacion-mascota-1.html"')

# Modify the form
new_main_content = """
                    <h2 class="form-main-title">Datos del Dueño</h2>
                    <p class="form-desc">Ingresa tus datos de contacto para enviarte la propuesta formal.</p>
                    
                    <div class="form-group" style="margin-bottom: 20px;">
                        <label class="form-label">Nombre completo</label>
                        <input type="text" class="form-input" placeholder="Ej: Juan Pérez" />
                    </div>

                    <div class="form-group" style="margin-bottom: 20px;">
                        <label class="form-label">RUT</label>
                        <input type="text" class="form-input" placeholder="Ej: 12.345.678-9" />
                    </div>

                    <div class="form-group" style="margin-bottom: 20px;">
                        <label class="form-label">Correo electrónico</label>
                        <input type="email" class="form-input" placeholder="Ej: juan@gmail.com" />
                    </div>

                    <div class="form-group" style="margin-bottom: 30px;">
                        <label class="form-label">Teléfono</label>
                        <input type="tel" class="form-input" placeholder="Ej: +56 9 1234 5678" />
                    </div>

                    <div class="form-actions">
                        <a href="cotizacion-mascota-3.html" class="btn-aurora-gradient btn-continue">
                            <span>Continuar</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
"""

pattern = re.compile(r'<h2 class="form-main-title">.*?<div class="form-actions">.*?</div>', re.DOTALL)
c2 = pattern.sub(new_main_content.strip(), c2)

with open("cotizacion/cotizacion-mascota-2.html", "w", encoding="utf-8") as f:
    f.write(c2)

print("Created cotizacion-mascota-2.html")
