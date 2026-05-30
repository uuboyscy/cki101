import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome

chrome_options = Options()


# chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")

# Configure User Agent
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36")

# Instantiate driver while avoiding automation flag
driver = Chrome(
    options=chrome_options,
    version_main=148,
)

url = "https://www.dcard.tw/f/photography"

driver.get(url)
time.sleep(5)

# Scroll down to a position 5000px from the top
driver.execute_script('var s = document.documentElement.scrollTop=5000')
time.sleep(5)

# Scroll back to the top of the page
driver.execute_script('var s = document.documentElement.scrollTop=0')
time.sleep(5)

driver.execute_script('var s = document.documentElement.scrollTop=10000')
time.sleep(5)

# Retrieve the current HTML string
html = driver.execute_script(
    "return document.getElementsByTagName('html')[0].outerHTML"
)
print(html)