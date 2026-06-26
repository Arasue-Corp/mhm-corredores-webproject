import re

with open("cotizacion/cotizacion.html", "r") as f:
    content = f.read()

# Add the script right before </body>
script_block = """<script>
        const productsData = [
            // GENERALES
            {
                id: 'auto', category: 'generales', title: 'Seguro de Auto', icon: 'fa-car', tag: 'Protección Vehicular',
                desc: 'Protección completa para tu vehículo personal o comercial. El Seguro Automotriz es un medio eficaz para la protección frente a las consecuencias de los riesgos, daños de un automóvil y frente a terceros.',
                covers: ['Daños materiales del vehículo (parcial/total)', 'Robo y/o hurto del vehículo', 'Responsabilidad frente a terceros', 'Asistencia en ruta 24/7'],
                link: 'cotizacion-1.html'
            },
            {
                id: 'moto', category: 'generales', title: 'Seguro de Moto', icon: 'fa-motorcycle', tag: 'Protección 2 Ruedas',
                desc: 'Asegura tu motocicleta y rueda con total tranquilidad ante accidentes, robos o daños a terceros.',
                covers: ['Daños materiales', 'Robo, hurto o uso no autorizado', 'Responsabilidad Civil', 'Asistencia de grúa'],
                link: '#'
            },
            {
                id: 'soap', category: 'generales', title: 'SOAP', icon: 'fa-file-invoice-dollar', tag: 'Seguro Obligatorio',
                desc: 'Seguro Obligatorio de Accidentes Personales digital y rápido. Exigido por ley para transitar.',
                covers: ['Cobertura por muerte accidental', 'Incapacidad permanente total y parcial', 'Gastos médicos y hospitalarios', 'Cobertura para el conductor y terceros'],
                link: '#'
            },
            {
                id: 'bici', category: 'generales', title: 'Seguro de Bicicleta', icon: 'fa-bicycle', tag: 'Micro-movilidad',
                desc: 'Protege tu bici y accesorios contra robo y daños, permitiéndote moverte por la ciudad sin preocupaciones.',
                covers: ['Robo con fuerza', 'Daños accidentales', 'Responsabilidad civil', 'Asistencia al ciclista'],
                link: '#'
            },
            {
                id: 'hogar', category: 'generales', title: 'Seguro de Hogar', icon: 'fa-house-chimney', tag: 'Protección Residencial',
                desc: 'Protege tu propiedad y bienes familiares ante incendios, sismos, robos y otros imprevistos.',
                covers: ['Incendio y riesgos adicionales', 'Sismo (Opcional)', 'Robo de bienes (Contenido)', 'Asistencia domiciliaria 24/7'],
                link: '#'
            },
            // SALUD
            {
                id: 'salud', category: 'salud', title: 'Seguro de Salud', icon: 'fa-briefcase-medical', tag: 'Bienestar',
                desc: 'Planes de salud complementaria y catastrófica para reducir tus gastos médicos ambulatorios y hospitalarios.',
                covers: ['Reducción de gastos médicos', 'Cobertura hospitalaria y catastrófica', 'Medicamentos en farmacias', 'Protección para cargas familiares'],
                link: '#'
            },
            {
                id: 'deporte', category: 'salud', title: 'Seguro de Deporte', icon: 'fa-person-running', tag: 'Actividad Física',
                desc: 'Cobertura especializada para deportistas amateur y pro ante lesiones deportivas y accidentes.',
                covers: ['Lesiones en entrenamientos o competición', 'Gastos médicos, kinesiología', 'Incapacidad temporal', 'Cobertura internacional'],
                link: '#'
            },
            {
                id: 'dental', category: 'salud', title: 'Seguro Dental', icon: 'fa-tooth', tag: 'Salud Bucal',
                desc: 'Amplia red odontológica y reembolsos preferenciales en tratamientos dentales para toda la familia.',
                covers: ['Consultas y diagnóstico', 'Tratamientos de prevención', 'Ortodoncia e implantes', 'Urgencias dentales 24/7'],
                link: '#'
            },
            {
                id: 'vida', category: 'salud', title: 'Vida Temporal', icon: 'fa-heart', tag: 'Tranquilidad Familiar',
                desc: 'Respaldo económico y tranquilidad para tu familia en caso de fallecimiento o invalidez.',
                covers: ['Fallecimiento natural o accidental', 'Invalidez total y permanente', 'Anticipo por enfermedades graves', 'Asistencia funeraria'],
                link: '#'
            },
            // ASISTENCIAS
            {
                id: 'viajes', category: 'asistencias', title: 'Asistencia de Viajes', icon: 'fa-plane', tag: 'Viajes Seguros',
                desc: 'Cobertura médica y soporte en el extranjero 24/7 para que viajes con total tranquilidad.',
                covers: ['Asistencia médica por enfermedad o accidente', 'Pérdida o retraso de equipaje', 'Cancelación de vuelo', 'Repatriación sanitaria'],
                link: '#'
            },
            {
                id: 'carretera', category: 'asistencias', title: 'Asistencia en Carretera', icon: 'fa-truck-pickup', tag: 'Apoyo Vial',
                desc: 'Servicio de grúa, cambio de neumático, carga de batería y más, estés donde estés.',
                covers: ['Remolque o grúa', 'Cambio de neumáticos', 'Paso de corriente', 'Envío de combustible'],
                link: '#'
            },
            {
                id: 'telemed', category: 'asistencias', title: 'Telemedicina', icon: 'fa-stethoscope', tag: 'Salud Digital',
                desc: 'Consultas médicas online inmediatas sin salir de casa, disponibles las 24 horas.',
                covers: ['Medicina general 24/7', 'Recetas médicas digitales', 'Órdenes de exámenes', 'Orientación pediátrica'],
                link: '#'
            }
        ];

        let currentActiveItem = null;
        let currentCategoryItems = [];

        function filterCategory(category, btnElement) {
            // Update tabs UI
            document.querySelectorAll('.hub-tab-btn').forEach(btn => btn.classList.remove('active'));
            if(btnElement) btnElement.classList.add('active');

            // Get items for this category
            currentCategoryItems = productsData.filter(p => p.category === category);
            
            // Build sidebar
            const sidebar = document.getElementById('dynamic-sidebar');
            sidebar.innerHTML = '';
            
            currentCategoryItems.forEach((p, index) => {
                const itemDiv = document.createElement('div');
                itemDiv.className = `canvas-menu-item ${index === 0 ? 'active' : ''}`;
                itemDiv.id = `menu-item-${p.id}`;
                itemDiv.innerHTML = `
                    <div class="menu-icon"><i class="fa-solid ${p.icon}"></i></div>
                    <div class="menu-text">${p.title}</div>
                `;
                itemDiv.addEventListener('mouseenter', () => updateCanvas(p));
                sidebar.appendChild(itemDiv);
            });

            // Update canvas with the first item
            if (currentCategoryItems.length > 0) {
                updateCanvas(currentCategoryItems[0]);
            }
        }

        function updateCanvas(product) {
            if (currentActiveItem === product) return;
            
            // Update active state in sidebar
            if (currentActiveItem) {
                const oldItem = document.getElementById(`menu-item-${currentActiveItem.id}`);
                if(oldItem) oldItem.classList.remove('active');
            }
            const newItem = document.getElementById(`menu-item-${product.id}`);
            if(newItem) newItem.classList.add('active');
            
            currentActiveItem = product;

            const content = document.getElementById('showcase-content');
            const graphic = document.getElementById('sc-bg-icon');

            // Fade out
            content.classList.add('fade-out');
            graphic.style.transform = 'rotate(-30deg) scale(0.8)';
            graphic.style.opacity = '0';
            
            setTimeout(() => {
                // Update content
                document.getElementById('sc-tag').textContent = product.tag;
                document.getElementById('sc-title').textContent = product.title;
                document.getElementById('sc-desc').textContent = product.desc;
                graphic.className = `fa-solid ${product.icon}`;
                
                // Fade in
                content.classList.remove('fade-out');
                graphic.style.transform = 'rotate(-15deg) scale(1)';
                graphic.style.opacity = '1';
            }, 150);
        }

        function openModalFromCanvas() {
            if (!currentActiveItem) return;
            const p = currentActiveItem;
            
            document.getElementById('modal-title').textContent = p.title;
            document.getElementById('modal-desc').textContent = p.desc;
            document.getElementById('modal-tag').textContent = p.tag;
            
            document.getElementById('modal-icon-big').className = `fa-solid ${p.icon}`;
            document.getElementById('modal-image-text').textContent = p.title;

            const coversList = document.getElementById('modal-covers');
            coversList.innerHTML = '';
            p.covers.forEach(c => {
                if(c.trim() !== '') {
                    const li = document.createElement('li');
                    li.textContent = c;
                    coversList.appendChild(li);
                }
            });
            
            const quoteBtn = document.getElementById('dynamic-quote-btn');
            
            if (p.link !== '#') {
                quoteBtn.href = p.link;
                quoteBtn.removeAttribute('onclick');
            } else {
                quoteBtn.href = 'javascript:void(0)';
                quoteBtn.setAttribute('onclick', 'closeModal(); openComingSoon();');
            }

            const modalOverlay = document.getElementById('product-modal');
            modalOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
        
        function closeModal() {
            document.getElementById('product-modal').classList.remove('active');
            document.body.style.overflow = '';
        }

        function openComingSoon() {
            document.getElementById('comingSoonModal').classList.add('active');
        }

        function closeComingSoon() {
            document.getElementById('comingSoonModal').classList.remove('active');
        }

        // Close modals on overlay click
        document.getElementById('product-modal').addEventListener('click', function(e) {
            if(e.target === this) closeModal();
        });
        document.getElementById('comingSoonModal').addEventListener('click', function(e) {
            if(e.target === this) closeComingSoon();
        });

        // Initialize first category on load
        document.addEventListener('DOMContentLoaded', () => {
            filterCategory('generales', document.querySelector('.hub-tab-btn.active'));
        });
    </script>
    <script src="../js/script.js?v=1781129809"></script>
    <script src="../js/script-quote.js?v=1781129809"></script>
</body>"""

# Replace the broken script tag and append the new script block
content = re.sub(r"<script src=\"\.\./js/components\.js.*?</script>", "", content)

# Inject just before </body>
content = content.replace("</body>", script_block)

with open("cotizacion/cotizacion.html", "w") as f:
    f.write(content)
