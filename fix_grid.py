import re

with open("cotizacion/cotizacion-9-1.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the grid container entirely
content = content.replace(
    '<div class="payer-data-grid" style="grid-template-columns: 1fr;">',
    '<div class="payer-data-grid" style="display: flex; flex-direction: column !important; width: 100%; gap: 15px;">'
)

# Also ensure dashboard grid is split correctly
content = content.replace(
    '<div class="dashboard-grid-main mb-5" style="grid-template-columns: 1fr 1fr;">',
    '<div class="dashboard-grid-main mb-5" style="display: grid; grid-template-columns: 1fr 1fr !important; gap: 20px;">'
)

# And add a style tag at the end just to be nuclear about it
nuclear_css = """
<style>
.payer-data-grid {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
}
.pd-item {
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: stretch !important;
}
.pd-input {
    width: 100% !important;
    box-sizing: border-box !important;
}
.dashboard-grid-main {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
}
@media(max-width: 768px) {
    .dashboard-grid-main {
        grid-template-columns: 1fr !important;
    }
}
</style>
"""

content = content.replace("</head>", nuclear_css + "\n</head>")

with open("cotizacion/cotizacion-9-1.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Nuclear fix applied.")
