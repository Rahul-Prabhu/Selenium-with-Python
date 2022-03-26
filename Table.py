from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver_win32 (7)\chromedriver.exe")

driver.get("http://demo.guru99.com/test/web-table-element.php")

rows=len(driver.find_elements_by_xpath("/html/body/div/div[3]/div[1]/table/tbody/tr"))
cols=len(driver.find_elements_by_xpath("/html/body/div/div[3]/div[1]/table/tbody/tr[1]/td"))

print(rows)
print(cols)
print("\n"+"        Company"+"      Group"+"        Prev Close (Rs)"+"      Current Price (Rs)"+"       % Change")
for r in range(2,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='       ')
    print()