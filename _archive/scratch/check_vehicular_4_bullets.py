from bs4 import BeautifulSoup

with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("Bullet points:")
for li in soup.find_all('li'):
    print(li.text)
