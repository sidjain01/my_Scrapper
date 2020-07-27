import re
from locators.books_locator import BookLocator


class BookParser:
    RATING = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return (f'<Book: {self.name}, £{self.price} ({self.rating} stars), link: {self.link}>')

    @property
    def name(self):
        locator = BookLocator.NAME_LOCATOR
        book = self.parent.select_one(locator)
        book_name = book.attrs['title']
        return book_name

    @property
    def link(self):
        locator = BookLocator.LINK_LOCATOR
        link = self.parent.select_one(locator)
        book_link = link.attrs['href']
        return book_link

    @property
    def price(self):
        locator = BookLocator.PRICE_LOCATOR
        price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        book_price = re.search(pattern, price)
        return float(book_price.group(1))

    @property
    def rating(self):
        locator = BookLocator.RATING_LOCATOR
        rating = self.parent.select_one(locator)
        rating_class = rating.attrs['class']
        book_rating = [r for r in rating_class if r != 'star-rating']
        book_rate = BookParser.RATING.get(book_rating[0])
        return book_rate
