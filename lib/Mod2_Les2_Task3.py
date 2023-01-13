from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, "num1").text)
    y = int(browser.find_element(By.ID, "num2").text)

    r = str(x + y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(r)

    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(5)
    browser.quit()