import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/berita-popular')
def berita_popular():
    html_doc = requests.get('https://www.detik.com/terpopuler')

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    popular_area = soup.find(attrs={'class':'grid-row list-content'})

    titles = popular_area.find_all(attrs={'class':'media__title'})
    images = popular_area.find_all(attrs={'class':'media__image'})

    # call html file with argumen gambar=images
    return render_template('index.html', gambars=images)

if __name__ == '__main__':
    app.run(debug=True)