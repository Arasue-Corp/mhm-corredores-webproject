import re
import os

def main():
    root_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main'
    terms_path = os.path.join(root_dir, 'terminos-condiciones/index.html')

    with open(terms_path, 'r', encoding='utf-8') as f:
        html = f.read()

    new_legal_content = """<div class="legal-content-area">
                    <section id="privacidad" class="legal-card">
                        <h2 class="card-title">1. Política de privacidad</h2>
                        <p class="mb-2">MHM CORREDORA DE SEGUROS tiene por finalidad y compromiso el respetar la confidencialidad y privacidad de los datos personales de sus clientes, potenciales clientes, y en general toda persona que se relacione con MHM CORREDORA DE SEGUROS, ajustando su actuar a lo dispuesto en al artículo 19 N°4 de la Constitución Política de la República de Chile y a la Ley 19.628 de Protección a la Vida Privada, principios OCDE y buenas prácticas en materia de protección de datos personales, esto sumado a que nuestros profesionales basan su trabajo en el secreto profesional.</p>
                        <p>Ninguna persona que acceda a nuestro sitio para navegar en él se encuentra obligado a proporcionar su información personal. No obstante, lo anterior, la persona puede optar por completar sus datos personales los cuales se despliegan solicitando los siguientes datos: edad, región, e-mail, nombre completo, esto para efectos de poder responderle adecuadamente. En ese evento, haremos tratamiento de sus datos sólo para comunicarnos con usted y poder brindarle la información que usted ha solicitado en conjunto con las cotizaciones necesarias a enviar. No compartiremos su información personal con ningún tercero, excepto cuando sea requerido por ley. También podemos utilizar sus datos para comunicarnos con usted para preguntarle si le gustaría recibir información sobre nuestros eventos, publicaciones y otros servicios que podrían ser de su interés. No lo añadiremos a ninguna de nuestras listas de distribución de correos sin su consentimiento expreso.</p>
                    </section>

                    <section id="cookies" class="legal-card">
                        <h2 class="card-title">2. Cookies</h2>
                        <p>Una cookie es un pequeño fragmento de información que un sitio web almacena en el archivo de cookies de su navegador y que permite que el sitio recuerde al Usuario. Estas cookies no recuperan la información almacenada en su disco duro y no causan daño ni a su equipo ni a los archivos que se guardan en ella. Usted no está obligado a aceptar cookies, y de hecho, puede modificar su navegador para que no las acepte. En el caso del Canal de Atención constituido por el sitio web, MHM CORREDORA DE SEGUROS utiliza cookies para identificar a los Usuarios que visitan el Sitio Web, recordar las preferencias de los Usuarios y proporcionar servicios personalizados, así como para hacer un seguimiento de la utilización del Sitio Web. Asimismo, el Sitio Web puede incluir cookies de terceros tales como empresas afiliadas, proveedores de servicios y/o contenidos.</p>
                    </section>

                    <section id="seguridad" class="legal-card">
                        <h2 class="card-title">3. Seguridad de la información</h2>
                        <p>MHM CORREDORA DE SEGUROS se compromete a tratar toda la información de sus titulares con reserva y a adoptar los resguardos posibles y razonables de conformidad con los estándares y prácticas de la industria relacionados con la seguridad de la información, utilizando una tecnología a nivel de infraestructura de la página web con el objeto de proteger de manera razonable la información personal recolectada, limitando en lo posible y razonablemente el acceso de terceros.</p>
                    </section>

                    <section id="circular" class="legal-card">
                        <h2 class="card-title">4. Circular N°2131 CMF</h2>
                        <p>INFORMACION SOBRE ATENCION DE CLIENTES Y PRESENTACIÓN DE CONSULTAS Y RECLAMOS En virtud de la Circular Nº 2131 de 28 de noviembre de 2013, las compañías de seguros, corredores de seguros y liquidadores de siniestros, deberán recibir, registrar y responder todas las presentaciones, consultas o reclamos que se les presenten directamente por el contratante, asegurado, beneficiarios o legítimos interesados o sus mandatarios. Las presentaciones pueden ser efectuadas en todas las oficinas de las entidades en que se atienda público, presencialmente, por correo postal, medios electrónicos, o telefónicamente, sin formalidades, en el horario normal de atención. Recibida una presentación, consulta o reclamo, ésta deberá ser respondida en el plazo más breve posible, el que no podrá exceder de 20 días hábiles contados desde su recepción. El interesado, en caso de disconformidad respecto de lo informado, o bien cuando exista demora injustificada de la respuesta, podrá recurrir a la Superintendencia de Valores y Seguros, Área de Protección al Inversionista y Asegurado, cuyas oficinas se encuentran ubicadas en Av. Libertador Bernardo O´Higgins 1449, piso 1°, Santiago, o a través del sitio web <a href="https://www.svs.cl" target="_blank" style="color:var(--aurora-blue);">www.svs.cl</a>.</p>
                    </section>
                </div>"""

    # Replace legal-content-area
    html = re.sub(r'<div class="legal-content-area">.*?</div>\s*</div>\s*</div>\s*</main>', new_legal_content + '\n            </div>\n        </div>\n    </main>', html, flags=re.DOTALL)
    
    new_toc = """<nav class="toc-nav">
                                <a href="#privacidad" class="toc-link active">1. Política de privacidad</a>
                                <a href="#cookies" class="toc-link">2. Cookies</a>
                                <a href="#seguridad" class="toc-link">3. Seguridad de la información</a>
                                <a href="#circular" class="toc-link">4. Circular N°2131 CMF</a>
                            </nav>"""
                            
    # Replace toc-nav
    html = re.sub(r'<nav class="toc-nav">.*?</nav>', new_toc, html, flags=re.DOTALL)
    
    # Replace header text
    html = re.sub(r'Terms & <span class="text-gradient-tech">Conditions</span>', 'Términos y <span class="text-gradient-tech">Condiciones</span>', html)
    html = re.sub(r'<i class="fa-regular fa-clock"></i> Last Updated: <strong>February 24, 2024</strong>', '<i class="fa-regular fa-clock"></i> Última actualización: <strong>26 de Mayo, 2026</strong>', html)
    html = re.sub(r'<i class="fa-solid fa-globe"></i> Region: <strong>Global / US</strong>', '<i class="fa-solid fa-globe"></i> Región: <strong>Chile</strong>', html)
    html = re.sub(r'<span class="dot-pulse"></span> Active', '<span class="dot-pulse"></span> Activo', html)
    html = re.sub(r'<span class="sidebar-header">Table of Contents</span>', '<span class="sidebar-header">Índice</span>', html)
    html = re.sub(r'<strong class="d-block text-dark">Download Terms</strong>\s*<span class="text-muted text-xs">Offline Version</span>', '<strong class="d-block text-dark">Descargar Términos</strong>\n                                    <span class="text-muted text-xs">Versión Offline</span>', html)

    with open(terms_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Terms and conditions content updated successfully.")

if __name__ == '__main__':
    main()
