import os
import re
import time

timestamp = str(int(time.time()))

def update_cache_busters(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()
                
                # Replace existing ?v=... with new timestamp
                content = re.sub(r'(\.css|\.js)(\?v=[0-9]+)?', r'\1?v=' + timestamp, content)
                
                with open(filepath, 'w') as f:
                    f.write(content)

# Run on root and cotizacion folder
update_cache_busters('.')
print("Cache busters updated to version " + timestamp)
