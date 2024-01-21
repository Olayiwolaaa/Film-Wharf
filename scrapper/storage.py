import requests
from bs4 import BeautifulSoup

url = "https://nkiri.com/category/international/"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

movies = soup.find_all("div", class_="blog-entry-inner clr left-position center")
# print(movies)

for movie in movies:
    download_link = movie.find('a').get('href')
    print(download_link)
    image_url = movie.find('img').get('src')
    print(image_url)
    name = movie.get_text('')
    # print(name)
    
    