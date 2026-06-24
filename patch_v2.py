import re

# 1. Update CSS
css_path = "css/style-quote.css"
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

new_css = """
/* Premium Data Readout Styles */
.data-readout-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
}

.data-readout-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1.2rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.02);
}

.data-readout-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.data-readout-card:hover {
    transform: translateY(-2px);
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(255, 255, 255, 0.15);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12), inset 0 0 0 1px rgba(255, 255, 255, 0.05);
}

.data-readout-card:hover::before {
    opacity: 1;
}

.readout-icon {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: rgba(45, 212, 191, 0.1);
    color: #2dd4bf;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
}

.readout-icon.purple { background: rgba(168, 85, 247, 0.1); color: #a855f7; }
.readout-icon.blue { background: rgba(59, 130, 246, 0.1); color: #3b82f6; }
.readout-icon.amber { background: rgba(245, 158, 11, 0.1); color: #f59e0b; }

.readout-content {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    z-index: 1;
}

.readout-label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: rgba(255, 255, 255, 0.5);
    font-weight: 600;
}

.readout-value {
    font-size: 1.05rem;
    font-weight: 600;
    color: #ffffff;
    word-break: break-word;
}

.verified-badge-corner {
    position: absolute;
    top: 0.75rem;
    right: 0.75rem;
    color: rgba(45, 212, 191, 0.4);
    font-size: 0.85rem;
}

.data-section-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
    margin-top: 2rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.data-section-title i {
    color: #a855f7;
}

.data-section-title:first-child {
    margin-top: 0;
}
"""

if "/* Premium Data Readout Styles */" not in css_content:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n" + new_css)


# 2. Update HTML
html_path = "cotizacion/cotizacion-7-1.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

