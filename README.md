# qpcr_parser.py
This function reads in a qpcr text export from a AB 7900HT 384 well qpcr machine (SDS software) and puts the results into long or wide format for analysis.
## Usage:
`qpcr_parser.py infile format`  
infile: file from txt export of SDS  
format: `long` or `wide`  

## Output: 
`infile_parsed_format.txt`  
Outputs a parsed file in long or wide format  

## Example outputs: 
````
python qpcr_parser.py ~QPCR-rep1.txt long
head QPCR-rep1_parsed_long.txt

	ct	gene	sample	replicate
0	20.283422	Actin	20-Hpa-A	1
1	20.22835	Actin	20-Hpa-A	2
2	20.246635	Actin	20-Hpa-A	3
3	19.674856	Actin	20-Hpa-C	1
4	19.629658	Actin	20-Hpa-C	2
5	19.60467	Actin	20-Hpa-C	3

python qpcr_parser.py ~QPCR-rep1.txt wide
head QPCR-rep1_parsed_wide.txt
sample	replicate	Actin	R_BMP2_4	R_Bra	
20-Hpa-A	1	20.283422	29.478012	31.504375
20-Hpa-A	2	20.22835	29.18948	32.223377
20-Hpa-A	3	20.246635	29.463856	31.789627
20-Hpa-C	1	19.674856	30.925789	31.71433
20-Hpa-C	2	19.629658	29.980974	35.7609
20-Hpa-C	3	19.60467	30.315958	32.874588
``` 
