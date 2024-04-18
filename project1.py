from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
sleep(2)
driver.find_element(By.NAME,"username").clear()
sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
sleep(2)
driver.find_element(By.NAME,"password").send_keys("admin123")

sleep(2)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()
actual_title=driver.title
expected_title="OrangeHRM"
if(actual_title==expected_title):
    print("Login test passed")
else:
    print("Login test failed")
driver.close()