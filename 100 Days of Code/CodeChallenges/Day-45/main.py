from bs4 import BeautifulSoup

# Open HTML file and read it
with open(file="website.html") as data:
    contents = data.read()

# Create BeautifulSoup object and pass it the contents variable and tell it to use the html parser to read it
soup = BeautifulSoup(contents, "html.parser")

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
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")