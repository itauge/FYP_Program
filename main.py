import sumy_summarize
import ts6
import pandas
#first sentenc
MINI_WORD = 190
MID_WORD = 530
LONG_WORD = 1080
RESULT_LIST = []
#second sentence
# Count the word
def word_count(string):
    return (len(string.strip().split(" ")))

def main():
    #Read the excel file, get the content
    dataframe = pandas.read_excel("H:\FYP\Team 6\Categorized 44 Selected Journal\Cluster 2\sample_excel.xlsx")
    abstract_list = dataframe["Abstract"].tolist()

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

    #Save to the excel
    output_data = pandas.DataFrame(RESULT_LIST, columns="AfterSummarize")
    output_data.to_csv("text.csv", index=False)

if __name__ == "__main__":
     main()