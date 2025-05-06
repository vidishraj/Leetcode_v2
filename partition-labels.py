class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # We have to remember the farthest part we have to travel till and then 
        # partition from there onwards
        
        # Find first index and last index of all the letters 
        endDict = {}
        for index, letter in enumerate(s):
            endDict[letter] = index
        idxToTravelTo = endDict[s[0]]
        currIdx = 0
        lastSplit = -1
        res = []
        # last index will be the last partition
        while currIdx<len(s):
            if currIdx == idxToTravelTo:
                partitionLen = currIdx-lastSplit
                #Make partition here
                res.append(partitionLen)
                lastSplit = currIdx
                if currIdx==len(s)-1:
                    return res
                else:
                    idxToTravelTo=endDict[s[currIdx+1]]

            else:
                idxToTravelTo=max(idxToTravelTo, endDict[s[currIdx]])
            currIdx+=1
        return res