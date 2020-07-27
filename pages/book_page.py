import re
from bs4 import BeautifulSoup
from locators.all_page_locator import ALlPageLocator
from parsers.book_parser import BookParser


class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = ALlPageLocator.ALL_PAGE_LOCATOR
        books_tag = self.soup.select(locator)
        return [BookParser(e) for e in books_tag]

    @property
    def page_count(self):
        locator = ALlPageLocator.PAGER
        page_count = self.soup.select_one(locator).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, page_count)
        pages= int(matcher[1])
        return pages
