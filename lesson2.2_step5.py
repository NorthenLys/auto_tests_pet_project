import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    ans = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", ans)    
    ans.send_keys(y)      
    
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    radiob = browser.find_element(By.ID, "robotsRule")
    radiob.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
       
finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла
