from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("http://127.0.0.1:8000/cotizacion/cotizacion-mascota-nueva-1.html")

time.sleep(2)

print("--- CONSOLE LOGS ---")
for entry in driver.get_log('browser'):
    print(entry)

print("--- HTML OF policyList ---")
try:
    elem = driver.find_element("id", "policyList")
    print(elem.get_attribute('outerHTML'))
except Exception as e:
    print("policyList not found:", e)

driver.quit()
