from bs4 import BeautifulSoup
with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
inputs = soup.find_all(['input', 'select'])
for idx, inp in enumerate(inputs):
    print(f"{idx}: {inp.get('placeholder') or inp.get('name') or inp.get('id')}")
