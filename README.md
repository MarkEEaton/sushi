# sushi
Scripts to use pycounter to gather and summarize COUNTER reports

These two scripts allow for the automation of fetching and parsing COUNTER reports. They are built on top of the excellent work done by the [pycounter](https://github.com/pitthsls/pycounter) library.

#### To use sushi.py

`sushi.py` fetches COUNTER reports from vendors' SUSHI endpoints. Populate `cred.template` with your SUSHI credentials (as a list of dictionaries), and rename it `cred.py`. Then run:

`$ python sushi.py path/to/where/you/want/the/reports`

#### To use report.py

`report.py` summarizes information from many COUNTER reports into one `.csv` report. To use it, run:

`$ python report.py /path/to/where/your/reports/live`.
