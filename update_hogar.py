import re

def main():
    with open('/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    with open('/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/hogar/index.html', 'r', encoding='utf-8') as f:
        hogar_content = f.read()

    # Extract header from index.html (from <div class="top-header-aurora"> to </header>)
    header_match = re.search(r'(<div class="top-header-aurora">.*?</header>)', index_content, re.DOTALL)
    if not header_match:
        print("Header not found in index.html")
        return
    header_html = header_match.group(1)
    
    # Extract footer and floating from index.html (from <footer class="footer-aurora"> to </html>)
    footer_match = re.search(r'(<footer class="footer-aurora">.*)</body>', index_content, re.DOTALL)
    if not footer_match:
        print("Footer not found in index.html")
        return
    footer_html = footer_match.group(1)

    # Adjust paths for subdirectory
    header_html = header_html.replace('href="./', 'href="../').replace('src="./', 'src="../')
    footer_html = footer_html.replace('href="./', 'href="../').replace('src="./', 'src="../')

    # Now replace the header in hogar
    hogar_content = re.sub(r'<div class="top-header-aurora">.*?</header>', header_html, hogar_content, flags=re.DOTALL)
    
    # Replace footer in hogar
    hogar_content = re.sub(r'<footer class="footer-aurora">.*</body>', footer_html + '\n</body>', hogar_content, flags=re.DOTALL)
    
    # Update title and meta
    hogar_content = hogar_content.replace('<title>Alex AI Insurtech - Seguro de hogar</title>', '<title>MHM Corredora de Seguros - Seguro de hogar</title>')
    hogar_content = hogar_content.replace(
        '<meta name="description" content="AI-powered insurance, handled by humans. Get smart protection in 90 seconds.">',
        '<meta name="description" content="Seguros potenciados por IA, gestionados por humanos. Obtén protección inteligente en 90 segundos.">'
    )

    # Now for the main content
    main_replacement = """    <main>
        <section class="hero-sign-section">
            <div class="aurora-light-mesh"></div>
            <div class="tech-grid-light"></div>

            <div class="container position-relative z-2">
                <div class="hero-grid-split">
                    
                    <div class="hero-content-tech">
                        <div class="inline-badge-premium mb-3">
                            <span class="pulse-dot-purple"></span> Protección Completa del Hogar
                        </div>
                        <h1 class="display-title-hero">
                            Seguro de hogar, que te
                            <span class="text-gradient-corp">tiene cubierto.</span>
                        </h1>
                        <p class="lead-text-hero">
                            Ya sea que estés comprando o protegiendo tu hogar, MHM hace que asegurar sea fácil.
                        </p>
                        
                        <div class="hero-actions-row">
                            <a href="../cotizacion/cotizacion.html" class="btn-aurora-primary">
                                <span>Obtén tu cotización de hogar</span> <i class="fa-solid fa-arrow-right-long"></i>
                            </a>
                        </div>
                    </div>

                    <div class="hero-visual-tech">
                        <div class="glass-frame-monitor">
                            <div class="monitor-header">
                                <div class="dots-row"><span></span><span></span><span></span></div>
                                <div class="address-bar">mhmseguros.cl/hogar</div>
                            </div>
                            <div class="arch-visual-col">
                                <div class="arch-visual-wrapper">     
                                    <div class="arch-glow-back"></div>
                                    <div class="arch-glass-frame">
                                        <img src="../assets/img/alex-hero-8.webp" alt="MHM Hero" class="arch-img"> 
                                        <div class="arch-shimmer"></div>
                                        <div class="arch-reflection"></div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="floating-status-card" style="z-index: 999;">
                                <div class="icon-box-success"><i class="fa-solid fa-shield-halved"></i></div>
                                <div>
                                    <strong>Seguro anterior detectado</strong>
                                    <span>Verificado mediante sistema inteligente</span>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <section id="carriers" class="trust-dock-section">

            <div class="social-header text-center">
                <div class="inline-badge-premium mb-3">
                    <span class="pulse-dot-purple"></span> Aseguradoras de nivel top
                </div>
            </div>
            
            <div class="container">
                
                <div class="aurora-dock">
                    
                    <div class="dock-gradient-top"></div>

                    <div class="dock-label">
                        <div class="status-indicator">
                            <span class="pulse-ring"></span>
                            <span class="dot"></span>
                        </div>
                        <div class="label-text">
                            <span class="sub">Red verificada</span>
                            <span class="main text-gradient-corp">Aseguradoras aliadas</span>
                        </div>
                    </div>

                    <div class="dock-divider desktop-only"></div>

                    <div class="dock-slider-area">
                        <div class="infinite-track">
                            <div class="tech-logo"><img src="../assets/img/logo-aspor.webp" alt="Aspor"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-bci-seguros.webp" alt="BCI Seguros"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-chubb.webp" alt="Chubb"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-continental.webp" alt="Continental"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-consorcio.webp" alt="Consorcio"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-fid.webp" alt="FID"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-hdi-seguros.webp" alt="HDI Seguros"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-liberty-seguros.webp" alt="Liberty Seguros"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-renta.webp" alt="Renta Nacional"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-sura.webp" alt="Sura"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-unnio.webp" alt="Unnio"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-zurich.webp" alt="Zurich"></div>

                            <div class="tech-logo"><img src="../assets/img/logo-aspor.webp" alt="Aspor"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-bci-seguros.webp" alt="BCI Seguros"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-chubb.webp" alt="Chubb"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-continental.webp" alt="Continental"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-consorcio.webp" alt="Consorcio"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-fid.webp" alt="FID"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-hdi-seguros.webp" alt="HDI Seguros"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-liberty-seguros.webp" alt="Liberty Seguros"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-renta.webp" alt="Renta Nacional"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-sura.webp" alt="Sura"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-unnio.webp" alt="Unnio"></div>
                            <div class="tech-logo"><img src="../assets/img/logo-zurich.webp" alt="Zurich"></div>
                        </div>
                        
                        <div class="dock-fade-left"></div>
                        <div class="dock-fade-right"></div>
                    </div>

                </div>
                
            </div>
        </section>

        <section class="features-aurora-section">
            <div class="container">
                <div class="section-head-tech text-center mb-5">
                        <div class="inline-badge-premium mb-3">
                            <span class="pulse-dot-purple"></span> Tus Coberturas
                        </div>
                    <h2 class="display-title-sm">Soluciones de <span class="text-gradient-corp">cobertura integral</span></h2>
                </div>

                <div class="features-grid-tech">
                    
                    <div class="feature-glass-card">
                        <div class="feature-icon-box icon-blue">
                            <i class="fa-solid fa-house-chimney-crack"></i>
                        </div>
                        <h3>Daños a la casa</h3>
                        <p>Protección contra daños por incendios, tormentas y otros eventos cubiertos.</p>
                    </div>

                    <div class="feature-glass-card">
                        <div class="feature-icon-box icon-purple">
                            <i class="fa-solid fa-house-laptop"></i>
                        </div>
                        <h3>Bienes personales en el interior</h3>
                        <p>Cobertura para tus pertenencias dentro de la casa, como muebles y electrónicos.</p>
                    </div>

                    <div class="feature-glass-card">
                        <div class="feature-icon-box icon-cyan">
                            <i class="fa-solid fa-user-shield"></i>
                        </div>
                        <h3>Protección de responsabilidad civil</h3>
                        <p>Te protege contra demandas por lesiones corporales o daños a la propiedad que tú o los miembros de tu familia causen.</p>
                    </div>

                    <div class="feature-glass-card">
                        <div class="feature-icon-box icon-indigo">
                            <i class="fa-solid fa-hand-holding-dollar"></i>
                        </div>
                        <h3>Gastos de manutención temporales</h3>
                        <p>Ayuda a cubrir el costo de una vivienda temporal si tu casa se vuelve inhabitable debido a un evento cubierto.</p>
                    </div>

                    <div class="feature-glass-card">
                        <div class="feature-icon-box icon-dark">
                            <i class="fa-solid fa-calculator"></i>
                        </div>
                        <h3>Complementos opcionales</h3>
                        <p>Personaliza tu cobertura con opciones para electrónicos, joyas y más.</p>
                    </div>

                </div>
            </div>
        </section>
        <br><br>

        <section class="aurora-arch-section">
            <div class="container position-relative z-2">
                
                <div class="aurora-arch-grid">
                    
                    <div class="arch-content-col">
                        
                        <div class="social-header text-center">
                            <div class="inline-badge-premium mb-3">
                                <span class="pulse-dot-purple"></span> La Ventaja MHM
                            </div>
                        </div>

                        <h2 class="arch-title text-center">
                            Seguro diseñado para <br>
                            <span class="arch-gradient-text">rapidez y precisión.</span>
                        </h2>
                        
                        <p class="arch-lead text-center">
                            Reemplazamos el papeleo obsoleto con inteligencia. Experimenta el equilibrio perfecto entre la precisión y la experiencia humana dedicada.
                        </p>

                        <div class="arch-features-stack">
                            
                            <div class="arch-feature-row">
                                <div class="arch-icon-box theme-blue">
                                    <i class="fa-solid fa-wand-magic-sparkles"></i>
                                </div>
                                <div class="arch-text">
                                    <h6>Impulsado por Tecnología</h6>
                                    <p>Analizamos tus necesidades para recomendar la mejor cobertura.</p>
                                </div>
                            </div>

                            <div class="arch-feature-row">
                                <div class="arch-icon-box theme-green">
                                    <i class="fa-solid fa-file-circle-check"></i>
                                </div>
                                <div class="arch-text">
                                    <h6>Aprobado por Prestamistas</h6>
                                    <p>Cumple con todos los requisitos hipotecarios.</p>
                                </div>
                            </div>

                            <div class="arch-feature-row">
                                <div class="arch-icon-box theme-blue">
                                    <i class="fa-solid fa-bolt"></i>
                                </div>
                                <div class="arch-text">
                                    <h6>Rápido y Moderno</h6>
                                    <p>Obtén una cotización con información mínima en minutos.</p>
                                </div>
                            </div>

                            <div class="arch-feature-row">
                                <div class="arch-icon-box theme-purple">
                                    <i class="fa-solid fa-user-shield"></i>
                                </div>
                                <div class="arch-text">
                                    <h6>Soporte de Conserjería</h6>
                                    <p>Reclamos complejos manejados por humanos autorizados, no chatbots.</p>
                                </div>
                            </div>

                        </div>

                        <div class="arch-action-area">
                            <a href="../cotizacion/cotizacion.html" class="btn-aurora-primary">
                                Obtén tu tarifa <i class="fa-solid fa-arrow-right"></i>
                            </a>
                            <span class="arch-secure-label"><i class="fa-solid fa-shield-halved"></i> Seguro y Verificado</span>
                        </div>

                    </div>

                    <div class="arch-visual-col">
                        <div class="arch-visual-wrapper">
                            
                            <div class="arch-glow-back"></div>

                            <div class="arch-glass-frame">
                                <img src="../assets/img/alex-support.webp" alt="MHM Support" class="arch-img">
                                
                                <div class="arch-shimmer"></div>
                                
                                <div class="arch-reflection"></div>
                            </div>

                            <div class="arch-floating-tags">
                                <div class="glass-tag tag-top">
                                    <span class="status-pulse"></span>
                                    <div>
                                        <strong>Póliza Activa</strong>
                                        <span>Protección Verificada</span>
                                    </div>
                                </div>
                                <div class="glass-tag tag-bottom">
                                    <div class="icon-flash"><i class="fa-solid fa-bolt"></i></div>
                                    <div>
                                        <strong>Cotización Instantánea</strong>
                                        <span>Menos de 2 minutos</span>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>

                </div>

            </div>
        </section>

        <section class="reviews-aurora-section bg-white-soft">
            <div class="social-header text-center">
                <div class="inline-badge-premium mb-3">
                    <span class="pulse-dot-purple"></span> Nuestras Reseñas
                </div>
            </div>
            <div class="container">
                <div class="glass-reviews-grid">
                    
                    <div class="review-glass-card card-featured-glass">
                        <div class="card-glass-content">
                            <div class="review-meta">
                                <div class="user-info">
                                    <img src="../assets/img/Profile-arantxa.webp" onerror="this.src='https://placehold.co/50x50'" alt="Arantxa" class="avatar-sm">
                                    <div>
                                        <h4>Arantxa M.</h4>
                                        <span class="verified-tag"><i class="fa-solid fa-certificate"></i> Usuario Verificado</span>
                                    </div>
                                </div>
                                <div class="cotizacion-mark-aurora"><i class="fa-solid fa-quote-right"></i></div>
                            </div>

                            <div class="aurora-stars">
                                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                            </div>

                            <h3 class="cotizacion-headline">"¡Contraté una póliza en menos de 3 minutos! ⚡️"</h3>
                            <p class="cotizacion-body">
                                "Sinceramente, no pensé que obtener un seguro de hogar pudiera ser tan rápido. Respondí algunas preguntas sobre mi propiedad y el sistema generó una cotización personalizada al instante. Sin llamadas telefónicas, sin esperar en la línea. La interfaz es súper limpia y moderna. Así es como deberían ser los seguros hoy en día."
                            </p>
                        </div>
                    </div>

                    <div class="reviews-column-right">
                        
                        <div class="review-glass-card">
                            <div class="card-glass-content">
                                <div class="review-meta-compact">
                                    <img src="../assets/img/Profile-joel.png" onerror="this.src='https://placehold.co/50x50'" alt="Joel" class="avatar-sm">
                                    <div class="meta-text">
                                        <h4>Joel C.</h4>
                                        <span>Gerente de Proyectos</span>
                                    </div>
                                </div>
                                <p class="cotizacion-body-sm">"Dudaba en probar una compañía moderna porque no quería hablar con un robot cuando las cosas salen mal. MHM es diferente. El proceso manejó mi cotización en segundos, pero luego mi agente, Sarah, se comunicó personalmente para explicarme los detalles. No solo leía un guion; realmente le importaba que tuviera la cobertura adecuada. Es el equilibrio perfecto."</p>
                            </div>
                        </div>

                        <div class="review-glass-card">
                            <div class="card-glass-content">
                                <div class="review-meta-compact">
                                    <img src="../assets/img/Profile-antony.png" onerror="this.src='https://placehold.co/50x50'" alt="Antony" class="avatar-sm">
                                    <div class="meta-text">
                                        <h4>Antony G.</h4>
                                        <span>Arquitecto</span>
                                    </div>
                                </div>
                                <p class="cotizacion-body-sm">"Tuvimos una tubería rota a las 2 AM. El sistema de MHM fue increíble: presenté el reclamo al instante en mi teléfono sin esperar en línea. Pero lo que realmente importó fue que mi agente dedicado me llamó a primera hora de la mañana solo para preguntar: '¿Están bien?'. No se puede programar ese tipo de empatía. El reclamo se pagó rápido, pero la amabilidad es la razón por la que me quedo."</p>
                            </div>
                        </div>

                        <div class="review-glass-card">
                            <div class="card-glass-content">
                                <div class="review-meta-compact">
                                    <img src="../assets/img/Profile-jenny.png" onerror="this.src='https://placehold.co/50x50'" alt="Jenny" class="avatar-sm">
                                    <div class="meta-text">
                                        <h4>Jenny R.</h4>
                                        <span>Diseñadora</span>
                                    </div>
                                </div>
                                <p class="cotizacion-body-sm">"Me encanta que puedo enviarle un mensaje de texto a mi agente y obtener una respuesta al instante, pero también me encanta que su sistema monitoree mi póliza. El sistema detectó que el valor de mi casa había aumentado y mi agente organizó proactivamente una videollamada rápida para ajustar mis límites y no quedar con seguro insuficiente. Siento que siempre me están cuidando."</p>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </section>

        <section id="app" class="app-marketing-section">
            <div class="container">
                <div class="app-showcase-wrapper">
                    
                    <div class="app-text-content">
                        <div class="social-header text-center">
                            <div class="inline-badge-premium mb-3">
                                <span class="pulse-dot-purple"></span> App Móvil
                            </div>
                            <h2 class="display-title-app">Seguros que se adaptan a <span class="text-gradient-corp">tu vida real.</span></h2>
                            <p class="lead-text-app" style="text-align: center;">Olvídate del papeleo. Gestiona tu póliza, presenta reclamos en segundos y cobra más rápido, todo desde tu bolsillo.</p>
                        </div>
                        
                        <div class="benefit-visual-list">
                            
                            <div class="benefit-item">
                                <div class="benefit-icon-box box-blue">
                                    <i class="fa-solid fa-bolt-lightning"></i>
                                </div>
                                <div class="benefit-details">
                                    <strong>Solicita Cambios en tu Póliza</strong>
                                    <p>Agrega un vehículo, conductor o cobertura fácilmente.</p>
                                </div>
                            </div>

                            <div class="benefit-item">
                                <div class="benefit-icon-box box-purple">
                                    <i class="fa-solid fa-user-shield"></i>
                                </div>
                                <div class="benefit-details">
                                    <strong>Asesoría Experta</strong>
                                    <p>Chatea con humanos autorizados 24/7.</p>
                                </div>
                            </div>

                            <div class="benefit-item">
                                <div class="benefit-icon-box box-cyan">
                                    <i class="fa-solid fa-sliders"></i>
                                </div>
                                <div class="benefit-details">
                                    <strong>Control Total</strong>
                                    <p>Ajusta la cobertura al instante.</p>
                                </div>
                            </div>

                        </div>

                        <div class="store-btn-group">
                            <a href="https://apps.apple.com/us/app/alex-ai-insurtech-app/id6752793999" target="_blank">
                                <button class="btn-store-unified">
                                    <i class="fa-brands fa-apple"></i>
                                    <div class="btn-text-col">
                                        <span>Consíguelo en el</span>
                                        <strong>App Store</strong>
                                    </div>
                                </button>
                            </a>
                            <a href="https://play.google.com/store/apps/details?id=cloud.alexai.movil&pcampaignid=web_share&pli=1" target="_blank">
                                <button class="btn-store-unified">
                                    <i class="fa-brands fa-google-play"></i>
                                    <div class="btn-text-col">
                                        <span>Disponible en</span>
                                        <strong>Google Play</strong>
                                    </div>
                                </button>
                            </a>
                        </div>
                    </div>

                    <div class="app-visual-marketing">
                        
                    <div class="phone-core-video">
                        <div class="phone-aura-clean"></div>
                        
                        <div class="phone-chassis-premium organic-box position-relative" id="smartVideoContainer">
                            
                            <video class="js-hover-video app-screen-video" loop playsinline id="marketingVideo">
                                <source src="../assets/videos/video-mhm-1.mp4" type="video/mp4">
                            </video>

                            <div class="video-overlay">
                                
                                <div class="corporate-cta-button shimmer-btn">
                                    <div class="cta-icon">
                                        <svg viewBox="0 0 24 24" fill="currentColor">
                                            <path d="M8 5v14l11-7z"/>
                                        </svg>
                                    </div>
                                    <div class="cta-text-group">
                                        <span class="cta-main-text">Míralo en acción</span>
                                        <span class="cta-sub-text desktop-only">Oprime para ver</span>
                                        <span class="cta-sub-text mobile-only">Oprime para ver</span>
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>

                        <div class="marketing-card card-payout">
                            <div class="icon-circle-marketing icon-green"><i class="fa-solid fa-file-signature"></i></div>
                            <div class="marketing-info">
                                <strong class="benefit-title">Mi póliza en minutos</strong>
                                <span class="benefit-desc">Documentos enviados directamente.</span>
                            </div>
                        </div>

                        <div class="marketing-card card-help">
                            <div class="agent-stack-marketing">
                                <img src="../assets/img/Profile-stephanie.webp" alt="Agent" class="avatar-marketing">
                                <span class="online-dot-marketing"></span>
                            </div>
                            <div class="marketing-info">
                                <strong class="benefit-title">Estamos aquí 24/7</strong>
                                <span class="benefit-desc">Ayuda real, al instante.</span>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </section>

        <section id="faq" class="faq-aurora-section">
            <div class="container">
                <div class="faq-grid-layout">
                    
                    <div class="faq-sidebar">
                        <div class="lab-header text-center">
                            <div class="header-status-light">
                                <span class="pulse-blue"></span>Base de Conocimiento
                            </div>
                            <h2 class="display-title-lab">Preguntas <span class="text-gradient-anim">Frecuentes.</span></h2>
                            <p class="lead-text-faq" style="text-align: center;">Todo lo que necesitas saber sobre el ecosistema de seguros, protocolos de cobertura y seguridad.</p>
                        </div>

                        <div class="support-glass-card">
                            <div class="icon-support-glow"><i class="fa-solid fa-headset"></i></div>
                            <div class="support-text">
                                <strong>¿Aún tienes preguntas?</strong>
                                <p>Nuestro equipo de expertos está en línea.</p>
                            </div>
                            <a href="../contactoo/index.html">
                                <button class="btn-chat-support">Chatea con nosotros</button>
                            </a>
                        </div>
                    </div>

                    <div class="faq-content-column">
                        
                        <div class="faq-item active"> <div class="faq-question">
                                <h3>¿Qué cubre normalmente el seguro de hogar?</h3>
                                <div class="faq-toggle"><i class="fa-solid fa-plus"></i></div>
                            </div>
                            <div class="faq-answer">
                                <p>La cobertura generalmente incluye:
                                <br>• La estructura de tu casa (paredes, techo, piso, etc.).
                                <br>• Pertenencias personales dentro del hogar.
                                <br>• Responsabilidad civil (lesiones o daños a la propiedad de terceros).
                                <br>• Gastos de manutención adicionales si tu hogar se vuelve inhabitable.
                                <br>• Protecciones opcionales (inundación, terremoto, etc.).
                                <br>Todas las pólizas pueden agruparse para máxima eficiencia y ahorro.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question">
                                <h3>¿Es obligatorio el seguro de hogar?</h3>
                                <div class="faq-toggle"><i class="fa-solid fa-plus"></i></div>
                            </div>
                            <div class="faq-answer">
                                <p>Si tienes una hipoteca, sí, tu prestamista lo requerirá. Incluso si eres dueño de tu casa en su totalidad, es muy recomendable proteger tu patrimonio de desastres inesperados.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question">
                                <h3>¿Por qué obtener un seguro a través de MHM Corredores?</h3>
                                <div class="faq-toggle"><i class="fa-solid fa-plus"></i></div>
                            </div>
                            <div class="faq-answer">
                                <p>Nosotros buscamos por ti. Obtenemos cotizaciones de las mejores aseguradoras y te ayudamos a comparar coberturas, precios y características para que obtengas la mejor oferta con menos esfuerzo.</p>
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question">
                                <h3>¿Puedo agrupar hogar y auto?</h3>
                                <div class="faq-toggle"><i class="fa-solid fa-plus"></i></div>
                            </div>
                            <div class="faq-answer">
                                <p>Definitivamente. Muchas de nuestras aseguradoras asociadas ofrecen descuentos por paquetes, y MHM Corredores busca automáticamente esos descuentos para ayudarte a ahorrar aún más.</p>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </section>
    </main>"""

    hogar_content = re.sub(r'<main>.*?</main>', main_replacement, hogar_content, flags=re.DOTALL)

    with open('/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/hogar/index.html', 'w', encoding='utf-8') as f:
        f.write(hogar_content)
    
    print("Done writing to hogar/index.html")

if __name__ == '__main__':
    main()
