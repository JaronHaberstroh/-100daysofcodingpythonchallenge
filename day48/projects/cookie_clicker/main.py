import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CHECK = 1
END = 60 * 5


def get_store_dict():
    store_items = driver.find_elements_by_css_selector("#store div")[::-1]
    store_costs = driver.find_elements_by_css_selector("#store b")[::-1]
    store_dict = {}

    for idx, cookies in enumerate(store_costs):
        if store_items[idx].get_attribute("class") != "grayed":
            num = cookies.text.split("-")[1].replace(",", "")
            store_dict[idx] = {
                "item": store_items[idx],
                "cost": int(num),
            }

    return store_dict


def get_money():
    cookies = driver.find_element_by_id("money").text
    return int(cookies.replace(",", ""))


def get_cps():
    return driver.find_element_by_id("cps").text


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

store = get_store_dict()
check = time.time() + CHECK
end = time.time() + END

while True:
    cookie.click()
    if time.time() >= check:
        store = get_store_dict()
        money = get_money()

        for key, value in store.items():
            item = value["item"]
            cost = value["cost"]

            if cost < money:
                money = get_money()
                item.click()
                break

        check = time.time() + CHECK

    if time.time() >= end:
        print(get_cps())
        break

driver.quit()