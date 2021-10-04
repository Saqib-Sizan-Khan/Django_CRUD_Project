from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\ASUS\\Downloads\\web_driver\\chromedriver.exe")

driver.get("http://127.0.0.1:8000/posts/")
print(driver.current_url)
time.sleep(2)

driver.find_element(By.ID, "add").click()
print("find Nav Bar\n")
time.sleep(2)

driver.find_element(By.NAME, "title").send_keys("Sizan Khan")
print("find title field\n")
time.sleep(2)

driver.find_element(By.NAME, "excerpt").send_keys("Hello I am Sizan Khan from Dhaka")
print("find excerpt field\n")
time.sleep(2)

driver.find_element(By.NAME, "author").send_keys("Sizan")
print("find author field\n")
time.sleep(2)

driver.find_element(By.NAME, "slug").send_keys("sizan")
print("find slug field\n")
time.sleep(2)


driver.find_element(By.NAME, "save").click()
print("find save button\n")
time.sleep(2)

driver.find_element(By.NAME, "delete").click()
print("find delete button\n")
time.sleep(2)

driver.find_element(By.NAME, "confirm").click()
print("find confirm button\n")
time.sleep(2)

driver.close()
