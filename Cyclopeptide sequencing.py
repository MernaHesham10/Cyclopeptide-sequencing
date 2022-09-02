from builtins import range, print
weightAminoAcidDictionary = {156: 'R',
                             114: 'N',
                             115: 'D',
                             103: 'C',
                             129: 'E',
                             128: 'Q',
                             57: 'G',
                             137: 'H',
                             113: 'I',
                             113: 'L',
                             128: 'K',
                             131: 'M',
                             147: 'F',
                             97: 'P',
                             87: 'S',
                             101: 'T',
                             186: 'W',
                             163: 'Y',
                             99: 'V',
                             71: 'A'}

aminoAcidWeightDictionary ={
     'R': 156,
     'N': 114,
     'D': 115,
     'C': 103,
     'E': 129,
     'Q': 128,
     'G': 57,
     'H': 137,
     'I': 113,
     'L': 113,
     'K': 128,
     'M': 131,
     'F': 147,
     'P': 97,
     'S': 87,
     'T': 101,
     'W': 186,
     'Y': 163,
     'V': 99,
     'A':71
}

def CalculateInitialList(inputWeightsList):

    convertInputWeightsToAminAcide = []

    for j in range(len(inputWeightsList)):
        if inputWeightsList[j] in weightAminoAcidDictionary.keys():
            convertInputWeightsToAminAcide.append(weightAminoAcidDictionary.get(inputWeightsList[j]))

    return (convertInputWeightsToAminAcide)


def CalculateLinearSpectrum(InputSequenceToCalc):
    sequenceDivisionsList = []
    finalWeightList = []

    for i in range(len(InputSequenceToCalc)):
        for j in range(len(InputSequenceToCalc)):
            if (i + j) < len(InputSequenceToCalc):
                sequenceDivisionsList.append(InputSequenceToCalc[j:j + i + 1])

    for i in sequenceDivisionsList:
        finalWeightList.append(CalculateWeightInput(i))
    calulateSortedWeights = sorted(finalWeightList)
    return calulateSortedWeights


def CalculateWeightInput(InputSequenceToGetWeight):
    sumResultWeight = 0
    for o in InputSequenceToGetWeight:
        sumResultWeight += aminoAcidWeightDictionary[o]
    return sumResultWeight


def CalculatePossibilityList(outputOfInputWeights):
    resultOfInputWeightsList = []
    resultOfInputWeightsList = CalculateInitialList(inputWeightsCheckList)

    outputOfInputWeightsString = ''
    i = 0
    for i in outputOfInputWeights:
        outputOfInputWeightsString = outputOfInputWeightsString + i + " "

    i = 0
    outputOfInputWeightsStrTemp = ''
    for i in outputOfInputWeights:
        outputOfInputWeightsStrTemp = outputOfInputWeightsStrTemp + i + ','

    outputOfInputWeightsStrTemp2 = []
    z = 0
    s2_new_string = ""
    for string in outputOfInputWeights:
        s2_new_string = outputOfInputWeightsStrTemp.replace(",", "")
    outputOfInputWeightsStrTemp2.append(s2_new_string)
    z = z + 1

    outputOfInputWeightsStrTemp3 = ''
    for i in outputOfInputWeightsStrTemp2:
        outputOfInputWeightsStrTemp3 = outputOfInputWeightsStrTemp3 + i + " "
    outputOfInputWeightsStrTemp4 = ''
    outputOfInputWeightsStrTemp4 = outputOfInputWeightsStrTemp3.replace(' ', '')

    z = 0
    count = 0
    outputOfInputWeightsStrTemp5 = []
    itemOfTemp5 = outputOfInputWeightsStrTemp.replace(",", "")

    j = 0
    i = 0
    u = 0
    for u in range(len(resultOfInputWeightsList)):
        for i in range(len(outputOfInputWeights)):
            for j in range((len(itemOfTemp5))):
                if len(itemOfTemp5[count:count + 1]):
                    outputOfInputWeightsStrTemp5.insert(z, resultOfInputWeightsList[u])
                    outputOfInputWeightsStrTemp5.insert(z + 1, itemOfTemp5[count:count + len(outputOfInputWeights[0])])
                    count = count + len(outputOfInputWeights[0])
                    z = z + len(outputOfInputWeights[0]) + 1
            count = 0
    f = ''.join(outputOfInputWeightsStrTemp5)

    ff = []
    i = 0
    ff = [f[i:i + len(outputOfInputWeights[0]) + 1] for i in range(0, len(f), len(outputOfInputWeights[0]) + 1)]

    i = 0
    ResultOfCalculatePossibility = list(dict.fromkeys(ff))

    i = 0
    for i in range(len(ResultOfCalculatePossibility)):
        if(len(ResultOfCalculatePossibility[0]) != len(ResultOfCalculatePossibility[i])):
            ResultOfCalculatePossibility.pop(i)
    print('Result Of Calculate Possibility: ', ResultOfCalculatePossibility)
    return ResultOfCalculatePossibility


def CheckIfConsistent(ResultOfCalculatePossibility, inputWeightsList):

    while True:
        ResultOfCalculatePossibilityLength = len(ResultOfCalculatePossibility[0])
        dicCheckPossibility = {}
        i = 0
        k = 0
        for i in range(len(ResultOfCalculatePossibility)):
            if(len(ResultOfCalculatePossibility[0]) != len(ResultOfCalculatePossibility[i])):
                ResultOfCalculatePossibility.pop(i)

        for i in range(len(ResultOfCalculatePossibility)):
            for j in range(ResultOfCalculatePossibilityLength):
                dicCheckPossibility[ResultOfCalculatePossibility[i]] = (CalculateLinearSpectrum(ResultOfCalculatePossibility[i]))

        i = 0
        j = 0
        t = False
        inputWeightsListTemp = inputWeightsList.copy()
        for i in range(len(ResultOfCalculatePossibility)):
            for j in range(len(dicCheckPossibility[ResultOfCalculatePossibility[i]])):
                if (dicCheckPossibility[ResultOfCalculatePossibility[i]][j] in inputWeightsListTemp):
                    inputWeightsListTemp.remove(dicCheckPossibility[ResultOfCalculatePossibility[i]][j])
                else:
                    dicCheckPossibility.pop(ResultOfCalculatePossibility[i])
                    break
            inputWeightsListTemp = inputWeightsList.copy()

        if dicCheckPossibility == {}:
            return False
            break
        else:
            print("Result Of Check If Input Sequence Is Consistent Or Not = ", dicCheckPossibility)
            CheckIfConsistent(CalculatePossibilityList(list(dicCheckPossibility.keys())), inputWeightsList)
            return True

#################################################################################################################################################################################

inputWeightsCheckList = []
inputWeightsString = input('Enter Weight(s) To Get Its All Possibility Separated By Space: ')
inputWeightsCheckList = inputWeightsString.split()

# Convert inputWeightsCheckList From Type String to Int so can deal with it by push it to Initial_List Function
for i in range(len(inputWeightsCheckList)):
    inputWeightsCheckList[i] = int(inputWeightsCheckList[i])

checkList = CalculateInitialList(inputWeightsCheckList)

checkList = CalculatePossibilityList(checkList)

CheckIfConsistent(checkList, inputWeightsCheckList)