from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.com/Bloodborne-Board-Game-Blood-Expansion/dp/B08WHWLDNM/ref=sr_1_102?crid=3TEON94EAOAYR&keywords=board+games&qid=1686894251&refinements=p_36%3A1253564011&rnid=386491011&s=toys-and-games&sprefix=board+games%2Caps%2C92&sr=1-102")

# price = driver.find_element_by_class_name("a-price-whole")
# print(price.text)

# search_bar = driver.find_element_by_name("field-keywords")
# print(search_bar.get_attribute("placeholder"))

# nav_link = driver.find_element_by_css_selector(".nav-progressive-content a")
# print(nav_link.text)

nav_link = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[2]")
print(nav_link.text)

driver.quit()
