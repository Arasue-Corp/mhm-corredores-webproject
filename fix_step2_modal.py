import re

with open("cotizacion/cotizacion-mascota-2.html", "r", encoding="utf-8") as f:
    c = f.read()

# The modal starts with <div id="quotesModal" class="modal-backdrop-aurora">
# and ends before <footer class="footer-aurora">
# Let's completely remove everything from `<div id="quotesModal"` up to `<footer class="footer-aurora">`

c = re.sub(r'<div id="quotesModal".*?(?=<footer class="footer-aurora">)', '', c, flags=re.DOTALL)

with open("cotizacion/cotizacion-mascota-2.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Removed quotesModal")
