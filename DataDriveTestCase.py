import xlutils

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

path="C:\SeleniumProject\Login1.xlsx"

rows=xlutils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=xlutils.readData(path,'Sheet1',r,1)
    password=xlutils.readData(path,'Sheet1',r,2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("submit").click()

    if driver.title == "Login: Mercury Tours":
        print("Test is passed")
        xlutils.writeData(path,"Sheet1",r,3,"Test passed")
    else:
        print("Test failed")
        xlutils.writeData(path,"Sheet1",r,3,"Test failed")

    driver.find_element_by_link_text("Home").click()