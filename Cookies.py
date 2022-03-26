from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe")
driver.get("http://www.amazon.in/")


#Collect all the cookies from browser
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

driver.add_cookie({"name":"MyCookie", "value":"123456"})        #Add cookie

cookies=driver.get_cookies()
print(len(cookies))     #print no of cookies
print(cookies)          #print cookies after inserting cookies

driver.delete_cookie("MyCookie")        #Delete cookie
cookies=driver.get_cookies()        #get cookies after deleting cookie
print(len(cookies))                 #print no of cookies

driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)