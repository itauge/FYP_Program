# Extract keywords from multiple PDF files, create a dataframe, then export it to an .xlsx file.
import io

import pdfminer
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

import os                        # provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory
import pandas as pd              # flexible open source data analysis/manipulation tool
import glob                      # generates lists of files matching given patterns
import pdfplumber                # extracts information from .pdf documents
#hello world
"""
Obtain key words from repetitive documents, then extract as a dataframe to an .xlsx !
"""

# Perform layout analysis for all text
laparams = pdfminer.layout.LAParams()
setattr(laparams, 'all_texts', True)

#solve the spacing problem method
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=laparams)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text.lower()

#Define the range between word
def get_keyword(start, end, text):
    """
    start: should be the word prior to the keyword.
    end: should be the word that comes after the keyword.
    text: represents the text from the page(s) you've just extracted.
    """
    for i in range(len(start)):
        try:
            field = ((text.split(start[i]))[1].split(end[i])[0])
            return field
        except:
            continue

def pdf_capture():
    # create an empty dataframe, from which keywords from multiple .pdf files will be later appended by rows.
    my_dataframe = pd.DataFrame()

    for files in glob.glob("H:\FYP\Team 6\Categorized 44 Selected Journal\Cluster 2\*.pdf"):

            text = extract_text_from_pdf(files)
            text = " ".join(text.split())

            # with pdfplumber.open(files) as pdf:
            #     page = pdf.pages[0]
            #     text = page.extract_text()
            #     text = " ".join(text.split())

            # concluding remarks

            # obtain keyword #1
            start = ['abstract']
            end = ['introduction']
            keyword1 = get_keyword(start, end, text.lower())

            # obtain keyword #2
            start = ['conclusion']
            end = ['references']
            keyword2 = get_keyword(start, end, text.lower())

            # create a list with the keywords extracted from current document.
            my_list = [keyword1, keyword2]

            # append my list as a row in the dataframe.
            my_list = pd.Series(my_list)

            # append the list of keywords as a row to my dataframe.
            my_dataframe = my_dataframe.append(my_list, ignore_index=True)

            print(keyword1, keyword2)
            print("Document's keywords have been extracted successfully!")

    # rename dataframe columns using dictionaries.
    my_dataframe = my_dataframe.rename(columns={0:'Abstract',
                                                    1:'Conclusion'
                                                    })

    # change my current working directory
    save_path = ('H:\FYP\Team 6\Categorized 44 Selected Journal\Cluster 2')
    os.chdir(save_path)

    # extract my dataframe to an .xlsx file!
    my_dataframe.to_excel('sample_excel.xlsx', sheet_name = 'my dataframe')
    # print("")
    # print(my_dataframe)

if __name__ == '__main__':
    pdf_capture()