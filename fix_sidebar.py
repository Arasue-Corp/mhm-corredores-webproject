with open("cotizacion/cotizacion-mascota-2.html", "r", encoding="utf-8") as f:
    c = f.read()

target = '<div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px; border-bottom: 1px solid #E2E8F0; padding-bottom: 15px;">\n                    Resumen de Selección\n                </div>'

ruta_html = """
                <div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px;">
                    Ruta de Contratación
                </div>
                <ul class="aurora-list" style="margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px;">
                    <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Selección de Plan</li>
                    <li class="active"><span class="pulse-dot"></span> Datos del Contratante</li>
                    <li><i class="fa-regular fa-circle"></i> Datos de la Mascota</li>
                    <li><i class="fa-regular fa-circle"></i> Pago y Emisión</li>
                </ul>

                <div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px; border-bottom: 1px solid #E2E8F0; padding-bottom: 15px;">
                    Resumen de Selección
                </div>
"""

# Replace
if target in c:
    c = c.replace(target, ruta_html)
else:
    print("TARGET NOT FOUND. Trying fallback.")
    target2 = 'Resumen de Selección'
    c = c.replace(target2, "Ruta de Contratación\n                </div>\n                <ul class=\"aurora-list\" style=\"margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px;\">\n                    <li style=\"color: #10B981; font-weight: 600;\"><i class=\"fa-solid fa-circle-check\" style=\"color: #10B981;\"></i> Selección de Plan</li>\n                    <li class=\"active\"><span class=\"pulse-dot\"></span> Datos del Contratante</li>\n                    <li><i class=\"fa-regular fa-circle\"></i> Datos de la Mascota</li>\n                    <li><i class=\"fa-regular fa-circle\"></i> Pago y Emisión</li>\n                </ul>\n\n                <div class=\"sidebar-title text-gradient-corp\" style=\"font-size: 1.25rem; font-weight: 800; margin-bottom: 20px; border-bottom: 1px solid #E2E8F0; padding-bottom: 15px;\">\n                    Resumen de Selección")

with open("cotizacion/cotizacion-mascota-2.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Added Ruta de Contratacion")
