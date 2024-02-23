import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)


web_code_all = response.text

soup = BeautifulSoup(web_code_all, "html.parser")

movie_title_reverse = soup.select("h3.title")

# print(movie_title_reverse)
length_of_movie_name = len(movie_title_reverse)

for movie in movie_title_reverse:
    movie = movie_title_reverse[length_of_movie_name - 1]
    # print(movie.text)
    with open("Starting Code - 100 movies to watch start/movies.txt", "a", encoding="utf8") as file:
        file.write(movie.text+"\n")
        # print(movie.text)
    length_of_movie_name -= 1
    