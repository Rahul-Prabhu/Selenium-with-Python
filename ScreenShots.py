from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

# driver.save_screenshot("C:\SeleniumProject\home.png")
#Saving screenshot as a file
driver.get_screenshot_as_file("C:\SeleniumProject\home2.png")