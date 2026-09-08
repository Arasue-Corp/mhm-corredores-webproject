import glob, re

print("Removing height: 0 from floating-menu-container...")
html_files = glob.glob('**/*.html', recursive=True)
count = 0

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will regex replace the block
    pattern = r'#floating-menu-container\s*\{\s*height:\s*0\s*!important;\s*overflow:\s*visible\s*!important;\s*display:\s*block\s*!important;\s*\}'
    
    new_content = re.sub(pattern, '', content)
    
    if new_content != content:
        count += 1
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Fixed {count} HTML files.")
