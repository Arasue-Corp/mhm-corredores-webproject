import os

file_path = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-hogar-1.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_tbody = """                    <tbody style="color: #334155;">
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

new_tbody = """                    <tbody style="color: #334155;">
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
                    </tbody>"""

if old_tbody in content:
    content = content.replace(old_tbody, new_tbody)
    print("Replaced table body")
else:
    print("Table body not found")

old_text = '<h4>Información del Estudiante</h4>\\n                                <p>Nombre, edad y nivel escolar de tu hijo(a).</p>'
new_text = '<h4>Información de la Propiedad</h4>\\n                                <p>Dirección y detalles del hogar a proteger.</p>'
if old_text in content:
    content = content.replace(old_text, new_text)
    print("Replaced leftover text")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
