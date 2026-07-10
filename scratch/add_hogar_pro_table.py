import os

file_path = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-hogar-1.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the tables
old_table_block = """                <table class="responsive-table" id="table-hogar" style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
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
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA PLOMERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA ELECTRICIDAD</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA CERRAJERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA VIDRIERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">INSTALACIÓN DE CORTINAS</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">PERFORACIONES EN MURO</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$150.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">12</td>
                        </tr>
                    </tbody>
                </table>
                <div style="text-align: center; font-size: 0.85rem; font-weight: 700; color: #1C4E5E; padding: 20px;">
                    Los servicios de asistencia al hogar están sujetos a disponibilidad técnica y geográfica.
                </div>"""

new_table_block = """                <table class="responsive-table" id="table-hogar" style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
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
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA PLOMERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA ELECTRICIDAD</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA CERRAJERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA VIDRIERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">INSTALACIÓN DE CORTINAS</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">PERFORACIONES EN MURO</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$150.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">12</td>
                        </tr>
                    </tbody>
                </table>
                
                <table class="responsive-table" id="table-hogar-pro" style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem; display: none;">
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
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA PLOMERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA ELECTRICIDAD</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA CERRAJERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ASISTENCIA VIDRIERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">INSTALACIÓN DE LUMINARIAS Y/O LÁMPARAS</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$30.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">2</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">INSTALACIÓN DE CORTINAS</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$60.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">PERFORACIONES EN MURO</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$200.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">12</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">PINTURA BAÑO Y COCINA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">$150.000</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">4</td>
                        </tr>
                    </tbody>
                </table>
                <div style="text-align: center; font-size: 0.85rem; font-weight: 700; color: #1C4E5E; padding: 20px;">
                    Los descuentos y beneficios de salud son entregados en línea a través de i-Med o a través de red de prestadores propios
                </div>"""

if old_table_block in content:
    content = content.replace(old_table_block, new_table_block)
else:
    print("WARNING: Table block not found")

# 2. Update JS function openCoverageModal
old_js = """    function openCoverageModal(planId) {
        const modal = document.getElementById('coverageModal');
        
        // Show table
        const titleEl = document.getElementById('covModalTitle');
        titleEl.innerText = 'Coberturas: ' + plans[planId].name;
        
        if(modal) {
            modal.style.display = 'flex';"""

new_js = """    function openCoverageModal(planId) {
        const modal = document.getElementById('coverageModal');
        
        // Show table
        const titleEl = document.getElementById('covModalTitle');
        titleEl.innerText = 'Coberturas: ' + plans[planId].name;
        
        // Toggle tables based on plan
        const tableHogar = document.getElementById('table-hogar');
        const tableHogarPro = document.getElementById('table-hogar-pro');
        if (tableHogar && tableHogarPro) {
            if (planId === 'hogar') {
                tableHogar.style.display = 'table';
                tableHogarPro.style.display = 'none';
            } else if (planId === 'hogar-pro') {
                tableHogar.style.display = 'none';
                tableHogarPro.style.display = 'table';
            }
        }
        
        if(modal) {
            modal.style.display = 'flex';"""

if old_js in content:
    content = content.replace(old_js, new_js)
else:
    print("WARNING: JS block not found")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Pro Table and JS toggle successfully")
