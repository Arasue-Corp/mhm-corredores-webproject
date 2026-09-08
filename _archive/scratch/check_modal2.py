with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'id="successModal".*?</script>', html, re.DOTALL)
if match:
    print(match.group(0)[:1500])
