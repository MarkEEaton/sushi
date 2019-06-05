""" test report.py """
from sushi import report
from expected_results2 import (
    expected_JR1_results,
    expected_BR2_results,
    expected_DB1_results,
)
import os

data = "test_data2/"


def test_for_test_data():
    assert os.path.isdir("./" + data), "Test data should be available"


def test_jr1_exists():
    with open(os.devnull, "w") as outfile:
        report_data = report.jr1(outfile, data)
        assert report_data is not None, "jr1() returns data"


def test_jr1_returns():
    with open(os.devnull, "w") as outfile:
        report_data = report.jr1(outfile, data)
        for item in report_data:
            assert report_data[item] == expected_JR1_results[item], "jr1() data is as expected"


def test_br2_exists():
    with open(os.devnull, "w") as outfile:
        report_data = report.br2(outfile, data)
        assert report_data is not None, "br1() returns data"


def test_br2_returns():
    with open(os.devnull, "w") as outfile:
        report_data = report.br2(outfile, data)
        for item in report_data:
            assert report_data[item] == expected_BR2_results[item], "br1() data is as expected"


def test_db1_exists():
    with open(os.devnull, "w") as outfile:
        report_data = report.db1(outfile, data)
        assert report_data is not None, "db1() returns data"


def test_db1_returns():
    with open(os.devnull, "w") as outfile:
        report_data = report.db1(outfile, data)
        for item in report_data:
            assert report_data[item] == expected_DB1_results[item], "db1() data is as expected"


if __name__ == "__main__":
    test_jr1_returns()