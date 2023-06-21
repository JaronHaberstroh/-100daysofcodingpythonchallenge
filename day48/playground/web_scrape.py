from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")


event_dates = [date.text for date in driver.find_elements_by_css_selector(".event-widget time")]
event_links = [link.text for link in driver.find_elements_by_css_selector(".event-widget li a")]

events_dict = {}
for idx, date in enumerate(event_dates):
    events_dict[idx] = {
        "date": date,
        "name": event_links[idx],
        }

print(events_dict)






driver.quit()
