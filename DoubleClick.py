from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver_win32 (7)\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()        #maximize the page
#locate click location
element=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button")

actions=ActionChains(driver)

actions.double_click(element).perform()     #double click on the button