import re
import logging
from bs4 import BeautifulSoup

from locators.book_page_locators import BooksLocator
from parsers.book import BookParser


logger = logging.getLogger('scraping.books_page')


class BooksPage:
    def __init__(self, book):
        logger.debug('Parsing content with BeautifulSoup HTML Parser')
        self.soup = BeautifulSoup(book, 'html.parser')

    @property
    def books(self):
        logger.debug(f'finding all books in the page using `{BooksLocator.BOOK}`.')
        locator = BooksLocator.BOOK
        return [BookParser(b) for b in self.soup.select(locator)]

    @property
    def page_count(self):
        logger.debug('Finding the total number of catalogue pages available...')
        content = self.soup.select_one(BooksLocator.PAGER).string
        logger.info(f'Found `{content} catalogue pages available`')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted `{pages}` number of pages as integer')
        return pages
