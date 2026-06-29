import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# Replace the previous CSS for the toggle
old_css_pattern = r'/\* Mobile Details Toggle \*/.*?</style>'

new_css = """/* Native Mobile Details Accordion */
        .mobile-details { width: 100%; margin: 0; padding: 0; }
        .mobile-details summary { display: none; }
        
        @media (max-width: 768px) {
            .mobile-details summary {
                display: flex;
                background: #F1F5F9; border: 1px solid #E2E8F0; color: #334155; 
                font-weight: 600; font-size: 0.85rem; padding: 8px 16px; border-radius: 20px;
                cursor: pointer; margin: 15px auto 0; text-align: center; width: max-content;
                align-items: center; justify-content: center; transition: all 0.2s ease;
                list-style: none; /* hide arrow */
                outline: none;
            }
            .mobile-details summary::-webkit-details-marker { display: none; }
            .mobile-details summary:hover { background: #E2E8F0; }
            .mobile-details summary i { margin-left: 6px; transition: transform 0.3s; }
            .mobile-details[open] summary i { transform: rotate(180deg); }
            
            /* Change text dynamically using pseudo element */
            .mobile-details summary span::before { content: "Ver detalles"; }
            .mobile-details[open] summary span::before { content: "Ocultar detalles"; }
        }
        
        @media (min-width: 769px) {
            .mobile-details .pet-feature-list {
                display: block !important; 
            }
        }
    </style>"""

c = re.sub(old_css_pattern, new_css, c, flags=re.DOTALL)

# Replace the buttons and wrap the ul in <details>
c = re.sub(
    r'<button type="button" class="details-toggle-btn" onclick="toggleDetails\(\'list-basico\', this\)">.*?</button>\s*<ul class="pet-feature-list" id="list-basico">',
    r'<details class="mobile-details">\n                <summary><span></span> <i class="fa-solid fa-chevron-down"></i></summary>\n                <ul class="pet-feature-list">',
    c
)
c = re.sub(
    r'<button type="button" class="details-toggle-btn" onclick="toggleDetails\(\'list-pro\', this\)">.*?</button>\s*<ul class="pet-feature-list" id="list-pro">',
    r'<details class="mobile-details">\n                <summary><span></span> <i class="fa-solid fa-chevron-down"></i></summary>\n                <ul class="pet-feature-list">',
    c
)
c = re.sub(
    r'<button type="button" class="details-toggle-btn" onclick="toggleDetails\(\'list-senior\', this\)">.*?</button>\s*<ul class="pet-feature-list" id="list-senior">',
    r'<details class="mobile-details">\n                <summary><span></span> <i class="fa-solid fa-chevron-down"></i></summary>\n                <ul class="pet-feature-list">',
    c
)

# We need to close the <details> tag after the </ul> for each list.
# The structure is: 
# </ul>
# <div class="qty-controls">
c = c.replace('</ul>\n                <div class="qty-controls">', '</ul>\n                </details>\n                <div class="qty-controls">')


# Remove the JS function completely
js_pattern = r'    function toggleDetails\(listId, btn\) \{.*?    \}\n'
c = re.sub(js_pattern, '', c, flags=re.DOTALL)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Native HTML accordion implemented successfully!")
