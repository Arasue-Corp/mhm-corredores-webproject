import sys

mascota_file = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-mascota-5.html'
escolar_file = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-escolar-5.html'

with open(escolar_file, 'r', encoding='utf-8') as f:
    escolar_lines = f.readlines()

# lines 303 to 724
new_content_lines = escolar_lines[302:724] 
new_content = "".join(new_content_lines)

new_content = new_content.replace(
    '<i class="fa-solid fa-paw"></i>',
    '<i class="fa-solid fa-user-graduate"></i>'
)
new_content = new_content.replace(
    '<h4 class="cs-name">Mascotas</h4>',
    '<h4 class="cs-name">Escolar</h4>'
)

with open(mascota_file, 'r', encoding='utf-8') as f:
    mascota_lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(mascota_lines):
    if '<div class="specs-layout-grid">' in line and start_idx == -1:
        start_idx = i
    if start_idx != -1 and '</aside>' in line:
        end_idx = i + 1
        break

if start_idx != -1 and end_idx != -1:
    final_lines = mascota_lines[:start_idx] + [new_content + "\n"] + mascota_lines[end_idx+1:]
    with open(mascota_file, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print("Success")
else:
    print(f"Could not find indices: {start_idx}, {end_idx}")
