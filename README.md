## FYP_Program

##Environment
Python == 3.9

Spacy == 3.1.4 -> (en_core_web_lg)

Sumy == 0.8.1

panda == 1.3.3

##Run
###Preparation
1. All the PDF file that want to analysis
2. VOSviewer Result (Better) OR Web Of Sciences Result

###Two case
1. VOSviewer (Excel)   ***Recommend**
2. Web Of Sciences Result (Excel)

In `main.py`, fill all the blank with absolute path: \
`ALL_PDF_PATH =` *refer to the pdf(s) file path\
`WOS_EXCEL_PATH = ` *refer to the Web Of Science Excel file \
`VOS_EXCEL_PATH = ` *refer to the VOSviewer Result Excel file

Run and get the result with excel file

##notice
If you decide to use the Case 2(Web Of Seiences Result), note that the WOS results are processed to automatically select influential articles, and the algorithm is to select articles with a number of citations that is higher than the average number of citations for all articles.
