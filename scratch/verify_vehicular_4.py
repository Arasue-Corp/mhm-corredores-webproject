import re
with open('cotizacion/cotizacion-vehicular-4.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Title:', re.search(r'<h1 class="text-gradient-corp">.*?</h1>', html).group(0))
print('Subtitle:', re.search(r'<p class="text-slate-500 mb-8">.*?</p>', html).group(0))
print('Icon:', re.search(r'fa-car', html) is not None)
print('Width:', re.search(r'max-width: 100%;', html) is not None)
