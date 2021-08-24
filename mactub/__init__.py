"""

[  ¬¬¬ ... ¬¬¬  >  ¬¬¬ ...  ]
[  ... ¬¬¬ ...  <  ... ¬¬¬  ]
[  ╔╦╗ ╔═╗ ╔═╗ ╔╦╗ ╦ ╦ ╔╗   ]
[  ║║║ ╠═╣ ║    ║  ║ ║ ╠╩╗  ]
[  ╩ ╩ ╩ ╩ ╚═╝  ╩  ╚═╝ ╚═╝  ]
[  ... ¬¬¬ ...  <  ... ¬¬¬  ]
[  ¬¬¬ ... ¬¬¬  >  ¬¬¬ ...  ]

~     مكتب     ~
by Ahmed Yousif
"""
# add version
from cover import Cover
from book import Book
from tessera import read_by_path

btest = Book()
btest.fetch()
book = btest.get_title()
print(book)

test = Cover(book)
print(test.get_cover("front"))
print(test.get_cover("back"))
read_by_path(test.get_cover("back"))
