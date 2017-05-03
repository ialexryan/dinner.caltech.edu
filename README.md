# dinner.caltech.edu

* [`download.sh`](download.sh) scrapes the PDF menu from the dining website to the server and converts it to a PNG.
* [`crop.py`](crop.py) uses basic image processing to crop the menu into five day PNGs.

    [the above two scripts run on a cron job every hour]

* [`logic.js`](logic.js) determines the current day and requests the appropriate image asset from the server.
