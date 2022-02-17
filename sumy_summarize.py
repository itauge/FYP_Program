# -*- coding: utf-8 -*-
# https://github.com/miso-belica/sumy

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# algorithms
from sumy.summarizers.lex_rank import LexRankSummarizer as LR
from sumy.summarizers.text_rank import TextRankSummarizer as TR
from sumy.summarizers.lsa import LsaSummarizer as LSA
from sumy.summarizers.kl import KLSummarizer as KLS
from sumy.summarizers.luhn import LuhnSummarizer as LUHN
from sumy.summarizers.reduction import ReductionSummarizer as RE
from sumy.summarizers.sum_basic import SumBasicSummarizer as SB

LANGUAGE = "english"
SENTENCES_COUNT = 3

def fileDataSummary(text, summarizer):
    # parser = PlaintextParser.from_file(files, Tokenizer(LANGUAGE))
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
	# can change the summarizer
    summarizer = summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        return sentence


if __name__ == "__main__":
     fileDataSummary("THEs sdf sd ssdfsd fsdf sd fsdsd", TR)