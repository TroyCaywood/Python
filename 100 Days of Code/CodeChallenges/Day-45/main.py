import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movie_tag = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
print(movies)

with open(file="movies.txt", mode="w") as data:
    for movie in movies:
        data.writelines(f"{movie}\n")
