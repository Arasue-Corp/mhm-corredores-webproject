import re
from bs4 import BeautifulSoup

with open("cotizacion/cotizacion.html", "r") as f:
    html = f.read()

# We use BeautifulSoup to modify the hub-cards
soup = BeautifulSoup(html, "html.parser")

products_dict = {
    "Seguro de Auto": {
        "tag": "Protección Vehicular",
        "desc": "Protección completa para tu vehículo personal o comercial. El Seguro Automotriz es un medio eficaz para la protección frente a las consecuencias de los riesgos, daños de un automóvil y frente a terceros.",
        "covers": "['Daños materiales del vehículo (parcial/total)', 'Robo y/o hurto del vehículo', 'Responsabilidad frente a terceros', 'Asistencia en ruta 24/7']",
        "link": "cotizacion-1.html",
        "icon": "fa-car"
    },
    "Seguro de Moto": {
        "tag": "Protección 2 Ruedas",
        "desc": "Asegura tu motocicleta y rueda con total tranquilidad ante accidentes, robos o daños a terceros.",
        "covers": "['Daños materiales', 'Robo, hurto o uso no autorizado', 'Responsabilidad Civil', 'Asistencia de grúa']",
        "link": "#",
        "icon": "fa-motorcycle"
    },
    "SOAP": {
        "tag": "Seguro Obligatorio",
        "desc": "Seguro Obligatorio de Accidentes Personales digital y rápido. Exigido por ley para transitar.",
        "covers": "['Cobertura por muerte accidental', 'Incapacidad permanente total y parcial', 'Gastos médicos y hospitalarios', 'Cobertura para el conductor y terceros']",
        "link": "#",
        "icon": "fa-file-invoice-dollar"
    },
    "Seguro de Bicicleta": {
        "tag": "Micro-movilidad",
        "desc": "Protege tu bici y accesorios contra robo y daños, permitiéndote moverte por la ciudad sin preocupaciones.",
        "covers": "['Robo con fuerza', 'Daños accidentales', 'Responsabilidad civil', 'Asistencia al ciclista']",
        "link": "#",
        "icon": "fa-bicycle"
    },
    "Seguro de Hogar": {
        "tag": "Protección Residencial",
        "desc": "Protege tu propiedad y bienes familiares ante incendios, sismos, robos y otros imprevistos.",
        "covers": "['Incendio y riesgos adicionales', 'Sismo (Opcional)', 'Robo de bienes (Contenido)', 'Asistencia domiciliaria 24/7']",
        "link": "#",
        "icon": "fa-house-chimney"
    },
    "Seguro de Salud": {
        "tag": "Bienestar",
        "desc": "Planes de salud complementaria y catastrófica para reducir tus gastos médicos ambulatorios y hospitalarios.",
        "covers": "['Reducción de gastos médicos', 'Cobertura hospitalaria y catastrófica', 'Medicamentos en farmacias', 'Protección para cargas familiares']",
        "link": "#",
        "icon": "fa-briefcase-medical"
    },
    "Seguro de Deporte": {
        "tag": "Actividad Física",
        "desc": "Cobertura especializada para deportistas amateur y pro ante lesiones deportivas y accidentes.",
        "covers": "['Lesiones en entrenamientos o competición', 'Gastos médicos, kinesiología', 'Incapacidad temporal', 'Cobertura internacional']",
        "link": "#",
        "icon": "fa-person-running"
    },
    "Seguro Dental": {
        "tag": "Salud Bucal",
        "desc": "Amplia red odontológica y reembolsos preferenciales en tratamientos dentales para toda la familia.",
        "covers": "['Consultas y diagnóstico', 'Tratamientos de prevención', 'Ortodoncia e implantes', 'Urgencias dentales 24/7']",
        "link": "#",
        "icon": "fa-tooth"
    },
    "Vida Temporal": {
        "tag": "Tranquilidad Familiar",
        "desc": "Respaldo económico y tranquilidad para tu familia en caso de fallecimiento o invalidez.",
        "covers": "['Fallecimiento natural o accidental', 'Invalidez total y permanente', 'Anticipo por enfermedades graves', 'Asistencia funeraria']",
        "link": "#",
        "icon": "fa-heart"
    },
    "Asistencia de Viajes": {
        "tag": "Viajes Seguros",
        "desc": "Cobertura médica y soporte en el extranjero 24/7 para que viajes con total tranquilidad.",
        "covers": "['Asistencia médica por enfermedad o accidente', 'Pérdida o retraso de equipaje', 'Cancelación de vuelo', 'Repatriación sanitaria']",
        "link": "#",
        "icon": "fa-plane"
    },
    "Asistencia en Carretera": {
        "tag": "Apoyo Vial",
        "desc": "Servicio de grúa, cambio de neumático, carga de batería y más, estés donde estés.",
        "covers": "['Remolque o grúa', 'Cambio de neumáticos', 'Paso de corriente', 'Envío de combustible']",
        "link": "#",
        "icon": "fa-truck-pickup"
    },
    "Telemedicina": {
        "tag": "Salud Digital",
        "desc": "Consultas médicas online inmediatas sin salir de casa, disponibles las 24 horas.",
        "covers": "['Medicina general 24/7', 'Recetas médicas digitales', 'Órdenes de exámenes', 'Orientación pediátrica']",
        "link": "#",
        "icon": "fa-stethoscope"
    }
}

