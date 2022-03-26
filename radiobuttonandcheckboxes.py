from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver_win32 (7)\chromedriver.exe")
driver.get("link")
status=driver.find_element_by_id("id_name1").is_selected()
print(status)
driver.find_element_by_id("id_name2").click()       #click radio button

driver.find_element_by_id("id_name3").click()       #click radio button