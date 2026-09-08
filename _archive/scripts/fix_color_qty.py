import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

old_css = """                background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); color: #059669; 
                font-weight: 600; font-size: 0.85rem; padding: 8px 16px; border-radius: 20px;"""

new_css = """                background: #F1F5F9; border: none; color: #475569; 
                font-weight: 700; font-size: 0.95rem; padding: 10px 20px; border-radius: 12px;"""
c = c.replace(old_css, new_css)

old_hover = """.mobile-details summary:hover { background: rgba(16, 185, 129, 0.2); }"""
new_hover = """.mobile-details summary:hover { background: #E2E8F0; color: #0F172A; }"""
c = c.replace(old_hover, new_hover)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Button color changed to match qty-btn!")
