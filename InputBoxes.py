# https://forms.office.com/Pages/ResponsePage.aspx?id=wZ-qArwYmEegIOAchU3UNK8k1ZoWavNNuQmFoP1sR0ZUOFM0WEhJUlpBNjZZWUdVSVk4WlkyTzZVWC4u
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Dev\WebDriver\chromedriver_win32 (7)\chromedriver.exe")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScDgxW7tA9c9klw2tCzuhe_jRT1BaeA6jwN3La9qOxwVIjjiw/viewform?usp=pp_url")

print(len(driver.find_elements(By.CLASS_NAME,'freebirdFormviewerComponentsQuestionBaseTitleDescContainer')))
#name

driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span").click()        #click to sign in your mail
#enter your mail
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("rahulprabhu14")

#click next
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()

#enter password




driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Rahul")
#Email

driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("rahulprabhu14@gmail.com")
#Address

driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys("Goregaon(W)")
#Phone number

driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("9969921122")
#Comments


driver.find_element(By.XPATH,'/html/body/div/div[3]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys("Hi")
