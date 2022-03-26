from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source_element=driver.find_element_by_id("box3")
dest_element=driver.find_element_by_id("box103")

actions=ActionChains(driver)
actions.drag_and_drop(source_element,dest_element).perform()
