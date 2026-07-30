import re

with open('cotizacion/cotizacion-mascota-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the wrong CSS injected earlier
if '/* VEH TYPE CARD STYLES */' in content:
    content = re.sub(r'/\* VEH TYPE CARD STYLES \*/.*?(?=</style>)', '', content, flags=re.DOTALL)

# Extract correct CSS from hogar
with open('cotizacion/cotizacion-asistencia-hogar-1.html', 'r', encoding='utf-8') as f:
    hogar_content = f.read()

# Grab from .veh-type-grid to the end of .qty-value
match = re.search(r'(\.veh-type-grid\s*\{.*\.qty-value\s*\{.*?\})', hogar_content, re.DOTALL)
if match:
    correct_css = match.group(1)
    
    # Inject correct CSS
    new_content = content.replace('</style>', '\n        ' + correct_css + '\n    </style>')
    
    with open('cotizacion/cotizacion-mascota-1.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("CSS successfully replaced with the correct design.")
else:
    print("Could not find correct CSS in hogar.")
