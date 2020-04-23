""" a tool to download counter reports """
import datetime
import logging
import pycounter
import cred
import argparse
from dateutil.rrule import rrule, MONTHLY

logging.basicConfig(level=logging.DEBUG, filename="debug.log", filemode="w")

default_start_date = datetime.date(2018, 5, 1)
default_end_date = datetime.date(2019, 4, 30)


def main(data, args):
    """ get the reports """
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

        date_list = [dt for dt in rrule(MONTHLY, dtstart=start_date, until=end_date)]
        formatted_date = [d.strftime("%b-%Y") for d in date_list]

        # run the reports
        for report_name in item["reports"]:
            warning = ""
            outfile = args.directory + item["name"] + "-" + report_name + ".tsv"
            try:
                report = pycounter.sushi.get_report(
                    wsdl_url=item["wsdl_url"],
                    requestor_id=item.get("requestor_id"),
                    start_date=start_date,
                    end_date=end_date,
                    customer_reference=item["customer_reference"],
                    customer_name=item.get("customer_name"),
                    release=args.version,
                    report=report_name,
                    sushi_dump=True,
                )

                # check that all of the dates are present in the table
                table = report.as_generic()
                for d in formatted_date:
                    if d in table[7]:
                        pass
                    else:
                        warning = "\033[91mDates missing!\033[0m"

                report.write_tsv(outfile)
                print(outfile, custom, warning)

            except Exception as e:
                print(outfile + " : report not found : " + e.__class__.__name__, custom)
                pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetches counter reports")
    parser.add_argument(
        "directory",
        metavar="[directory]",
        type=str,
        help="the directory to put the reports in",
    )
    parser.add_argument(
        "version",
        metavar="[version]",
        type=int,
        help="the sushi version you want to use",
    )
    args = parser.parse_args()

    if args.directory[-1] != "/":
        args.directory = args.directory + "/"

    if args.version == 4:
        main(cred.dbs4, args)
    elif args.version == 5:
        main(cred.dbs5, args)
    else:
        print("Unrecognized version. Please select 4 or 5")
