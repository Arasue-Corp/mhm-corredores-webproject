import os
import re

file_path = "cotizacion/cotizacion-salud-5.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the modal HTML
modal_start = content.find('<!-- Beneficiary Modal HTML -->')
if modal_start == -1:
    print("Modal not found")
    exit(1)

# Find the end of the modal HTML
# The modal ends with </div> just before </div></div>
# Let's extract it carefully by finding the next </div>\n                    </div>\n                </div>
# Actually, the modal is:
# <!-- Beneficiary Modal HTML -->
# <div id="beneficiaryModal" ...>
# ...
# </div>
# </div> (this closes premium-white-card)

modal_pattern = re.compile(r'(<!-- Beneficiary Modal HTML -->.*?</div>\s*</div>\s*</div>)', re.DOTALL)
match = modal_pattern.search(content)

if match:
    modal_html = match.group(1)
    # Remove it from its current location
    content = content.replace(modal_html, '')
    
    # Put it before <script> at the bottom
    script_pos = content.find('<script>')
    if script_pos != -1:
        content = content[:script_pos] + modal_html + '\n    ' + content[script_pos:]
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Modal moved to the bottom of the body.")
    else:
        print("Script tag not found")
else:
    print("Modal pattern not found")
