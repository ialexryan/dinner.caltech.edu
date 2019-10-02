#!/bin/bash

url=http://dining.sites.caltech.edu/$(curl -s http://dining.caltech.edu/locations/chandler | grep -o "documents/[0-9]*/Board[A-Za-z0-9_\.]*\.pdf" | head -1)

wget -O menu.pdf --quiet --timestamping "$url"
pdftoppm -png menu.pdf menu
