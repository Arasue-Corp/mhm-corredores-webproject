with open('cotizacion/cotizacion-vehicular-3.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
if 'successModal' in html:
    print('Modal found in step 3')
    match = re.search(r'id="successModal".*?</script>', html, re.DOTALL)
    if match:
        print(match.group(0)[:1500])
else:
    print('Modal NOT found in step 3')
