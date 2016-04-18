#!/bin/bash

wget --quiet --timestamping "http://dining.caltech.edu/documents/42-boardmenu.pdf"
pdftoppm -f 1 -singlefile -png 42-boardmenu.pdf menu

convert menu.png -crop 245x925+307+143 Monday.png
convert menu.png -crop 245x925+552+143 Tuesday.png
convert menu.png -crop 245x925+797+143 Wednesday.png
convert menu.png -crop 245x925+1042+143 Thursday.png
convert menu.png -crop 270x925+1287+143 Friday.png

