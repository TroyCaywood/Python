from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = (article_tag.getText())
    article_texts.append(text)
    article_link1 = article_tag.find("a")
    link = article_link1.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(f"{largest_number} votes")

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# article_upvote =
# Open HTML file and read it
# with open(file="website.html") as data:
#     contents = data.read()

# Create BeautifulSoup object and pass it the contents variable and tell it to use the html parser to read it
# soup = BeautifulSoup(contents, "html.parser")

# Print title tag from website
# print(soup.title)

# Print title tag name
# print(soup.title.name)

# Print title string
# print(soup.title.string)

# Print the entire html
# print(soup)

# Print the entire html with formatting
# print(soup.prettify())

# Print text and links from all a tags
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")