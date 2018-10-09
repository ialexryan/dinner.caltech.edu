#!/bin/bash

url=http://dining.sites.caltech.edu/$(curl -s http://dining.sites.caltech.edu/students | grep -o "/documents/[0-9]*/Board_Menu_[0-9]*\.[0-9]*\.pdf")

wget -O menu.pdf --quiet --timestamping "$url"
pdftoppm -f 1 -singlefile -png menu.pdf menu
