from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe")
driver.get("https://www.expedia.co.in/")

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[4]/div/div[1]/div/div/div/div/ul/li[2]/a/span").click() #click flight
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[4]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/button").click()   #click source
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element(By.ID,"location-field-leg1-origin").clear()
driver.find_element(By.ID,"location-field-leg1-origin").send_keys("Mumbai")    #type source location


time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[4]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]/button").click()   #click destination

time.sleep(5)
driver.find_element(By.ID,"location-field-leg1-destination").clear()
driver.find_element(By.ID,"location-field-leg1-destination").send_keys("Newyork")  #type destination location


time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[4]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[2]/button").click()       #click Search button

wait=WebDriverWait(driver, 10)
element=wait.until(EC.element_to_be_clickable(By.XPATH, "//*[@id='stopFilter_stops-0']"))

element.click()

time.sleep(5)

driver.quit()