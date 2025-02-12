class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        checkDict={}
        answer=0
        for word in words:
            if checkDict.get(''.join(reversed(word))):
                answer+=1
            checkDict[word]=True
        return answer