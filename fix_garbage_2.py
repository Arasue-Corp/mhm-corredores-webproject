import glob, re, os

print("Fixing remaining garbage HTML in cotizacion funnels...")
html_files = glob.glob('cotizacion/cotizacion*.html')
count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if there is <div class="c-slide" data-step="2">
    if '<div class="c-slide" data-step="2">' in content:
        # Regex to remove everything from <div class="c-slide" data-step="2"> until the end of the file except </body></html>
        # We can just split by <div class="c-slide" data-step="2">, take the first part, and add </body>\n</html>
        
        parts = content.split('<div class="c-slide" data-step="2">')
        new_content = parts[0].strip()
        
        # If the file originally had <!-- Modal Leads -->, we might have just deleted it, but wait, those were already fixed by the first script!
        # The remaining ones are the ones WITHOUT <!-- Modal Leads -->.
        # Let's just append the closing tags.
        new_content += '\n</body>\n</html>\n'
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Cleaned garbage in {count} HTML files.")
