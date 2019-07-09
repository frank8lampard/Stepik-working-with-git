from selenium import webdriver
import os
import math

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_elem = browser.find_element_by_id("input_value")
x=x_elem.text
y = calc(x)
red= browser.find_element_by_id("answer")
red.send_keys(y)
option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

button = browser.find_element_by_tag_name("button")

browser.execute_script("return arguments[0].scrollIntoView(true);", button)

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button.click()
