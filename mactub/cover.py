"""Get cover MS-DOS paths"""
import pathlib
import sys

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
        bindings = [cover.stem for cover in p]


### more
