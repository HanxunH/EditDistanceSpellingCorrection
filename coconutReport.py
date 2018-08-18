from __future__ import division
import utilHelper as helper
import datetime

class report:
    def __init__(self, method, threshold, ngram,filePath):
        self.methodName = method.__name__
        self.threshold = threshold
        self.ngram = ngram
        self.reportFilePath = filePath
        self.utilHelper = helper.utilHelper()
        self.startTime = datetime.datetime.now()

    def addMisspelledFileName(self,fileName):
        self.misspelledFileName = fileName
        return

    def addCorrectFileName(self,fileName):
        self.correctFileName = fileName
        return

    def calculateStatisticReport(self,predictList,correctList):
        self.endTime = datetime.datetime.now()
        self.totalWordCount = len(correctList)
        # Calculate Accuracy
        correctCount = 0
        predictCount = 0
        for index in range(0,len(correctList)):
            predictCount = predictCount + len(predictList[index])
            for item in predictList[index]:
                if item == correctList[index]:
                    correctCount = correctCount + 1

        self.totalCorrectWord = correctCount
        self.totalPredictCount = predictCount
        self.accuracy = self.totalCorrectWord / self.totalWordCount
        self.precision = self.totalCorrectWord / self.totalPredictCount
        self.generateReport()
        self.printReport()
        self.writeToFile()
        return

    def generateReport(self):
        self.reportItemlist = []
        self.reportItemlist.append("=====================================")
        self.reportItemlist.append("MisspelledFileName: " + self.misspelledFileName)
        self.reportItemlist.append("CorrectFileName: " + self.correctFileName)
        self.reportItemlist.append("Method Name: " + self.methodName)
        if self.methodName == "nGram":
            self.reportItemlist.append("n: " + self.ngram)
        self.reportItemlist.append("Threshold: " + str(self.threshold))
        self.reportItemlist.append("TotalWords: " + str(self.totalWordCount))
        self.reportItemlist.append("TotalCorrectWords: " + str(self.totalCorrectWord))
        self.reportItemlist.append("TotalPredictWords: " + str(self.totalPredictCount))
        self.reportItemlist.append("Accuracy(Recall): " + str(self.accuracy))
        self.reportItemlist.append("Precision: " + str(self.precision))
        self.reportItemlist.append("TimeUsed: " + str(self.endTime-self.startTime))
        self.reportItemlist.append("=====================================")
        return

    def printReport(self):
        for item in self.reportItemlist:
            print item
        return

    def writeToFile(self):
        self.utilHelper.writeDictionaryListToFile(self.reportItemlist,self.reportFilePath)
        return
