import pandas
import pandas as pd
import numpy as np
import datetime

SHEET_NAME = "savedrecs"
YEAR = int(datetime.date.today().year)
dataframe = ""

#Pls fill the absolute path
WOS_EXCEL_PATH = "C:\\Users\itaug\Desktop\\testfyp\wos_result_411.xlsx"


def revise_WOS_output():
    revise_WOS_dataframe(WOS_EXCEL_PATH)
    # Output to the excel file
    dataframe.reset_index(drop=True, inplace=True)
    dataframe.to_excel("revise_wos_result.xlsx", columns=["Author Full Names", "Article Title", "Publication Year",
                                               "Times Cited, WoS Core", "Cited Reference Count", "Abstract",
                                               "Publisher"], index=True, sheet_name='savedrecs')


def revise_WOS_dataframe(WOS_EXCEL_PATH):
    global dataframe
    dataframe = pd.read_excel(WOS_EXCEL_PATH, sheet_name=SHEET_NAME)
    cite_mean = dataframe['Times Cited, WoS Core'].mean()

    # define the value of "time cited" are their over the mean
    dataframe['Count_Cited'] = np.where(dataframe['Times Cited, WoS Core'] < round(cite_mean), 0, 1)

    # if publish year are empty == 2022
    dataframe['Publication Year'] = np.where(np.isnan(dataframe['Publication Year']), YEAR,
                                             dataframe['Publication Year'])

    # chose the columns ['Count_Cited'] == 1
    dataframe = dataframe[dataframe['Count_Cited'].isin([1])].sort_values(by='Publication Year')

    # save the abstract to list
    # abstract_list = dataframe["Abstract"].tolist()

    return dataframe

def modify_WOS_dataframe(WOS_EXCEL_PATH):
    global dataframe
    dataframe = pd.read_excel(WOS_EXCEL_PATH, sheet_name=SHEET_NAME)
    return dataframe

def modify_VOS_dataframe(VOS_EXCEL_PATH):
    global dataframe
    dataframe = pd.read_excel(VOS_EXCEL_PATH, sheet_name=SHEET_NAME)
    return dataframe

def pdf_dataframe(PDF_EXCEL_PATH):
    global dataframe
    dataframe = pd.read_excel(PDF_EXCEL_PATH, sheet_name='my dataframe')
    return dataframe

if __name__ == "__main__":
    revise_WOS_output()