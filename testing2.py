from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\ASUS\\Downloads\\web_driver\\chromedriver.exe")

driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
print(driver.current_url)
time.sleep(2)

driver.find_element(By.NAME, "username").send_keys("Sizan")
print("find username field\n")
time.sleep(2)

driver.find_element(By.NAME, "password").send_keys("201037")
print("find password field\n")
time.sleep(2)

driver.find_element(By.CLASS_NAME, "submit-row").click()
print("find Login\n")
time.sleep(2)

driver.find_element(By.XPATH,"//a[contains(text(),'Log out')]").click()
print("find Logout\n")
time.sleep(2)

driver.close()