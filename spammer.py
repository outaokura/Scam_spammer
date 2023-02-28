import undetected_chromedriver as uc
import time
import selenium.webdriver.common.keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = uc.ChromeOptions()
options.add_argument("--headless")
driver = uc.Chrome(options=options)
while True:
    driver.get('https://form.run/@gametrade-supportbot')
    emailbox = driver.find_element(By.NAME, "_field_1")
    emailbox.send_keys("a@a.com")
    passwordbox = driver.find_element(By.NAME, "_field_2")
    passwordbox.send_keys("awawa1919!")
    aa = driver.find_elements(By.XPATH, "/html/body/form/div[1]/div/div/div/div[4]/div/div/div/div[2]/button")
    for a in aa:
        a.click()
    driver.delete_all_cookies()
    print("Send")