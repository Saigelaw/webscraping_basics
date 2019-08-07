import logging

from app import books_list

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the following
-'b' to look at best rated books
-'c' to look at the cheapest books
-'n' to get the next available book on the catalogue
-'q' to quit

Enter your choice: '''


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books_list, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding cheapest books by price...')
    cheapest_books = sorted(books_list, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


book_gen = (book for book in books_list)


def print_next_book():
    logger.info('Getting the next book from book_gen a generator of all books')
    print(next(book_gen))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Incorrect choice selected. Please try again.')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program')


menu()
