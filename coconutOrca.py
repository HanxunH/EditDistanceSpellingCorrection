import utilHelper as helper
import time
import orcaCorrect
import sys


class coconutOrca:
    def __init__(self):
        self.dictionaryFile = "2018S2-90049P1-data/dict.txt"
        utilHelper = helper.utilHelper()
        self.logger = utilHelper.getLogger()
        return

    def main(self):
        utilHelper = helper.utilHelper()
        correctHandler = orcaCorrect.orcaAutoCorrect()
        dictionaryList = utilHelper.getUpDictionaryList(self.dictionaryFile)

        # Command Handling
        if "-i" in sys.argv:
            while True:
                print "Try a misspelled word "
                userInputWord = sys.stdin.readline()
                self.logger.info("Analyzing")
                list = correctHandler.correctWord(dictionaryList,userInputWord,correctHandler.correctMethods.levenshtein,2,1)
                print "Did you mean: " + list[0] + " ?"
                print ""
        elif "-f" in sys.argv:
            
        #correctHandler.correctWord(dictionaryList,"abandonned", correctHandler.correctMethods.levenshtein ,2, 1)

        return


runable = coconutOrca()
runable.main()
