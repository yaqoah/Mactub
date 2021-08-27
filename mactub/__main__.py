import argparse
import pathlib
import sys

from tkinter import *
from PIL import ImageTk, Image
from book import Book
from cover import Cover
import tessera
from __init__ import __version__

mac, args, realm, root, synopsis, cover = [None for var in range(6)]


def get_args():
    """get script CL arguments"""

    description = "~Mactub~ Access books in a device" \
                  " and print synopsis in back"

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("--width", metavar="'px'",
                        help="What width to display book cover in",
                        default=640)

    parser.add_argument("--height", metavar="'px'",
                        help="What height to display book cover in",
                        default=620)

    parser.add_argument("--books_path", metavar="'path/to/dir'",
                        help="Path to folder containing "
                             "(i.e: .PDF,.EPUB,.TXT)"
                             "book files",
                        default=pathlib.Path("D:/Books/Texts"),
                        type=pathlib.Path)

    parser.add_argument("--covers_path", metavar="'path/to/dir'",
                        help="Path to folder containing "
                             "(i.e: .PNG,.JPEG,.GIF)"
                             "book covers (back,front) file",
                        default=pathlib.Path("D:/Books/Covers"),
                        type=pathlib.Path)

    parser.add_argument("--default_img", metavar="'path/to/dir'",
                        help="What image will be displayed "
                             "upon initialisation of window",
                        default=pathlib.Path("D:/Books/Covers/heya.png"),
                        type=pathlib.Path)

    parser.add_argument("--version", action="store_true",
                        help="'Mactub' version")

    parser.add_argument("--display", action="store_true",
                        help="Allow slideshow view of book covers"
                             "in synchrony with "
                             "synopsis of book printed")

    return parser.parse_args()


def get_synopsis(to_show, index, last):
    """
    Prints out text in back cover periodically
    :param to_show: predetermined text to show for following period
    :param index: index of list to start adding to text string from
    :param last: last element in list
    """
    global realm, cover, synopsis

    realm.config(image=cover)

    limit = 5
    ended = False

    for line in synopsis[index + 1:]:

        if line == last:
            to_show += ("\n" + line)
            time_reading = tessera.duration(to_show)
            print(to_show)
            ended = True
            break

        if not limit:
            time_reading = tessera.duration(to_show)
            print(to_show)

            if not line.strip():
                limit += 1
                continue

            else:
                to_show = ""
                to_show += ("\n" + line)
                index = synopsis.index(line)
                break

        if limit:
            to_show += ("\n" + line)
            limit -= 1
            index = synopsis.index(line)

    if ended:
        root.after(time_reading, lambda: slideshow_manager())

    else:
        root.after(time_reading, lambda: get_synopsis(to_show, index, last))


def slideshow_manager():
    """
    Chooses book to present is image slideshow
    and show synopsis in console
    """
    global mac, cover, realm, synopsis, args, root

    mac.fetch()
    name = mac.get_title()
    author = mac.get_author()
    print(f"{author}-  author of: {name}")

    tub = Cover(name, args.covers_path)
    front_cover_path = tub.get_cover("front")
    front_cover_image = tessera.resize(tessera.create(front_cover_path), args.width, args.height)
    back_cover_path = tub.get_cover("back")
    back_cover_image = tessera.create(back_cover_path)
    temp = tessera.resize(front_cover_image, args.width, args.height)

    front = ImageTk.PhotoImage(front_cover_image, master=root)

    cover = front
    realm.config(image=front)
    realm.front_cover_image = front

    back = ImageTk.PhotoImage(tessera.resize(back_cover_image, args.width, args.height), master=root)
    synopsis = tessera.read(back_cover_image)

    for line in reversed(synopsis):

        if not line.strip():
            continue

        else:
            last = line
            break

    cover = back
    root.after(7000, lambda: get_synopsis("\n", -1, last))


def main():
    global args, mac, root, cover, realm

    args = get_args()
    mac = Book(args.books_path)

    root = Tk()
    root.geometry(str(args.width) + "x" + str(args.height))
    cover = ImageTk.PhotoImage(tessera.resize(Image.open(args.default_img),
                                              args.width,
                                              args.height),
                               master=root)
    realm = Label(root, image=cover)
    realm.pack()
    root.after(200, lambda: slideshow_manager())
    root.mainloop()


if __name__ == '__main__':
    main()
