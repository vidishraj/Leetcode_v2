class Solution:
    
    def isSuffixAndPrefix(self, word, pattern):
        return (word.startswith(pattern) and word.endswith(pattern)) or (word==pattern)
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(words[j])>=len(words[i]):
                    if self.isSuffixAndPrefix(words[j],words[i]):
                        count+=1
        return count