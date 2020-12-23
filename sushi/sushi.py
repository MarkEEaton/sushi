""" a tool to download counter reports """
import requests
import json
import datetime
import logging
import pycounter
import cred
import argparse
from time import sleep
from pprint import pprint
from dateutil.rrule import rrule, MONTHLY

logging.basicConfig(level=logging.DEBUG, filename="debug.log", filemode="w")

default_start_date = datetime.date(2019, 7, 1)
default_end_date = datetime.date(2020, 6, 30)


def five(data, args):
    """ Get the COUNTER 5 reports """
    for item in data:

        custom = "\033[93m"
        # use specified dates or default dates
        if item.get("custom_start_date"):
            start_date = item["custom_start_date"]
            custom = custom + "Custom start date. "
        else:
            start_date = default_start_date

        if item.get("custom_end_date"):
            end_date = item["custom_end_date"]
            custom = custom + "Custom end date."
        else:
            end_date = default_end_date

        custom = custom + "\033[0m"

        rest_str = "?"
        for a in item["auth"]:
            rest_str = rest_str + a + "=" + item["auth"][a] + "&"

        # run the reports
        for report_name in item["reports"]:
            sleep(3)
            outfile = args.directory + item["name"] + "-" + report_name + ".json"
            try:
                headers = {
                    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"
                }  # necessary for Wiley COUNTER 5 reports
                url = (
                    item["wsdl_url"]
                    + report_name
                    + rest_str
                    + "begin_date="
                    + start_date.strftime("%Y-%m-%d")
                    + "&end_date="
                    + end_date.strftime("%Y-%m-%d")
                )
                print(url)
                resp = requests.get(url, headers=headers)

                j = json.loads(resp.text)
                with open(outfile, "w") as f:
                    json.dump(j, f)
                print(outfile, custom)

            except Exception as e:
                raise
                print(outfile + " : report not found : " + e.__class__.__name__, custom)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetches counter reports")
    parser.add_argument(
        "directory",
        metavar="[output directory]",
        type=str,
        help="the directory to put the reports in",
    )
    parser.add_argument(
        "version",
        metavar="[SUSHI version]",
        type=int,
        help="the sushi version you want to use",
    )
    args = parser.parse_args()

    if args.directory[-1] != "/":
        args.directory = args.directory + "/"

    if args.version == 5:
        five(cred.dbs5, args)
    else:
        print("Unrecognized version. Only version 5 is currently supported.")
