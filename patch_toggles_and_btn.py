import re

html_path = "cotizacion/cotizacion-7-1.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Persona Radios
content = content.replace(
    '<input type="radio" name="correct_p" id="correct_p_yes" value="yes" checked>',
    '<input type="radio" name="correct_p" id="correct_p_yes" value="yes" onchange="toggleContinueBtn()">'
)
content = content.replace(
    '<input type="radio" name="correct_p" id="correct_p_no" value="no">',
    '<input type="radio" name="correct_p" id="correct_p_no" value="no" checked onchange="toggleContinueBtn()">'
)

# 2. Update Empresa Radios
content = content.replace(
    '<input type="radio" name="correct_e" id="correct_e_yes" value="yes" checked>',
    '<input type="radio" name="correct_e" id="correct_e_yes" value="yes" onchange="toggleContinueBtn()">'
)
content = content.replace(
    '<input type="radio" name="correct_e" id="correct_e_no" value="no">',
    '<input type="radio" name="correct_e" id="correct_e_no" value="no" checked onchange="toggleContinueBtn()">'
)

# 3. Update Continue Button and Link
old_button = """<a href="cotizacion-8-1.html" style="text-decoration:none;">
                            <button type="button" class="btn-hero-gradient" id="btnNext" style="cursor:pointer; padding: 12px 32px; font-size: 1.1rem; border-radius: 100px;">
                                Continuar Emisión <i class="fa-solid fa-arrow-right-long"></i>
                            </button>
                        </a>"""

new_button = """<a href="cotizacion-8-1.html" id="linkNext" style="text-decoration:none; pointer-events: none;">
                            <button type="button" class="btn-hero-gradient disabled" id="btnNext" style="cursor:not-allowed; padding: 12px 32px; font-size: 1.1rem; border-radius: 100px; opacity: 0.5;" disabled>
                                Continuar Emisión <i class="fa-solid fa-arrow-right-long"></i>
                            </button>
                        </a>"""

content = content.replace(old_button, new_button)

# 4. Update Trust Seal Text Color
old_db_msg = '<div class="db-msg" style="margin-top: 0.5rem; font-size: 0.85rem;">Tus datos son procesados bajo estrictos estándares bancarios de encriptación.</div>'
new_db_msg = '<div class="db-msg" style="margin-top: 0.5rem; font-size: 0.85rem; color: #334155;">Tus datos son procesados bajo estrictos estándares bancarios de encriptación.</div>'
content = content.replace(old_db_msg, new_db_msg)

# 5. Add toggleContinueBtn Function
js_function = """function toggleContinueBtn() {
    const isPersona = document.getElementById('panel-persona').classList.contains('active');
    const btnNext = document.getElementById('btnNext');
    const linkNext = document.getElementById('linkNext');
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
        linkNext.style.pointerEvents = 'auto';
    } else {
        btnNext.disabled = true;
        btnNext.classList.add('disabled');
        btnNext.style.cursor = 'not-allowed';
        btnNext.style.opacity = '0.5';
        linkNext.style.pointerEvents = 'none';
    }
}

// Call on load and on entity switch
document.addEventListener("DOMContentLoaded", toggleContinueBtn);
"""

if "function toggleContinueBtn()" not in content:
    content = content.replace('</script>', js_function + '\n</script>')

# 6. Call toggleContinueBtn() inside switchEntityToggle so it updates when switching
if "toggleContinueBtn();" not in content:
    content = content.replace("if (sideIndicator) sideIndicator.innerText = \"Contratante Empresa\";", "if (sideIndicator) sideIndicator.innerText = \"Contratante Empresa\";\n        toggleContinueBtn();")
    content = content.replace("if (sideIndicator) sideIndicator.innerText = \"Contratante Persona\";", "if (sideIndicator) sideIndicator.innerText = \"Contratante Persona\";\n        toggleContinueBtn();")


with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updates completed successfully")
