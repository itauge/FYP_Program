import pandas
import pandas as pd
import numpy as np
import datetime

WOS_EXCEL_PATH = "C:\\Users\itaug\Desktop\Keyword1_WithAbstract.xlsx"
VOS_EXCEL_PATH = "C:\\Users\itaug\Downloads\91_cluster.xls"
SHEET_NAME = "savedrecs"
YEAR = int(datetime.date.today().year)
dataframe = ""


def output():
    modify_WOS_dataframe()
    # Output to the excel file
    dataframe.to_excel("output.xlsx", columns=["Author Full Names", "Article Title", "Publication Year",
                                               "Times Cited, WoS Core", "Cited Reference Count", "Abstract",
                                               "Publisher"], index=False)


def modify_WOS_dataframe():
    global dataframe
    dataframe = pd.read_excel(WOS_EXCEL_PATH, sheet_name=SHEET_NAME)
    cite_mean = dataframe['Times Cited, WoS Core'].mean()

    # define the value of "time cited" are their over the mean
    dataframe['Count_Cited'] = np.where(dataframe['Times Cited, WoS Core'] < cite_mean, 0, 1)

    # if publish year are empty == 2022
    dataframe['Publication Year'] = np.where(np.isnan(dataframe['Publication Year']), YEAR,
                                             dataframe['Publication Year'])

    # chose the columns ['Count_Cited'] == 1
    dataframe = dataframe[dataframe['Count_Cited'].isin([1])].sort_values(by='Publication Year')

    # save the abstract to list
    # abstract_list = dataframe["Abstract"].tolist()

    return dataframe


def modify_VOS_dataframe():
    global dataframe
    dataframe = pd.read_excel(VOS_EXCEL_PATH, sheet_name=SHEET_NAME)
    return dataframe
