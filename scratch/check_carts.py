import glob
import re

base_dir = '/home/alex-ai/Documents/Workspace/Alex AI Insurtech/Desarrollo/MHM Corredores de seguros/V1 webproject/mhm-corredores-webproject-main/cotizacion'
files = glob.glob(base_dir + '/*-1.html')

for f in files:
    with open(f, 'r') as file:
        content = file.read()
        match = re.search(r"sessionStorage\.setItem\('([^']+)'", content)
        if match:
            print(f"{f.split('/')[-1]}: {match.group(1)}")
        else:
            print(f"{f.split('/')[-1]}: NO SETITEM FOUND")
