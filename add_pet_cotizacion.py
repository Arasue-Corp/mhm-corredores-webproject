file_path = "cotizacion/cotizacion.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

pet_card = """<div class="hub-card" data-covers="['Consultas veterinarias de urgencia', 'Gastos médicos por accidentes', 'Vacunación y chequeos preventivos', 'Asistencia telefónica veterinaria 24/7']" data-desc="Protege a tus mascotas con nuestro seguro de asistencia veterinaria. Cubre gastos médicos, accidentes y más." data-icon="fa-paw" data-link="#" data-tag="Mascotas" data-title="Asistencia Veterinaria" onclick="openModal(this)" onmouseenter="showCustomPopover(this)" onmouseleave="hideCustomPopover()">
<div class="hub-icon"><i class="fa-solid fa-paw"></i></div>
<h3>Asistencia Veterinaria</h3>
<p>Seguro y asistencia completa para tus mascotas.</p>
</div>
"""

# Find the end of tab-asistencias
# It ends with:
# </div>
# </div>
# </main>
# We can just inject it before the last </div> of tab-asistencias.

insert_target = """<h3>Telemedicina</h3>
<p>Consultas médicas online inmediatas sin salir de casa.</p>
</div>"""

if insert_target in content:
    content = content.replace(insert_target, insert_target + "\n" + pet_card)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
