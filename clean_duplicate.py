with open('cotizacion/cotizacion-escolar-5.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The clean content ends at line 522/523.
# The script starts at line 822.
# We want to keep up to line 523 (which is index 522), and then keep from line 822 (which is index 821) to the end.
# Let's verify by printing a few lines around these indices.

# Let's just find the exact boundaries by string matching to be safe.
# Find the end of cross-sell-wrapper
# Which is followed by </div>\n        </div>\n</div>\n    </div>
start_del_idx = -1
end_del_idx = -1

for i, line in enumerate(lines):
    if '<div class="aurora-border-glow"></div>' in line and i > 500:
        start_del_idx = i
        break

for i in range(start_del_idx, len(lines)):
    if '<script>' in lines[i] and 'document.addEventListener' in lines[i+1]:
        end_del_idx = i
        break

if start_del_idx != -1 and end_del_idx != -1:
    new_lines = lines[:start_del_idx] + lines[end_del_idx:]
    with open('cotizacion/cotizacion-escolar-5.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Deleted from line {start_del_idx} to {end_del_idx}")
else:
    print("Could not find boundaries")
