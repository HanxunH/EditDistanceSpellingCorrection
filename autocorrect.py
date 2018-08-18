import utilHelper as helper
import Levenshtein

class autoCorrectMethods:
    def __init__(self):
        utilHelper = helper.utilHelper()
        self.logger = utilHelper.getLogger()
        self.debug = False
        return

    def printMatrix(self, matrix):
        for columnIndex in range(0,len(matrix)):
            print matrix[columnIndex]

    def globalEditDistence(self, originalWord, targetWord):
        # Parameters
        matchCost = 1
        insertCost = -1
        deleteCost = -1
        replaceCost = -1

        # Initializing
        lengthOriginal = len(originalWord) + 1
        lengthTarget = len(targetWord) + 1
        matrix = [[0 for x in range(lengthOriginal)] for y in range(lengthTarget)]
        count = 0
        for index in range(0,lengthOriginal):
            matrix[0][index] = count
            count = count - 1
        count = 0
        for index in range(0,lengthTarget):
            matrix[index][0] = count
            count = count - 1

        #Needleman-Wunsch
        for indexTarget in range(1,lengthTarget):
            for indexOriginal in range(1,lengthOriginal):
                x1 = matrix[indexTarget][indexOriginal-1] + deleteCost
                x2 = matrix[indexTarget-1][indexOriginal] + insertCost
                x3 = matrix[indexTarget-1][indexOriginal-1]
                if originalWord[indexOriginal-1] == targetWord[indexTarget-1]:
                    x3 = x3 + matchCost
                else:
                    x3 = x3 + replaceCost

                matrix[indexTarget][indexOriginal] = max(x1,x2,x3)
                if self.debug:
                    print "cordinate: " + str(indexOriginal) + " " + str(indexTarget)
                    print "compareWord: "+originalWord[indexOriginal-1]+" "+targetWord[indexTarget-1]
                    print "x1 = " + str(matrix[indexTarget][indexOriginal-1])
                    print "x2 = " + str(matrix[indexTarget-1][indexOriginal])
                    print "x3 = " + str(matrix[indexTarget-1][indexOriginal-1])
                    print "final x1 = " + str(x1)
                    print "final x2 = " + str(x2)
                    print "final x3 = " + str(x3)
                    self.printMatrix(matrix)

        if self.debug:
            print "========================"
            self.printMatrix(matrix)

        return matrix[lengthTarget-1][lengthOriginal-1]

    def localEditDistence(self, originalWord, targetWord):
        # Parameters
        matchCost = 1
        insertCost = -1
        deleteCost = -1
        replaceCost = -1

        # Initializing
        lengthOriginal = len(originalWord) + 1
        lengthTarget = len(targetWord) + 1
        matrix = [[0 for x in range(lengthOriginal)] for y in range(lengthTarget)]
        for index in range(0,lengthOriginal):
            matrix[0][index] = 0
        count = 0
        for index in range(0,lengthTarget):
            matrix[index][0] = 0

        #Needleman-Wunsch
        maxScore = 0
        for indexTarget in range(1,lengthTarget):
            for indexOriginal in range(1,lengthOriginal):
                x1 = matrix[indexTarget][indexOriginal-1] + deleteCost
                x2 = matrix[indexTarget-1][indexOriginal] + insertCost
                x3 = matrix[indexTarget-1][indexOriginal-1]
                if originalWord[indexOriginal-1] == targetWord[indexTarget-1]:
                    x3 = x3 + matchCost
                else:
                    x3 = x3 + replaceCost

                matrix[indexTarget][indexOriginal] = max(x1,x2,x3,0)
                maxScore = max(maxScore,matrix[indexTarget][indexOriginal])

                if self.debug:
                    print "cordinate: " + str(indexOriginal) + " " + str(indexTarget)
                    print "compareWord: "+originalWord[indexOriginal-1]+" "+targetWord[indexTarget-1]
                    print "x1 = " + str(matrix[indexTarget][indexOriginal-1])
                    print "x2 = " + str(matrix[indexTarget-1][indexOriginal])
                    print "x3 = " + str(matrix[indexTarget-1][indexOriginal-1])
                    print "final x1 = " + str(x1)
                    print "final x2 = " + str(x2)
                    print "final x3 = " + str(x3)
                    self.printMatrix(matrix)

        if self.debug:
            print "========================"
            self.printMatrix(matrix)

        return maxScore

    def nGramProcessInitialStringHelper(self,word):
        return "#" + word + "#"

    def nGramSplitHelper(self,word,n):
        list = []
        for index in range(0,len(word)-n+1):
            gram = word[index:index+n]
            list.append(gram)
        if self.debug:
            print list
        return list

    def nGram(self, originalWord, targetWord, n):
        processedOriginalWord = self.nGramProcessInitialStringHelper(originalWord)
        processedTargetWord = self.nGramProcessInitialStringHelper(targetWord)
        originalGramList = self.nGramSplitHelper(processedOriginalWord,n)
        targetGramList = self.nGramSplitHelper(processedTargetWord,n)
        mutualCount = 0
        for item in originalGramList:
            if item in targetGramList:
                mutualCount = mutualCount + 1
        score = len(originalGramList) + len(targetGramList) - 2 * mutualCount

        if self.debug:
            print score

        return score

    def levenshtein(self,originalWord,targetWord):

        print Levenshtein.distance(originalWord,targetWord)
        return
