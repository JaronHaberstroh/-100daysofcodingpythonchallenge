from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/experiments/cookie/")

store_items = driver.find_elements_by_css_selector("#store div")
store_items.reverse()
costs = [item.text.split("-")[1].split("\n")[0].replace(",", "").strip() for item in store_items if item.text != ""]

store = zip(store_items, costs)
for item in store:
    print(item)
