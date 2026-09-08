import re

with open("cotizacion/cotizacion-1.html", "r", encoding="utf-8") as f:
    c1 = f.read()

# Grab the block from <div class="term-legal"> all the way to <div class="mhm-premium-features"> ... </div></div>
# Actually, I'll grab from <div class="term-legal"> to </div>\n            </aside>
# Wait, let's just grab by regex from cotizacion-1.html
match = re.search(r'<div class="term-legal">.*?</aside>', c1, re.DOTALL)
if match:
    missing_block = match.group(0)
    # We should also replace the terms legal text inside missing_block for the pet context
    missing_block = missing_block.replace(
        '<p>Al continuar, confirmas que has elegido correctamente la categoría de tu vehículo para que MHM Corredores pueda brindarte la mejor opción disponible.</p>',
        '<p>Al continuar, confirmas que has elegido el plan adecuado para tu mascota.</p>'
    )
    # Fix the JS for the pet context
    js_pattern = re.compile(r"if\(type === 'liviano'\) {.*?else if \(type === 'pesado' \|\| type === 'km'\)", re.DOTALL)
    new_js = """if(type === 'basico' || type === 'pro' || type === 'senior') {
                // Add a subtle transition effect before redirecting
                document.body.style.opacity = '0';
                document.body.style.transition = 'opacity 0.3s ease';
                setTimeout(() => {
                    window.location.href = 'cotizacion-mascota-2.html';
                }, 300);
            } else if (false)"""
    missing_block = js_pattern.sub(new_js, missing_block)

    # Now let's put it into cotizacion-mascota-1.html
    with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
        c_pet = f.read()
    
    # We need to replace `</aside>` in cotizacion-mascota-1.html with missing_block
    # Because right now it just has:
    # </div>
    #         </aside>
    # We should replace that specific `</aside>` with the missing_block (which includes `</aside>`)
    
    c_pet = c_pet.replace("            </aside>", missing_block)
    
    with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
        f.write(c_pet)
    
    print("Fixed layout by restoring missing block!")
else:
    print("Could not find the missing block in cotizacion-1.html")

