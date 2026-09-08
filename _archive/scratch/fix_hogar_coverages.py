import os

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'

old_list = """                        <ul style="list-style: none; padding: 0; margin: 0 0 20px 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Urgencia médica por accidente.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Descuento en farmacias.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Consulta médica general y Telemedicina.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Orientación médica telefónica.
                            </li>
                        </ul>"""

new_list = """                        <ul style="list-style: none; padding: 0; margin: 0 0 20px 0; color: #475569; font-size: 0.95rem; line-height: 1.6;">
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Plomería.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Electricidad.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Cerrajería.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Vidriería.
                            </li>
                            <li style="display: flex; align-items: start; margin-bottom: 10px;">
                                <i class="fa-solid fa-circle" style="font-size: 0.4rem; color: #104C5C; margin-top: 8px; margin-right: 12px;"></i>
                                Instalación de cortinas.
                            </li>
                        </ul>"""

for i in range(1, 6):
    file_path = os.path.join(base_dir, f'cotizacion-asistencia-hogar-{i}.html')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if old_list in content:
            content = content.replace(old_list, new_list)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated list in {file_path}")

old_table = """                    <tbody style="color: #334155;">
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
                    </tbody>"""

new_table = """                    <tbody style="color: #334155;">
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">PLOMERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Ilimitado</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">ELECTRICIDAD</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Ilimitado</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">CERRAJERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Ilimitado</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">VIDRIERÍA</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Ilimitado</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">INSTALACIÓN DE CORTINAS</td>
                            <td style="padding: 15px;"><strong style="color: #E11D48;">100%</strong></td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Ilimitado</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">3</td>
                        </tr>
                    </tbody>"""

step1 = os.path.join(base_dir, 'cotizacion-asistencia-hogar-1.html')
if os.path.exists(step1):
    with open(step1, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_table in content:
        content = content.replace(old_table, new_table)
        content = content.replace("Los descuentos y beneficios de salud son entregados en línea a través de i-Med o a través de red de prestadores propios", "Los servicios de asistencia al hogar están sujetos a disponibilidad técnica y geográfica.")
        with open(step1, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated table in step 1")

plan = '/home/alex-ai/.gemini/antigravity/brain/c524acb4-25b1-4b6e-8c52-1687d5d51e80/implementation_plan.md'
if os.path.exists(plan):
    os.remove(plan)
