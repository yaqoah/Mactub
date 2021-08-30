"""
Dust shalt thou be blown
"""
import re
import sys
import random

from exceptions import MissingHardDisk


class Book:
    """Book infos are to be known"""

    def __init__(self, shelf):
        """Initialize book object """

        self.exhibited = []
        self.__title = ""
        self.__author = ""

        try:
            self.path = shelf
            if not self.path.exists():
                raise MissingHardDisk(shelf, "Plugin your 'D' drive")

        except MissingHardDisk as hdd:
            sys.exit("1)Check book path.\n2)" + str(hdd))

    def fetch(self):
        """Obtain book title and author from path data in directory"""

        p = self.path.glob('*')
        books = [book for book in p if book not in self.exhibited]

        if books:
            book = random.choice(books)
            self.exhibited.append(book)
            info = re.split(" By ", book.stem)
            self.__title = info[0]
            self.__author = info[1]

        else:
            self.exhibited = []
            self.fetch()

    def get_title(self):
        """
        :return: title of book
        """
        return self.__title

    def get_author(self):
        """
        :return: author name of book
        """
        return self.__author
