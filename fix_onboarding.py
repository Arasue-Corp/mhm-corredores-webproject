from bs4 import BeautifulSoup
import re

# 1. Restore sessionStorage check in script-quote.js
with open("js/script-quote.js", "r") as f:
    js_content = f.read()

old_js = """document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('alexOnboarding')) {
        // Force show during development by ignoring sessionStorage
        setTimeout(() => {
            document.getElementById('alexOnboarding').classList.add('active');
        }, 600);
    }
});"""

new_js = """document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('alexOnboarding')) {
        if (!sessionStorage.getItem('onboardingSeen')) {
            setTimeout(() => {
                document.getElementById('alexOnboarding').classList.add('active');
            }, 600);
        }
    }
});"""

if old_js in js_content:
    js_content = js_content.replace(old_js, new_js)
    with open("js/script-quote.js", "w") as f:
        f.write(js_content)

# 2. Remove alexOnboarding from cotizacion-2.html
with open("cotizacion/cotizacion-2.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")
onboarding = soup.find(id="alexOnboarding")
if onboarding:
    onboarding.decompose()
    with open("cotizacion/cotizacion-2.html", "w") as f:
        f.write(str(soup))
