""" a tool to download counter reports """
import datetime
import cred
import pycounter

def main():
    """ get the reports """
    data = cred.dbs
    for item in data:
        for report_name in item['reports']:
            outfile = item['name'] + '-' + report_name + '.tsv'
            try:
                report = pycounter.sushi.get_report(wsdl_url=item['wsdl_url'],
                                                    start_date=datetime.date(2017, 7, 1),
                                                    end_date=datetime.date(2018, 6, 30),
                                                    requestor_id=item['requestor_id'],
                                                    customer_reference=item['customer_reference'],
                                                    report=report_name,
                                                    release=item['release'])
                report.write_tsv(outfile)
            except Exception as e:
                print(outfile + ' : report not found : ' + e.__class__.__name__)
                raise

if __name__ == '__main__':
    main()
