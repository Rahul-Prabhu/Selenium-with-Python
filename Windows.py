from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver_win32 (7)\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()

print(driver.current_window_handle)     #handle value of current window
handles=driver.window_handles       #all the handle values of the opened window browsers
print(handles)
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == 'Frames & Windows':
        driver.close()
# driver.quit()