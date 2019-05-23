""" produce a single report from all of the downloaded reports """

import csv
import argparse
from pathlib import Path

def jr1(outfile, directory):
    """ make the JR1 report """
    print('')
    print('Journal Report 1')
    print('----------------------------------------')
    outfile.write('Journal Report 1\n')
    outfile.write('\n')
    outfile.write('Database,Reporting Period Total\n')
    pathlist = Path(directory).glob('*-JR1.tsv')
    for path in pathlist:
        with open(path, encoding='latin-1') as file1:
            csv1 = list(csv.reader(file1, delimiter='\t'))
            if csv1[8][2] == 'GOLD':
                csv1[8][2] = 'Gale'
            print('{0:>32} {1:>25} {2:<6}'.format(csv1[8][2],
                                                  'reporting period total:',
                                                  csv1[8][7]))
            outfile.write('{0},{1}\n'.format(csv1[8][2], csv1[8][7]))

def db1(outfile, directory):
    """ make the DB1 report """
    print('')
    print('Database Report 1')
    print('-----------------------------------------')
    outfile.write('\n')
    outfile.write('Database Report 1\n')
    outfile.write('\n')
    outfile.write(',Searches,Views\n')
    pathlist = Path(directory).glob('*-DB1.tsv')
    for path in pathlist:
        searches_total = 0
        views_total = 0
        with open(path, encoding='latin-1') as file2:
            csv2 = list(csv.reader(file2, delimiter='\t'))
            if csv2[8][2] == 'GOLD':
                csv2[8][2] = 'Gale'
            for line in csv2:
                try:
                    if line[3] == 'Regular Searches':
                        searches_total += int(line[4])
                    if line[3] == 'Record Views':
                        views_total += int(line[4])
                except IndexError:
                    pass
            print('{0:>32} {1:>10} {2:<8}'.format(csv2[8][2], 'searches:', str(searches_total)))
            print('{0:>32} {1:>10} {2:<8}'.format('', 'views:', str(views_total)))
            outfile.write('{0},{1},{2}\n'.format(csv2[8][2], str(searches_total), str(views_total)))

def br2(outfile, directory):
    """ make the br2 report """
    print('')
    print('Book Report 2')
    print('-----------------------------------------')
    outfile.write('\n')
    outfile.write('Book Report 2\n')
    outfile.write('\n')
    outfile.write('Database,Reporting Period Total\n')
    pathlist = Path(directory).glob('*-BR2.tsv')
    for path in pathlist:
        with open(path, encoding='latin-1') as file3:
            csv3 = list(csv.reader(file3, delimiter='\t'))
            print('{0:>32} {1:>25} {2:<6}'.format(csv3[8][2],
                                                  'reporting period total:',
                                                  csv3[8][7]))
            outfile.write('{0},{1}\n'.format(csv3[8][2], csv3[8][7]))

def main():
    """ make it run """
    parser = argparse.ArgumentParser(description='Generates a usage report')
    parser.add_argument('directory', metavar='[directory]', type=str,
                        help='the directory containing the reports')
    args = parser.parse_args()

    with open(args.directory + 'summary-report.csv', 'w') as outfile:
        jr1(outfile, args.directory)
        db1(outfile, args.directory)
        br2(outfile, args.directory)
    print('')


if __name__ == '__main__':
    main()
