import glob, re

css_addition = """
/* --- CRITICAL FIX FOR MOBILE POPUPS SQUISHING --- */
#floating-menu-container, #floating-chat-container {
    overflow: visible !important;
}
.nav-command-center {
    width: 290px !important;
    min-width: 290px !important;
    max-width: 90vw !important;
    right: 0 !important;
}
.alex-chat-window {
    width: 360px !important;
    min-width: 360px !important;
    max-width: 90vw !important;
    right: 0 !important;
}
@media (max-width: 768px) {
    .nav-command-center {
        width: 280px !important;
        min-width: 280px !important;
    }
    .alex-chat-window {
        width: 320px !important;
        min-width: 320px !important;
    }
}
"""

print("Appending CSS fixes...")
for css_file in ['css/style.css', 'css/style-quote.css']:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write('\n' + css_addition)

print("Updating cache buster...")
import time
new_v = str(int(time.time()))

html_files = glob.glob('**/*.html', recursive=True)
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update cache buster
    new_content = re.sub(r'(\.css\?v=)\d+', r'\g<1>' + new_v, content)
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Fixes applied and cache buster updated!")
