# FYP_Program

## Environment
Python == 3.9

Spacy == 3.1.4 -> (en_core_web_lg)

Sumy == 0.8.1

panda == 1.3.3

## Run
### Preparation
1. All the PDF file that want to analysis
2. Web Of Sciences Result

### Case
1. Web Of Sciences Result (WOS)

### Step 1 : Finding the influential articles in WOS result excel 

In wos_simplify.py, fill the line ‘11’ blank with absolute path: 

`WOS_EXCEL_PATH = ` *refer to the Web Of Science Excel file

After fill the path, it can be run it and get the new WOS excel file that is already modify. 

*Note that this step is processed to automatically select influential articles, and the algorithm is to select articles with a number of citations that is higher than the average number of citations for all articles.  

### Step 2 : Download and rename the articles

After you get the new WOS result file, you can download all the article for analysis.  

*Note that all pdf files have to be sorted the same as the new WOS results file \
(Can rename the pdf in ID number)

### Step 3: Get the result for analysis 
In `main.py`, fill all the blank with absolute path: \
`ALL_PDF_PATH =` *refer to the pdf(s) file path\
`UPDATE_WOS_EXCEL_PATH = ` *refer to the output in wos_simplify.py \

Run and get the result with excel file

* The total number of the PDF file need to same with column of the excel file and the sort of the PDF must be same with Excel. \


## Notice
If you want to analysis all the articles in WOS results or use self-organised datasets , you can skip the step 1 and directly jump into the step 2. Note that the row include "Author Full Names", "Article Title", "Publication Year", "Times Cited, WoS Core", "Cited Reference Count", "Abstract", "Publisher" must to remain. Also, the pdf file must sort same with the excel file.