import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/berita-popular')
def berita_popular():
    html_doc = requests.get('https://www.detik.com/terpopuler')

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    popular_area = soup.find(attrs={'class':'grid-row list-content'})

    titles = popular_area.find_all(attrs={'class':'media__title'})
    images = popular_area.find_all(attrs={'class':'media__image'})

    # call html file with argumen gambars=images
    return render_template('popular-scraper.html', gambars=images)

@app.route('/idr-rates')
def idr_rates():
    source = requests.get('https://www.floatrates.com/daily/idr.json')
    json_data = source.json()

    return render_template('idr-rates.html', datas=json_data.values())

if __name__ == '__main__':
    app.run(debug=True)