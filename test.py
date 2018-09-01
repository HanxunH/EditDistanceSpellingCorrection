import orcaAutoCorrectMethod

ac = orcaAutoCorrectMethod.autoCorrectMethods()
ac.debug = True
ac.globalEditDistence("lended","blenders")
ac.localEditDistence("lended","blenders")


possibleList = PriorityQueue()
for word in dictionary:
    score = method(misspelledWord,word)
    possibleList.push((item,score))
for index in range(0,threshold):
    (word,score) = possibleList.pop()
    bestMatchList.append(word)
