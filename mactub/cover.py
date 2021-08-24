"""Get cover MS-DOS paths"""
import pathlib
import sys
import re

from exceptions import MissingHardDisk


class Cover:
    """Get back and front paths"""

    def __init__(self, book, bindings="D:/Books/Covers"):
        self.book = book

        try:
            self.book_path = pathlib.Path(bindings)
            if not self.book_path.exists():
                raise MissingHardDisk("Plugin your 'D' drive")

        except MissingHardDisk as hdd:
            sys.exit("1)Check cover path.\n2)" + str(hdd))

    def get_cover(self, face):
        p = self.book_path.glob('*')
        bindings = [cover for cover in p]
        book_acronym = ''.join([word[0].upper()
                                for word in
                                self.book.split()])

        for binding in bindings:
            if re.search(book_acronym, binding.stem):
                if face == "front":
                    if binding.stem[-1] == "0":
                        return pathlib.Path(str(self.book_path)
                                            + "/"
                                            + binding.name)

                else:
                    if binding.stem[-1] == "1":
                        return pathlib.Path(str(self.book_path)
                                            + "/"
                                            + binding.name)
