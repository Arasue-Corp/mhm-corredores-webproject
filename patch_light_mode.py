import re

html_path = "cotizacion/cotizacion-7-1.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace quoteFormStep7 background
content = content.replace(
    'class="premium-white-card" id="quoteFormStep7" style="background: rgba(15, 15, 26, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.05);"',
    'class="premium-white-card" id="quoteFormStep7" style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px); border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.03);"'
)

# Replace row-switch-container backgrounds
content = content.replace(
    'class="row-switch-container compact" style="background: rgba(255,255,255,0.02); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05);"',
    'class="row-switch-container compact" style="background: rgba(0,0,0,0.02); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(0,0,0,0.05);"'
)

# Replace white text in sl-title
content = content.replace(
    'class="sl-title" style="font-size:1.2rem; color:#fff;"',
    'class="sl-title" style="font-size:1.2rem; color:var(--text-dark, #333);"'
)

# Replace hero-action-area border
content = content.replace(
    'class="hero-action-area mt-5" style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 1.5rem;"',
    'class="hero-action-area mt-5" style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 1.5rem;"'
)

# Replace organic-panel in sidebar
content = content.replace(
    'class="organic-panel" style="background: rgba(20, 20, 30, 0.7); backdrop-filter: blur(15px);"',
    'class="organic-panel" style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.03);"'
)

# Also fix the tabs (if they have white text, they inherit, but let's make sure they are not dark)
# Let's write the modified content
with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Dark mode inline styles removed!")
