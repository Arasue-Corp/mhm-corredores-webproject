import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# Add CSS
css_addition = """
        /* Mobile Details Toggle */
        .details-toggle-btn {
            display: none;
            background: none; border: none; color: #2563EB; font-weight: 700; font-size: 0.9rem;
            cursor: pointer; margin-top: 10px; padding: 0; text-align: left; width: 100%; justify-content: center;
        }
        .details-toggle-btn i { margin-left: 5px; transition: transform 0.3s; }
        .details-toggle-btn.open i { transform: rotate(180deg); }
        
        @media (max-width: 768px) {
            .details-toggle-btn { display: flex; align-items: center; }
            .pet-feature-list { display: none; }
            .pet-feature-list.show-details { display: block; animation: fadeIn 0.3s ease; }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-5px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>"""

c = c.replace("</style>", css_addition, 1)

# Add Toggle Button before <ul class="pet-feature-list">
c = c.replace('<ul class="pet-feature-list">', '<button type="button" class="details-toggle-btn" onclick="toggleDetails(this)">Ver detalles <i class="fa-solid fa-chevron-down"></i></button>\n                <ul class="pet-feature-list">')

# Add JS Function
js_addition = """
    function toggleDetails(btn) {
        const list = btn.nextElementSibling;
        list.classList.toggle('show-details');
        btn.classList.toggle('open');
        if (list.classList.contains('show-details')) {
            btn.innerHTML = 'Ocultar detalles <i class="fa-solid fa-chevron-up"></i>';
        } else {
            btn.innerHTML = 'Ver detalles <i class="fa-solid fa-chevron-down"></i>';
        }
    }
"""

c = c.replace("function updateQty", js_addition + "\n    function updateQty")

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Toggle buttons added successfully!")
