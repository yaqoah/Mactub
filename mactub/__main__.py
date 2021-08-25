import argparse
import pathlib
import time
import sys

from tkinter import *
from PIL import ImageTk
from book import Book
from cover import Cover
import tessera
from __init__ import __version__


def get_args():
    """get script CL arguments"""

    description = "Mactub - Access and view books downloaded " \
                  "to assist in selecting by reading short synopsis"

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("--width", metavar="'px'",
                        help="What width to display book cover in",
                        default=2560)

    parser.add_argument("--height", metavar="'px'",
                        help="What height to display book cover in",
                        default=1600)

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

    #may add one here for only image/synopsis

    return parser.parse_args()


def slideshow(args, room, root):
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

    front_tk = ImageTk.PhotoImage(tessera.resize(front_cover_image,
                                                 args.width,
                                                 args.height))
    room.config(image=front_tk)
    time.sleep(1.5)

    back_tk = ImageTk.PhotoImage(tessera.resize(back_cover_image,
                                                args.width,
                                                args.height))
    room.config(image=back_tk)
    text_ls = tessera.read(back_cover_image).split("\n\n")
    limit = 3
    to_show = ""
    for few_lines in text_ls:

        if limit and text_ls:
            to_show += few_lines
            text_ls.remove(few_lines)
            limit -= 1

        if not limit or not text_ls:
            time_reading = tessera.duration(to_show)
            print(to_show)
            time.sleep(time_reading/1000)
            limit = 3
            to_show = ""
    root.after(200, slideshow(args, room, root))


def main():
    args = get_args()

    root = Tk()
    root.geometry(str(args.width) + "x" + str(args.height))
    room = Label()
    room.pack()
    root.after(200, slideshow(args, room, root))
    root.mainloop()


if __name__ == '__main__':
    main()