for card in soup.find_all(class_="hub-card"):
    title_el = card.find('h3')
    if not title_el:
        continue
    title = title_el.text.strip()
    if title in products_dict:
        data = products_dict[title]
        # Modify the card to use onclick
        if card.name == 'a':
            card.name = 'div'
            del card['href']
        
        card['onclick'] = 'openModal(this)'
        card['data-title'] = title
        card['data-tag'] = data['tag']
        card['data-desc'] = data['desc']
        card['data-covers'] = data['covers']
        card['data-link'] = data['link']
        card['data-icon'] = data['icon']
        # add popover handler
        card['onmouseenter'] = 'showPopover(this)'
        card['onmouseleave'] = 'hidePopover()'

# We need to inject the CSS for popover and modal, and HTML for popover and modal
injection_css = """
<style>
/* POPOVER HOVER */
.card-popover {
    position: absolute;
    width: 320px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(121, 107, 252, 0.3);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    z-index: 1000;
    pointer-events: none; /* Let clicks pass through to card */
    opacity: 0;
    transform: translateY(10px) scale(0.95);
    transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    text-align: left;
}
.card-popover.visible {
    opacity: 1;
    transform: translateY(0) scale(1);
}
.popover-tag {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #796bfc;
    margin-bottom: 8px;
    display: inline-block;
}
.popover-title {
    font-size: 1.3rem;
    font-weight: 800;
    color: #0F172A;
    margin: 0 0 10px 0;
}
.popover-desc {
    font-size: 0.9rem;
    color: #64748B;
    line-height: 1.5;
    margin: 0;
}

/* PREMIUM MODAL */
.glass-modal-overlay {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(8px);
    z-index: 10000; display: none; align-items: center; justify-content: center;
    opacity: 0; transition: 0.3s;
}
.glass-modal-overlay.active { display: flex; opacity: 1; }
.glass-modal {
    background: white; width: 95%; max-width: 900px; border-radius: 24px;
    overflow: hidden; display: flex; transform: scale(0.9); transition: 0.3s;
    box-shadow: 0 25px 50px rgba(0,0,0,0.2); position: relative;
}
.glass-modal-overlay.active .glass-modal { transform: scale(1); }
.modal-split { display: flex; width: 100%; }
.modal-image-panel {
    width: 40%; background: linear-gradient(135deg, #796bfc, #2ed9c3);
    display: flex; align-items: center; justify-content: center; color: white;
}
.modal-image-placeholder { text-align: center; }
.modal-image-placeholder i { font-size: 4rem; margin-bottom: 15px; }
.modal-image-placeholder span { display: block; font-weight: 600; font-size: 1.2rem; }
.modal-data-panel { width: 60%; padding: 40px; }
.modal-tag {
    display: inline-block; padding: 6px 12px; background: rgba(121, 107, 252, 0.1);
    color: #796bfc; border-radius: 100px; font-size: 0.8rem; font-weight: 700;
    margin-bottom: 15px;
}
.modal-title { font-size: 2rem; font-weight: 800; color: #0F172A; margin-bottom: 15px; }
.modal-desc { font-size: 1rem; color: #64748B; margin-bottom: 30px; line-height: 1.6; }
.modal-benefits { margin-bottom: 30px; }
.benefits-title { font-size: 1.1rem; color: #0F172A; font-weight: 700; margin-bottom: 15px; display: flex; align-items: center; gap: 8px;}
.benefits-title i { color: #2ed9c3; }
.modal-covers-list { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
.modal-covers-list li {
    font-size: 0.9rem; color: #475569; display: flex; align-items: flex-start; gap: 10px;
}
.modal-covers-list li::before {
    content: '\\f00c'; font-family: 'Font Awesome 6 Free'; font-weight: 900;
    color: #796bfc; margin-top: 2px;
}
.modal-actions { display: flex; gap: 15px; }
.modal-btn-primary {
    padding: 14px 28px; background: #796bfc; color: white; border-radius: 12px;
    font-weight: 600; text-decoration: none; display: flex; align-items: center; gap: 10px;
    transition: 0.2s; border: none; cursor: pointer;
}
.modal-btn-primary:hover { background: #6151e3; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(121,107,252,0.2); }
.modal-close-btn {
    position: absolute; top: 20px; right: 20px; width: 40px; height: 40px;
    background: #F1F5F9; border: none; border-radius: 50%; color: #64748B;
    font-size: 1.2rem; cursor: pointer; display: flex; align-items: center; justify-content: center;
    transition: 0.2s; z-index: 10;
}
.modal-close-btn:hover { background: #E2E8F0; color: #0F172A; transform: rotate(90deg); }

@media (max-width: 768px) {
    .modal-split { flex-direction: column; }
    .modal-image-panel { width: 100%; height: 150px; }
    .modal-data-panel { width: 100%; padding: 25px; }
    .modal-covers-list { grid-template-columns: 1fr; }
}
</style>
"""

