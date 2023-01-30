from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time



link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "book")
WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

x_element = browser.find_element(By.ID, "input_value")
x_element_int = int(x_element.text)

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


c = calc(x_element_int)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(c)


input4 = browser.find_element(By.ID, "solve")
input4.click()


    # закрываем браузер после всех манипуляций
    #browser.quit()
