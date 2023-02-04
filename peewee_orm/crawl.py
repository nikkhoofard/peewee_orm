import requests
from bs4 import BeautifulSoup


def crawl_page(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', attrs={'class': 'news-detail-header'})
        title = div.find('h1')
        print(title.text)


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


if __name__ == '__main__':

    #  links = ['https://www.trthaber.com/haber/spor/fenerbahce-taraftari-tffyi-protesto-etti-743533.html',
    #          'https://www.trthaber.com/haber/spor/manchester-united-zirve-takibini-surdurdu-743532.html',
    #          'https://www.trthaber.com/haber/spor/galatasaray-trabzonspor-macina-hazir-743522.html',
    #          'https://www.trthaber.com/haber/spor/bandirmasporda-mesut-bakkalin-sozlesmesi-feshedildi-743514.html',
    #          ]
    # for link in links:
    #     crawl_page(link)
    get_links()

