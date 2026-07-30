import os, glob, re

files = glob.glob('cotizacion/*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We use a loop or re.sub. We must be careful not to wrap already wrapped ones.
    if '<div class="card-actions-row">' not in content:
        content = re.sub(
            r'(<div class="qty-controls">.*?</div>)\s*(<button[^>]+>.*?</button>)',
            r'<div class="card-actions-row">\n\1\n\2\n</div>',
            content,
            flags=re.DOTALL
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Processed HTML for {file}")
    else:
        print(f"Already processed HTML for {file}")
