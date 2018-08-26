""" produce a single report from all of the downloaded reports """

import csv
from pathlib import Path

def main():
    """ make the report """
    print('')
    print('Journal Report 1')
    print('----------------------------------------')
    pathlist = Path('reports/').glob('*-JR1.tsv')
    for path in pathlist:
        with open(path, encoding='latin-1') as file1:
            c = list(csv.reader(file1, delimiter='\t'))
            print('{0:<33} {1:<25} {2:>6}'.format(c[8][2], 'reporting period total:', c[8][7]))

    print('')
    print('Database Report 1')
    print('-----------------------------------------')
    pathlist = Path('reports/').glob('*-DB1.tsv')
    for path in pathlist:
        searches_total = 0
        views_total = 0
        with open(path, encoding='latin-1') as file2:
            c = list(csv.reader(file2, delimiter='\t'))
            for line in c:
                try:
                    if line[3] == 'Regular Searches':
                        searches_total += int(line[4])
                    if line[3] == 'Record Views':
                        views_total += int(line[4])
                except IndexError:
                    pass
            print('{0:<33} {1:>10} {2:>8}'.format(c[8][2], 'searches:', str(searches_total)))
            print('{0:<33} {1:>10} {2:>8}'.format(c[8][2], 'views:', str(views_total)))

    print('')

if __name__ == '__main__':
    main()
