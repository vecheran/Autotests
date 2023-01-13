from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/get_attribute.html"

try:
    # browser = webdriver.Chrome()
    # browser.get(link)
    #
    # browser.find_element(By.TAG_NAME, "select").click()
    # browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("1")  # ищем элемент с текстом "Python"

    # Можно использовать еще два метода: \
    # select.select_by_visible_text("text")
    # и
    # select.select_by_index(index).Первый

finally:
    time.sleep(10)
    browser.quit()