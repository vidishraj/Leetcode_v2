import numpy as np
class Solution:
    def calculate(self, s: str) -> int:
        operatorMatch=["/","+","-","*"]
        numberString=""
        numberList=[]
        operatorList=[]
        for letter in s:
            if not letter in operatorMatch:
                numberString+=letter
            else:
                numberList.append(int(float(numberString)))
                numberString=""
                operatorList.append(letter)
        numberList.append(int(float(numberString)))
        numberPair=(0,1)
        remainingOperator=[]
        for index,operator in enumerate(operatorList):
            if operator=="*" or operator=="/":
                firstNumber=numberList[numberPair[0]]
                secondNumber=numberList[numberPair[1]]
                numberList.pop(numberPair[0])
                numberList.pop(numberPair[0])
                if operator=="/":
                    numberList.insert(numberPair[0],math.floor(firstNumber/secondNumber))
                else:
                    numberList.insert(numberPair[0], math.floor(firstNumber*secondNumber))
            else:
                remainingOperator.append(operator)
                numberPair=[numberPair[0]+1, numberPair[1]+1]
        if len(numberList)==1:
            return numberList[0]
        numberArray = np.array(numberList)
        remainingOperatorArray=np.array(remainingOperator)
        reversed_array = numberArray[::-1]
        numberList=reversed_array.tolist()
        reversed_array = remainingOperatorArray[::-1]
        remainingOperator=reversed_array.tolist()
        while len(remainingOperator)>0:
            operator=remainingOperator.pop()
            firstNumber = numberList.pop()
            secondNumber = numberList.pop()
            if operator=="+":
                numberList.append(firstNumber+secondNumber)
            else:
                numberList.append(firstNumber-secondNumber)
        return numberList[0]