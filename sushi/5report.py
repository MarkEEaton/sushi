import json
import argparse
from pprint import pprint
from pathlib import Path

def sum_it(directory):
    """ parse the tr_b1 reports """
    pathlist1 = Path(directory).glob("*tr_b1.json")
    pathlist2 = Path(directory).glob("*tr_j1.json")
    pathlist3 = Path(directory).glob("*dr_d*.json")
    pathlist = list(pathlist1) + list(pathlist2) + list(pathlist3)
    for path in pathlist:
        total = 0
        with open(path, 'r') as file_name:
            data = json.loads(file_name.read())
        try:
            for item in data["Report_Items"]:
                for perf in item["Performance"]:
                    for inst in perf["Instance"]:
                        if inst["Metric_Type"] == "Total_Item_Requests":
                            total += inst["Count"]
        except:
            print("error!", data)
        print(path, total, '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates a usage report")
    parser.add_argument(
        "directory",
        metavar="[directory]",
        type=str,
        help="the directory containing the reports",
    )
    args = parser.parse_args()

    sum_it(args.directory)
