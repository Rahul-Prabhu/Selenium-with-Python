from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()
time.sleep(5)

driver.switch_to_alert().accept()       #closes the alert box using OK button

# driver.switch_to_alert().dismiss()      #closes the alert box using cancel button
