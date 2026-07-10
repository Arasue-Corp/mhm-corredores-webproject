import re

# Read step 5 for template
with open("cotizacion/cotizacion-salud-5.html", "r", encoding="utf-8") as f:
    html5 = f.read()

# Read step 6 for content
with open("cotizacion/cotizacion-salud-6.html", "r", encoding="utf-8") as f:
    html6 = f.read()

# Extract from html5: Top until <div class="specs-layout-grid">
grid_start_idx = html5.find('<div class="specs-layout-grid">')
if grid_start_idx == -1:
    print("Could not find specs-layout-grid in step 5")
    exit(1)

html_top = html5[:grid_start_idx + len('<div class="specs-layout-grid">')]

# Also grab the config-sidebar from step 5, but we actually don't need it or maybe we do for layout?
# In step 5, after main-spec-col, there's config-sidebar. Let's just use a single column layout or include the sidebar.
# The user's screenshot was full width for the cards, so a single column grid is fine, but maybe we need page-wrapper.
# In html_top, we want to change the step 5 active state to step 6 (Resumen).
html_top = html_top.replace('<li class="active"><span class="pulse-dot"></span> Beneficiarios</li>', '<li><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Beneficiarios</li>')
html_top = html_top.replace('<li><i class="fa-regular fa-circle"></i> Pago Seguro</li>', '<li class="active"><span class="pulse-dot"></span> Resumen</li>')
# Also the top wizard track
html_top = html_top.replace('width: 16%;', 'width: 80%;')
# The header title
html_top = re.sub(r'<h1[^>]*>.*?</h1>', '<h1 class="text-gradient-corp">Resumen de Cotización</h1>', html_top)
html_top = re.sub(r'<p>Puedes agregar hasta.*?</p>', '<p>Revisa cuidadosamente los datos antes de proceder al pago.</p>', html_top)


# Extract from html6: <div class="main-spec-col anim-entry delay-1"> ... to its end
main_col_start = html6.find('<div class="main-spec-col anim-entry delay-1">')
main_col_end = html6.find('</main>')
if main_col_start == -1 or main_col_end == -1:
    print("Could not find main-spec-col or main end in step 6")
    exit(1)

html_main_content = html6[main_col_start:main_col_end]
# We need to trim some closing divs from html_main_content because </main> in step 6 closed specs-layout-grid and container.
# html_main_content ends with </div></div></div>
html_main_content = html_main_content.rsplit('</div>', 3)[0] + '</div>' # Just keep main-spec-col closed

# Extract JS from html6
js_start = html6.find('<script>')
js_end = html6.find('</script>', js_start)
html_js = html6[js_start:js_end + len('</script>')]

# Extract from html5: Footer
# Find where specs-layout-grid ends. It ends after config-sidebar.
sidebar_start = html5.find('<aside class="config-sidebar')
if sidebar_start != -1:
    # We will include the sidebar too for consistency, or not? The screenshot didn't have it, but the user said "fijate en el contenido. El diseño debe ser el que ya nosotros hemos definido para MHM". The defined MHM design for quote steps has a right sidebar.
    sidebar_end = html5.find('</aside>', sidebar_start) + len('</aside>')
    sidebar_content = html5[sidebar_start:sidebar_end]
    
    # Update sidebar content for step 6
    sidebar_content = sidebar_content.replace('<li class="active"><span class="pulse-dot"></span> Beneficiarios</li>', '<li style="color: #10B981; font-weight: 600;"><i class="fa-solid fa-circle-check" style="color: #10B981;"></i> Beneficiarios</li>')
    sidebar_content = sidebar_content.replace('<li><i class="fa-regular fa-circle"></i> Pago Seguro</li>', '<li class="active"><span class="pulse-dot"></span> Resumen</li>')
    
    # Get the rest of the HTML (footer, etc)
    rest_start = html5.find('</div>', sidebar_end) # close specs-layout-grid
    html_bottom = html5[rest_start:]
    
    # Replace step 5 JS with step 6 JS
    # We will just append step 6 JS right before </body>
    html_bottom = re.sub(r'<script>.*?</script>', '', html_bottom, flags=re.DOTALL)
    html_bottom = html_bottom.replace('</body>', html_js + '\n</body>')
    
    final_html = html_top + '\n' + html_main_content + '\n' + sidebar_content + html_bottom
else:
    # No sidebar
    html_bottom = html5[html5.find('</main>'):] if '</main>' in html5 else html5[html5.rfind('</div>', 0, html5.find('<footer')):]
    final_html = html_top + '\n' + html_main_content + '\n</div></div>' + html_bottom

with open("cotizacion/cotizacion-salud-6.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Modification complete.")
