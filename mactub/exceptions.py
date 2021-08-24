"""more on exception to improve this file"""


class MissingHardDisk(Exception):
    """Exception raised when hard disk not (plugged) on"""

    def __int__(self, message):
        super.__init__(message)