injection_html = """
<!-- POPOVER -->
<div id="card-popover" class="card-popover">
    <span class="popover-tag" id="po-tag">Tag</span>
    <h3 class="popover-title" id="po-title">Title</h3>
    <p class="popover-desc" id="po-desc">Desc</p>
</div>

<!-- PREMIUM MODAL -->
<div id="product-modal" class="glass-modal-overlay">
    <div class="glass-modal">
        <button class="modal-close-btn" id="modal-close-btn" onclick="closeModal()"><i class="fa-solid fa-xmark"></i></button>
        <div class="modal-split">
            <div class="modal-image-panel">
                <div class="modal-image-placeholder">
                    <i class="fa-regular fa-image" id="modal-icon-big"></i>
                    <span id="modal-image-text">Imagen</span>
                </div>
            </div>
            <div class="modal-data-panel">
                <div class="modal-tag" id="modal-tag">Categoría</div>
                <h2 class="modal-title" id="modal-title">Título</h2>
                <p class="modal-desc" id="modal-desc">Descripción</p>
                
                <div class="modal-benefits">
                    <h3 class="benefits-title"><i class="fa-solid fa-check-circle"></i> Características Principales</h3>
                    <ul class="modal-covers-list" id="modal-covers">
                    </ul>
                </div>

                <div class="modal-actions">
                    <a href="#" class="modal-btn-primary" id="dynamic-quote-btn">
                        Cotizar este seguro <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    // Popover Logic
    const popover = document.getElementById('card-popover');
    let popoverTimeout;
    
    function showPopover(cardElement) {
        clearTimeout(popoverTimeout);
        const rect = cardElement.getBoundingClientRect();
        
        // Fill data
        document.getElementById('po-title').textContent = cardElement.getAttribute('data-title');
        document.getElementById('po-tag').textContent = cardElement.getAttribute('data-tag');
        document.getElementById('po-desc').textContent = cardElement.getAttribute('data-desc');
        
        // Position
        // Center popover horizontally relative to card, place it above
        const popoverWidth = 320;
        let left = rect.left + window.scrollX + (rect.width / 2) - (popoverWidth / 2);
        let top = rect.top + window.scrollY - 200; // rough height estimate
        
        // Adjust for edges
        if (left < 10) left = 10;
        if (left + popoverWidth > window.innerWidth - 10) left = window.innerWidth - popoverWidth - 10;
        
        // If it goes off top of screen, place it below
        if (rect.top < 220) {
            top = rect.bottom + window.scrollY + 20;
        }
        
        popover.style.left = left + 'px';
        popover.style.top = top + 'px';
        
        popover.classList.add('visible');
    }
    
    function hidePopover() {
        popoverTimeout = setTimeout(() => {
            popover.classList.remove('visible');
        }, 100); // small delay to prevent flickering
    }

    // Modal Logic
    const modalOverlay = document.getElementById('product-modal');
    
    function openModal(element) {
        hidePopover();
        
        const title = element.getAttribute('data-title');
        const desc = element.getAttribute('data-desc');
        const tag = element.getAttribute('data-tag');
        const coversAttr = element.getAttribute('data-covers');
        const link = element.getAttribute('data-link');
        const icon = element.getAttribute('data-icon');
        
        let covers = [];
        try {
            covers = coversAttr.replace(/^\[|\]$/g, '').split("', '").map(s => s.replace(/^'|'$/g, ''));
        } catch(e) {
            console.error(e);
        }

        document.getElementById('modal-title').textContent = title;
        document.getElementById('modal-desc').textContent = desc;
        document.getElementById('modal-tag').textContent = tag;
        
        document.getElementById('modal-icon-big').className = `fa-solid ${icon}`;
        document.getElementById('modal-image-text').textContent = title;

        const coversList = document.getElementById('modal-covers');
        coversList.innerHTML = '';
        covers.forEach(c => {
            if(c.trim() !== '') {
                const li = document.createElement('li');
                li.textContent = c;
                coversList.appendChild(li);
            }
        });
        
        const quoteBtn = document.getElementById('dynamic-quote-btn');
        if (link !== '#') {
            quoteBtn.href = link;
            quoteBtn.removeAttribute('onclick');
        } else {
            quoteBtn.href = 'javascript:void(0)';
            quoteBtn.setAttribute('onclick', 'closeModal(); document.getElementById("comingSoonModal").classList.add("active");');
        }

        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    document.getElementById('product-modal').addEventListener('click', function(e) {
        if(e.target === this) closeModal();
    });
</script>
"""

# Insert CSS into <head>
head_close = soup.find('head')
if head_close:
    head_close.append(BeautifulSoup(injection_css, 'html.parser'))

# Insert HTML before </body>
body_close = soup.find('body')
if body_close:
    body_close.append(BeautifulSoup(injection_html, 'html.parser'))

with open("cotizacion/cotizacion.html", "w") as f:
    f.write(str(soup))

