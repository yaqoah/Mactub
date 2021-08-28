"""
Cover images related functions
"""
from PIL import Image
from pytesseract import pytesseract

import sys
import re

tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
READ_TIME = 24
WORD_COUNT = 100


def create(image_path):
    """
    Creates image by path to it
    :param image_path:
    :return: PIL image created
    """

    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        sys.exit(1)

    return img


def resize(img, width, height):
    """
    Change dimensions of image
    :param img: Image to be manipulated
    :param width: desired width of image
    :param height: desired height of image
    :return: PIL image
    """

    resized_img = img.resize((width, height))
    return resized_img


def read(img):
    """
    Reads text in image
    :param img: The cover image to be read
    :return: the text extracted from the image
    """

    pytesseract.tesseract_cmd = tesseract_path
    text = pytesseract.image_to_string(img)
    clean_text = text[:-1].split("\n")

    return clean_text


def duration(text):
    """
    Calculates time to read particular text
    :param text: the plaintext to be read
    :return: time in milliseconds
    """

    words_count = len(re.findall(r'\w+', text))
    dur = (words_count * READ_TIME) / WORD_COUNT
    dur_milli = dur * 1000
    dur_int = round(dur_milli)

    return dur_int
