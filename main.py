import sumy_summarize
import ts6
import wos_simplify
import pandas

MINI_WORD = 190
MID_WORD = 530
LONG_WORD = 1080
RESULT_LIST = []


# Count the word
def word_count(string):
    word = len(str(string).strip().split(" "))
    return word


def main():
    # Method 1 : Read the excel file, get the content(the file can get from the pdf_capture.py)
    # dataframe = pandas.read_excel("H:\FYP\Team 6\Categorized 44 Selected Journal\Cluster 2\sample_excel.xlsx")
    # abstract_list = dataframe["Abstract"].tolist()

    #Method 2 : WOS dataframe
    # dataframe = wos_simplify.modify_WOS_dataframe()
    # abstract_list = dataframe["Abstract"].tolist()

    #Method 3 : VOS dataframe
    dataframe = wos_simplify.modify_VOS_dataframe()
    id_list = dataframe["id"].tolist()
    cluster_list = dataframe["cluster"].tolist()
    abstract_list = dataframe["Abstract"].tolist()



    #Result of the excel file
    # wos_simplify.output()

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

        RESULT_LIST.append(result)

    # Save to the excel
    data = {'ID': id_list, 'Cluster': cluster_list, 'Abstract': abstract_list, 'AfterSummarize': RESULT_LIST}
    output_data = pandas.DataFrame(data)
    # output_data = pandas.DataFrame(RESULT_LIST, columns=["AfterSummarize"])
    output_data.to_csv("result.csv", index=False)


if __name__ == "__main__":
    main()
