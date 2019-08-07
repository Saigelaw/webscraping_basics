import requests
import logging
from books.books_page import BooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com/').content

book = BooksPage(page_content)

books_list = book.books

for page_num in range(1, book.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num +1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating BooksPage from page content ')
    book = BooksPage(page_content)
    books_list.extend(book.books)

