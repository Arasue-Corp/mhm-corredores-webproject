import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# Replace the CSS
old_css_pattern = r'/\* Native Mobile Details Accordion \*/.*?</style>'

new_css = """/* Mobile CSS Checkbox Accordion */
        .accordion-checkbox { display: none; }
        .accordion-label { display: none; }
        
        @media (max-width: 768px) {
            .accordion-label {
                display: flex;
                background: #F1F5F9; border: none; color: #475569; 
                font-weight: 700; font-size: 0.95rem; padding: 10px 20px; border-radius: 12px;
                cursor: pointer; margin: 15px auto 0; text-align: center; width: max-content;
                align-items: center; justify-content: center; transition: all 0.2s ease;
                user-select: none;
            }
            .accordion-label:hover { background: #E2E8F0; color: #0F172A; }
            .accordion-label i { margin-left: 6px; transition: transform 0.3s; }
            
            .pet-feature-list {
                max-height: 0;
                overflow: hidden;
                opacity: 0;
                transition: all 0.3s ease-in-out;
                margin-top: 0 !important;
                margin-bottom: 0 !important;
            }
            
            .accordion-checkbox:checked ~ .pet-feature-list {
                max-height: 500px;
                opacity: 1;
                margin-top: 15px !important;
                margin-bottom: 15px !important;
            }
            
            .accordion-checkbox:checked ~ .accordion-label i {
                transform: rotate(180deg);
            }
            .accordion-checkbox:checked ~ .accordion-label .label-text::before {
                content: attr(data-open);
            }
            .accordion-checkbox:not(:checked) ~ .accordion-label .label-text::before {
                content: attr(data-closed);
            }
            .accordion-label .label-text { font-size: 0; } 
            .accordion-label .label-text::before { font-size: 0.95rem; }
        }
    </style>"""

c = re.sub(old_css_pattern, new_css, c, flags=re.DOTALL)

# Replace the <details> and <summary> wrappers
def replace_details(match):
    idx = match.group(1) # 'basico', 'pro', or 'senior'
    content = match.group(2) # the ul content
    
    return f"""<input type="checkbox" id="toggle-{idx}" class="accordion-checkbox">
                <label for="toggle-{idx}" class="accordion-label">
                    <span class="label-text" data-open="Ocultar detalles" data-closed="Ver detalles">Ver detalles</span>
                    <i class="fa-solid fa-chevron-down"></i>
                </label>
                <ul class="pet-feature-list">{content}</ul>"""

# The regex needs to match:
# <details class="mobile-details">
#    <summary><span></span> <i class="fa-solid fa-chevron-down"></i></summary>
#    <ul class="pet-feature-list">...</ul>
# </details>
# But wait, we have 3 of them and we need to inject the specific ID 'basico', 'pro', 'senior'.
# I'll just do it manually with string replacements.

# Basico
c = re.sub(
    r'<details class="mobile-details">\s*<summary><span></span> <i class="fa-solid fa-chevron-down"></i></summary>\s*<ul class="pet-feature-list">\s*(.*?)\s*</ul>\s*</details>\s*<div class="qty-controls">\s*<button type="button" class="qty-btn" onclick="updateQty\(\'basico\', -1\)">',
    r'<input type="checkbox" id="toggle-basico" class="accordion-checkbox">\n                <label for="toggle-basico" class="accordion-label">\n                    <span class="label-text" data-open="Ocultar detalles" data-closed="Ver detalles">Ver detalles</span>\n                    <i class="fa-solid fa-chevron-down"></i>\n                </label>\n                <ul class="pet-feature-list">\n\1\n                </ul>\n                <div class="qty-controls">\n                    <button type="button" class="qty-btn" onclick="updateQty(\'basico\', -1)">',
    c, flags=re.DOTALL
)

# Pro
c = re.sub(
    r'<details class="mobile-details">\s*<summary><span></span> <i class="fa-solid fa-chevron-down"></i></summary>\s*<ul class="pet-feature-list">\s*(.*?)\s*</ul>\s*</details>\s*<div class="qty-controls">\s*<button type="button" class="qty-btn" onclick="updateQty\(\'pro\', -1\)">',
    r'<input type="checkbox" id="toggle-pro" class="accordion-checkbox">\n                <label for="toggle-pro" class="accordion-label">\n                    <span class="label-text" data-open="Ocultar detalles" data-closed="Ver detalles">Ver detalles</span>\n                    <i class="fa-solid fa-chevron-down"></i>\n                </label>\n                <ul class="pet-feature-list">\n\1\n                </ul>\n                <div class="qty-controls">\n                    <button type="button" class="qty-btn" onclick="updateQty(\'pro\', -1)">',
    c, flags=re.DOTALL
)

# Senior
c = re.sub(
    r'<details class="mobile-details">\s*<summary><span></span> <i class="fa-solid fa-chevron-down"></i></summary>\s*<ul class="pet-feature-list">\s*(.*?)\s*</ul>\s*</details>\s*<div class="qty-controls">\s*<button type="button" class="qty-btn" onclick="updateQty\(\'senior\', -1\)">',
    r'<input type="checkbox" id="toggle-senior" class="accordion-checkbox">\n                <label for="toggle-senior" class="accordion-label">\n                    <span class="label-text" data-open="Ocultar detalles" data-closed="Ver detalles">Ver detalles</span>\n                    <i class="fa-solid fa-chevron-down"></i>\n                </label>\n                <ul class="pet-feature-list">\n\1\n                </ul>\n                <div class="qty-controls">\n                    <button type="button" class="qty-btn" onclick="updateQty(\'senior\', -1)">',
    c, flags=re.DOTALL
)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("CSS checkbox accordion implemented successfully!")
