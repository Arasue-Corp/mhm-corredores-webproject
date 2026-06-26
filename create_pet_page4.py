import re

with open("cotizacion/cotizacion-17.html", "r", encoding="utf-8") as f:
    c4 = f.read()

# Modify title
c4 = c4.replace("<title>Alex AI Car Insurance Quote | Review Information</title>", "<title>Cotización Asistencia Mascota | Resumen | MHM</title>")

c4 = c4.replace('<span>15</span>/<span>15</span>', '<span>4</span>/<span>4</span>') # though cotizacion-17 might not have this, it's just in case

# Replace header
c4 = c4.replace('Review Information', 'Resumen de Cotización')
c4 = c4.replace('Verify your details below. Changes trigger automatic recalculation.', 'Verifica los datos de tu mascota y tu plan antes de finalizar.')

# We will replace all the forms with a simpler Pet Summary card
new_main_content = """
        <header class="brand-page-header">
            <div class="title-group">
                <h1 class="text-gradient-corp">Resumen de Cotización</h1>
                <div class="aurora-line"></div> 
            </div>
            <p>Verifica los datos de tu mascota y tu plan antes de finalizar.</p>
        </header>

        <form id="editForm" onsubmit="event.preventDefault(); window.location.href='../index.html';">

            <div class="section-label">
                <h2><i class="fa-solid fa-user text-indigo"></i> Datos del Dueño</h2>
            </div>

            <div class="premium-card">
                <div class="card-body">
                    <div class="grid-2">
                        <div class="inp-group"><label>Nombre Completo</label><input type="text" class="clean-input locked" value="Juan Pérez" readonly></div>
                        <div class="inp-group"><label>RUT</label><input type="text" class="clean-input locked" value="12.345.678-9" readonly></div>
                        <div class="inp-group"><label>Correo Electrónico</label><input type="text" class="clean-input locked" value="juan@gmail.com" readonly></div>
                        <div class="inp-group"><label>Teléfono</label><input type="text" class="clean-input locked" value="+56 9 1234 5678" readonly></div>
                    </div>
                </div>
            </div>

            <div class="section-label mt-60" style="margin-top: 40px;">
                <h2><i class="fa-solid fa-paw text-indigo"></i> Datos de la Mascota</h2>
            </div>

            <div class="premium-card">
                <div class="card-body">
                    <div class="grid-2">
                        <div class="inp-group"><label>Nombre de la Mascota</label><input type="text" class="clean-input locked" value="Firulais" readonly></div>
                        <div class="inp-group"><label>Especie</label><input type="text" class="clean-input locked" value="Perro" readonly></div>
                        <div class="inp-group"><label>Raza</label><input type="text" class="clean-input locked" value="Mestizo" readonly></div>
                        <div class="inp-group"><label>Edad</label><input type="text" class="clean-input locked" value="3 años" readonly></div>
                    </div>
                </div>
            </div>

            <div class="section-label mt-60" style="margin-top: 40px;">
                <h2><i class="fa-solid fa-shield-dog text-indigo"></i> Plan Seleccionado</h2>
            </div>
            
            <div class="premium-card">
                <div class="card-body">
                    <div class="grid-2">
                        <div class="inp-group"><label>Plan</label><input type="text" class="clean-input locked" value="Asistencia Mascota Pro" style="color: var(--brand-blue, #2563EB); font-weight: bold;" readonly></div>
                        <div class="inp-group"><label>Valor Mensual Referencial</label><input type="text" class="clean-input locked" value="$8.990 CLP" readonly></div>
                    </div>
                </div>
            </div>

            <div class="legal-accordian" style="margin-top: 40px;">
                <details>
                    <summary>Términos y Condiciones <i class="fa-solid fa-chevron-down"></i></summary>
                    <div class="legal-text">
                        <p>Al hacer clic en "Finalizar Cotización", confirmas que los datos ingresados son correctos y aceptas los términos y condiciones de MHM Seguros para el producto de Asistencia Veterinaria.</p>
                    </div>
                </details>
            </div>

            <div class="dock-wrapper">
                <div class="dock-glass" id="tour-action-dock">
                    <button type="button" class="dock-btn text" onclick="window.history.back()">
                        Volver
                    </button>
                    <button type="button" class="dock-btn primary" onclick="window.location.href='../index.html'">
                       <i class="fa-solid fa-check"></i> Finalizar Cotización
                    </button>
                </div>
            </div>
        </form>
"""

pattern = re.compile(r'<header class="brand-page-header">.*?</form>', re.DOTALL)
c4 = pattern.sub(new_main_content.strip(), c4)

with open("cotizacion/cotizacion-mascota-4.html", "w", encoding="utf-8") as f:
    f.write(c4)

print("Created cotizacion-mascota-4.html")
