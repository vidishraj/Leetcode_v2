class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer=[]
        finalAnswer=[]
        for word in words:
            word=word.strip(separator)
            answer+=word.split(separator)
        for word in answer:
            if word!="":
                finalAnswer.append(word)
        return finalAnswer