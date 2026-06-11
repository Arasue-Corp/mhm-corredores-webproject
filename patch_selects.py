import os
import re

def patch_file(filepath, replacements):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content, flags=re.MULTILINE)
        
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Patched {filepath}")
    else:
        print(f"No changes made to {filepath}")

quote_js = 'js/script-quote.js'
script_js = 'js/script.js'
html_file = 'cotizacion/cotizacion-14.html'

# 1. Update script-quote.js
quote_replacements = [
    # Replace <select class="rich-input validate-req"
    (r'<select class="rich-input validate-req"', r'<select class="rich-input validate-req premium-select"'),
    # Replace <select class="rich-input"
    (r'<select class="rich-input"(?!.*premium-select)', r'<select class="rich-input premium-select"'),
    
    # Add initPremiumSelects() after adding new car
    (r'(container\.appendChild\(newPanel\);\s*\n\s*populateLists\(newId\);)', r'\1\n        if (typeof initPremiumSelects === "function") initPremiumSelects();'),
    
    # Add initPremiumSelects() after adding new driver
    (r'(driverContainer\.appendChild\(newPanel\);\s*\n\s*updateNavVisibilityDrivers\(\);\s*\n\s*switchTabDrivers\(`driver-\$\{newId\}`,\s*newTab\);)', r'\1\n        if (typeof initPremiumSelects === "function") initPremiumSelects();')
]

# 2. Update script.js
script_replacements = [
    # Add initPremiumSelects() after adding loss incident
    (r'(lossContainer\.insertAdjacentHTML\(\'beforeend\', html\);)', r'\1\n                    if (typeof initPremiumSelects === "function") initPremiumSelects();'),
]

# 3. Update cotizacion-14.html
html_replacements = [
    (r'<select class="rich-input" id="countryCode">', r'<select class="rich-input premium-select" id="countryCode">')
]

patch_file(quote_js, quote_replacements)
patch_file(script_js, script_replacements)
patch_file(html_file, html_replacements)

