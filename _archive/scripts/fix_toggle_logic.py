import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# Replace buttons to pass ID
c = c.replace('<button type="button" class="details-toggle-btn" onclick="toggleDetails(this)">Ver detalles <i class="fa-solid fa-chevron-down"></i></button>\n                <ul class="pet-feature-list">',
              '<button type="button" class="details-toggle-btn" onclick="toggleDetails(\'list-basico\', this)">Ver detalles <i class="fa-solid fa-chevron-down"></i></button>\n                <ul class="pet-feature-list" id="list-basico">', 1)

c = c.replace('<button type="button" class="details-toggle-btn" onclick="toggleDetails(this)">Ver detalles <i class="fa-solid fa-chevron-down"></i></button>\n                <ul class="pet-feature-list">',
              '<button type="button" class="details-toggle-btn" onclick="toggleDetails(\'list-pro\', this)">Ver detalles <i class="fa-solid fa-chevron-down"></i></button>\n                <ul class="pet-feature-list" id="list-pro">', 1)

c = c.replace('<button type="button" class="details-toggle-btn" onclick="toggleDetails(this)">Ver detalles <i class="fa-solid fa-chevron-down"></i></button>\n                <ul class="pet-feature-list">',
              '<button type="button" class="details-toggle-btn" onclick="toggleDetails(\'list-senior\', this)">Ver detalles <i class="fa-solid fa-chevron-down"></i></button>\n                <ul class="pet-feature-list" id="list-senior">', 1)

# Fix JS
old_js = """    function toggleDetails(btn) {
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

new_js = """    function toggleDetails(listId, btn) {
        const list = document.getElementById(listId);
        if (!list) return;
        
        if (list.classList.contains('show-details') || list.style.display === 'block') {
            list.classList.remove('show-details');
            list.style.setProperty('display', 'none', 'important');
            btn.innerHTML = 'Ver detalles <i class="fa-solid fa-chevron-down"></i>';
        } else {
            list.classList.add('show-details');
            list.style.setProperty('display', 'block', 'important');
            btn.innerHTML = 'Ocultar detalles <i class="fa-solid fa-chevron-up"></i>';
        }
    }"""

c = c.replace(old_js, new_js)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Toggle logic hardcoded with IDs and inline styles!")
