#!/bin/bash

url=http://dining.sites.caltech.edu/$(curl -s http://dining.sites.caltech.edu/students | grep -o "/documents/[0-9]*/Board[A-Za-z0-9_\.]*\.pdf")

wget -O menu.pdf --quiet --timestamping "$url"

rm menu-*.png
pdftoppm -png menu.pdf menu
