from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.chrome.options import Options

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "C:\Downloads"})

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver.exe",chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()        #Maximize Window

#1 Enter data
driver.find_element_by_id("textbox").send_keys("Hello World")

#2. Generate File
driver.find_element_by_id("createTxt").click()

#Download the link
driver.find_element_by_id("link-to-download").click()
