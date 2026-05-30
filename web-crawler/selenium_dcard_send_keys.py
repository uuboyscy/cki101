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

url = "https://www.dcard.tw/f"

driver.get(url)

time.sleep(3)

driver.find_element(
    by=By.XPATH,
    value='//*[@id="__next"]/div[1]/div/div[1]/div/div/form/input',
).send_keys("攝影")

time.sleep(1)

driver.find_element(
    by=By.XPATH,
    value='//*[@id="__next"]/div[1]/div/div[1]/div/div/form/button[2]',
).click()

time.sleep(10)
