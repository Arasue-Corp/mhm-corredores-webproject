import glob, re, os

print("Fixing garbage HTML in cotizacion funnels...")
html_files = glob.glob('cotizacion/cotizacion-*.html')
count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find <div class="c-slide" data-step="2"> and remove everything until <!-- Modal Leads -->
    # We use re.sub
    new_content = re.sub(r'<div class="c-slide" data-step="2">[\s\S]*?(?=<!-- Modal Leads -->)', '', content)
    
    if new_content != content:
        count += 1
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Cleaned garbage in {count} HTML files.")

print("Adding .card-popover CSS...")
style_path = 'css/style.css'
with open(style_path, 'a', encoding='utf-8') as f:
    f.write("""
/* FIX POPOVER WHITE SPACE ISSUE */
.card-popover {
    position: absolute;
    background: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    z-index: 1000;
    pointer-events: none;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease;
}
.card-popover.visible {
    opacity: 1;
    visibility: visible;
}
.popover-tag { font-size: 0.7rem; color: #796bfc; font-weight: bold; text-transform: uppercase; display: block; margin-bottom: 5px; }
.popover-title { font-size: 1rem; font-weight: 800; color: #1E293B; margin: 0 0 5px 0; }
.popover-desc { font-size: 0.85rem; color: #64748B; margin: 0; line-height: 1.4; }
""")
print("Done!")
