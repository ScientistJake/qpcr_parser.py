import sys
import pandas as pd

infile = sys.argv[1]
#note that I need Ur for universal newline
opened = open(infile, 'Ur')

#get the values from the qpcr file
d = []
for line in opened:
    cols=line.split('\t')
    #this loop skips the empty lines and gets data
    if cols[0].isdigit():  
        if cols[1] != 'NORT':
            sample = cols[1]
            gene = cols[2]
            ct = cols[5]    
            d.append({'sample': sample, 'gene': gene, 'ct': ct})

#this function works ok to convert to a df
df = pd.DataFrame(d, dtype=float)

#I need to add another variable so the index will be 'unique'
df['replicate'] = [1,2,3] * (len(d)/3)
#replace undetermined with python friendly NaN
df = df.replace('Undetermined', 'NaN', regex=True)
#get ct to float (instead of string)
df['ct'] = df['ct'].astype(float)
#gets the table in wide formate

#write it out
if sys.argv[2] == 'long':
    outfile = open('%s_parsed_long.txt' %(sys.argv[1][:-4]), 'w')
    df.to_csv(outfile, sep='\t')

if sys.argv[2] == 'wide':
    outfile = open('%s_parsed_wide.txt' %(sys.argv[1][:-4]), 'w')
    df = df.pivot_table(index=['sample','replicate'], columns='gene',values='ct')
    df.to_csv(outfile, sep='\t')
