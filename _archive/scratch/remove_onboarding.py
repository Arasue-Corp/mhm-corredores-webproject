import os
import re

html_files = [
    'cotizacion-asistencia-ciclista-1.html',
    'cotizacion-asistencia-hogar-1.html',
    'cotizacion-escolar-1.html',
    'cotizacion-mascota-1.html',
    'cotizacion-salud-1.html',
    'cotizacion-vehicular-1.html'
]

onboarding_regex = r'<div id="alexOnboarding".*?<!-- END ONBOARDING -->|<!-- MODAL ONBOARDING -->.*?<div id="alexOnboarding".*?</div>\s*</div>\s*</div>\s*</div>'

for file_name in html_files:
    path = os.path.join('cotizacion', file_name)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the onboarding div explicitly if regex misses
    start_str = '<div id="alexOnboarding"'
    if start_str in content:
        start_idx = content.find(start_str)
        # Assuming the onboarding block ends before the <script> tags or at a specific comment
        # Let's find the close of the overlay
        end_str = 'function closeWelcomeOnboarding()'
        
        # We also need to remove the JS function closeWelcomeOnboarding
        js_regex = r'function closeWelcomeOnboarding\(\)\s*\{.*?\}'
        
        # Just remove the block by extracting it
        # Actually, let's use a robust approach:
        # We know it starts at <div id="alexOnboarding" class="crystal-overlay">
        # And it's an overlay div containing the modal.
        # We can remove lines from <div id="alexOnboarding" to its matching </div>.
        
        # A simpler way is to just hide it via CSS in the files or replace the display logic.
        # But user wants to "elimina el onboarding" (remove it).
        pass

    # A better way to delete:
    # <div id="alexOnboarding" class="crystal-overlay">
    # ... everything inside ...
    # </div> (the overlay close)
    
    # We can match up to the next <div class="step-container"> or similar.
    # Let's just find <div id="alexOnboarding" and the next <script> tag.
    new_content = re.sub(r'<div id="alexOnboarding" class="crystal-overlay">.*?</div>\s*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # Also remove JS function if it exists
    new_content = re.sub(r'function closeWelcomeOnboarding\(\)\s*\{.*?\}', '', new_content, flags=re.DOTALL)
    
    # And remove window.onload if it opens the modal
    new_content = re.sub(r'window\.onload\s*=\s*function\(\)\s*\{\s*setTimeout\(function\(\)\s*\{\s*document\.getElementById\(\'alexOnboarding\'\)\.style\.display\s*=\s*\'flex\';\s*\},\s*500\);\s*\};', '', new_content, flags=re.DOTALL)

    # In case there are other variations
    new_content = re.sub(r'document\.getElementById\(\'alexOnboarding\'\)\.style\.display\s*=\s*\'flex\';', '', new_content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('Done')
