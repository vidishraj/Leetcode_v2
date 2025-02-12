class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result=list()
        mapList = list()
        runningCount = 0
        vowels=['a','e','i','o','u']
        for word in words:
            mapList.append(runningCount)
            if word[0] in vowels and word[-1] in vowels:
                runningCount+=1
        mapList.append(runningCount)
        print(mapList)
        for query in queries:
            result.append(mapList[query[1]+1]-mapList[query[0]])
        return result