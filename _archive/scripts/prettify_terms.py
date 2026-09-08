import re
import os

def main():
    root_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main'
    terms_path = os.path.join(root_dir, 'terminos-condiciones/index.html')

    with open(terms_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the pdf widget
    pdf_widget_pattern = re.compile(r'<div class="sidebar-widget pdf-widget">.*?</div>\s*</div>\s*</aside>', re.DOTALL)
    html = pdf_widget_pattern.sub('</div>\n                </aside>', html)

    # Prettify the content area
    new_legal_content = """<div class="legal-content-area">
                    <section id="privacidad" class="legal-card highlight-card">
                        <h2 class="card-title"><i class="fa-solid fa-shield-halved" style="color: var(--aurora-blue); margin-right: 12px;"></i>1. Política de privacidad</h2>
                        <p class="mb-4" style="color: #334155; font-size: 1.05rem;"><strong>MHM CORREDORA DE SEGUROS</strong> tiene por finalidad y compromiso el respetar la confidencialidad y privacidad de los datos personales de sus clientes, potenciales clientes, y en general toda persona que se relacione con nosotros, ajustando su actuar a lo dispuesto en el artículo 19 N°4 de la Constitución Política de la República de Chile y a la Ley 19.628 de Protección a la Vida Privada, principios OCDE y buenas prácticas en materia de protección de datos personales.</p>
                        
                        <div class="compliance-box mb-4">
                            <div class="icon-check" style="background-color: var(--aurora-blue);"><i class="fa-solid fa-user-shield"></i></div>
                            <div>
                                <strong style="color: var(--aurora-blue); display: block; margin-bottom: 5px;">Secreto Profesional</strong>
                                <p class="mb-0 text-sm" style="color: #475569;">Nuestros profesionales basan su trabajo en el más estricto secreto profesional para garantizar tu seguridad y confianza.</p>
                            </div>
                        </div>

                        <p style="color: #475569;">Ninguna persona que acceda a nuestro sitio para navegar en él se encuentra obligado a proporcionar su información personal. No obstante, si optas por completar tus datos personales (edad, región, e-mail, nombre completo), haremos tratamiento de tus datos <strong>sólo para comunicarnos contigo</strong> y poder brindarte la información solicitada en conjunto con las cotizaciones necesarias.</p>
                        
                        <div class="alert-box-blue" style="border-left: 4px solid var(--aurora-purple); background: #F8FAFC; padding: 15px 20px; border-radius: 8px; margin-top: 20px;">
                            <strong style="color: var(--aurora-purple);"><i class="fa-solid fa-handshake" style="margin-right: 8px;"></i>Nuestro Compromiso</strong>
                            <p class="mb-0 mt-2 text-sm" style="color: #475569;">No compartiremos tu información personal con ningún tercero, excepto cuando sea requerido por ley. No te añadiremos a ninguna de nuestras listas de distribución de correos sin tu consentimiento expreso.</p>
                        </div>
                    </section>

                    <section id="cookies" class="legal-card">
                        <h2 class="card-title"><i class="fa-solid fa-cookie-bite" style="color: #D97706; margin-right: 12px;"></i>2. Uso de Cookies</h2>
                        <p style="color: #475569; font-size: 1.05rem;">Una <strong>cookie</strong> es un pequeño fragmento de información que un sitio web almacena en el archivo de cookies de su navegador y que permite que el sitio recuerde al Usuario. Estas cookies no recuperan la información almacenada en su disco duro y no causan daño ni a su equipo ni a los archivos que se guardan en ella.</p>
                        <p style="color: #475569;">Usted no está obligado a aceptar cookies, y de hecho, puede modificar su navegador para que no las acepte. En el caso del Canal de Atención constituido por el sitio web, MHM CORREDORA DE SEGUROS utiliza cookies para:</p>
                        <ul style="color: #475569; margin-left: 20px; margin-bottom: 20px; list-style-type: disc;">
                            <li style="margin-bottom: 8px;">Identificar a los Usuarios que visitan el Sitio Web.</li>
                            <li style="margin-bottom: 8px;">Recordar las preferencias de los Usuarios y proporcionar servicios personalizados.</li>
                            <li style="margin-bottom: 8px;">Hacer un seguimiento de la utilización del Sitio Web.</li>
                        </ul>
                        <p style="color: #475569; font-size: 0.9rem; font-style: italic;">Asimismo, el Sitio Web puede incluir cookies de terceros tales como empresas afiliadas, proveedores de servicios y/o contenidos.</p>
                    </section>

                    <section id="seguridad" class="legal-card">
                        <h2 class="card-title"><i class="fa-solid fa-lock" style="color: var(--aurora-indigo); margin-right: 12px;"></i>3. Seguridad de la información</h2>
                        <p style="color: #475569;">MHM CORREDORA DE SEGUROS se compromete a tratar toda la información de sus titulares con reserva y a adoptar los resguardos posibles y razonables de conformidad con los estándares y prácticas de la industria relacionados con la seguridad de la información.</p>
                        
                        <div class="compliance-box" style="background: #F4F4F5; border-color: #E4E4E7; margin-top: 15px;">
                            <div class="icon-check" style="background-color: var(--aurora-indigo);"><i class="fa-solid fa-server"></i></div>
                            <div>
                                <strong style="color: var(--aurora-indigo); display: block; margin-bottom: 5px;">Infraestructura Protegida</strong>
                                <p class="mb-0 text-sm" style="color: #475569;">Utilizamos una tecnología a nivel de infraestructura de la página web con el objeto de proteger de manera razonable la información personal recolectada, limitando en lo posible y razonablemente el acceso de terceros.</p>
                            </div>
                        </div>
                    </section>

                    <section id="circular" class="legal-card">
                        <h2 class="card-title"><i class="fa-solid fa-building-columns" style="color: var(--aurora-coral); margin-right: 12px;"></i>4. Circular N°2131 CMF</h2>
                        
                        <div style="background: linear-gradient(to right, rgba(239, 68, 68, 0.05), transparent); padding: 20px; border-left: 4px solid var(--aurora-coral); border-radius: 0 8px 8px 0; margin-bottom: 20px;">
                            <h4 style="color: var(--aurora-coral); font-size: 1.1rem; margin-bottom: 10px; font-weight: 700;">Información sobre atención de clientes y presentación de consultas y reclamos</h4>
                            <p style="color: #334155; margin-bottom: 0;">En virtud de la Circular Nº 2131 de 28 de noviembre de 2013, las compañías de seguros, corredores de seguros y liquidadores de siniestros, deberán recibir, registrar y responder todas las presentaciones, consultas o reclamos que se les presenten directamente por el contratante, asegurado, beneficiarios o legítimos interesados o sus mandatarios.</p>
                        </div>

                        <div class="misc-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 25px;">
                            <div class="misc-card" style="background: #F8FAFC; padding: 20px; border-radius: 12px; border: 1px solid #E2E8F0;">
                                <h5 style="color: var(--aurora-blue); font-size: 1rem; margin-bottom: 10px;"><i class="fa-solid fa-pen-to-square" style="margin-right: 8px;"></i>¿Cómo presentar?</h5>
                                <p style="color: #475569; font-size: 0.9rem; margin-bottom: 0;">Las presentaciones pueden ser efectuadas en todas las oficinas presencialmente, por correo postal, medios electrónicos, o telefónicamente, <strong>sin formalidades</strong>, en el horario normal de atención.</p>
                            </div>
                            <div class="misc-card" style="background: #F8FAFC; padding: 20px; border-radius: 12px; border: 1px solid #E2E8F0;">
                                <h5 style="color: var(--aurora-blue); font-size: 1rem; margin-bottom: 10px;"><i class="fa-solid fa-stopwatch" style="margin-right: 8px;"></i>Tiempos de respuesta</h5>
                                <p style="color: #475569; font-size: 0.9rem; margin-bottom: 0;">Recibida una presentación, consulta o reclamo, ésta deberá ser respondida en el plazo más breve posible, el que <strong>no podrá exceder de 20 días hábiles</strong> contados desde su recepción.</p>
                            </div>
                        </div>

                        <p style="color: #475569;">El interesado, en caso de disconformidad respecto de lo informado, o bien cuando exista demora injustificada de la respuesta, podrá recurrir a la Superintendencia de Valores y Seguros, Área de Protección al Inversionista y Asegurado, cuyas oficinas se encuentran ubicadas en Av. Libertador Bernardo O´Higgins 1449, piso 1°, Santiago, o a través del sitio web <a href="https://www.svs.cl" target="_blank" style="color: var(--aurora-blue); font-weight: 600; text-decoration: none;">www.svs.cl</a>.</p>
                    </section>
                </div>"""

    # Replace legal-content-area
    html = re.sub(r'<div class="legal-content-area">.*?</div>\s*</div>\s*</div>\s*</main>', new_legal_content + '\n            </div>\n        </div>\n    </main>', html, flags=re.DOTALL)

    with open(terms_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Terms and conditions prettified successfully.")

if __name__ == '__main__':
    main()
