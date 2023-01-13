from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element(By.TAG_NAME, "button").click()

    browser.execute_script("window.scrollBy(0, 100);")

    x = int(browser.find_element(By.ID, 'input_value').text)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(math.log(abs(12 * math.sin(x)))))

    submit = browser.find_element(By.ID, "solve")
    submit.click()

    alert = browser.switch_to.alert
    code = alert.text.split(': ')[-1]
    alert.accept()

finally:
    time.sleep(20)
    browser.quit()
    print(code)