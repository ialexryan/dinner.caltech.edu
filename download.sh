#!/bin/bash

wget --quiet --timestamping "http://dining.caltech.edu/documents/42-boardmenu.pdf"
pdftoppm -f 1 -singlefile -png 42-boardmenu.pdf menu

