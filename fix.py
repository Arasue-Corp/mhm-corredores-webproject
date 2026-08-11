import sys
import re

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-vehicular-1.html'
with open(filepath, 'r') as f:
    content = f.read()

# Remove the old bottom-section-grid
old_bottom_pattern = r'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 40px;" class="bottom-section-grid">\s*<style>\s*@media \(max-width: 768px\) {\s*\.bottom-section-grid { grid-template-columns: 1fr !important; }\s*}\s*</style>'
content = re.sub(old_bottom_pattern, '', content)

# Remove the closing div of veh-type-grid and bottom-section-grid
# we will just rebuild the skeleton around the existing containers
veh_grid_start = content.find('<div class="veh-type-grid">')
veh_card_start = content.find('<div class="veh-type-card">', veh_grid_start)
why_mhm_start = content.find('<div class="why-mhm-container">')
why_mhm_end = content.find('</div>\n    </div>\n</form>', why_mhm_start)
cart_start = content.find('<div class="cart-summary-container">')
cart_end = content.find('<div class="why-mhm-container">', cart_start)

# Extract blocks
veh_card_html = content[veh_grid_start:cart_start]
cart_html = content[cart_start:why_mhm_start]
why_html = content[why_mhm_start:why_mhm_end+6]

# Ensure we close veh_card_html properly if it has extra closing divs
# The original had:
# </div> <!-- card -->
# </div> <!-- grid -->

# Reconstruct
new_layout = f"""
    <style>
        .main-split-layout {{ display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 40px; align-items: start; margin-top: 20px; }}
        @media (max-width: 900px) {{
            .main-split-layout {{ grid-template-columns: 1fr; }}
        }}
    </style>
    <div class="main-split-layout">
        <div class="left-split-col" style="display: flex; flex-direction: column; gap: 40px;">
{veh_card_html}
{why_html}
        </div>
        <div class="right-split-col" style="position: sticky; top: 20px;">
{cart_html}
        </div>
    </div>
"""

# replace everything from veh_grid_start to why_mhm_end+6
content = content[:veh_grid_start] + new_layout + content[why_mhm_end+6:]

# write back
with open(filepath, 'w') as f:
    f.write(content)

