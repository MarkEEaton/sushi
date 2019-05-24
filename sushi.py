""" a tool to download counter reports """
import datetime
import logging
import pycounter
import cred
import argparse

logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w')

def main(data, directory):
    """ get the reports """
    for item in data:
        for report_name in item['reports']:
            outfile = directory + item['name'] + '-' + report_name + '.tsv'
            try:
                report = pycounter.sushi.get_report(wsdl_url=item['wsdl_url'],
                                                    start_date=datetime.date(2018, 5, 1),
                                                    end_date=datetime.date(2019, 4, 30),
                                                    requestor_id=item['requestor_id'],
                                                    customer_reference=item['customer_reference'],
                                                    customer_name=item.get('customer_name'),
                                                    release=item['release'],
                                                    report=report_name,
                                                    sushi_dump=True)
                report.write_tsv(outfile)
                print(outfile)
            except Exception as e:
                print(outfile + ' : report not found : ' + e.__class__.__name__)
                pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates a usage report')
    parser.add_argument('directory', metavar='[directory]', type=str,
                        help='the directory containing the reports')
    args = parser.parse_args()
    #main(cred.dbs4, args.directory)
    main(cred.dbs5, args.directory)
