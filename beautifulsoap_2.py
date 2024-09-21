from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com"
url = f"{root}/movies"

response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())

box = soup.find('article', class_='main-article')
# print(box)

movies = box.find_all('a', href=True)
movie_list = []
movie_url = []
# print(movies)
for movie in movies:
    movie_list.append(movie.get_text(strip=True))
    movie_url.append(movie['href'])

print(movie_url)

with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(movie + ",")

for link in movie_url:
    url = f"{root}/{link}"
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True)

    with open(f"{title}.txt", "w") as file:
        file.write(transcript)
