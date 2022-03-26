from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver_win32 (7)\chromedriver.exe")

# driver.get("https://www.facebook.com/")
# print(driver.title)
# time.sleep(5)
#
# driver.get("https://www.youtube.com/")
# print(driver.title)
# time.sleep(5)
# print(driver.current_url)
# driver.back()   #for going to history page
# print(driver.title)
# time.sleep(5)
#
# driver.forward()    #for going to current page
# print(driver.title)
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
driver.get("http://demo.guru99.com/test/newtours/")
user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("submit").click()
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()
roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")

print(roundtrip_radio.is_selected())    #print status of roundtrip

# driver.close()  #closes current browser tab
# driver.quit()   #closes all the browser tabs

