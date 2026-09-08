import re

with open("cotizacion/cotizacion-mascota-2.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Remove quotesModal
quotes_modal_pattern = r'<div class="modal-backdrop-aurora" id="quotesModal">.*?</div>\s*</div>\s*</div>'
# Let's just find where it starts and where footer starts, or use a more precise regex.
# Since it's right before the footer, we can just replace everything between </div> </div> and <footer...
# Actually, the best way to remove it is to match the exact string or use regex.
c = re.sub(r'<div class="modal-backdrop-aurora" id="quotesModal">.*?(?=<footer class="footer-aurora">)', '', c, flags=re.DOTALL)

# Also remove leadModal which might be below footer
c = re.sub(r'<!-- Modal Leads -->.*?</div>\s*</div>\s*</div>', '', c, flags=re.DOTALL)


# 2. Add Ruta de Contratación to the sidebar
sidebar_title_pattern = r'(<div class="organic-panel"[^>]*>)'
ruta_html = """\\1
                <div class="sidebar-title text-gradient-corp" style="font-size: 1.25rem; font-weight: 800; margin-bottom: 20px;">
                    Ruta de Contratación
                </div>
                <ul class="aurora-list" style="margin-bottom: 30px; border-bottom: 1px solid #E2E8F0; padding-bottom: 20px;">
                    <li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Selección de Plan</li>
                    <li class="active"><span class="pulse-dot"></span> Datos del Contratante</li>
                    <li><i class="fa-regular fa-circle"></i> Datos de la Mascota</li>
                    <li><i class="fa-regular fa-circle"></i> Pago y Emisión</li>
                </ul>
"""
c = re.sub(sidebar_title_pattern, ruta_html, c, count=1)

with open("cotizacion/cotizacion-mascota-2.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Fixed cotizacion-mascota-2.html")
