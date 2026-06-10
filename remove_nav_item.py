import os
import re

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match the line containing "Cotizar seguro" inside an <li>
    pattern = re.compile(r'^\s*<li><a[^>]*>Cotizar seguro</a></li>\r?\n', re.MULTILINE)
    
    new_content, count = pattern.subn('', content)
    
    if count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path} (removed {count} occurrences)")

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
