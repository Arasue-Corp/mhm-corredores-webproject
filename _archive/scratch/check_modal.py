with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'id="purchaseModal".*?</script>', html, re.DOTALL)
if match:
    print(match.group(0)[:1000])
else:
    print("Modal not found")
