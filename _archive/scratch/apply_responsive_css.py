import os

quote_css_path = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/css/style-quote.css'
style_css_path = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/css/style.css'

quote_append = """

/* =========================================
   ESTRUCTURA RESPONSIVE PREMIUM UNIFICADA
   ========================================= */

@media (max-width: 1024px) {
    /* Mover el Sidebar de resumen debajo del formulario en pantallas pequeñas */
    .specs-layout-grid {
        display: flex !important;
        flex-direction: column !important;
        gap: 30px;
    }
    .config-sidebar {
        order: 2;
    }
    .specs-main-content {
        order: 1;
    }
}

@media (max-width: 768px) {
    /* Grillas a una columna en móviles */
    .detail-grid,
    .cs-grid,
    .form-grid-2 {
        grid-template-columns: 1fr !important;
        gap: 20px;
    }
    
    /* Ajustes generales de espaciado para móviles */
    .page-wrapper {
        padding: 20px 15px !important;
    }
    
    .wizard-container {
        padding: 20px 15px !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
    }
    
    .harmonic-card {
        padding: 20px 15px !important;
    }

    .plan-grid {
        grid-template-columns: 1fr !important;
    }
}
"""

style_append = """

/* =========================================
   TIPOGRAFÍA FLUIDA Y AJUSTES TÁCTILES
   ========================================= */

/* Tipografía que escala automáticamente desde el tamaño de móvil hasta escritorio */
h1.text-gradient-corp, .hero-section h1 {
    font-size: clamp(2rem, 5vw, 3.5rem) !important;
    line-height: 1.2;
}

.headline-tech {
    font-size: clamp(1.8rem, 4vw, 3rem) !important;
    line-height: 1.2;
}

h2 {
    font-size: clamp(1.5rem, 3.5vw, 2.5rem) !important;
    line-height: 1.3;
}

h3 {
    font-size: clamp(1.2rem, 3vw, 1.8rem) !important;
    line-height: 1.3;
}

/* Área mínima táctil para botones e inputs (Estándares UX) */
.premium-btn,
.btn-aurora-gradient,
.btn-tech,
.lead-submit,
.harmonic-input,
.pet-input,
select.harmonic-input,
input.harmonic-input {
    min-height: 48px;
}

/* Espaciado de seguridad móvil global */
@media (max-width: 768px) {
    .container {
        padding-left: 15px !important;
        padding-right: 15px !important;
    }
    
    .hero-layout,
    .pricing-lab-wrapper,
    .app-showcase-wrapper,
    .social-hub-grid,
    .footer-grid,
    .faq-grid-layout,
    .glass-reviews-grid {
        padding-left: 15px !important;
        padding-right: 15px !important;
    }
}
"""

with open(quote_css_path, 'a', encoding='utf-8') as f:
    f.write(quote_append)

with open(style_css_path, 'a', encoding='utf-8') as f:
    f.write(style_append)

print("CSS Premium Responsive aplicado con exito.")
