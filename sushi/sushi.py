""" a tool to download counter reports """
import datetime
import logging
import pycounter
import cred
import argparse

logging.basicConfig(level=logging.DEBUG, filename="debug.log", filemode="w")

default_start_date = datetime.date(2018, 5, 1)
default_end_date = datetime.date(2019, 4, 30)


def main(data, directory):
    """ get the reports """
    for item in data:

        custom = '\033[93m'
        # use specified dates or default dates
        if item.get("custom_start_date"):
            start_date = item["custom_start_date"]
            custom = custom + "Custom start date. "
        else:
            start_date = default_start_date
        if item.get("custom_end_date"):
            end_date = item["custom_end_date"]
            custom = custom + "Custom end date. "
        else:
            end_date = default_end_date
        custom = custom + '\033[0m'

        # run the reports
        for report_name in item["reports"]:
            outfile = directory + item["name"] + "-" + report_name + ".tsv"
            try:
                report = pycounter.sushi.get_report(
                    wsdl_url=item["wsdl_url"],
                    requestor_id=item.get("requestor_id"),
                    start_date=start_date,
                    end_date=end_date,
                    customer_reference=item["customer_reference"],
                    customer_name=item.get("customer_name"),
                    release=item["release"],
                    report=report_name,
                    sushi_dump=True,
                )
                report.write_tsv(outfile)
                print(outfile, custom)
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
    args = parser.parse_args()

    if args.directory[-1] != "/":
        args.directory = args.directory + "/"

    main(cred.dbs4, args.directory)
