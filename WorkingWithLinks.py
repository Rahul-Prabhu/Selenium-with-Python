from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver_win32 (7)\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links:",len(links))

for link in links:
    print(link.text)

#clicking on the link
# driver.find_element(By.LINK_TEXT,'REGISTER').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'RE').click()

# driver.close()