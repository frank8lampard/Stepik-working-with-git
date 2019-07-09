from selenium import webdriver
import os
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
<<<<<<< HEAD

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

price = WebDriverWait(browser, 11).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
=======
price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000")
>>>>>>> b5434b050ea64290ac313834e45d1b64d87c8c72
    )
button = browser.find_element_by_id("book")
button.click()

browser.execute_script("return arguments[0].scrollIntoView(true);", button)
x_elem = browser.find_element_by_id("input_value")
x=x_elem.text
y = calc(x)
red= browser.find_element_by_id("answer")
red.send_keys(y)
<<<<<<< HEAD

button2 = browser.find_element_by_id("solve")
button2.click()
=======
button = browser.find_element_by_css_selector("button.btn")
button.click()
>>>>>>> b5434b050ea64290ac313834e45d1b64d87c8c72
