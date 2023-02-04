from models import Category, Article, database


def create_table():
    database.create_tables([Article, Category])
