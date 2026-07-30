import glob, re, time

print("Updating cache busters in all HTML files...")
html_files = glob.glob('**/*.html', recursive=True)
count = 0
new_v = str(int(time.time()))

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace ?v=1234567890 with ?v=new_v
    new_content = re.sub(r'\?v=\d+', f'?v={new_v}', content)
    
    if new_content != content:
        count += 1
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Updated cache busters in {count} HTML files to ?v={new_v}.")
