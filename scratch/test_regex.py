import re

with open('cotizacion/cotizacion-mascota-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's see if we can find the qty-controls
print("Finding qty-controls block...")
matches = re.finditer(r'(<div class="qty-controls">.*?</div>)\s*(<button[^>]+>.*?</button>)', content, flags=re.DOTALL)
count = 0
for m in matches:
    print(f"Match found:\n{m.group(0)[:100]}...\n")
    count += 1
print(f"Total matches: {count}")

# Check if card-actions-row exists
print("Card actions row present:", "card-actions-row" in content)
