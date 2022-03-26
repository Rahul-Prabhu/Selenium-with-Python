from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe")
driver.get("link")
element=driver.find_element_by_id("button1")        #finding dropdown box
drp=Select(element)     #Clicking drop down box of the form
drp.select_by_visible_text("text of any option of dropdown")        #Clicking the option of the dropdown box
drp.select_by_index("index of any option")
drp.select_by_value("value of the option")

#count no of options
len(drp.options)

#capture all options and print them
all_options=drp.options

for option in all_options:
    print(option.text)
