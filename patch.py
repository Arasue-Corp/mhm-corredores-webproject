import re

html_path = "cotizacion/cotizacion-7-1.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Wizard Top
content = content.replace('<div class="wizard-title"><i class="fa-solid fa-id-card"></i>Insurance History</div>', 
                          '<div class="wizard-title"><i class="fa-solid fa-file-contract"></i>Detalles de Contratación</div>')

# Replace Title
content = content.replace('<h1 class="text-gradient-corp">Prior Coverage</h1>', 
                          '<h1 class="text-gradient-corp">Contrato 100% Digital</h1>')
content = content.replace('<p>Continuous coverage is one of the biggest factors for discounts.</p>', 
                          '<p>Verifica los datos del contratante antes de emitir tu póliza.</p>')

new_main_col = """
            <div class="main-spec-col">
                
                <div class="car-tabs-integrated" id="entityTabs">
                    <button type="button" class="tab-int active" onclick="switchEntityTab('persona', this)">
                        <span class="tab-txt"><i class="fa-solid fa-user"></i> Persona</span>
                    </button>
                    <button type="button" class="tab-int" onclick="switchEntityTab('empresa', this)">
                        <span class="tab-txt"><i class="fa-solid fa-building"></i> Empresa</span>
                    </button>
                </div>

                <div class="premium-white-card" id="quoteFormStep7">
                    
                    <!-- FORMULARIO PERSONA -->
                    <div id="panel-persona" class="car-panel active" data-id="persona">
                        
                        <div class="info-banner-blue mb-4">
                            <div class="banner-icon"><i class="fa-solid fa-id-card"></i></div>
                            <div><strong>Datos del contratante</strong></div>
                        </div>

                        <div class="premium-group">
                            <div class="grid-2-tight">
                                <div class="inp-rich-group">
                                    <label>RUT</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-hashtag"></i></div>
                                        <input type="text" class="rich-input" value="10.042.595-5" disabled>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Fecha de Nacimiento</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-calendar"></i></div>
                                        <input type="text" class="rich-input" value="22/05/1981" disabled>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="grid-2-tight mt-3">
                                <div class="inp-rich-group">
                                    <label>Nombre</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-user"></i></div>
                                        <input type="text" class="rich-input" value="Cristian Gonzalo" disabled>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Apellidos</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-users"></i></div>
                                        <input type="text" class="rich-input" value="Martinez" disabled>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="info-banner-blue mb-4 mt-4" style="background: rgba(203, 108, 230, 0.08); border-color: rgba(203, 108, 230, 0.3); color: #cb6ce6;">
                            <div class="banner-icon" style="color: #cb6ce6;"><i class="fa-solid fa-map-location-dot"></i></div>
                            <div style="color: #0f0f1a;"><strong>Contacto del contratante</strong></div>
                        </div>

                        <div class="premium-group">
                            <div class="grid-2-tight">
                                <div class="inp-rich-group">
                                    <label>Región</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-map"></i></div>
                                        <input type="text" class="rich-input" value="DE LOS RÍOS" disabled>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Comuna</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-city"></i></div>
                                        <input type="text" class="rich-input" value="VALDIVIA" disabled>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="grid-2-tight mt-3">
                                <div class="inp-rich-group">
                                    <label>Dirección</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-road"></i></div>
                                        <input type="text" class="rich-input" value="Calle Los Robles" disabled>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Número</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-hashtag"></i></div>
                                        <input type="text" class="rich-input" value="1234" disabled>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="pg-header mt-4">
                            <div class="pg-header-badge blue">
                                <i class="fa-solid fa-envelope"></i> ¿Cómo te gustaría que te enviáramos tu nuevo seguro?
                            </div>
                            <div class="pg-header-line"></div>
                        </div>

                        <div class="premium-group">
                            <div class="grid-2-tight">
                                <div class="inp-rich-group">
                                    <label>Teléfono Móvil</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-mobile-screen"></i></div>
                                        <input type="text" class="rich-input" value="+56 999 999 999" disabled>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Correo</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-at"></i></div>
                                        <input type="text" class="rich-input" value="cristian.martinez@email.com" disabled>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="divider-hairline mt-4 mb-4"></div>

                        <div class="row-switch-container compact">
                            <div class="switch-label-group">
                                <div class="sl-text"><span class="sl-title" style="font-size:1.1rem; color:#796bfc;">¿Los datos están correctos?</span></div>
                            </div>
                            <div class="aurora-toggle-segment">
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
                        
                        <div class="info-banner-blue mb-4">
                            <div class="banner-icon"><i class="fa-solid fa-building"></i></div>
                            <div><strong>Datos de la Empresa</strong></div>
                        </div>

                        <div class="premium-group">
                            <div class="grid-2-tight">
                                <div class="inp-rich-group">
                                    <label>RUT</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-hashtag"></i></div>
                                        <input type="text" class="rich-input" value="76.543.210-K" disabled>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Razón Social</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-building-columns"></i></div>
                                        <input type="text" class="rich-input" value="Tech Innovators SpA" disabled>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="inp-rich-group mt-3">
                                <label>Denominación social</label>
                                <div class="input-rich-wrapper compact-premium theme-teal">
                                    <div class="icon-slot"><i class="fa-solid fa-tag"></i></div>
                                    <input type="text" class="rich-input" value="Tech Innovators" disabled>
                                </div>
                            </div>
                        </div>

                        <div class="info-banner-blue mb-4 mt-4" style="background: rgba(203, 108, 230, 0.08); border-color: rgba(203, 108, 230, 0.3); color: #cb6ce6;">
                            <div class="banner-icon" style="color: #cb6ce6;"><i class="fa-solid fa-map-location-dot"></i></div>
                            <div style="color: #0f0f1a;"><strong>Contacto de la Empresa</strong></div>
                        </div>

                        <div class="premium-group">
                            <div class="grid-2-tight">
                                <div class="inp-rich-group">
                                    <label>Región</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-map"></i></div>
                                        <input type="text" class="rich-input" value="METROPOLITANA" disabled>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Comuna</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-city"></i></div>
                                        <input type="text" class="rich-input" value="PROVIDENCIA" disabled>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="grid-2-tight mt-3">
                                <div class="inp-rich-group">
                                    <label>Dirección</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-road"></i></div>
                                        <input type="text" class="rich-input" value="Av. Nueva Providencia" disabled>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Número</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-hashtag"></i></div>
                                        <input type="text" class="rich-input" value="456" disabled>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="pg-header mt-4">
                            <div class="pg-header-badge blue">
                                <i class="fa-solid fa-envelope"></i> ¿Cómo te gustaría que te enviáramos tu nuevo seguro?
                            </div>
                            <div class="pg-header-line"></div>
                        </div>

                        <div class="premium-group">
                            <div class="grid-2-tight">
                                <div class="inp-rich-group">
                                    <label>Teléfono Móvil</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-mobile-screen"></i></div>
                                        <input type="text" class="rich-input" value="+56 988 888 888" disabled>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Correo</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-at"></i></div>
                                        <input type="text" class="rich-input" value="empresa@email.com" disabled>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="divider-hairline mt-4 mb-4"></div>

                        <div class="row-switch-container compact">
                            <div class="switch-label-group">
                                <div class="sl-text"><span class="sl-title" style="font-size:1.1rem; color:#796bfc;">¿Los datos están correctos?</span></div>
                            </div>
                            <div class="aurora-toggle-segment">
                                <input type="radio" name="correct_e" id="correct_e_yes" value="yes" checked>
                                <label for="correct_e_yes">Sí</label>
                                <input type="radio" name="correct_e" id="correct_e_no" value="no">
                                <label for="correct_e_no">No</label>
                                <div class="segment-highlight"></div>
                            </div>
                        </div>

                    </div>

                    <div class="hero-action-area mt-5" style="display: flex; justify-content: space-between; align-items: center;">
                        <div class="secure-badge-modern"><i class="fa-solid fa-shield-halved"></i> Datos Encriptados</div>
                        <a href="cotizacion-8-1.html" style="text-decoration:none;">
                            <button type="button" class="btn-hero-gradient" id="btnNext" style="cursor:pointer; padding: 12px 24px; font-size: 1rem;">
                                Siguiente <i class="fa-solid fa-arrow-right-long"></i>
                            </button>
                        </a>
                    </div>

                </div>
            </div>
"""

pattern = re.compile(r'<div class="main-spec-col">.*?</aside>', re.DOTALL)
content = pattern.sub(new_main_col + '\n            <aside class="config-sidebar">', content)

script_injection = """
<script>
function switchEntityTab(entityType, btn) {
    const tabs = document.querySelectorAll('#entityTabs .tab-int');
    tabs.forEach(t => t.classList.remove('active'));
    btn.classList.add('active');

    const panelPersona = document.getElementById('panel-persona');
    const panelEmpresa = document.getElementById('panel-empresa');

    if (entityType === 'persona') {
        panelPersona.style.display = 'block';
        panelEmpresa.style.display = 'none';
        
        panelPersona.classList.remove('animate-on-scroll');
        void panelPersona.offsetWidth;
        panelPersona.classList.add('animate-on-scroll');
    } else {
        panelPersona.style.display = 'none';
        panelEmpresa.style.display = 'block';
        
        panelEmpresa.classList.remove('animate-on-scroll');
        void panelEmpresa.offsetWidth;
        panelEmpresa.classList.add('animate-on-scroll');
    }
}
</script>
</body>
"""
content = content.replace("</body>", script_injection)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("File updated")