new_main_col = """
            <div class="main-spec-col">
                
                <div class="car-tabs-integrated" id="entityTabs" style="margin-bottom: 2rem;">
                    <button type="button" class="tab-int active" onclick="switchEntityTab('persona', this)" style="font-size: 1.1rem; padding: 1rem;">
                        <span class="tab-txt"><i class="fa-solid fa-user"></i> Contratante: Persona</span>
                    </button>
                    <button type="button" class="tab-int" onclick="switchEntityTab('empresa', this)" style="font-size: 1.1rem; padding: 1rem;">
                        <span class="tab-txt"><i class="fa-solid fa-building"></i> Contratante: Empresa</span>
                    </button>
                </div>

                <div class="premium-white-card" id="quoteFormStep7" style="background: rgba(15, 15, 26, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.05);">
                    
                    <!-- FORMULARIO PERSONA -->
                    <div id="panel-persona" class="car-panel active" data-id="persona">
                        
                        <div class="data-section-title">
                            <i class="fa-solid fa-id-card"></i> Identidad Verificada
                        </div>

                        <div class="data-readout-grid">
                            <div class="data-readout-card animate-on-scroll">
                                <div class="readout-icon blue"><i class="fa-solid fa-hashtag"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">RUT</span>
                                    <span class="readout-value">10.042.595-5</span>
                                </div>
                                <i class="fa-solid fa-circle-check verified-badge-corner"></i>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.1s;">
                                <div class="readout-icon blue"><i class="fa-solid fa-calendar-day"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Nacimiento</span>
                                    <span class="readout-value">22/05/1981</span>
                                </div>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.2s;">
                                <div class="readout-icon blue"><i class="fa-solid fa-user"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Nombres</span>
                                    <span class="readout-value">Cristian Gonzalo</span>
                                </div>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.3s;">
                                <div class="readout-icon blue"><i class="fa-solid fa-users"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Apellidos</span>
                                    <span class="readout-value">Martinez</span>
                                </div>
                            </div>
                        </div>

                        <div class="data-section-title mt-5">
                            <i class="fa-solid fa-map-location-dot" style="color: #2dd4bf;"></i> Residencia & Contacto
                        </div>

                        <div class="data-readout-grid">
                            <div class="data-readout-card animate-on-scroll">
                                <div class="readout-icon"><i class="fa-solid fa-map"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Región</span>
                                    <span class="readout-value">DE LOS RÍOS</span>
                                </div>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.1s;">
                                <div class="readout-icon"><i class="fa-solid fa-city"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Comuna</span>
                                    <span class="readout-value">VALDIVIA</span>
                                </div>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.2s;">
                                <div class="readout-icon"><i class="fa-solid fa-road"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Dirección</span>
                                    <span class="readout-value">Calle Los Robles 1234</span>
                                </div>
                            </div>
                        </div>

                        <div class="data-readout-grid mt-3">
                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.3s; background: rgba(168, 85, 247, 0.05); border-color: rgba(168, 85, 247, 0.2);">
                                <div class="readout-icon purple"><i class="fa-solid fa-mobile-screen"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Teléfono Móvil (Envío Póliza)</span>
                                    <span class="readout-value">+56 999 999 999</span>
                                </div>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.4s; background: rgba(168, 85, 247, 0.05); border-color: rgba(168, 85, 247, 0.2);">
                                <div class="readout-icon purple"><i class="fa-solid fa-at"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Correo (Envío Póliza)</span>
                                    <span class="readout-value">cristian.martinez@email.com</span>
                                </div>
                            </div>
                        </div>

                        <div class="divider-hairline mt-5 mb-4"></div>

                        <div class="row-switch-container compact" style="background: rgba(255,255,255,0.02); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05);">
                            <div class="switch-label-group">
                                <div class="sl-text">
                                    <span class="sl-title" style="font-size:1.2rem; color:#fff;">¿Confirma que los datos son correctos?</span>
                                    <span class="sl-sub" style="margin-top:0.25rem;">Esto es necesario para emitir su póliza digital legalmente.</span>
                                </div>
                            </div>
                            <div class="aurora-toggle-segment" style="transform: scale(1.1); margin-right: 1rem;">
                                <input type="radio" name="correct_p" id="correct_p_yes" value="yes" checked>
                                <label for="correct_p_yes">Sí</label>
                                <input type="radio" name="correct_p" id="correct_p_no" value="no">
                                <label for="correct_p_no">No</label>
                                <div class="segment-highlight"></div>
                            </div>
                        </div>

                    </div>

                    <!-- FORMULARIO EMPRESA -->
                    <div id="panel-empresa" class="car-panel" data-id="empresa" style="display:none;">
                        
                        <div class="data-section-title">
                            <i class="fa-solid fa-building-circle-check"></i> Entidad Legal Verificada
                        </div>

                        <div class="data-readout-grid">
                            <div class="data-readout-card animate-on-scroll">
                                <div class="readout-icon amber"><i class="fa-solid fa-hashtag"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">RUT Empresa</span>
                                    <span class="readout-value">76.543.210-K</span>
                                </div>
                                <i class="fa-solid fa-circle-check verified-badge-corner" style="color: rgba(245, 158, 11, 0.4);"></i>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.1s;">
                                <div class="readout-icon amber"><i class="fa-solid fa-building-columns"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Razón Social</span>
                                    <span class="readout-value">Tech Innovators SpA</span>
                                </div>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.2s; grid-column: span 2;">
                                <div class="readout-icon amber"><i class="fa-solid fa-tag"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Denominación Social</span>
                                    <span class="readout-value">Tech Innovators</span>
                                </div>
                            </div>
                        </div>

                        <div class="data-section-title mt-5">
                            <i class="fa-solid fa-map-location-dot" style="color: #2dd4bf;"></i> Domicilio & Contacto
                        </div>

                        <div class="data-readout-grid">
                            <div class="data-readout-card animate-on-scroll">
                                <div class="readout-icon"><i class="fa-solid fa-map"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Región</span>
                                    <span class="readout-value">METROPOLITANA</span>
                                </div>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.1s;">
                                <div class="readout-icon"><i class="fa-solid fa-city"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Comuna</span>
                                    <span class="readout-value">PROVIDENCIA</span>
                                </div>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.2s;">
                                <div class="readout-icon"><i class="fa-solid fa-road"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Dirección</span>
                                    <span class="readout-value">Av. Nueva Providencia 456</span>
                                </div>
                            </div>
                        </div>

                        <div class="data-readout-grid mt-3">
                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.3s; background: rgba(168, 85, 247, 0.05); border-color: rgba(168, 85, 247, 0.2);">
                                <div class="readout-icon purple"><i class="fa-solid fa-mobile-screen"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Teléfono Móvil (Envío Póliza)</span>
                                    <span class="readout-value">+56 988 888 888</span>
                                </div>
                            </div>

                            <div class="data-readout-card animate-on-scroll" style="animation-delay: 0.4s; background: rgba(168, 85, 247, 0.05); border-color: rgba(168, 85, 247, 0.2);">
                                <div class="readout-icon purple"><i class="fa-solid fa-at"></i></div>
                                <div class="readout-content">
                                    <span class="readout-label">Correo (Envío Póliza)</span>
                                    <span class="readout-value">contacto@techinnovators.cl</span>
                                </div>
                            </div>
                        </div>

                        <div class="divider-hairline mt-5 mb-4"></div>

                        <div class="row-switch-container compact" style="background: rgba(255,255,255,0.02); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05);">
                            <div class="switch-label-group">
                                <div class="sl-text">
                                    <span class="sl-title" style="font-size:1.2rem; color:#fff;">¿Confirma que los datos son correctos?</span>
                                    <span class="sl-sub" style="margin-top:0.25rem;">Esto es necesario para emitir su póliza digital legalmente.</span>
                                </div>
                            </div>
                            <div class="aurora-toggle-segment" style="transform: scale(1.1); margin-right: 1rem;">
                                <input type="radio" name="correct_e" id="correct_e_yes" value="yes" checked>
                                <label for="correct_e_yes">Sí</label>
                                <input type="radio" name="correct_e" id="correct_e_no" value="no">
                                <label for="correct_e_no">No</label>
                                <div class="segment-highlight"></div>
                            </div>
                        </div>

                    </div>

                    <div class="hero-action-area mt-5" style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 1.5rem;">
                        <div class="secure-badge-modern"><i class="fa-solid fa-lock" style="color: #2dd4bf;"></i> Conexión Encriptada 256-bit</div>
                        <a href="cotizacion-8-1.html" style="text-decoration:none;">
                            <button type="button" class="btn-hero-gradient" id="btnNext" style="cursor:pointer; padding: 12px 32px; font-size: 1.1rem; border-radius: 100px;">
                                Continuar Emisión <i class="fa-solid fa-arrow-right-long"></i>
                            </button>
                        </a>
                    </div>

                </div>
            </div>
"""

