from selenium import webdriver
import os
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element_by_tag_name("button")
button.click()
confirm = browser.switch_to.alert
confirm.accept()
x_elem = browser.find_element_by_id("input_value")
x=x_elem.text
y = calc(x)

red= browser.find_element_by_id("answer")
red.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()

