# dinner.caltech.edu

* `download.sh` scrapes the PDF menu from the dining website to the server and converts it to a PNG.
* `crop.py` uses basic image processing to crop the menu into five day PNGs.

    [the above runs on a cron job every hour]

* `logic.js` determines the current day and requests the appropriate image asset from the server.
