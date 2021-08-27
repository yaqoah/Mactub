"""Custom Exceptions"""


class MissingHardDisk(Exception):
    """Exception raised when drive not plugged"""

    def __int__(self, directory, message):
        self.message = message + f"\n[Error] Directory " \
                                 f"{str(directory)} -> not found"
        super.__init__(self.message)
