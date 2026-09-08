import re

with open('cotizacion/cotizacion-escolar-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Title and main headings
html = html.replace('Asistencia Escolar', 'Asistencia Vehicular')
html = html.replace('escolar', 'vehicular')
html = html.replace('ESCOLAR', 'VEHICULAR')

# Price
html = html.replace('3.780', '5.390')
html = html.replace('3780', '5390')
html = html.replace('3,780', '5,390')

# Image
html = html.replace('article-3.webp', 'seguro-auto.jpg')

# Replace coverages in card
card_cov_regex = r'(<ul class=\"pet-feature-list\">\s*)(.*?)(\s*</ul>)'
new_card_cov = '''
                    <li><i class="fa-solid fa-check"></i> Protección para neumáticos</li>
                    <li><i class="fa-solid fa-check"></i> Protección para amortiguadores</li>
                    <li><i class="fa-solid fa-check"></i> Protección al vidrio lateral del vehículo</li>
                    <li><i class="fa-solid fa-check"></i> Cerrajería Vehicular</li>
                    <li><i class="fa-solid fa-check"></i> Protección insignia o emblema</li>
'''
html = re.sub(card_cov_regex, r'\g<1>' + new_card_cov.strip() + r'\g<3>', html, flags=re.DOTALL)

# Replace table in modal
table_regex = r'(<tbody style=\"color: #334155;\">\s*)(.*?)(\s*</tbody>)'
new_table = '''
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Protección para neumáticos</td>
                            <td style="padding: 15px;">Sí</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Según Plan</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">-</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Protección para amortiguadores</td>
                            <td style="padding: 15px;">Sí</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Según Plan</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">-</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F8FAFC;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Protección al vidrio lateral del vehículo</td>
                            <td style="padding: 15px;">Sí</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Según Plan</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">-</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Cerrajería Vehicular</td>
                            <td style="padding: 15px;">Sí</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Según Plan</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">-</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0;">
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Protección insignia o emblema</td>
                            <td style="padding: 15px;">Sí</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">Según Plan</td>
                            <td style="padding: 15px; font-weight: 600; color: #1C4E5E;">-</td>
                        </tr>
'''
html = re.sub(table_regex, r'\g<1>' + new_table.strip() + r'\g<3>', html, flags=re.DOTALL)

# Onboarding texts
html = html.replace('Datos del Apoderado', 'Tus Datos')
html = html.replace('Información del Estudiante', 'Información del Vehículo')
html = html.replace('Nombre, RUT, curso y edad.', 'Patente, marca, modelo y año.')
html = html.replace('fa-graduation-cap', 'fa-car')

with open('cotizacion/cotizacion-vehicular-1.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Generated cotizacion-vehicular-1.html')
