import sys
from utils.db import create_table
from models import Article, Category


def run():

    print(f'Hi')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    if sys.argv[1] == 'create_tables':
        create_table()
    elif sys.argv[1] == 'run':
        run()
