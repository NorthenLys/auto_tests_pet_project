from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

       
    num1 = browser.find_element(By.ID, "num1")
    n1 = num1.text
    i1 = int(n1)
    num2 = browser.find_element(By.ID, "num2")
    n2 = num2.text
    i2 = int(n2)    
    s = i1 + i2            
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    
    select.select_by_value(str(s))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
       
finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла
