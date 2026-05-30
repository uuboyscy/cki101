import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless=new")

driver = Chrome(options=chrome_options)

driver.get("https://www.ptt.cc/bbs/index.html")

# time.sleep(3)

driver.find_element(
    by=By.XPATH,
    value='//*[@id="main-container"]/div[2]/div[1]/a',
).click()

# time.sleep(3)

driver.find_element(
    by=By.XPATH,
    value='/html/body/div[2]/form/div[1]/button',
).click()

print(driver.find_element(by=By.TAG_NAME, value='html').text)

cookie = driver.get_cookies()
print(cookie)

# time.sleep(10)
