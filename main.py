import pandas as pd
import regex as re

with open('kraftstoff.csv', 'r') as f:
    for i in f:
        #print(i)
        if 'Kategorie' in i:
            datum = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', i)
            print(datum.group(0))

#df = pd.read_csv('kraftstoff.csv')
#print(df)