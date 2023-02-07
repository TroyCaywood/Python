# Day 45 - Web Scraping with Beautiful Soup

- Some websites do not have an API available. That's where [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) comes in. It allows you to pull data off of a website that doesn't have an API to do so.

- To begin, first import BeautifulSoup using `from bs4 import BeautifulSoup`
- Then you have to read the html or xml file
```python
# Open HTML file and read it
with open(file="website.html") as data:
    contents = data.read()
```
- Now you can create a BeautifulSoup object `soup = BeautifulSoup(contents, "html.parser")`
- Depending on the type of content you're using BeautifulSoup for, you might have to use a different [parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser).
- Here are a few things you can do to search the HTML file. The first four options only find the first tag of that type, but the last one finds and prints all of the `<a>` tags.
```python
# Print title tag from website
print(soup.title)

# Print title tag name
print(soup.title.name)

# Print title string
print(soup.title.string)

# Print the entire html
print(soup)

# Print the entire html with formatting
print(soup.prettify())

# Print text and links from all a tags
all_anchor_tags = soup.find_all(name="a")

```

- You can also find all tags of a specific name/class and loop through them
```python
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))
```

```python
heading = soup.find(name="h1", id="name")
```

- BeautifulSoup can also be used on live websites on the internet:
```python
import requests

response = requests.get("https://news.ycombinator.com")
```

- Looking at the source for this site, the scores of an article are stored in a class called `score` and the article link is stored in a class called `storylink`
- We can use that information to get the highest scored articles
- First we'll get the title of the first article
```python
article_tag = soup.find(name="span", class_="titleline")
print(article_tag.getText())
```
- Now we'll find all the articles and loop through them
```python
# Find all articles
articles = soup.find_all(name="span", class_="titleline")
# Lists for storing articles and links
article_texts = []
article_links = []

# Loop through articles and add text and links to lists
for article_tag in articles:
    text = (article_tag.getText())
    article_texts.append(text)
    article_link1 = article_tag.find("a")
    link = article_link1.get("href")
    article_links.append(link)

# Get all upvotes and then split the text it has list with a number and the string 'points' then get just the first index and convert it to an integer. Save to list.
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Find the largest number in upvotes list
largest_number = max(article_upvotes)
# Find the index of the largest number
largest_index = article_upvotes.index(largest_number)

# Print the most upvoted article, link and number of votes using largest number index
print(article_texts[largest_index])
print(article_links[largest_index])
print(f"{largest_number} votes")
```
### Is web scraping legal?

- You are allowed to scrap a website's data as long as you are scraping data that is publicly available and not copyrighted.
- If you're using data privately it doesn't really matter too much, but if you're selling the data you're scraping it's different.
- You cannot scrape data that is behind authentication.
- If data is not behind authentication and isn't copyrighted you should be ok to scrape.
- Ethically, if a website has a public API, use that first.
- Respect the web owner. You can tell what the site doesn't want scraped by going to /robots.txt on that site. Most will have a craw delay that tells you how long you should wait before scraping again. You could potentially DDOS a site if you scrape too quickly and too much.
- It's good practice not to scrape more than once per minute. Even if there isn't a crawl limit in robots.txt

## Day 45 [Code Challenge](https://github.com/TroyCaywood/Python/tree/main/100%20Days%20of%20Code/CodeChallenges/Day-45) - Web Scraping 100 Movies That you Must Watch
