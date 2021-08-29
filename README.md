# :green_book: Mactub

[![PyPI version shields.io](https://img.shields.io/pypi/v/0.0.1)](https://pypi.python.org/pypi/ansicolortags/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/travis/com/yaqoah/Mactub)](https://app.travis-ci.com/github/yaqoah/Mactub)

***Mactub*** is a daemon that accesses books by ```path``` 
and reads downloaded book jackets in the specified directory, 
to generate the synopsis of a book in the console periodically,
presenting a slideshow of books available by cover in synchrony via a window.

## Installation

    pip3 install --user mactub

## Usage 

```
usage: mactub [-h] [--width 'px'] [--height 'px'] [--books_path 'path/to/dir'] [--covers_path 'path/to/dir'] [--default_img 'path/to/dir'] [--version]

mactub - Read and display books and respective synopsis periodically.

optional arguments: 
  -h, --help,
  --width 'px'    What width to display book cover in (and the window).
  --height 'px'   What height to display book cover in
  --books_path 
    'path/to/dir' Path to folder containing (.PDF/.EPUB/.TXT) book files.
  --covers_path 
    'path/to/dir' Path to folder containing (.PDF/.EPUB/.TXT) cover files.
  --default_img 
    'path/to/dir' What image will be displayed intially on window (path)
  --version       'mactub' version.
  --display       default: True. Show slideshow of covers.
    
```
