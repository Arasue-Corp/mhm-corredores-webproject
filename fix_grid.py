import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

old_css = r"""\.veh-type-grid \{
\s*display: grid; 
\s*grid-template-columns: repeat\(auto-fit, minmax\(300px, 1fr\)\); 
\s*gap: 25px; 
\s*margin-bottom: 40px;
\s*\}"""

new_css = """.veh-type-grid {
            display: grid; 
            grid-template-columns: repeat(3, 1fr); 
            gap: 20px; 
            margin-bottom: 40px;
        }
        @media (max-width: 992px) {
            .veh-type-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 768px) {
            .veh-type-grid { grid-template-columns: 1fr; }
        }"""

c = re.sub(old_css, new_css, c)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Grid layout forced to 3 columns!")
