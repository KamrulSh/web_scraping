from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com"
url = f"{root}/movies_letter-A"
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, 'lxml')

# pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

for page in range(1, int(last_page) + 1)[:2]:
    response = requests.get(f"{url}?page={page}")
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')
    movies = box.find_all('a', href=True)
    movie_url = []
    # print(movies)
    for movie in movies:
        movie_url.append(movie['href'])

    for link in movie_url:
        try:
            print(link)
            response = requests.get(f"{root}/{link}")
            content = response.text
            soup = BeautifulSoup(content, 'lxml')
            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True)

            with open(f"{title}.txt", "w") as file:
                file.write(transcript)
        except:
            print("------ Error ------")
            print(link)
            pass
