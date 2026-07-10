import re

with open('cotizacion/cotizacion-escolar-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the CSS hover effect
content = content.replace("""        .veh-type-card:hover { 
            border-color: #2ED9C3; transform: translateY(-5px); 
            box-shadow: 0 15px 35px rgba(46, 217, 195, 0.15); 
            background: white;
        }""", """        .veh-type-card:hover { 
            border-color: #93C524; transform: translateY(-5px); 
            box-shadow: 0 15px 35px rgba(147, 197, 36, 0.3); 
        }""")

# 2. Fix the JS block 
js_start = content.find('    function closeCoverageModal() {')
js_end = content.find('</script>', js_start)

if js_start != -1 and js_end != -1:
    correct_js = """    function closeCoverageModal() {
        const modal = document.getElementById('coverageModal');
        if(modal) {
            modal.classList.remove('is-visible');
            setTimeout(() => {
                modal.style.display = 'none';
            }, 400);
        }
    }
"""
    content = content[:js_start] + correct_js + content[js_end:]

# 3. Replace the tables in the modal
modal_body_start = content.find('<div class="modal-body-tech" style="overflow-x: auto;">')
if modal_body_start != -1:
    modal_body_end = content.find('</div>\n            <div class="modal-footer-tech"', modal_body_start)
    
    table_html = """<div class="modal-body-tech" style="padding: 0; overflow-x: auto;">
                <table class="responsive-table" id="table-escolar" style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
                    <thead style="background: #1C4E5E; color: white;">
                        <tr>
                            <th style="padding: 15px; font-weight: 700; border: 1px solid #E2E8F0;">SERVICIO</th>
                            <th style="padding: 15px; font-weight: 700; border: 1px solid #E2E8F0;">PROTECCIÓN</th>
                            <th style="padding: 15px; font-weight: 700; border: 1px solid #E2E8F0;">LÍMITE</th>
                            <th style="padding: 15px; font-weight: 700; border: 1px solid #E2E8F0;">MAX EVENTOS AL AÑO</th>
                        </tr>
                    </thead>
                    <tbody style="color: #334155;">
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">URGENCIA MÉDICA AL ALUMNO POR ACCIDENTE</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong> ISAPRE - FONASA<br> / <strong style="color: #E11D48;">50%</strong> FONASA A</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">21 UF</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">12</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">CONSULTA MÉDICA GENERAL</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong> ISAPRE - FONASA<br> / <strong style="color: #E11D48;">50%</strong> FONASA A</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">2 UF</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">5</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">DESCUENTO EN FARMACIAS</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">50%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$10.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">12</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">TELEMEDICINA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">2 UF</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">5</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ORIENTACIÓN MÉDICA TELEFÓNICA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">2 UF</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">12</td>
                        </tr>
                    </tbody>
                </table>
                <div style="text-align: center; font-size: 0.85rem; font-weight: 700; color: #1C4E5E; padding: 20px;">
                    Los descuentos y beneficios de salud son entregados en línea a través de i-Med o a través de red de prestadores propios
                </div>
    """
    if modal_body_end != -1:
        content = content[:modal_body_start] + table_html + content[modal_body_end:]

with open('cotizacion/cotizacion-escolar-1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done fixing CSS, JS, and Modal")
