import os

files_to_patch = [
    "cotizacion/cotizacion-salud-2.html",
    "cotizacion/cotizacion-salud-3.html",
    "cotizacion/cotizacion-salud-4.html",
    "cotizacion/cotizacion-salud-5.html"
]

for file_path in files_to_patch:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace the color for the h2 titles
    content = content.replace(
        '<h2 style="font-size: 1.5rem; color: #0F172A; margin-bottom: 30px; font-weight: 800;">Datos del Comprador</h2>',
        '<h2 style="font-size: 1.5rem; color: #796bfc; margin-bottom: 30px; font-weight: 800;">Datos del Contratante</h2>'
    )
    content = content.replace(
        '<h2 style="font-size: 1.5rem; color: #0F172A; margin-bottom: 20px; font-weight: 800;">Datos del Titular</h2>',
        '<h2 style="font-size: 1.5rem; color: #796bfc; margin-bottom: 20px; font-weight: 800;">Datos del Titular</h2>'
    )
    content = content.replace(
        '<h2 style="font-size: 1.5rem; color: #0F172A; margin-bottom: 30px; font-weight: 800;">Datos del Producto</h2>',
        '<h2 style="font-size: 1.5rem; color: #796bfc; margin-bottom: 30px; font-weight: 800;">Datos del Producto</h2>'
    )
    content = content.replace(
        '<h2 style="font-size: 1.5rem; color: #0F172A; margin-bottom: 30px; font-weight: 800;">Beneficiarios</h2>',
        '<h2 style="font-size: 1.5rem; color: #796bfc; margin-bottom: 30px; font-weight: 800;">Beneficiarios</h2>'
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Titles updated!")
