from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/Users/troycaywood/Development/ChromeDriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get("https://en.wikipedia.org")

# counter = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# counter.click()

# community_portal = driver.find_element(By.LINK_TEXT, "Community portal")
# community_portal.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
