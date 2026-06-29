import re

with open("cotizacion/cotizacion-mascota-2.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Remove alexOnboarding modal completely
c = re.sub(r'<div id="alexOnboarding" class="crystal-overlay">.*?(?=<footer class="footer-aurora">)', '', c, flags=re.DOTALL)
# Wait, let's be careful not to delete scripts. The `alexOnboarding` is usually at the bottom.
# Let's delete from `<div id="alexOnboarding"` to the very end of its closing tag. 
# A safer way: just replace `<div id="alexOnboarding".*?</div>\s*</div>\s*</div>` maybe?
# I'll just remove the whole div block. It's safe to use a generic regex if I'm careful.

c = re.sub(r'<div id="alexOnboarding".*?</button>.*?</div>.*?</div>.*?</div>', '', c, flags=re.DOTALL)
# Actually, the modal might have a lot of nested divs.
# I will just write a function to delete it by finding matching tags.

def remove_div_by_id(html, div_id):
    start = html.find(f'<div id="{div_id}"')
    if start == -1: return html
    
    count = 0
    i = start
    while i < len(html):
        if html[i:i+4] == '<div':
            count += 1
            i += 4
        elif html[i:i+6] == '</div>':
            count -= 1
            i += 6
            if count == 0:
                return html[:start] + html[i:]
        else:
            i += 1
    return html

c = remove_div_by_id(c, "alexOnboarding")

# 2. Insert aside after main-spec-col closing tags
target_insertion = """</script>

                </div>
            </div>"""

if target_insertion in c:
    aside_html = """</script>

                </div>
            </div>
            
            <aside class="config-sidebar anim-entry delay-2">
                <div class="organic-panel" style="position: sticky; top: 100px;">
                    
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
                    
                    <div id="cart-summary-step2">
                        <!-- Javascript will render selected plans here -->
                    </div>

                    <div style="background: rgba(16, 185, 129, 0.05); border: 1px dashed #10B981; border-radius: 12px; padding: 15px; margin-top: 25px; text-align: center;">
                        <i class="fa-solid fa-shield-cat" style="font-size: 2rem; color: #10B981; margin-bottom: 10px;"></i>
                        <h4 style="margin: 0 0 5px 0; color: #0F172A; font-weight: 700; font-size: 1rem;">Protección Activa</h4>
                        <p style="margin: 0; font-size: 0.85rem; color: #64748B;">Estás a pocos pasos de asegurar a tu mascota.</p>
                    </div>
                </div>
            </aside>
"""
    c = c.replace(target_insertion, aside_html)
    print("ASIDE INSERTED.")
else:
    print("TARGET NOT FOUND FOR INSERTION.")

with open("cotizacion/cotizacion-mascota-2.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Fixed step 2")
