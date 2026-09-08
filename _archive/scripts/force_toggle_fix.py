import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# Make the CSS default hide aggressively
old_css = """        @media (max-width: 768px) {
            .details-toggle-btn { display: flex; position: relative; z-index: 10; }
            .pet-feature-list { 
                max-height: 0; 
                overflow: hidden; 
                opacity: 0; 
                transition: all 0.4s ease-in-out; 
                margin-top: 0 !important;
            }
            .pet-feature-list.show-details { 
                max-height: 500px; 
                opacity: 1; 
                margin-top: 15px !important;
            }
        }"""

new_css = """        @media (max-width: 768px) {
            .details-toggle-btn { display: flex; position: relative; z-index: 10; }
            .pet-feature-list { 
                display: none; 
            }
        }"""

c = c.replace(old_css, new_css)

# Update JS to explicitly force CSS text
old_js = """    function toggleDetails(listId, btn) {
        console.log('Toggling details for:', listId);
        const list = document.getElementById(listId);
        if (!list) return;
        
        // Ensure any hardcoded inline display is removed
        list.style.display = '';
        
        if (list.classList.contains('show-details')) {
            list.classList.remove('show-details');
            btn.innerHTML = 'Ver detalles <i class="fa-solid fa-chevron-down"></i>';
        } else {
            list.classList.add('show-details');
            btn.innerHTML = 'Ocultar detalles <i class="fa-solid fa-chevron-up"></i>';
        }
    }"""

new_js = """    function toggleDetails(listId, btn) {
        const list = document.getElementById(listId);
        if (!list) {
            console.error('List not found:', listId);
            return;
        }
        
        const isHidden = window.getComputedStyle(list).display === 'none';
        
        if (isHidden || list.style.display === 'none') {
            list.style.setProperty('display', 'block', 'important');
            btn.innerHTML = 'Ocultar detalles <i class="fa-solid fa-chevron-up"></i>';
        } else {
            list.style.setProperty('display', 'none', 'important');
            btn.innerHTML = 'Ver detalles <i class="fa-solid fa-chevron-down"></i>';
        }
    }"""

c = c.replace(old_js, new_js)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Aggressive JS toggle fix applied!")
