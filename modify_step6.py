import re

with open("cotizacion/cotizacion-salud-6.html", "r", encoding="utf-8") as f:
    html = f.read()

# Generate the new HTML block
new_main = """
                    <div class="premium-white-card" style="padding: 40px; border-radius: 20px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); background: #ffffff;">
                        <div style="text-align: center; margin-bottom: 30px;">
                            <h2 style="color: #A3CC39; margin-bottom: 10px; font-size: 2rem;">Resumen</h2>
                            <p style="color: #64748B; font-size: 1.05rem;">Revisa que todos los datos sean correctos antes de confirmar tu solicitud.</p>
                        </div>

                        <!-- Sección: Comprador y Titular -->
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px;">
                            <!-- Datos del Comprador -->
                            <div style="border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;">
                                <h3 style="margin: 0 0 15px 0; font-size: 1.1rem; color: #1E293B; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px;">Datos del Comprador</h3>
                                <div style="display: grid; gap: 10px; color: #1E293B; font-size: 0.95rem;">
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">RUT:</div><span id="s-comp-rut">-</span></div>
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">Nombre completo:</div><span id="s-comp-full">-</span></div>
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">Email:</div><span id="s-comp-email">-</span></div>
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">Teléfono:</div><span id="s-comp-telefono">-</span></div>
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">Dirección:</div><span id="s-comp-dir">Pezoa Veliz 9247, Santiago</span></div>
                                </div>
                            </div>
                            
                            <!-- Datos del Titular -->
                            <div style="border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;">
                                <h3 style="margin: 0 0 15px 0; font-size: 1.1rem; color: #1E293B; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px;">Datos del Titular</h3>
                                <div style="display: grid; gap: 10px; color: #1E293B; font-size: 0.95rem;">
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">RUT:</div><span id="s-tit-rut">-</span></div>
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">Nombre completo:</div><span id="s-tit-full">-</span></div>
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">Email:</div><span id="s-tit-email">-</span></div>
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">Teléfono:</div><span id="s-tit-telefono">-</span></div>
                                    <div><div style="font-size: 0.8rem; color: #94A3B8;">Dirección:</div><span id="s-tit-dir">Pezoa Veliz 9247, Santiago</span></div>
                                </div>
                            </div>
                        </div>

                        <!-- Sección: Producto -->
                        <div style="border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; margin-bottom: 30px;">
                            <h3 style="margin: 0 0 15px 0; font-size: 1.1rem; color: #1E293B; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px;">Datos del Producto</h3>
                            <div style="display: flex; justify-content: space-between; align-items: flex-start; color: #475569; font-size: 0.95rem;">
                                <div>
                                    <div style="font-size: 0.8rem; color: #94A3B8;">Producto:</div>
                                    <div style="color: #3B82F6; font-weight: 600; font-size: 1.1rem;" id="s-producto-nombre">-</div>
                                    <div style="margin-top: 15px; font-size: 0.8rem; color: #94A3B8;">Total a pagar:</div>
                                    <div style="color: #10B981; font-weight: 700; font-size: 1.3rem;" id="s-producto-total">$0</div>
                                    <div style="font-size: 0.8rem; color: #94A3B8;">Mensual</div>
                                </div>
                                <div>
                                    <div style="font-size: 0.8rem; color: #94A3B8;">Precio del producto:</div>
                                    <div style="font-weight: 600; color: #1E293B;" id="s-producto-precio">$0</div>
                                </div>
                            </div>
                        </div>

                        <!-- Sección: Prestaciones -->
                        <div style="margin-bottom: 30px;">
                            <h3 style="margin: 0 0 15px 0; font-size: 1.1rem; color: #1E293B; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px;">Prestaciones</h3>
                            
                            <div style="display: flex; justify-content: space-between; padding: 0 15px 10px 15px; font-size: 0.85rem; font-weight: 600; color: #1E293B;">
                                <span>Prestación</span>
                                <span>Límite</span>
                            </div>
                            
                            <div id="prestaciones-list" style="border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden;">
                                <!-- Llenado por JS -->
                            </div>
                        </div>

                        <!-- Sección: Beneficiarios -->
                        <div style="margin-bottom: 30px;">
                            <h3 style="margin: 0 0 15px 0; font-size: 1.1rem; color: #1E293B; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px;">Beneficiarios</h3>
                            <div style="border: 1px solid #E2E8F0; border-radius: 8px; overflow: hidden;">
                                <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem;">
                                    <thead>
                                        <tr style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
                                            <th style="padding: 15px; font-weight: 600; color: #475569;">RUT</th>
                                            <th style="padding: 15px; font-weight: 600; color: #475569;">Nombre Completo</th>
                                            <th style="padding: 15px; font-weight: 600; color: #475569;">Parentesco</th>
                                        </tr>
                                    </thead>
                                    <tbody id="s-ben-list">
                                        <!-- JS -->
                                    </tbody>
                                </table>
                                <div id="s-ben-empty" style="display: none; text-align: center; color: #94A3B8; padding: 20px;">
                                    No se agregaron beneficiarios.
                                </div>
                            </div>
                        </div>

                        <!-- T&C -->
                        <div style="border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; text-align: center; margin-bottom: 20px;">
                            <label style="cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 0.95rem; color: #475569;">
                                <input type="checkbox" id="accept-tc" onchange="validateFinalize()" style="width: 18px; height: 18px; accent-color: #A3CC39;">
                                <span>Acepto los <a href="#" style="color: #3B82F6; text-decoration: underline;">términos y condiciones</a></span>
                            </label>
                        </div>

                        <!-- Alerta -->
                        <div style="background: #ECFDF5; border: 1px solid #10B981; border-left: 4px solid #10B981; border-radius: 8px; padding: 20px; display: flex; gap: 15px; margin-bottom: 30px;">
                            <i class="fa-solid fa-circle-info" style="color: #10B981; font-size: 1.2rem; margin-top: 2px;"></i>
                            <div>
                                <h4 style="margin: 0 0 5px 0; color: #065F46; font-size: 1rem;">Revisa tus datos</h4>
                                <p style="margin: 0; color: #047857; font-size: 0.9rem; line-height: 1.5;">Por favor, revisa cuidadosamente toda la información antes de confirmar tu compra. Al hacer clic en "Finalizar", aceptas los términos y condiciones del producto contratado.</p>
                            </div>
                        </div>

                        <!-- Botones de Acción -->
                        <div style="display: flex; justify-content: center; gap: 20px;">
                            <button onclick="window.location.href='cotizacion-salud-5.html'" style="padding: 12px 40px; font-size: 1rem; font-weight: 600; border: 1px solid #A3CC39; background: white; color: #A3CC39; border-radius: 8px; cursor: pointer; transition: 0.3s;" onmouseover="this.style.background='#F7FEE7'" onmouseout="this.style.background='white'">
                                Anterior
                            </button>
                            <button id="btn-finalizar" onclick="confirmQuote()" style="padding: 12px 40px; font-size: 1rem; font-weight: 600; opacity: 0.5; pointer-events: none; border-radius: 8px; background: #C4D69B; border: none; color: white; cursor: pointer; transition: 0.3s;" onmouseover="this.style.background='#b0c878'" onmouseout="this.style.background='#C4D69B'">
                                Finalizar
                            </button>
                        </div>
                    </div>
"""

