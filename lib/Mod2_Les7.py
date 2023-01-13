from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # v = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.TAG_NAME, "button").click()

    # print(y)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()