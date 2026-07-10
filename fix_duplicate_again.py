with open('cotizacion/cotizacion-escolar-5.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# lines[0] to lines[694] correspond to line 1 to 695 in view_file.
# lines[1060] corresponds to line 1061 in view_file which is <script>.

new_lines = lines[:695] + ['        </div>\n', '        </div>\n'] + lines[1060:]

with open('cotizacion/cotizacion-escolar-5.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Cleanup complete.")
