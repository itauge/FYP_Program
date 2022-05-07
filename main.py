import sumy_summarize
import ts6
import wos_simplify
import pandas
import pdf_capture

MINI_WORD = 190
MID_WORD = 530
LONG_WORD = 1080
ABSTRACT_RESULT_LIST = []
CONCLUSION_RESULT_LIST = []

#Absolute Path
ALL_PDF_PATH = "C:\\Users\itaug\Desktop\FYP\\all_pdf\*.pdf"
WOS_EXCEL_PATH = "C:\\Users\itaug\Desktop\Keyword1_WithAbstract.xlsx"
VOS_EXCEL_PATH = "C:\\Users\itaug\Downloads\85_cluster.xls"


# Count the word
def word_count(string):
    word = len(str(string).strip().split(" "))
    return word


def main():

    # Method 1 : WOS dataframe
    # dataframe = wos_simplify.modify_WOS_dataframe(WOS_EXCEL_PATH)
    # abstract_list = dataframe["Abstract"].tolist()

    # Method 2 : VOS dataframe (Better)
    dataframe_vos = wos_simplify.modify_VOS_dataframe(VOS_EXCEL_PATH)
    id_list = dataframe_vos["id"].tolist()
    cluster_list = dataframe_vos["cluster"].tolist()
    abstract_list = dataframe_vos["Abstract"].tolist()


    # dataframe_pdf = wos_simplify.pdf_dataframe()
    dataframe_pdf = pdf_capture.pdf_capture(ALL_PDF_PATH)
    conclusion_list = dataframe_pdf["Conclusion"].tolist()

    for abstract in abstract_list:
        wordCount = word_count(abstract)

        if wordCount > LONG_WORD:
            result = sumy_summarize.fileDataSummary(abstract, sumy_summarize.TR)
        elif wordCount > MID_WORD:
            result = ts6.summarize(abstract)
        elif wordCount > MINI_WORD:
            result = sumy_summarize.fileDataSummary(abstract, sumy_summarize.TR)
        else:
            result = ts6.summarize(abstract)

        ABSTRACT_RESULT_LIST.append(result)

    for conclusion in conclusion_list:
        wordCount = word_count(conclusion)

        if wordCount > LONG_WORD:
            result = sumy_summarize.fileDataSummary(conclusion, sumy_summarize.TR)
        elif wordCount > MID_WORD:
            result = ts6.summarize(conclusion)
        elif wordCount > MINI_WORD:
            result = sumy_summarize.fileDataSummary(conclusion, sumy_summarize.TR)
        else:
            result = ts6.summarize(conclusion)

        CONCLUSION_RESULT_LIST.append(result)

    # Save to the excel
    data = {'ID': id_list, 'Cluster': cluster_list, 'Abstract': abstract_list,
            'Summarize_Abstract': ABSTRACT_RESULT_LIST, 'Conclusion': conclusion_list,
            'Summarize_Conclusion': CONCLUSION_RESULT_LIST}
    output_data = pandas.DataFrame(data)
    # output_data = pandas.DataFrame(RESULT_LIST, columns=["AfterSummarize"])
    output_data.to_csv("result.csv", index=False)


if __name__ == "__main__":



    main()
