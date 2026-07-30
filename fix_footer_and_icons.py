import os
import glob
import re

print("Starting fixes...")

# 1. Remove welcome-onboarding-overlay from all cotizacion*.html
html_files = glob.glob('cotizacion/cotizacion*.html')
count_overlay = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to remove the welcome-onboarding-overlay div and everything inside it up to its closing tag
    # The overlay usually starts with <div class="welcome-onboarding-overlay" id="welcomeOnboarding">
    # and ends after the c-footer.
    # It's better to just search for the start and find the matching end.
    
    if 'welcome-onboarding-overlay' in content:
        count_overlay += 1
        # Simple extraction: find the index
        start_idx = content.find('<div class="welcome-onboarding-overlay"')
        if start_idx != -1:
            # We need to find the matching closing div.
            # We can count <div> and </div>
            div_count = 0
            i = start_idx
            while i < len(content):
                if content[i:i+4] == '<div':
                    div_count += 1
                elif content[i:i+6] == '</div>':
                    div_count -= 1
                    if div_count == 0:
                        end_idx = i + 6
                        # Remove it!
                        content = content[:start_idx] + content[end_idx:]
                        break
                i += 1
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print(f"Removed welcome-onboarding-overlay from {count_overlay} HTML files.")

# 2. Fix the footer logo in style.css
style_path = 'css/style.css'
with open(style_path, 'r', encoding='utf-8') as f:
    style = f.read()

# Replace footer-logo-img
old_logo = """.footer-logo-img {
    height: 8vh; /* Ajusta esta altura seggn el diseo de tu logo */
    width: auto; /* Mantiene la proporcin */
    display: block; /* Evita espacios extra debajo de la imagen */"""
new_logo = """.footer-logo-img {
    height: 60px; 
    max-width: 100%; 
    object-fit: contain; 
    display: block;"""

if old_logo in style:
    style = style.replace(old_logo, new_logo)
else:
    # Use regex
    style = re.sub(r'\.footer-logo-img\s*\{[^}]+\}', '.footer-logo-img {\n    height: 60px;\n    max-width: 100%;\n    object-fit: contain;\n    display: block;\n}', style)

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(style)
print("Fixed footer-logo-img in style.css")

# 3. Fix the overlapping buttons in style-quote.css and style.css
# In style-quote.css we have some !important bottoms
quote_path = 'css/style-quote.css'
if os.path.exists(quote_path):
    with open(quote_path, 'r', encoding='utf-8') as f:
        quote_style = f.read()
    
    # Let's just enforce a solid distance for these IDs at the end of both files
    append_css = """
/* ENFORCE FLOATING BUTTON POSITIONS TO PREVENT OVERLAP */
@media (max-width: 1200px) {
    #floating-chat-container { bottom: 120px !important; z-index: 9999 !important; }
    #floating-menu-container { bottom: 200px !important; z-index: 9998 !important; }
}
@media (max-width: 768px) {
    #floating-chat-container { bottom: 110px !important; }
    #floating-menu-container { bottom: 190px !important; }
}
"""
    with open(quote_path, 'a', encoding='utf-8') as f:
        f.write(append_css)
    with open(style_path, 'a', encoding='utf-8') as f:
        f.write(append_css)
    print("Added enforce CSS for floating buttons to prevent overlap.")

print("Done!")
