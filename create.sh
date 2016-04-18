#!/bin/bash

wget --quiet --timestamping "http://dining.caltech.edu/documents/42-boardmenu.pdf"
pdftoppm -f 1 -singlefile -png 42-boardmenu.pdf menu

convert menu.png -crop 245x925+325+143 Monday.png
convert menu.png -crop 245x925+577+143 Tuesday.png
convert menu.png -crop 245x925+822+143 Wednesday.png
convert menu.png -crop 245x925+1067+143 Thursday.png
convert menu.png -crop 245x925+1312+143 Friday.png

