import re
import glob
import json

files = [
    "cotizacion/cotizacion-1.html",
    "cotizacion/cotizacion-3-1.html",
    "cotizacion/cotizacion-4-1.html",
    "cotizacion/cotizacion-5-1.html",
    "cotizacion/cotizacion-6-1.html",
    "cotizacion/cotizacion-7-1.html",
    "cotizacion/cotizacion-8-1.html",
    "cotizacion/cotizacion-9-1.html",
    "cotizacion/cotizacion-10-1-fid.html"
]

results = {}

for f in files:
    try:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            
            # Find Next Link
            next_match = re.search(r'id="btnNext"([^>]*)(onclick="window\.location\.href=\'([^\']+)\'|href="([^"]+)")?', content)
            if not next_match:
                next_match = re.search(r'<a[^>]+id="linkNext"[^>]*href="([^"]+)"', content)
            
            # This regex is messy, let's just do a simple search for hrefs of Next buttons
            btn_next_block = re.search(r'id="btnNext"[^>]*>', content)
            link_next_block = re.search(r'id="linkNext"[^>]*href="([^"]+)"', content)
            
            next_link = "Not Found"
            if link_next_block:
                next_link = link_next_block.group(1)
            elif btn_next_block and 'onclick="window.location.href=' in btn_next_block.group(0):
                m = re.search(r'onclick="window\.location\.href=\'([^\']+)\'', btn_next_block.group(0))
                if m: next_link = m.group(1)

            # Back link
            back_block = re.search(r'id="linkBack"[^>]*href="([^"]+)"', content)
            back_link = back_block.group(1) if back_block else "Not Found"

            # AI Tip
            tip_block = re.search(r'<p class="chatbot-message"[^>]*>(.*?)</p>', content, re.DOTALL)
            tip = tip_block.group(1).strip() if tip_block else "Not Found"

            # Progress Bar Step
            # e.g., <div class="step-icon active"> or percentage
            # Let's search for "Paso X de Y" or active steps
            step_matches = re.findall(r'<div class="step-text[^"]*">(.*?)</div>', content)
            steps = [s.strip() for s in step_matches]

            results[f.split('/')[-1]] = {
                "back_link": back_link,
                "next_link": next_link,
                "tip": re.sub(r'<[^>]+>', '', tip)[:100].replace('\n', ' '), # Clean HTML tags and truncate
                "steps": steps
            }
    except Exception as e:
        results[f.split('/')[-1]] = str(e)

print(json.dumps(results, indent=2))
