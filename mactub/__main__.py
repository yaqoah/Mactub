import argparse
import pathlib
import time
import sys

from tkinter import *
from PIL import ImageTk, Image
from book import Book
from cover import Cover
import tessera
from __init__ import __version__

showing = None


def get_args():
    """get script CL arguments"""

    description = "Mactub - Access and view books downloaded " \
                  "in device,to assist in selecting " \
                  "by reading short synopsis"

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("--width", metavar="'px'",
                        help="What width to display book cover in",
                        default=640)

    parser.add_argument("--height", metavar="'px'",
                        help="What height to display book cover in",
                        default=590)

    parser.add_argument("--books_path", metavar="'path/to/dir",
                        help="Path to folder containing "
                             "(i.e: .PDF,.EPUB,.TXT)"
                             "book files",
                        default=pathlib.Path("D:/Books/Texts"),
                        type=pathlib.Path)

    parser.add_argument("--covers_path", metavar="'path/to/dir",
                        help="Path to folder containing "
                             "(i.e: .PNG,.JPEG,.GIF)"
                             "book covers (back,front) file",
                        default=pathlib.Path("D:/Books/Covers"),
                        type=pathlib.Path)

    parser.add_argument("--version", action="store_true",
                        help="print Mactub version")

    # may add one here for only image/synopsis

    return parser.parse_args()


def slideshow(args, realm, root):
    global showing

    mac = Book(args.books_path)
    mac.fetch()
    name = mac.get_title()
    author = mac.get_author()
    print(f"{author}-  author of: {name}")

    tub = Cover(name, args.covers_path)
    front_cover_path = tub.get_cover("front")
    front_cover_image = tessera.create(front_cover_path)
    back_cover_path = tub.get_cover("back")
    back_cover_image = tessera.create(back_cover_path)

    root.showing = ImageTk.PhotoImage(tessera.resize(front_cover_image,args.width,args.height), master=root)
    realm.config(image=root.showing)
    time.sleep(1.5)

    showing = ImageTk.PhotoImage(tessera.resize(back_cover_image,args.width,args.height),master=root)
    realm.config(image=root.showing)
    text = tessera.read(back_cover_image)

    limit = 5
    to_show = ""
    for line in text:

        if line.isspace():
            to_show += " \n"
            continue

        if limit and text:
            to_show += (line + " \n")
            limit -= 1

        if not limit or not text:
            time_reading = tessera.duration(to_show)
            print(to_show)
            time.sleep(time_reading)
            limit = 5
            to_show = ""

    root.after(300, lambda: slideshow(args, realm, root))


def main():
    global showing
    args = get_args()

    root = Tk()
    root.geometry(str(args.width) + "x" + str(args.height))
    root.showing = ImageTk.PhotoImage(tessera.resize(Image.open("heya.png"),
                                                args.width,
                                                args.height),
                                 master=root)
    realm = Label(root, image=root.showing)
    realm.pack()
    root.after(300, lambda: slideshow(args, realm, root))
    root.mainloop()


if __name__ == '__main__':
    main()
