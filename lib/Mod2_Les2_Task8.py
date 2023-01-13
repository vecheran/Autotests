from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

with open('test.txt', 'w') as file:
   file.write('Now I know how to test!!! ')

path = os.getcwd() + '/' + file.name

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Мастер")
    browser.find_element(By.NAME, "lastname").send_keys("Доминатор")
    browser.find_element(By.NAME, "email").send_keys("kungfu@master.ru")
    browser.find_element(By.ID, "file").send_keys(path)


    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()