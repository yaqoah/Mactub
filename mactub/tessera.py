from PIL import Image
from pytesseract import pytesseract
import sys

tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_by_path(image_path):
    global tesseract_path
    brief_img = ""

    try:
        brief_img = Image.open(image_path)
    except FileNotFoundError as f:
        sys.exit(0)

    pytesseract.tesseract_cmd = tesseract_path
    text = pytesseract.image_to_string(brief_img)

    print(text[:-1])
