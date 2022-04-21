import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def button_clicks():
    btn_button_clicks = driver.find_element(By.XPATH, "//*[@id='button-clicks']/div/div[1]/h1")
    btn_button_clicks.click()

    win_handles = driver.window_handles
    driver.switch_to.window(win_handles[1])

    driver.find_element(By.XPATH, "//p[text()='CLICK ME!']").click()
    driver.find_element(By.XPATH, "//*[@id='myModalClick']/div/div/div[3]/button").click()
    # Alert(driver).dismiss()

    # btn_js_button = driver.find_element_by_id("button2")
    btn_js_button = driver.find_element(by=By.ID, value="button2")
    driver.execute_script("arguments[0].click();", btn_js_button)
    driver.find_element(By.XPATH, "//*[@id='myModalJSClick']/div/div/div[3]/button").click()

    btn_js_button = driver.find_element(By.ID, "button3")
    driver.execute_script("arguments[0].click();", btn_js_button)
    driver.find_element(By.XPATH, "//*[@id='myModalMoveClick']/div/div/div[3]/button").click()
    driver.close()
    driver.switch_to.window(win_handles[0])


def dropdown_checkbox_radoibuttons():
    btn_dropdown_checkbox_radiobuttons = driver.find_element(By.XPATH,
                                                             "//h1[text()='DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)']")
    btn_dropdown_checkbox_radiobuttons.click()

    win_handles = driver.window_handles
    driver.switch_to.window(win_handles[1])

    # populating dropdowns
    sel_lang = Select(driver.find_element(By.ID, "dropdowm-menu-1"))
    sel_lang.select_by_visible_text("Python")
    sel_tool = Select(driver.find_element(By.ID, "dropdowm-menu-2"))
    sel_tool.select_by_visible_text("Maven")
    sel_front_end = Select(driver.find_element(By.ID, "dropdowm-menu-3"))
    sel_front_end.select_by_visible_text("JavaScript")

    # checking checkboxes
    driver.find_element(By.XPATH, "//input[@value='option-1']").click()
    driver.find_element(By.XPATH, "//input[@value='option-2']").click()
    driver.find_element(By.XPATH, "//input[@value='option-2']").click()

    # checking radio-buttons
    driver.find_element(By.XPATH, "//input[@value='green']")
    driver.find_element(By.XPATH, "//input[@value='blue']")
    driver.find_element(By.XPATH, "//input[@value='yellow']")
    driver.find_element(By.XPATH, "//input[@value='orange']")
    driver.find_element(By.XPATH, "//input[@value='purple']")
    driver.close()
    driver.switch_to.window(win_handles[0])


def scrolling_around():
    driver.find_element(By.XPATH, "//h1[text()='SCROLLING AROUND']").click()

    win_handles = driver.window_handles
    driver.switch_to.window(win_handles[1])

    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID, "zone1"))
    action.move_to_element(driver.find_element(By.ID, "zone2-entries"))
    action.move_to_element(driver.find_element(By.ID, "zone3-entries"))

    driver.close()
    driver.switch_to.window(win_handles[0])


def to_do_list():
    time.sleep(1)
    driver.find_element(By.XPATH, "//h1[text()='TO DO LIST']").click()

    win_handles = driver.window_handles
    driver.switch_to.window(win_handles[1])

    driver.find_element(By.XPATH, "// *[text() = ' Go to potion class']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "// *[text() = ' Buy new robes").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "// *[text() = ' Practice magic").click()

    driver.close()
    driver.switch_to.window(win_handles[0])


s = Service('/Users/ankshrivastav/PycharmProjects/Selenium_Projects/drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(2)
driver.get('https://webdriveruniversity.com/')
driver.maximize_window()

button_clicks()
dropdown_checkbox_radoibuttons()
scrolling_around()
to_do_list()

driver.quit()
