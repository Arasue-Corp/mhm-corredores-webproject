import os
import glob
import re

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'
files = glob.glob(os.path.join(base_dir, 'cotizacion-*.html'))

# Regex to find <style> blocks
style_pattern = re.compile(r'<style>(.*?)</style>', re.DOTALL | re.IGNORECASE)

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Find all style blocks
    def replacer(match):
        inner_css = match.group(1)
        # If it has the specs-layout-grid media query, strip it!
        if '@media' in inner_css and 'specs-layout-grid' in inner_css:
            return '' # strip the whole block
        # Maybe strip any other inline media queries to centralize them?
        if '@media (max-width: 900px)' in inner_css and 'wizard-container' in inner_css:
             return ''
        return match.group(0) # Keep it

    new_content = style_pattern.sub(replacer, content)
    
    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Stripped inline responsive style from {os.path.basename(filepath)}")

print("Done stripping.")
