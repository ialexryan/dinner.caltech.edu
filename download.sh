#!/bin/bash

# TODO this only works on Mondays
fname="Board_Menu_$(date +%-m).$(date +%-d).pdf"
wget --quiet --timestamping "http://dining.sites.caltech.edu/documents/3195/$fname"
pdftoppm -f 1 -singlefile -png $fname menu
