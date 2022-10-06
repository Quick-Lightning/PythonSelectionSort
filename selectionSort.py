def getSmallest(inputList):
    if len(inputList)==1:
        smallest = inputList[0]
        inputList.remove(inputList[0])
        return(smallest)
    else:
        for number in inputList:
            if number == min(inputList):
                smallest = number
                inputList.remove(number)
                return(smallest)
testList = []
def addSmallest(number):
    global testList
    testList.append(number)
    
def doSelectionSort(inputList):
    while True:
        addSmallest(getSmallest(inputList))
        if len(inputList)==0:
            break
    return(inputList)

#example
exampleList = [94,
22,
71,
16,
50,
46,
36,
25,
98,
80]

doSelectionSort(exampleList)
print(testList) #not entirely sure how to fix this but you get the result in testList for some reason