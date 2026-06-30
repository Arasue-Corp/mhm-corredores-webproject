import re
import os

def replace_section(content, section_name, start_tag, end_tag, new_content):
    pattern = re.compile(rf"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
    if not pattern.search(content):
        print(f"Warning: {section_name} not found in target file.")
        return content
    return pattern.sub(new_content.replace('\\', '\\\\'), content, count=1)

def main():
    root_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main'
    index_path = os.path.join(root_dir, 'index.html')
    terms_path = os.path.join(root_dir, 'terminos-condiciones/index.html')

    with open(index_path, 'r', encoding='utf-8') as f:
        index_html = f.read()

    with open(terms_path, 'r', encoding='utf-8') as f:
        terms_html = f.read()

    # Extract sections from index.html
    # Top header
    top_header_match = re.search(r'(<div class="top-header-aurora">.*?</div>\s*)<header', index_html, re.DOTALL)
    top_header = top_header_match.group(1) if top_header_match else ''

    # Header
    header_match = re.search(r'(<header class="site-header glass-navbar">.*?</header>)', index_html, re.DOTALL)
    header = header_match.group(1) if header_match else ''

    # Footer
    footer_match = re.search(r'(<footer class="footer-aurora">.*?</footer>)', index_html, re.DOTALL)
    footer = footer_match.group(1) if footer_match else ''

    # Floating menu
    floating_menu_match = re.search(r'(<div id="floating-menu-container">.*?</div>\s*)<div id="floating-chat-container">', index_html, re.DOTALL)
    floating_menu = floating_menu_match.group(1) if floating_menu_match else ''
    
    # In case floating menu match failed due to different structure, try simpler match
    if not floating_menu:
        floating_menu_match = re.search(r'(<div id="floating-menu-container">.*?</div>\s*)\n\s*<div', index_html, re.DOTALL)
        if floating_menu_match:
            floating_menu = floating_menu_match.group(1)

    # Floating chat
    floating_chat_match = re.search(r'(<div id="floating-chat-container">.*?</div>)', index_html, re.DOTALL)
    floating_chat = floating_chat_match.group(1) if floating_chat_match else ''

    def fix_paths(html):
        # Replace href="./ or src="./ with ../
        # and href="filename.html" with ../filename.html where appropriate
        # To be safe, just replace "./" with "../"
        html = html.replace('href="./', 'href="../')
        html = html.replace('src="./', 'src="../')
        
        # also fix naked paths like href="cotizacion/cotizacion.html" to href="../cotizacion/cotizacion.html"
        html = re.sub(r'href="((?!http|#|\.\./).*?)"', r'href="../\1"', html)
        # remove double slashes like ../../ except if they were valid
        html = html.replace('../../', '../') # A bit hacky but index.html only has 1 level down
        return html

    top_header = fix_paths(top_header)
    header = fix_paths(header)
    footer = fix_paths(footer)
    floating_menu = fix_paths(floating_menu)
    floating_chat = fix_paths(floating_chat)
    
    # The fix_paths might break "index.html" to "../index.html", which is actually correct for a subfolder!
    
    # Replace in terms_html
    # We will use regex to find the corresponding blocks
    
    # Replace top header
    terms_html = re.sub(r'<div class="top-header-aurora">.*?</div>\s*(?=<header)', top_header, terms_html, flags=re.DOTALL)
    
    # Replace header
    terms_html = re.sub(r'<header class="site-header glass-navbar">.*?</header>', header, terms_html, flags=re.DOTALL)
    
    # Replace footer
    terms_html = re.sub(r'<footer class="footer-aurora">.*?</footer>', footer, terms_html, flags=re.DOTALL)
    
    # Replace floating menu
    terms_html = re.sub(r'<div id="floating-menu-container">.*?</div>\s*(?=<div id="floating-chat-container">)', floating_menu, terms_html, flags=re.DOTALL)
    
    # Replace floating chat
    terms_html = re.sub(r'<div id="floating-chat-container">.*?</div>', floating_chat, terms_html, flags=re.DOTALL)

    # Update head links for consistency
    # (Optional, but let's just make sure title is somewhat correct)
    
    with open(terms_path, 'w', encoding='utf-8') as f:
        f.write(terms_html)

    print("Terms and conditions page updated successfully.")

if __name__ == '__main__':
    main()
