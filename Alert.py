import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("/Users/ankshrivastav/PycharmProjects/Selenium_Projects/drivers/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='content']/ul/li[29]/a").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
time.sleep(1)

alert_obj = driver.switch_to.alert
alert_text = alert_obj.text
time.sleep(1)
print('Alert text . . .', alert_text)
alert_obj.send_keys("Dummy Text")
time.sleep(1)
alert_obj.accept()

time.sleep(2)

driver.quit()
