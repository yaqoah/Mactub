from PIL import Image
from pytesseract import pytesseract

import sys
import re

tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
READ_TIME = 240
WORD_COUNT = 500


def create(image_path):
    img = None

    try:
        img = Image.open(image_path)
    except FileNotFoundError as f:
        sys.exit(1)

    return img


def resize(img, width, height):
    resized_img = img.resize((width, height))
    return resized_img


def read(img):
    pytesseract.tesseract_cmd = tesseract_path
    text = pytesseract.image_to_string(img)
    clean_text = text[:-1]

    return clean_text


def duration(text):
    words_count = len(re.findall(r'\w+', text))
    return (words_count * READ_TIME) / WORD_COUNT
