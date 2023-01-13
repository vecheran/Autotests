from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()

    alert = browser.switch_to.alert
    code = alert.text.split(': ')[-1]

finally:
    time.sleep(10)
    browser.quit()
    print(code)