new_script = """
    <script>
        const prestacionesList = [
            { title: "Consulta Médica General", limit: "100%", desc: "En caso de que el beneficiario requiera de atención médica ambulatoria en las especialidades: General, Pediátrica o Geriátrica; podrá solicitar la coordinación de una hora médica en cualquier centro salud en convenio..." },
            { title: "Telemedicina", limit: "100%", desc: "El beneficiario podrá solicitar la coordinación de una hora de Telemedicina con un médico certificado y habilitado por Serviclick, en el área de Medicina General..." },
            { title: "Urgencia Dental", limit: "60% hasta UF 5", desc: "La Asistencia de atención de urgencias dentales cubrirá las afecciones que no ponen en riesgo la vida del paciente, pero que requieren tratamiento inmediato..." },
            { title: "Orientación Médica Telefónica", limit: "100%", desc: "Este servicio pone a disposición del beneficiario, -de manera telefónica- personal sanitario que permita aclarar y/o asesorar cualquier duda respecto a cuadros clínicos..." },
            { title: "Parto Cesárea", limit: "40% hasta UF 5", desc: "El beneficiario podrá acceder a la cobertura de parto Cesárea siempre y cuando el Asegurado titular, cónyuge, conviviente civil o pareja asegurada cuente con la fecha probable..." },
            { title: "Radiografía Panorámica", limit: "100% hasta UF 2", desc: "El asegurado podrá acceder a realizarse una radiografía dental de tipo Panorámica bajo solicitud de una orden médica..." },
            { title: "Consulta Médica Especialista", limit: "100%", desc: "En caso de que el beneficiario requiera de atención médica ambulatoria en las especialidades: Fonoaudiología, Oncólogo, Kinesiólogo, Ginecólogo, Urología, Nutricionista, Oftalmología..." },
            { title: "Descuento en farmacias", limit: "50% hasta $10,000", desc: "Esta asistencia está desarrollada para que sea utilizada por todos los afiliados vigentes al momento de la compra y en todas las farmacias de Chile..." },
            { title: "Urgencia Médica por enfermedad", limit: "100% hasta UF 9", desc: "Este servicio corresponde a la atención médica inicial en una sala de urgencia, ocurrida a causa de una enfermedad..." },
            { title: "Limpieza Dental", limit: "100% hasta UF 2", desc: "Esta asistencia está desarrollada para que sea utilizada por todos los afiliados vigentes al momento de la compra..." },
            { title: "Exodoncia Simple", limit: "60% hasta UF 2", desc: "En caso el beneficiario requiera la atención dental para realizar una exodoncia simple..." },
            { title: "Urgencia Médica por accidente", limit: "100% hasta UF 9", desc: "Este servicio corresponde a la atención médica inicial en una sala de urgencia, ocurrida a causa de un accidente..." },
            { title: "Consulta Médica Psicológica", limit: "100%", desc: "En caso de que el beneficiario requiera de atención presencial en las especialidades: Psicología, podrá solicitar la Activación para asistir a una hora médica..." },
            { title: "Orientación Maternal Telefónica", limit: "100%", desc: "Este servicio pone a disposición del beneficiario, -de manera telefónica- personal Calificado que permita aclarar y/o asesorar cualquier duda..." },
            { title: "Examen Preventivo Oncológico", limit: "100% hasta UF 2", desc: "Cuando por motivo de una solicitud por parte de un profesional de la salud para realizar todos o algunos de los Exámenes que contemplan Antígeno prostático específico..." },
            { title: "Parto Normal", limit: "40% hasta UF 8", desc: "El beneficiario podrá acceder a la cobertura de parto Normal siempre y cuando el Asegurado titular..." },
            { title: "Examen Médico", limit: "100% hasta UF 2", desc: "Cuando por motivo de una solicitud por parte de un profesional de la salud para realizar todos o algunos de los Exámenes que contemplan hemograma, perfil bioquímico..." },
            { title: "Telemedicina Especialista", limit: "100%", desc: "El beneficiario podrá solicitar la coordinación de una hora de Telemedicina con un médico certificado y habilitado por Serviclick, en el área de Nutrición, Psicológica..." },
            { title: "Exodoncia Colgajo", limit: "60% hasta UF 2", desc: "En caso el beneficiario requiera la atención dental para realizar una exodoncia a colgajo solicitado por un médico bajo orden medica..." }
        ];

        document.addEventListener('DOMContentLoaded', () => {
            loadSummaryData();
            renderPrestaciones();
        });

        function toggleAccordion(id) {
            const el = document.getElementById('acc-content-' + id);
            const icon = document.getElementById('acc-icon-' + id);
            if(el.style.display === 'none') {
                el.style.display = 'block';
                icon.style.transform = 'rotate(180deg)';
            } else {
                el.style.display = 'none';
                icon.style.transform = 'rotate(0deg)';
            }
        }

        function renderPrestaciones() {
            const container = document.getElementById('prestaciones-list');
            let html = '';
            prestacionesList.forEach((p, i) => {
                html += `
                    <div style="border-bottom: 1px solid #E2E8F0;">
                        <div onclick="toggleAccordion(${i})" style="display: flex; justify-content: space-between; align-items: center; padding: 15px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#F8FAFC'" onmouseout="this.style.background='transparent'">
                            <div style="display: flex; align-items: center; gap: 10px; color: #1E293B; font-size: 0.95rem;">
                                <i id="acc-icon-${i}" class="fa-solid fa-chevron-down" style="color: #64748B; font-size: 0.8rem; transition: transform 0.3s;"></i>
                                ${p.title}
                            </div>
                            <div style="color: #475569; font-size: 0.9rem;">
                                ${p.limit}
                            </div>
                        </div>
                        <div id="acc-content-${i}" style="display: none; padding: 0 15px 15px 30px; color: #64748B; font-size: 0.85rem; line-height: 1.5;">
                            ${p.desc}
                        </div>
                    </div>
                `;
            });
            container.innerHTML = html;
        }

        function validateFinalize() {
            const chk = document.getElementById('accept-tc');
            const btn = document.getElementById('btn-finalizar');
            if(chk.checked) {
                btn.style.opacity = '1';
                btn.style.pointerEvents = 'auto';
                btn.style.background = '#A3CC39';
            } else {
                btn.style.opacity = '0.5';
                btn.style.pointerEvents = 'none';
                btn.style.background = '#C4D69B';
            }
        }

        function loadSummaryData() {
            const compRut = sessionStorage.getItem('compradorRut') || '-';
            const compNombres = sessionStorage.getItem('compradorNombres') || '';
            const compPaterno = sessionStorage.getItem('compradorPaterno') || '';
            const compMaterno = sessionStorage.getItem('compradorMaterno') || '';
            const compTelefono = sessionStorage.getItem('compradorTelefono') || '-';
            const compEmail = sessionStorage.getItem('compradorEmail') || '-';
            
            document.getElementById('s-comp-rut').textContent = compRut;
            document.getElementById('s-comp-full').textContent = `${compNombres} ${compPaterno} ${compMaterno}`.trim() || '-';
            document.getElementById('s-comp-telefono').textContent = compTelefono;
            document.getElementById('s-comp-email').textContent = compEmail;

            const isSame = sessionStorage.getItem('titularMismoComprador') === 'true';
            if (isSame) {
                document.getElementById('s-tit-rut').textContent = compRut;
                document.getElementById('s-tit-full').textContent = `${compNombres} ${compPaterno} ${compMaterno}`.trim() || '-';
                document.getElementById('s-tit-telefono').textContent = compTelefono;
                document.getElementById('s-tit-email').textContent = compEmail;
            } else {
                const titRut = sessionStorage.getItem('titularRut') || '-';
                const titNombres = sessionStorage.getItem('titularNombres') || '';
                const titPaterno = sessionStorage.getItem('titularPaterno') || '';
                const titMaterno = sessionStorage.getItem('titularMaterno') || '';
                const titTelefono = sessionStorage.getItem('titularTelefono') || '-';
                const titEmail = sessionStorage.getItem('titularEmail') || '-';
                
                document.getElementById('s-tit-rut').textContent = titRut;
                document.getElementById('s-tit-full').textContent = `${titNombres} ${titPaterno} ${titMaterno}`.trim() || '-';
                document.getElementById('s-tit-telefono').textContent = titTelefono;
                document.getElementById('s-tit-email').textContent = titEmail;
            }

            const prod = sessionStorage.getItem('selectedProduct');
            let nombre = 'Plan de Salud Básico';
            let precio = '$22.170';
            if(prod === 'integral') {
                nombre = 'Asistencia Integral Pro T+2';
                precio = '$22.170';
            } else if(prod === 'avanzado') {
                nombre = 'Plan de Salud Avanzado';
                precio = '$18.500';
            } else if(prod === 'basico') {
                nombre = 'Plan de Salud Básico';
                precio = '$12.000';
            } else if(prod) {
                nombre = prod;
            }
            document.getElementById('s-producto-nombre').textContent = nombre;
            document.getElementById('s-producto-precio').textContent = precio;
            document.getElementById('s-producto-total').textContent = precio;

            const benData = sessionStorage.getItem('beneficiariesData');
            const listEl = document.getElementById('s-ben-list');
            const emptyEl = document.getElementById('s-ben-empty');

            if (benData) {
                try {
                    const beneficiaries = JSON.parse(benData);
                    if (beneficiaries.length > 0) {
                        listEl.innerHTML = '';
                        beneficiaries.forEach((b) => {
                            const html = `
                                <tr style="border-bottom: 1px solid #E2E8F0; color: #1E293B;">
                                    <td style="padding: 15px;">${b.rut}</td>
                                    <td style="padding: 15px;">${b.nombre} ${b.paterno} ${b.materno}</td>
                                    <td style="padding: 15px;">${b.parentesco}</td>
                                </tr>
                            `;
                            listEl.innerHTML += html;
                        });
                    } else {
                        emptyEl.style.display = 'block';
                    }
                } catch(e) {
                    emptyEl.style.display = 'block';
                }
            } else {
                emptyEl.style.display = 'block';
            }
        }

        function confirmQuote() {
            alert('¡Cotización finalizada exitosamente! Te redirigiremos al portal de pagos.');
            // window.location.href = 'pago.html';
        }
    </script>
"""

# Find the start of the card content
card_start_str = r'<div class="premium-white-card" style="padding: 40px; border-radius: 20px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); background: #ffffff;">'
script_start_str = r'<script>'

match_start = re.search(card_start_str, html)
if not match_start:
    print("Could not find card start")
    exit(1)

# Find end of card by finding </div>\s*</div>\s*</div>\s*</div>\s*</main>
main_end_match = re.search(r'</main>', html)
if not main_end_match:
    print("Could not find </main>")
    exit(1)

# Replace between match_start and main_end_match minus the extra closing tags
html_before = html[:match_start.start()]

# find the closing tags of the main content 
end_tags = """
                </div>
            </div>
        </div>
    </main>
"""
# So we just replace up to </main> and add end_tags back
html_after_main = html[main_end_match.start() + len('</main>'):]

# Replace script
script_match = re.search(script_start_str, html_after_main)
if not script_match:
    print("Could not find script start")
    exit(1)

script_end_match = re.search(r'</script>', html_after_main)
html_after_script = html_after_main[script_end_match.end():]
footer_part = html_after_main[:script_match.start()]

final_html = html_before + new_main + end_tags + footer_part + new_script + html_after_script

with open("cotizacion/cotizacion-salud-6.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Modification complete.")
