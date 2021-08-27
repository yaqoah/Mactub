"""
Dust shalt thou be blown
"""
import pathlib
import sys
import random
import re

from exceptions import MissingHardDisk


class Book:
    """Book infos are to be known"""

    def __init__(self, shelf):
        """Initialize book object """

        self.exhibited = []
        self.title = ""
        self.author = ""

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
            self.title = info[0]
            self.author = info[1]

        else:
            self.exhibited = []
            self.fetch()

    def get_title(self):
        """
        :return: title of book
        """

        return self.title

    def get_author(self):
        """
        :return: author name of book
        """

        return self.author