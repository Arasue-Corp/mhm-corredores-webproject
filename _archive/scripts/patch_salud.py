import re

file_path = "cotizacion/cotizacion-salud-1.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the inline layout styles
old_div = '<div class="specs-layout-grid" style="max-width: none; margin-left: 15%; margin-right: 15%; padding: 0;">'
new_div = '<div class="specs-layout-grid salud-layout-container">'
content = content.replace(old_div, new_div)

# 2. Empty the table inline styles in JS
replacements = {
    "const tableStyle = 'width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;';": "const tableStyle = '';",
    "const theadStyle = 'background: #023859; color: white;';": "const theadStyle = '';",
    "const thStyle = 'padding: 12px; border: 1px solid #E2E8F0; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px; text-align: center;';": "const thStyle = '';",
    "const tdStyle = 'padding: 12px; border: 1px solid #E2E8F0; text-align: center;';": "const tdStyle = '';",
    "const tdStyleLimit = 'padding: 12px; border: 1px solid #E2E8F0; text-align: center; color: #4CAF50; font-weight: 600;';": "const tdStyleLimit = '';"
}
for old_code, new_code in replacements.items():
    content = content.replace(old_code, new_code)

# 3. Inject new responsive CSS before </head>
responsive_css = """
    <style>
        .salud-layout-container {
            margin-left: 15%; margin-right: 15%; padding: 0;
        }
        @media (max-width: 1200px) {
            .salud-layout-container {
                margin-left: 5%; margin-right: 5%;
            }
        }
        @media (max-width: 768px) {
            .salud-layout-container {
                margin-left: 16px; margin-right: 16px;
            }
            .veh-type-card {
                padding: 20px !important;
            }
            .veh-type-grid {
                gap: 16px !important;
            }
            .split-btn-container {
                gap: 8px !important;
            }
            .split-btn {
                font-size: 0.85rem !important;
                padding: 8px 4px !important;
            }
            .vt-info h4 {
                font-size: 1.3rem !important;
            }
            .plan-price {
                font-size: 1.5rem !important;
            }
        }

        /* Modal Table Responsive */
        .responsive-table {
            width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;
        }
        .responsive-table thead tr {
            background: #023859; color: white;
        }
        .responsive-table th {
            padding: 12px; border: 1px solid #E2E8F0; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px; text-align: center;
        }
        .responsive-table td {
            padding: 12px; border: 1px solid #E2E8F0; text-align: center;
        }
        .responsive-table td:nth-child(3),
        .responsive-table td:nth-child(4) {
            color: #4CAF50; font-weight: 600;
        }

        @media (max-width: 768px) {
            .responsive-table thead {
                display: none;
            }
            .responsive-table tr {
                display: block;
                margin-bottom: 1rem;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                background: #fff;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            }
            .responsive-table td {
                display: flex;
                justify-content: space-between;
                align-items: center;
                text-align: right !important;
                border: none;
                border-bottom: 1px solid #E2E8F0;
                padding: 12px 16px;
            }
            .responsive-table td:last-child {
                border-bottom: none;
            }
            .responsive-table td::before {
                content: attr(data-label);
                font-weight: 700;
                color: #64748B;
                text-transform: uppercase;
                font-size: 0.75rem;
                margin-right: 15px;
                text-align: left;
                flex-shrink: 0;
                max-width: 50%;
            }
        }
    </style>
</head>
"""

content = content.replace("</head>", responsive_css)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Patch applied successfully.")
