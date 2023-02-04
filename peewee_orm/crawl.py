import requests
from bs4 import BeautifulSoup

from models import Article


def crawl_page(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', attrs={'class': 'news-detail-header'})
        title = div.find('h1')
        body = soup.select_one(".detYazi")

        return {'body': body.text, 'title': title.text}


def get_links():
    response = requests.get('https://www.trthaber.com/haber/spor/')
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    if response.status_code == 200:
        for link in soup.find_all('a'):
            href = link.attrs.get("href")
            if href is not None and href.startswith('haber/spor/'):
                links.append("https://www.trthaber.com/"+href)
    return links



