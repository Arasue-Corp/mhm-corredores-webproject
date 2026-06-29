import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# Fix CSS
old_css = """        /* Mobile Details Toggle */
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
        }"""

new_css = """        /* Mobile Details Toggle */
        .details-toggle-btn {
            display: none;
            background: #F1F5F9; border: 1px solid #E2E8F0; color: #334155; 
            font-weight: 600; font-size: 0.85rem; padding: 8px 16px; border-radius: 20px;
            cursor: pointer; margin: 15px auto 0; text-align: center; width: max-content;
            align-items: center; justify-content: center; transition: all 0.2s ease;
        }
        .details-toggle-btn:hover { background: #E2E8F0; }
        .details-toggle-btn i { margin-left: 6px; transition: transform 0.3s; }
        .details-toggle-btn.open i { transform: rotate(180deg); }
        
        @media (max-width: 768px) {
            .details-toggle-btn { display: flex; }
            .pet-feature-list { display: none !important; }
            .pet-feature-list.show-details { display: block !important; animation: fadeIn 0.3s ease; }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-5px); }
            to { opacity: 1; transform: translateY(0); }
        }"""

c = c.replace(old_css, new_css)

# Fix JS
old_js = """    function toggleDetails(btn) {
        const list = btn.nextElementSibling;
        list.classList.toggle('show-details');
        btn.classList.toggle('open');
        if (list.classList.contains('show-details')) {
            btn.innerHTML = 'Ocultar detalles <i class="fa-solid fa-chevron-up"></i>';
        } else {
            btn.innerHTML = 'Ver detalles <i class="fa-solid fa-chevron-down"></i>';
        }
    }"""

new_js = """    function toggleDetails(btn) {
        // Find the next element sibling that is a UL
        let list = btn.nextElementSibling;
        while(list && list.tagName !== 'UL') {
            list = list.nextElementSibling;
        }
        
        if (!list) return;
        
        list.classList.toggle('show-details');
        btn.classList.toggle('open');
        if (list.classList.contains('show-details')) {
            btn.innerHTML = 'Ocultar detalles <i class="fa-solid fa-chevron-up"></i>';
        } else {
            btn.innerHTML = 'Ver detalles <i class="fa-solid fa-chevron-down"></i>';
        }
    }"""

c = c.replace(old_js, new_js)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Fixed toggle button CSS and JS!")
