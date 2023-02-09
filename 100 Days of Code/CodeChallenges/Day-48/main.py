from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Git/ChromeDriver/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager))

driver.get("https://www.amazon.com")

# search_bar = driver.find_element(By.NAME, "search_bar")

# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id=site-map"]/div[2]/div/ul/li[3/a')
# print(bug_link.text)