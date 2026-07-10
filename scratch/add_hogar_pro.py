import os
import re

file_path = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-asistencia-hogar-1.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the cards inside veh-type-grid
# The existing card is lines 390 to 422 roughly.
card_regex = r'(<div class="veh-type-card">.*?</div>\s*</div>)'
match = re.search(card_regex, content, re.DOTALL)
if match:
    card1 = match.group(1)
    
    # Let's adjust card 1 price
    card1 = card1.replace('$3.780', '$7.990')
    
    # Create card 2
    card2 = card1.replace('id="img-hogar"', 'id="img-hogar-pro"')
    card2 = card2.replace('<h4>Asistencia Hogar</h4>', '<h4>Asistencia Hogar Pro</h4>')
    card2 = card2.replace('$7.990 / mes', '$9.490 / mes')
    card2 = card2.replace('id="toggle-hogar"', 'id="toggle-hogar-pro"')
    card2 = card2.replace('for="toggle-hogar"', 'for="toggle-hogar-pro"')
    card2 = card2.replace("updateQty('hogar'", "updateQty('hogar-pro'")
    card2 = card2.replace('id="qty-hogar"', 'id="qty-hogar-pro"')
    card2 = card2.replace("openCoverageModal('hogar')", "openCoverageModal('hogar-pro')")
    
    # Strip the trailing </div> of the grid from card1 and append card2 + grid closer
    new_grid_content = card1[:-7] + '\n' + card2[:-7] + '\n</div>'
    
    content = content.replace(match.group(0), new_grid_content)

# 2. Update the JS plans object
old_plans = """    const plans = {
        'hogar': { name: 'Asistencia Hogar', price: 3780, qty: 0 }
    };"""

new_plans = """    const plans = {
        'hogar': { name: 'Asistencia Hogar', price: 7990, qty: 0 },
        'hogar-pro': { name: 'Asistencia Hogar Pro', price: 9490, qty: 0 }
    };"""

content = content.replace(old_plans, new_plans)

# 3. Update modal title
old_modal_js = "titleEl.innerText = 'Coberturas: Asistencia Hogar';"
new_modal_js = "titleEl.innerText = 'Coberturas: ' + plans[planId].name;"
content = content.replace(old_modal_js, new_modal_js)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated step 1 with 2 cards")
