import re

filepath = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion/cotizacion-salud-1.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace instances of:
# <td style="${tdStyle}">...</td>
# <td style="${tdStyle} color: #E11D48; font-weight: 700;">...</td>
# <td style="${tdStyleLimit}">...</td>
# <td style="${tdStyleLimit}">...</td>
# within the JS strings.

# A better way is to do a regex substitution on the <tr> tags in JS.
# The structure is: 
# <tr><td ...>Name</td><td ...>Percentage</td><td ...>Amount</td><td ...>Events</td></tr>

def replacer(match):
    td1 = match.group(1).replace('<td ', '<td data-label="Cobertura" ')
    td2 = match.group(2).replace('<td ', '<td data-label="Copago" ')
    td3 = match.group(3).replace('<td ', '<td data-label="Monto Máximo" ')
    td4 = match.group(4).replace('<td ', '<td data-label="Límite Anual" ')
    return f"<tr>{td1}{td2}{td3}{td4}</tr>"

# Find <tr>...</tr> with exactly 4 <td>s inside.
pattern = re.compile(r'<tr>(<td[^>]*>.*?</td>)(<td[^>]*>.*?</td>)(<td[^>]*>.*?</td>)(<td[^>]*>.*?</td>)</tr>')
new_content = pattern.sub(replacer, content)

if new_content != content:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed data-labels in cotizacion-salud-1.html")
else:
    print("No changes made.")

