from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/troycaywood/Development/ChromeDriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_titles[n].text
    }

print(events)

# search_bar = driver.find_element(By.NAME, "search_bar")

# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id=site-map"]/div[2]/div/ul/li[3/a')
# print(bug_link.text)