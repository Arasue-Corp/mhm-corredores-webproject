import re

with open("cotizacion/cotizacion-7-1.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Clean up duplicated scripts
content = re.sub(r'<script src="([^"]+)">.*?</script>', r'<script src="\1"></script>', content, flags=re.DOTALL)

# 2. Re-insert the proper bottom script without duplicates
# The bottom script already has toggleContinueBtn and switchEntityToggle, so we leave it alone.
# Wait, let's verify if the bottom script is intact. 
# It looks like: <script>\n\nfunction switchEntityToggle...
# That was not a <script src="..."> so it wasn't affected by the above regex.

# 3. Replace the button and anchor tag
old_btn = """<a href="cotizacion-8-1.html" id="linkNext" style="text-decoration:none; pointer-events: none;">
                            <button type="button" class="btn-hero-gradient disabled" id="btnNext" style="cursor:not-allowed; padding: 12px 32px; font-size: 1.1rem; border-radius: 100px; opacity: 0.5;" disabled>
                                Continuar Emisión <i class="fa-solid fa-arrow-right-long"></i>
                            </button>
                        </a>"""

new_btn = """<button type="button" class="btn-hero-gradient disabled" id="btnNext" style="cursor:not-allowed; padding: 12px 32px; font-size: 1.1rem; border-radius: 100px; opacity: 0.5;" disabled onclick="window.location.href='cotizacion-8-1.html'">
                                Continuar Emisión <i class="fa-solid fa-arrow-right-long"></i>
                            </button>"""
content = content.replace(old_btn, new_btn)

# 4. Update the toggleContinueBtn function to not use linkNext
# Since we removed linkNext, we must remove it from the JS so it doesn't throw a null reference error.
new_js = """function toggleContinueBtn() {
    const isPersona = document.getElementById('panel-persona').classList.contains('active');
    const btnNext = document.getElementById('btnNext');
    let isYesChecked = false;
    
    if (isPersona) {
        isYesChecked = document.getElementById('correct_p_yes').checked;
    } else {
        isYesChecked = document.getElementById('correct_e_yes').checked;
    }
    
    if (isYesChecked) {
        btnNext.disabled = false;
        btnNext.classList.remove('disabled');
        btnNext.style.cursor = 'pointer';
        btnNext.style.opacity = '1';
    } else {
        btnNext.disabled = true;
        btnNext.classList.add('disabled');
        btnNext.style.cursor = 'not-allowed';
        btnNext.style.opacity = '0.5';
    }
}"""

content = re.sub(r'function toggleContinueBtn\(\) \{.*?\n\}', new_js, content, flags=re.DOTALL)

with open("cotizacion/cotizacion-7-1.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed button navigation in 7-1")
