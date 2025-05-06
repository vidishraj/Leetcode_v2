class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for i in range(len(sentences)):
            list1=sentences[i].split()
            if(max<len(list1)):
                max=len(list1)
        return max
        