import re

html_path = "cotizacion/cotizacion-7-1.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_form = """
                    <!-- FORMULARIO PERSONA -->
                    <div id="panel-persona" class="car-panel active" data-id="persona">
                        <div class="info-banner-blue mb-4">
                            <div class="banner-icon"><i class="fa-solid fa-id-card"></i></div>
                            <div><strong>Identidad Verificada:</strong> Contratante Persona</div>
                        </div>

                        <div class="premium-group">
                            <div class="pg-header">
                                <div class="pg-header-badge blue">
                                    <i class="fa-solid fa-user-check"></i> DATOS DEL CONTRATANTE
                                </div>
                                <div class="pg-header-line"></div>
                            </div>
                            
                            <div class="grid-2-tight mb-3">
                                <div class="inp-rich-group">
                                    <label>RUT</label>
                                    <div class="input-rich-wrapper compact-premium theme-blue">
                                        <div class="icon-slot"><i class="fa-solid fa-hashtag"></i></div>
                                        <input type="text" class="rich-input" value="10.042.595-5" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                        <div class="verified-badge-inline" style="position:absolute; right: 15px; color: var(--success, #10b981);"><i class="fa-solid fa-circle-check"></i></div>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Fecha de Nacimiento</label>
                                    <div class="input-rich-wrapper compact-premium theme-blue">
                                        <div class="icon-slot"><i class="fa-solid fa-calendar-day"></i></div>
                                        <input type="text" class="rich-input" value="22/05/1981" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                            </div>
                            
                            <div class="grid-2-tight mb-4">
                                <div class="inp-rich-group">
                                    <label>Nombre(s)</label>
                                    <div class="input-rich-wrapper compact-premium theme-blue">
                                        <div class="icon-slot"><i class="fa-solid fa-user"></i></div>
                                        <input type="text" class="rich-input" value="Cristian Gonzalo" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Apellidos</label>
                                    <div class="input-rich-wrapper compact-premium theme-blue">
                                        <div class="icon-slot"><i class="fa-solid fa-users"></i></div>
                                        <input type="text" class="rich-input" value="Martinez" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                            </div>

                            <div class="pg-header">
                                <div class="pg-header-badge teal">
                                    <i class="fa-solid fa-map-location-dot"></i> RESIDENCIA & CONTACTO
                                </div>
                                <div class="pg-header-line"></div>
                            </div>
                            
                            <div class="grid-2-tight mb-3">
                                <div class="inp-rich-group">
                                    <label>Región</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-map"></i></div>
                                        <input type="text" class="rich-input" value="DE LOS RÍOS" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Comuna</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-city"></i></div>
                                        <input type="text" class="rich-input" value="VALDIVIA" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                            </div>

                            <div class="inp-rich-group mb-3">
                                <label>Dirección</label>
                                <div class="input-rich-wrapper compact-premium theme-teal">
                                    <div class="icon-slot"><i class="fa-solid fa-road"></i></div>
                                    <input type="text" class="rich-input" value="Calle Los Robles 1234" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                </div>
                            </div>

                            <div class="grid-2-tight mb-4">
                                <div class="inp-rich-group">
                                    <label>Teléfono Móvil (Envío Póliza)</label>
                                    <div class="input-rich-wrapper compact-premium theme-purple">
                                        <div class="icon-slot"><i class="fa-solid fa-mobile-screen"></i></div>
                                        <input type="text" class="rich-input" value="+56 999 999 999" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Correo (Envío Póliza)</label>
                                    <div class="input-rich-wrapper compact-premium theme-purple">
                                        <div class="icon-slot"><i class="fa-solid fa-at"></i></div>
                                        <input type="text" class="rich-input" value="cristian.martinez@email.com" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                            </div>
                            
                            <div class="row-switch-container">
                                <div class="switch-label-group">
                                    <div class="sl-icon"><i class="fa-solid fa-clipboard-check"></i></div>
                                    <div class="sl-text">
                                        <span class="sl-title" style="font-size:1.15rem;">¿Confirma que los datos son correctos?</span>
                                        <span class="sl-sub">Esto es necesario para emitir su póliza digital legalmente.</span>
                                    </div>
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
                    </div>

                    <!-- FORMULARIO EMPRESA -->
                    <div id="panel-empresa" class="car-panel" data-id="empresa" style="display:none;">
                        <div class="info-banner-blue mb-4">
                            <div class="banner-icon"><i class="fa-solid fa-building"></i></div>
                            <div><strong>Entidad Legal Verificada:</strong> Contratante Empresa</div>
                        </div>

                        <div class="premium-group">
                            <div class="pg-header">
                                <div class="pg-header-badge blue">
                                    <i class="fa-solid fa-building-circle-check"></i> DATOS DE LA EMPRESA
                                </div>
                                <div class="pg-header-line"></div>
                            </div>
                            
                            <div class="grid-2-tight mb-3">
                                <div class="inp-rich-group">
                                    <label>RUT Empresa</label>
                                    <div class="input-rich-wrapper compact-premium theme-blue">
                                        <div class="icon-slot"><i class="fa-solid fa-hashtag"></i></div>
                                        <input type="text" class="rich-input" value="76.543.210-K" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                        <div class="verified-badge-inline" style="position:absolute; right: 15px; color: var(--success, #10b981);"><i class="fa-solid fa-circle-check"></i></div>
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Denominación Social</label>
                                    <div class="input-rich-wrapper compact-premium theme-blue">
                                        <div class="icon-slot"><i class="fa-solid fa-tag"></i></div>
                                        <input type="text" class="rich-input" value="Tech Innovators" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                            </div>

                            <div class="inp-rich-group mb-4">
                                <label>Razón Social</label>
                                <div class="input-rich-wrapper compact-premium theme-blue">
                                    <div class="icon-slot"><i class="fa-solid fa-building-columns"></i></div>
                                    <input type="text" class="rich-input" value="Tech Innovators SpA" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                </div>
                            </div>

                            <div class="pg-header">
                                <div class="pg-header-badge teal">
                                    <i class="fa-solid fa-map-location-dot"></i> DOMICILIO & CONTACTO
                                </div>
                                <div class="pg-header-line"></div>
                            </div>
                            
                            <div class="grid-2-tight mb-3">
                                <div class="inp-rich-group">
                                    <label>Región</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-map"></i></div>
                                        <input type="text" class="rich-input" value="METROPOLITANA" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Comuna</label>
                                    <div class="input-rich-wrapper compact-premium theme-teal">
                                        <div class="icon-slot"><i class="fa-solid fa-city"></i></div>
                                        <input type="text" class="rich-input" value="PROVIDENCIA" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                            </div>

                            <div class="inp-rich-group mb-3">
                                <label>Dirección</label>
                                <div class="input-rich-wrapper compact-premium theme-teal">
                                    <div class="icon-slot"><i class="fa-solid fa-road"></i></div>
                                    <input type="text" class="rich-input" value="Av. Nueva Providencia 456" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                </div>
                            </div>

                            <div class="grid-2-tight mb-4">
                                <div class="inp-rich-group">
                                    <label>Teléfono Móvil (Envío Póliza)</label>
                                    <div class="input-rich-wrapper compact-premium theme-purple">
                                        <div class="icon-slot"><i class="fa-solid fa-mobile-screen"></i></div>
                                        <input type="text" class="rich-input" value="+56 988 888 888" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                                <div class="inp-rich-group">
                                    <label>Correo (Envío Póliza)</label>
                                    <div class="input-rich-wrapper compact-premium theme-purple">
                                        <div class="icon-slot"><i class="fa-solid fa-at"></i></div>
                                        <input type="text" class="rich-input" value="contacto@techinnovators.cl" disabled style="color: var(--text-dark, #333); font-weight: 600;">
                                    </div>
                                </div>
                            </div>
                            
                            <div class="row-switch-container">
                                <div class="switch-label-group">
                                    <div class="sl-icon"><i class="fa-solid fa-clipboard-check"></i></div>
                                    <div class="sl-text">
                                        <span class="sl-title" style="font-size:1.15rem;">¿Confirma que los datos son correctos?</span>
                                        <span class="sl-sub">Esto es necesario para emitir su póliza digital legalmente.</span>
                                    </div>
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
                    </div>
"""

pattern = re.compile(r'<!-- FORMULARIO PERSONA -->.*?<div class="hero-action-area', re.DOTALL)
content = pattern.sub(new_form + '\n                    <div class="hero-action-area', content)

# Remove the inline style from premium-white-card to revert to the default CSS
content = re.sub(
    r'class="premium-white-card" id="quoteFormStep7" style="[^"]*"',
    r'class="premium-white-card" id="quoteFormStep7"',
    content
)

# Remove the inline style from organic-panel
content = re.sub(
    r'class="organic-panel" style="[^"]*"',
    r'class="organic-panel"',
    content
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Rewritten with existing premium classes!")
