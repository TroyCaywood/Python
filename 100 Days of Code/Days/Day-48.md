# Day 48 - Selenium Webdriver Browser and Game Playing Bot

- [Selenium](https://www.selenium.dev/) is a tool that we can use to automate anything that you can do within a browser.
- Selenium can interact with many different browsers such as Chrome, Edge, Firefox, Opera etc.
- In order for Selenium to interact with your browser you have to user a driver. For example the [chrome driver](https://chromedriver.chromium.org/downloads)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Git/ChromeDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
```

- Now we can use `driver.get("https://www.google.com")` to open a new instance of chrome and go to google.com. There wil be a message at the top of chrome that says "Chrome is being controlled by automated test software."
- To close the browser you just call `driver.close()` to close the tab. Or if you use `driver.quit()` it will close the entire browser.
- Selenium can also be used to find elements on a webpage similar to BeautifulSoup. However, it's much shorter since you're driving a browser that is already sending headers and accessing the website the same way a human would.
- For example, we could use `driver.find_element(By.ID, "priceblock-ourprice)` to find the price of an item on amazon like in Day-47.
- `driver.find_element(By.NAME, "name")` is another useful way of finding elements on a page by name.
- There are [many other](https://selenium-python.readthedocs.io/locating-elements.html) ways of locating elements on a page.
- If you cannot locate an element by CSS, or ID or name etc. [Xpath](https://www.w3schools.com/xml/xpath_intro.asp) is another option for finding it.
- You can obtain the Xpath of an element by going into the source with inspect and then find the element you're looking for, then right click and copy as xpath
- `driver.find_element(By.XPATH, '//*[@id=site-map"]/div[2]/div/ul/li[3/a')` is an example of an XPATH
- To get all elements with the same id/class/name etc you cna use `driver.find_elements()` instead.
- To keep your browser from closing when the code finishes running add this
```python
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
```
- To tell selenium to click on an element, first select the element and then use `element.click()`
```python
driver.get("https://en.wikipedia.org")

counter = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
counter.click()
```

- An easy way to find a link on a page is by using `By.LINK_TEXT` and then you just add the text of the link.
```python
community_portal = driver.find_element(By.LINK_TEXT, "Community portal")
community_portal.click()
```
- To type in a field, first find the element for that field and then use `sendkeys("text")` to enter text into that field.
```python
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
```
- If you need to send a key such as return or backspace etc you'll need to import the `Keys` class first.
```python
from selenium.webdriver.common.keys import Keys

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
```