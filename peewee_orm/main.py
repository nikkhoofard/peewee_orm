import sys
from utils.db import create_table
from models import Article, Category
from crawl import get_links, crawl_page

# def wating()
def crawl_and_get_links():
    links = get_links()
    cat = Category.create(name="sport")
    for link in links:
        article = Article.create(url=link, category=cat)
        print(article.id)


def scrap_articles():
    articles = Article.select().where(Article.is_completed == False)

    for article in articles:
        try:
            data = crawl_page(article.url)
        except:
            article.is_completed = True
            article.save()
        else:
            article.title = data['title']
            article.body = data["body"]
            article.is_completed = True
            article.save()


def show_stats():
    articles = Article.select().where(Article.is_completed==False).count()
    category = Category.select().count()
    completed = Article.select().where(Article.is_completed==True).count()
    print(f"articles:{articles}\t category:{category}\t completed:{completed}")


if __name__ == '__main__':
    if sys.argv[1] == 'create_tables':
        create_table()
    elif sys.argv[1] == 'get_link':
        crawl_and_get_links()
    elif sys.argv[1] == 'stats':
        show_stats()
    elif sys.argv[1] == 'scrap':
        print(f'wating a moment...')
        scrap_articles()
        print(f'done')
