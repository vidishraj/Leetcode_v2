class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # All we have to find is the distance to the closeset L or R 
        rightLeftMap = []
        if dominoes.count(".")==len(dominoes):
            return dominoes
        for index, domino in enumerate(dominoes):
            if domino == ".":
                closestRight= closestLeft = -1
                for i in range(index, -1, -1):
                    if dominoes[i]=="R":
                        closestRight = index-i
                        break
                    elif dominoes[i]=="L":
                        break
                for j in range(index+1, len(dominoes)):
                    if dominoes[j]=="L":
                        closestLeft = j-index
                        break
                    elif dominoes[j]=="R":
                        break
                rightLeftMap.append((closestRight, closestLeft))
            else:
                rightLeftMap.append((-1, -1))
        # print(rightLeftMap)
        for index, item in enumerate(rightLeftMap):
            lC, rC = item
            r = dominoes[index]
            if lC != -1 and rC !=-1:
                if lC<rC:
                    r = "R"
                elif rC<lC:
                    r = "L"
            elif lC!=-1:
                r= "R"
            elif rC!=-1:
                r="L"
            dominoes= dominoes[:index]+r+dominoes[index+1:]
        return dominoes

