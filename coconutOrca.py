import utilHelper as helper
import coconutReport
import time
import orcaCorrect
import sys
import os

class coconutOrca:
    def __init__(self):
        self.dictionaryFile = "2018S2-90049P1-data/dict.txt"
        self.fileOrcaCorrectFilePath = "2018S2-90049P1-data"
        self.utilHelper = helper.utilHelper()
        self.logger = self.utilHelper.getLogger()
        self.correctHandler = orcaCorrect.orcaAutoCorrect()
        return

    def correctFileAndCompare(self, dictionary, misspelledFile, correctFile, method , n=2, threshold=1):
        misspelledFileName = os.path.basename(misspelledFile)
        correctFileFileName = os.path.basename(correctFile)

        misspelledFileDictionaryList = self.utilHelper.getFileDictionaryList(misspelledFile)
        correctFileDictionaryList = self.utilHelper.getFileDictionaryList(correctFile)

        if len(misspelledFileDictionaryList) != len(correctFileDictionaryList):
            self.utilHelper.logger.error("MisspelledFile and CorrectFile Word Cound Do Not Match")
            return

        orcaCorrectList = []
        orcaCorrectListWriteToFile = []

        statisticReport = coconutReport.report(method,threshold,n,self.fileOrcaCorrectFilePath + "/" + method.__name__ + "_" + "report" + "_"+misspelledFileName)
        statisticReport.addCorrectFileName(correctFileFileName)
        statisticReport.addMisspelledFileName(misspelledFileName)
        for item in misspelledFileDictionaryList:
            self.logger.info("==================")
            self.logger.info("Comparing: " + item)
            orcaPredictList = self.correctHandler.correctWord(dictionary,item,method,n,threshold)
            self.logger.info("Prediction: " + str(orcaPredictList))
            list = []
            for item in orcaPredictList:
                list.append(item)
            orcaCorrectList.append(list)
        for item in orcaCorrectList:
            orcaCorrectListWriteToFile.append(str(item))
        statisticReport.calculateStatisticReport(orcaCorrectList,correctFileDictionaryList)

        self.utilHelper.writeDictionaryListToFile(orcaCorrectListWriteToFile, self.fileOrcaCorrectFilePath + "/" + method.__name__ + "_"+misspelledFileName)
        return

    def main(self):
        dictionaryList = self.utilHelper.getFileDictionaryList(self.dictionaryFile)
        perdictThreshold = 1
        nGram = 2
        # Command Handling
        if "-t" in sys.argv:
            index = sys.argv.index("-t")
            perdictThreshold = int(sys.argv[index+1])

        if "-n" in sys.argv:
            index = sys.argv.index("-n")
            nGram = int(sys.argv[index+1])

        if "-i" in sys.argv:
            while True:
                print "Try a misspelled word "
                userInputWord = sys.stdin.readline()
                self.logger.info("Analyzing")
                list = correctHandler.correctWord(dictionaryList,userInputWord,self.correctHandler.correctMethods.levenshtein,2,1)
                print "Did you mean: " + list[0] + " ?"
                print ""
        elif "-f" in sys.argv:
            index = sys.argv.index("-f")
            misspledFile = sys.argv[index+1]
            correctFile = sys.argv[index+2]


        # Test Cases
        if "-l" in sys.argv:
            # Levenshtein Method
            self.correctFileAndCompare(dictionaryList,misspledFile,correctFile,self.correctHandler.correctMethods.levenshtein,nGram,perdictThreshold)
        elif "-ged" in sys.argv:
            # GlobalEditDistence Method
            self.correctFileAndCompare(dictionaryList,misspledFile,correctFile,self.correctHandler.correctMethods.globalEditDistence,nGram,perdictThreshold)
        elif "-led" in sys.argv:
            # LocalEditDistence Method
            self.correctFileAndCompare(dictionaryList,misspledFile,correctFile,self.correctHandler.correctMethods.localEditDistence,nGram,perdictThreshold)
        elif "-ngram" in sys.argv:
            # nGram Distence method
            self.correctFileAndCompare(dictionaryList,misspledFile,correctFile,self.correctHandler.correctMethods.nGram,nGram,perdictThreshold)

        return


runable = coconutOrca()
runable.main()
