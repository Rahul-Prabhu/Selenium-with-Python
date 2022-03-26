from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe")

driver.get("http://the-internet.herokuapp.com/upload")

driver.maximize_window()


time.sleep(5)

driver.find_element_by_id("file-upload").send_keys("C://Users/Admin/Pictures/Camera Roll/WIN_20200929_11_30_16_Pro.jpg")
time.sleep(5)
driver.find_element_by_id("file-submit").click()
