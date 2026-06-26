import re

with open("cotizacion/cotizacion-2.html", "r", encoding="utf-8") as f:
    c3 = f.read()

# Modify title
c3 = c3.replace("<title>Cotización de Seguro Automotriz | MHM Corredores</title>", "<title>Cotización de Asistencia Mascota | MHM Corredores</title>")

# Modify the progress header
c3 = c3.replace('<span>2</span>/<span>15</span>', '<span>3</span>/<span>3</span>')
c3 = c3.replace('Datos del vehículo', 'Datos de la mascota')
c3 = c3.replace('href="cotizacion-1.html"', 'href="cotizacion-mascota-2.html"')

# Modify the form
new_main_content = """
                    <h2 class="form-main-title">Datos de la mascota</h2>
                    <p class="form-desc">Cuéntanos un poco sobre tu mejor amigo.</p>
                    
                    <div class="form-group" style="margin-bottom: 20px;">
                        <label class="form-label">Nombre de la mascota</label>
                        <input type="text" class="form-input" placeholder="Ej: Firulais" />
                    </div>

                    <div class="form-group" style="margin-bottom: 20px;">
                        <label class="form-label">Especie</label>
                        <select class="form-input" style="appearance: none; background-color: #fff;">
                            <option value="">Selecciona...</option>
                            <option value="perro">Perro</option>
                            <option value="gato">Gato</option>
                        </select>
                    </div>

                    <div class="form-group" style="margin-bottom: 20px;">
                        <label class="form-label">Raza</label>
                        <input type="text" class="form-input" placeholder="Ej: Mestizo" />
                    </div>

                    <div class="form-group" style="margin-bottom: 30px;">
                        <label class="form-label">Edad (en años)</label>
                        <input type="number" class="form-input" placeholder="Ej: 3" />
                    </div>

                    <div class="form-actions">
                        <a href="cotizacion-mascota-4.html" class="btn-aurora-gradient btn-continue">
                            <span>Ver Resumen</span>
                            <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
"""

pattern = re.compile(r'<h2 class="form-main-title">.*?<div class="form-actions">.*?</div>', re.DOTALL)
c3 = pattern.sub(new_main_content.strip(), c3)

with open("cotizacion/cotizacion-mascota-3.html", "w", encoding="utf-8") as f:
    f.write(c3)

print("Created cotizacion-mascota-3.html")
