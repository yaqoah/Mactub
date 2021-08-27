"""Get cover MS-DOS paths"""
import pathlib
import sys
import re

from exceptions import MissingHardDisk


class Cover:
    """Get back and front cover (by path)"""

    def __init__(self, book, bindings):
        """Initialise cover (of book) object"""

        self.book = book

        try:
            self.path_to_cover = bindings
            if not self.path_to_cover.exists():
                raise MissingHardDisk(bindings, "Plugin your 'D' drive")

        except MissingHardDisk as hdd:
            sys.exit("1)Check cover path.\n2)" + str(hdd))

    def get_cover(self, face):
        """
        Get cover of book by specified face
        :param face: what side of cover (front or back)
        :return: path to face specified (front/back)
        """

        p = self.path_to_cover.glob('*')
        bindings = [cover for cover in p]
        book_acronym = ''.join([word[0].upper()
                                for word in
                                self.book.split()])

        for binding in bindings:
            if re.search(book_acronym, binding.stem):
                if face == "front":
                    if binding.stem[-1] == "0":
                        return pathlib.Path(str(self.path_to_cover)
                                            + "/"
                                            + binding.name)

                else:
                    if binding.stem[-1] == "1":
                        return pathlib.Path(str(self.path_to_cover)
                                            + "/"
                                            + binding.name)
