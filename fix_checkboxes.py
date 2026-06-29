import re

with open("cotizacion/cotizacion-mascota-1.html", "r", encoding="utf-8") as f:
    c = f.read()

# Add CSS
custom_css = """
        /* Custom Checkbox */
        .custom-chk {
            appearance: none;
            -webkit-appearance: none;
            width: 20px;
            height: 20px;
            border: 2px solid #CBD5E1;
            border-radius: 5px;
            background-color: white;
            cursor: pointer;
            position: relative;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            flex-shrink: 0;
            margin: 0;
        }
        .custom-chk:checked {
            background-color: #2ED9C3;
            border-color: #2ED9C3;
        }
        .custom-chk:checked::after {
            content: '';
            position: absolute;
            width: 5px;
            height: 10px;
            border: solid white;
            border-width: 0 2px 2px 0;
            transform: rotate(45deg);
            margin-top: -2px;
        }
    </style>"""

c = c.replace("</style>", custom_css, 1)

# Replace inline styles with class
c = c.replace(
    'id="chk-terms" onchange="validateForm()" style="width: 20px; height: 20px; accent-color: #2ED9C3;"',
    'id="chk-terms" onchange="validateForm()" class="custom-chk"'
)
c = c.replace(
    'id="chk-legal" onchange="validateForm()" style="width: 20px; height: 20px; accent-color: #2ED9C3;"',
    'id="chk-legal" onchange="validateForm()" class="custom-chk"'
)

with open("cotizacion/cotizacion-mascota-1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Custom checkboxes with white checkmarks applied.")
