from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe")

driver.get("https://docs.oracle.com/javase/8/docs/api/")


driver.switch_to.frame("packageListFrame")      #first frame
driver.find_element_by_link_text("java.awt.datatransfer").click()

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("packageFrame")      #second frame
driver.find_element_by_xpath("/html/body/div/ul[2]/li[2]/a").click()

driver.switch_to.default_content()


time.sleep(3)

driver.switch_to.frame("classFrame")        #third Frame
driver.find_element_by_xpath("/html/body/div[1]/ul/li[6]").click()
