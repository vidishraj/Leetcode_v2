from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        distanceBetweenMatches = {}
        occurenceDict = defaultdict(int)
        lastIndex = {}
        for card in cards:
            distanceBetweenMatches[card] = -1
            occurenceDict[card]+=1
        ansPossible = False
        for value in list(occurenceDict.values()):
            if value>1:
                ansPossible = True
        if ansPossible == False:
            return -1
        for index, card in enumerate(cards):
            if occurenceDict[card]>1:
                if lastIndex.get(card) is None:
                    lastIndex[card] = index
                else:
                    if distanceBetweenMatches[card]==-1:
                        distanceBetweenMatches[card] = index - lastIndex[card]
                    else:
                        distanceBetweenMatches[card] = min(distanceBetweenMatches[card], index - lastIndex[card])
                    lastIndex[card] = index
        res = len(cards)
        for item in list(distanceBetweenMatches.values()):
            if item !=-1 and item<res:
                res = item
        return res + 1