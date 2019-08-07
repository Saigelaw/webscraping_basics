import re
import logging
from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book')


class BookParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Title: {self.name}, URL: {self.link}, Price: £{self.price}, Ratings {self.rating} stars>'

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator)['title']
        logger.debug(f'Found book titled `{item_name}')
        return item_name

    @property
    def link(self):
        logger.debug('Finding the book link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator)['href']
        logger.debug(f'Found the book link as `{item_link}`')
        return item_link

    @property
    def price(self):
        logger.debug('Finding book price')
        locator = BookLocators.PRICE_LOCATOR
        item_link = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_link)
        float_price = float(matcher.group(1))
        logger.debug(f'Found the book price `{float_price}`')
        return float_price

    @property
    def rating(self):
        logger.debug('Finding book rating')
        locator = BookLocators.RATING_LOCATOR
        star_rating_flag = self.parent.select_one(locator)
        classes = star_rating_flag.attrs['class']
        classes_list = [c for c in classes if c != 'star-rating']
        ratings_number = BookParser.RATINGS.get(classes_list[0])
        logger.debug(f'Found book rating: `{ratings_number}`.')
        return ratings_number
