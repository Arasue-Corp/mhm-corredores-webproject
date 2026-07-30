import glob, os, re

css_fix = """
/* ---- REDESIGN UX/UI FIX CARDS WIDTH & FOOTER ---- */
.veh-type-card {
    max-width: 380px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}

.footer-logo-img {
    height: auto !important;
    max-width: 180px !important;
    object-fit: contain !important;
    display: block !important;
}

#floating-menu-container {
    height: 0 !important;
    overflow: visible !important;
    display: block !important;
}

/* Ensure html and body don't have extra bottom margin */
html, body {
    margin: 0 !important;
    padding: 0 !important;
}
/* ---- END REDESIGN FIX ---- */
"""

files = glob.glob('cotizacion/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicate injection
    if '/* ---- REDESIGN UX/UI FIX CARDS WIDTH & FOOTER ---- */' in content:
        content = re.sub(r'/\* ---- REDESIGN UX/UI FIX CARDS WIDTH & FOOTER ---- \*/.*?/\* ---- END REDESIGN FIX ---- \*/', '', content, flags=re.DOTALL)
    
    content = content.replace('</style>', css_fix + '\n</style>', 1)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {file}")
