from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm?firstname=&lastname=&photo=&continents=Asia&selenium_commands=Navigation+Commands&submit=")

fname_input = driver.find_element_by_name("firstname")
fname_input.send_keys("George")
lname_input = driver.find_element_by_name("lastname")
lname_input.send_keys("Feeney")

gender_radio = driver.find_element_by_css_selector("#mainContent > div:nth-child(7) > div:nth-child(1) > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > input:nth-child(2)")
gender_radio.click()
