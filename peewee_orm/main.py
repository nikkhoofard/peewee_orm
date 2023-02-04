import sys
from utils.db import create_table
from models import Article, Category
from crawl import get_links


def run():
    links = get_links()
    cat = Category.create(name="sport")
    for link in links:
        article = Article.create(url=link, category=cat)
        print(article.id)



if __name__ == '__main__':
    if sys.argv[1] == 'create_tables':
        create_table()
    elif sys.argv[1] == 'run':
        run()
