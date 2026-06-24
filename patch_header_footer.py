import re

# Read index.html to extract correct header and footer
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

# Extract top header aurora + site header
header_match = re.search(r'(<div class="top-header-aurora">.*?</header>)', index_content, re.DOTALL)
if header_match:
    correct_header = header_match.group(1)
    # Fix paths for subdirectory (replace ./ with ../)
    correct_header = correct_header.replace('href="./', 'href="../')
    correct_header = correct_header.replace('src="./', 'src="../')
else:
    print("Error: Could not find header in index.html")
    exit(1)

# Extract footer
footer_match = re.search(r'(<footer class="footer-aurora">.*?</footer>)', index_content, re.DOTALL)
if footer_match:
    correct_footer = footer_match.group(1)
    # Fix paths
    correct_footer = correct_footer.replace('href="./', 'href="../')
    correct_footer = correct_footer.replace('src="./', 'src="../')
else:
    print("Error: Could not find footer in index.html")
    exit(1)

# Read cotizacion-7-1.html
with open("cotizacion/cotizacion-7-1.html", "r", encoding="utf-8") as f:
    cot_content = f.read()

# Replace header in cot_content
cot_content = re.sub(r'<div class="top-header-aurora">.*?</header>', correct_header, cot_content, flags=re.DOTALL)

# Replace footer in cot_content
cot_content = re.sub(r'<footer class="footer-aurora">.*?</footer>', correct_footer, cot_content, flags=re.DOTALL)

# Write back
with open("cotizacion/cotizacion-7-1.html", "w", encoding="utf-8") as f:
    f.write(cot_content)

print("Header and Footer successfully replaced in cotizacion-7-1.html")
