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

    def __init__(self, shelf="D:/Books/Texts"):
        self.exhibited = []
        self.title = ""
        self.author = ""

        try:
            self.path = pathlib.Path(shelf)
            if not self.path.exists():
                raise MissingHardDisk("Plugin your 'D' drive")

        except MissingHardDisk as hdd:
            sys.exit("1)Check book path.\n2)" + str(hdd))

    def fetch(self):
        p = self.path.glob('*')
        books = [book for book in p if book not in self.exhibited]

        if books:
            book = random.choice(books).stem
            info = re.split(" By ", book)
            self.title = info[0]
            self.author = info[1]
            self.exhibited.append(book)

        else:
            self.exhibited = []
            self.fetch()

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author