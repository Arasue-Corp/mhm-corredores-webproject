import re

with open("cotizacion/cotizacion-mascota-3.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Modify the Flow button to trigger the modal
old_link = 'href="https://www.flow.cl/" target="_blank"'
new_link = 'href="javascript:void(0)" onclick="document.getElementById(\'successModal\').style.display=\'flex\';"'
c = c.replace(old_link, new_link)

# 2. Add the Success Modal HTML
# We can inject it right before </body>
modal_html = """
    <!-- Success Modal -->
    <div id="successModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(71, 102, 114, 0.9); z-index: 9999; align-items: center; justify-content: center; backdrop-filter: blur(4px);">
        <div style="background: white; border-radius: 20px; width: 90%; max-width: 450px; padding: 50px 30px 40px; text-align: center; box-shadow: 0 25px 50px rgba(0,0,0,0.15); position: relative; animation: modalPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
            
            <div style="position: relative; margin: 0 auto 30px; width: 120px; height: 120px; display: flex; align-items: center; justify-content: center;">
                <!-- Simulated Dog and Confetti -->
                <i class="fa-solid fa-dog" style="font-size: 5rem; color: #104C5C; position: relative; z-index: 2;"></i>
                <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; z-index: 1;">
                    <i class="fa-solid fa-star" style="position: absolute; top: 10%; left: 10%; color: #FCD34D; font-size: 1rem; animation: float 3s ease-in-out infinite;"></i>
                    <i class="fa-solid fa-circle" style="position: absolute; top: 20%; right: 10%; color: #F472B6; font-size: 0.6rem; animation: float 2.5s ease-in-out infinite 0.5s;"></i>
                    <i class="fa-solid fa-heart" style="position: absolute; bottom: 15%; left: 20%; color: #10B981; font-size: 0.8rem; animation: float 3.5s ease-in-out infinite 1s;"></i>
                    <i class="fa-solid fa-certificate" style="position: absolute; bottom: 20%; right: 15%; color: #A78BFA; font-size: 0.9rem; animation: float 2.8s ease-in-out infinite 0.2s;"></i>
                </div>
            </div>

            <h2 style="color: #104C5C; font-size: 1.6rem; font-weight: 800; margin-bottom: 25px; line-height: 1.3;">PROCESO DE COMPRA<br>COMPLETADO</h2>
            
            <p style="color: #1E293B; font-weight: 700; font-size: 1rem; margin-bottom: 5px;">¡Importante!</p>
            <p style="color: #475569; font-size: 0.95rem; margin-bottom: 40px; line-height: 1.5; font-weight: 500;">
                A continuación debes completar TUS DATOS Y<br>LOS DE TUS MASCOTAS.
            </p>

            <button onclick="window.location.href='cotizacion-mascota-4.html'" style="background: #104C5C; color: white; border: none; width: 100%; padding: 18px; border-radius: 12px; font-size: 1.25rem; font-weight: 700; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(16, 76, 92, 0.3);" onmouseover="this.style.background='#0A323D'; this.style.transform='translateY(-2px)';" onmouseout="this.style.background='#104C5C'; this.style.transform='translateY(0)';">
                ACEPTAR
            </button>
        </div>
    </div>
    
    <style>
        @keyframes modalPop {
            0% { transform: scale(0.8); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
    </style>
</body>"""

c = c.replace('</body>', modal_html)

with open("cotizacion/cotizacion-mascota-3.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Modal added to step 3.")
