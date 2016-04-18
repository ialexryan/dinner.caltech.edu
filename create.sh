#!/bin/bash

wget --quiet --timestamping "http://dining.caltech.edu/documents/42-boardmenu.pdf"
pdftoppm -f 1 -singlefile -png 42-boardmenu.pdf menu

convert menu.png -crop 245x970+330+143 Monday.png
convert menu.png -crop 245x970+582+143 Tuesday.png
convert menu.png -crop 245x970+827+143 Wednesday.png
convert menu.png -crop 245x970+1072+143 Thursday.png
convert menu.png -crop 245x970+1317+143 Friday.png

