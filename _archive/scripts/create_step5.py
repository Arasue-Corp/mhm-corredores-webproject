import re

with open('cotizacion/cotizacion-mascota-4.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace everything from <div class="wizard-container"> to the end of <div class="specs-layout-grid">
# or the </main> equivalent if there is one. 
# Let's find the page-wrapper.
wrapper_start = content.find('<div class="page-wrapper">')
if wrapper_start != -1:
    # find where page-wrapper closes
    # Actually, we can just replace everything inside <div class="page-wrapper">
    # Wait, the footer starts with <footer class="footer-aurora">
    footer_start = content.find('<footer class="footer-aurora">')
    
    head_content = content[:wrapper_start]
    footer_content = content[footer_start:]
    
    success_html = """
    <div class="page-wrapper" style="background: transparent; min-height: 80vh; display: flex; align-items: center; justify-content: center; position: relative;">
        <!-- Confetti Background (CSS based) -->
        <div class="confetti-container" style="position: absolute; top:0; left:0; width:100%; height:100%; overflow:hidden; z-index:0; pointer-events:none;">
            <!-- Simple dots via CSS background -->
        </div>
        
        <div class="success-card-wrapper" style="position: relative; z-index: 1; background: white; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); max-width: 800px; width: 95%; margin: 40px auto; overflow: hidden;">
            
            <div style="background: #A3D80E; color: white; text-align: center; padding: 20px; font-size: 1.4rem; font-weight: 800; letter-spacing: 1px;">
                ¡TU ASISTENCIA YA ESTÁ ACTIVA!
            </div>
            
            <div style="padding: 40px 30px;">
                <h3 style="color: #104C5C; font-size: 1.1rem; font-weight: 700; margin-bottom: 15px;">-Detalle de contratación:</h3>
                <ul style="list-style: none; padding: 0; margin: 0 0 35px 20px; color: #475569; line-height: 1.8;">
                    <li><strong style="color: #1E293B;">Nº de contrato:</strong> <span id="contractNumber">1234567</span></li>
                    <li><strong style="color: #1E293B;">Fecha de activación:</strong> <span id="activationDate">Cargando...</span></li>
                    <li><strong style="color: #1E293B;">Medio de pago:</strong> Tarjeta de débito terminada en *****4539</li>
                    <li><strong style="color: #1E293B;">Total mensual:</strong> <span id="totalMonthly">Cargando...</span></li>
                </ul>
                
                <h3 style="color: #104C5C; font-size: 1.1rem; font-weight: 700; margin-bottom: 15px;">-Acciones disponibles:</h3>
                <ul style="padding-left: 20px; margin: 0 0 40px 20px; color: #475569; line-height: 1.8;">
                    <li>Te enviamos una copia de tu contrato a <strong id="ownerEmail" style="color: #1E293B;">tu correo</strong> o <a href="#" style="color: #104C5C; font-weight: 700; text-decoration: underline;">descarga aquí</a>. *revisar por contrato dsp de 24 hrs.</li>
                    <li>Conoce el <a href="#" style="color: #104C5C; font-weight: 700; text-decoration: underline;">detalle legal de tu asistencia</a>.</li>
                </ul>
                
                <div style="text-align: center; margin-top: 50px;">
                    <h2 style="color: #104C5C; font-size: 1.4rem; font-weight: 800; margin-bottom: 10px;">CUIDAR LO QUE QUIERES NO TERMINA AQUÍ <i class="fa-solid fa-heart" style="color: #22C55E;"></i></h2>
                    <p style="color: #64748B; font-size: 1rem; margin-bottom: 30px;">Descubre otras asistencias que pueden ayudarte en tu día a día:</p>
                    
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
                        <!-- Hogar -->
                        <div style="background: #F8FAFC; border-radius: 16px; padding: 30px 20px; text-align: center; border: 1px solid #F1F5F9; transition: transform 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                            <div style="background: #104C5C; width: 90px; height: 90px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; color: white; font-size: 2.5rem;">
                                <i class="fa-solid fa-house"></i>
                            </div>
                            <h4 style="color: #104C5C; font-size: 1.2rem; font-weight: 800; margin-bottom: 5px; text-transform: uppercase; text-decoration: underline; text-decoration-color: #104C5C; text-decoration-thickness: 2px;">Hogar</h4>
                            <span style="color: #64748B; font-size: 0.8rem; font-weight: 700;">DESDE <strong style="color: #104C5C; font-size: 1.1rem;">$7.990</strong></span>
                        </div>
                        
                        <!-- Movilidad -->
                        <div style="background: #F8FAFC; border-radius: 16px; padding: 30px 20px; text-align: center; border: 1px solid #F1F5F9; transition: transform 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                            <div style="background: #104C5C; width: 90px; height: 90px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; color: white; font-size: 2.5rem;">
                                <i class="fa-solid fa-car-side"></i>
                            </div>
                            <h4 style="color: #104C5C; font-size: 1.2rem; font-weight: 800; margin-bottom: 5px; text-transform: uppercase; text-decoration: underline; text-decoration-color: #104C5C; text-decoration-thickness: 2px;">Movilidad</h4>
                            <span style="color: #64748B; font-size: 0.8rem; font-weight: 700;">DESDE <strong style="color: #104C5C; font-size: 1.1rem;">$3.200</strong></span>
                        </div>
                        
                        <!-- Salud -->
                        <div style="background: #F8FAFC; border-radius: 16px; padding: 30px 20px; text-align: center; border: 1px solid #F1F5F9; transition: transform 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                            <div style="background: #104C5C; width: 90px; height: 90px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; color: white; font-size: 2.5rem;">
                                <i class="fa-solid fa-hand-holding-medical"></i>
                            </div>
                            <h4 style="color: #104C5C; font-size: 1.2rem; font-weight: 800; margin-bottom: 5px; text-transform: uppercase; text-decoration: underline; text-decoration-color: #104C5C; text-decoration-thickness: 2px;">Salud</h4>
                            <span style="color: #64748B; font-size: 0.8rem; font-weight: 700;">DESDE <strong style="color: #104C5C; font-size: 1.1rem;">$3.780</strong></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Generar número de contrato random
            document.getElementById('contractNumber').innerText = Math.floor(Math.random() * 9000000) + 1000000;
            
            // Fecha actual
            const date = new Date();
            const options = { day: 'numeric', month: 'long', year: 'numeric' };
            document.getElementById('activationDate').innerText = date.toLocaleDateString('es-ES', options);
            
            // Obtener email del cliente
            const clientStr = sessionStorage.getItem('mhmPetClient');
            if (clientStr) {
                const client = JSON.parse(clientStr);
                if(client.email) {
                    document.getElementById('ownerEmail').innerText = client.email;
                }
            }
            
            // Calcular total mensual
            const cartStr = sessionStorage.getItem('mhmPetCart');
            if (cartStr) {
                const plans = JSON.parse(cartStr);
                let total = 0;
                for(let id in plans) {
                    if(plans[id].qty > 0) {
                        const price = parseInt(plans[id].price.replace(/\\D/g, ''));
                        total += price * plans[id].qty;
                    }
                }
                document.getElementById('totalMonthly').innerText = "$" + total.toLocaleString('es-CL');
            } else {
                document.getElementById('totalMonthly').innerText = "$5.555";
            }
        });
    </script>
    <style>
        .confetti-container {
            background-image: radial-gradient(#FDE047 15%, transparent 16%), radial-gradient(#FCA5A5 15%, transparent 16%), radial-gradient(#60A5FA 15%, transparent 16%), radial-gradient(#34D399 15%, transparent 16%);
            background-size: 90px 90px, 110px 110px, 130px 130px, 150px 150px;
            background-position: 0 0, 40px 60px, 100px 30px, 20px 120px;
            opacity: 0.2;
        }
        @media (max-width: 600px) {
            .success-card-wrapper {
                margin: 20px auto;
                border-radius: 12px;
            }
            .success-card-wrapper > div:first-child {
                font-size: 1.1rem;
                padding: 15px;
            }
            .success-card-wrapper > div:last-child {
                padding: 25px 15px;
            }
        }
    </style>
    """
    
    with open('cotizacion/cotizacion-mascota-5.html', 'w', encoding='utf-8') as f:
        f.write(head_content + success_html + footer_content)

print("Created cotizacion-mascota-5.html")
