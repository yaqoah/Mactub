import argparse
import pathlib
import sys

from tkinter import *
from PIL import ImageTk, Image
from book import Book
from cover import Cover
import tessera
from __init__ import __version__

cover = None
synopsis = ""


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

    # add default img

    return parser.parse_args()


def get_synopsis(args, realm, root, to_show):
    global cover, synopsis

    realm.config(image=cover)

    limit = 5
    ended = False
    for line in synopsis:

        if len(synopsis) == 1:
            to_show += (line + " \n" + synopsis[0])
            print(to_show)
            ended = True
            break

        if line.isspace():
            synopsis.remove(line)

        elif limit:
            to_show += (line + " \n")
            synopsis.remove(line)
            limit -= 1

        elif not limit:
            time_reading = tessera.duration(to_show)
            print(to_show)
            to_show = ""
            to_show += (line + " \n")
            synopsis.remove(line)
            break

    if ended:
        root.after(time_reading, lambda: slideshow(args, realm, root))

    else:
        root.after(time_reading, lambda: get_synopsis(args, realm, root, to_show))


def slideshow(args, realm, root):
    global cover, synopsis

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

    front = ImageTk.PhotoImage(tessera.resize(front_cover_image, args.width, args.height), master=root)
    back = ImageTk.PhotoImage(tessera.resize(back_cover_image, args.width, args.height), master=root)
    synopsis = tessera.read(back_cover_image)
    synopsis.append

    cover = front  # do I need this line? really?
    realm.config(image=cover)
    cover = back
    root.after(1500, lambda: get_synopsis(args, realm, root, "\n"))


def main():
    global cover
    args = get_args()

    root = Tk()
    root.geometry(str(args.width) + "x" + str(args.height))
    cover = ImageTk.PhotoImage(tessera.resize(Image.open("heya.png"),
                                              args.width,
                                              args.height),
                               master=root)
    realm = Label(root, image=cover)
    realm.pack()
    slideshow(args, realm, root)
    root.mainloop()


if __name__ == '__main__':
    main()
