from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Edge()

driver.get("http://www.google.com")
   
SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys("arroz")
SearchInput.submit()

sleep(2)

driver.close()