sidebar_html = """
            <aside class="config-sidebar">
                <div class="organic-panel" style="background: rgba(20, 20, 30, 0.7); backdrop-filter: blur(15px);">
                    <div class="sidebar-title">Contrato Digital</div>
                    
                    <ul class="aurora-list">
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Cotización</li>
                        <li class="done"><i class="fa-solid fa-circle-check"></i> Selección de Plan</li>
                        <li class="active"><span class="pulse-dot"></span> Verificación de Datos</li>
                        <li><i class="fa-regular fa-circle"></i> Opciones de Pago</li>
                        <li><i class="fa-regular fa-circle"></i> Emisión Final</li>
                    </ul>

                    <div class="discount-box-vibrant" style="background: linear-gradient(135deg, rgba(45, 212, 191, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%); border-color: rgba(45, 212, 191, 0.2);">
                        <i class="fa-solid fa-shield-halved bg-icon" style="color: rgba(45, 212, 191, 0.05);"></i>
                        <div class="db-title" style="color: #2dd4bf;">Sello de Confianza</div>
                        <div class="db-msg" style="margin-top: 0.5rem; font-size: 0.85rem;">Tus datos son procesados bajo estrictos estándares bancarios de encriptación.</div>
                    </div>
                </div>
            </aside>
"""

pattern = re.compile(r'<div class="main-spec-col">.*?</aside>', re.DOTALL)
html_content = pattern.sub(new_main_col + '\n' + sidebar_html, html_content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print("Files patched successfully")
