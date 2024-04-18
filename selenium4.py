#from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\soyeb\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.google.com")
driver.find_element(By.NAME,"q").send_keys("Goat")

driver.find_element(By.NAME,"q").click()
print("Successful")
driver.close()
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("path")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.google.com")
driver.find_element(By.ID,"q").send_keys("Goat")
'''