import utilHelper as helper
import orcaAutoCorrectMethod
import util

class orcaAutoCorrect:
    def __init__(self):
        self.correctMethods = orcaAutoCorrectMethod.autoCorrectMethods()
        utilHelper = helper.utilHelper()
        self.logger = utilHelper.getLogger()

    def correctWord(self, dictionary, targetWord, method , n = 2, threshold = 1):
        def pqfunc(item):
            (word,score) = item
            return score
        possibleList = util.PriorityQueueWithFunction(pqfunc)

        if method == self.correctMethods.pynGram:
            for item in dictionary:
                score = (-1) * method(targetWord,item,n)
                possibleList.push((item,score))

        elif method == self.correctMethods.levenshtein or self.correctMethods.damerauLevenshtein:
            for item in dictionary:
                score = method(targetWord,item)
                possibleList.push((item,score))

        elif method != self.correctMethods.nGram:
            for item in dictionary:
                score = (-1) * method(targetWord,item)
                possibleList.push((item,score))

        elif method == self.correctMethods.nGram:
            for item in dictionary:
                score = method(targetWord,item,n)
                possibleList.push((item,score))
        else:
            self.logger.debug("Method Not Found")

        bestMatchList = []
        for index in range(0,threshold):
            (word,score) = possibleList.pop()
            bestMatchList.append(word)

        return bestMatchList
