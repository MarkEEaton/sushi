import csv 

with open('examplecounterreport.tsv', encoding='latin-1') as f:
    c = list(csv.reader(f, delimiter='\t'))

print(c[8][2] + ': ' + c[8][7])
