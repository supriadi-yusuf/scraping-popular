import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler')

#print(html_doc.status_code)
#print(result.text)

soup = BeautifulSoup(html_doc.text, 'html.parser')
# print(soup)

popular_area = soup.find(attrs={'class':'grid-row list-content'})
#print(popular_area)

titles = popular_area.find_all(attrs={'class':'media__title'})

#for title in titles:
#    print(title)

images = popular_area.find_all(attrs={'class':'media__image'})
#for image in images:
#    print(image)

#for image in images:
#    print(image.find('a').find('img'))

for image in images:
    print(image.find('a').find('img')['title'])