import requests
from bs4 import BeautifulSoup


def start():
    url = 'https://www.trthaber.com/haber/spor/' \
         'fenerbahce-taraftari-tffyi-protesto-etti-743533.html'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', attrs={'class': 'news-detail-header'})
        title = div.find('h1')
        print(title.text)


if __name__ == '__main__':
    start()
