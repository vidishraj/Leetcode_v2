class Solution(object):
    def wordPattern(self, pattern, s):
        csMap={}
        scMap={}
        s=s.split(' ')
        if len(s)!=len(pattern): return False
        for i in range(len(pattern)):
            if csMap.get(pattern[i])!=None and csMap[pattern[i]]!=s[i]:
                return False
            if scMap.get(s[i]) is not None and scMap[s[i]]!=pattern[i]:
                return False
            csMap[pattern[i]]=s[i]
            scMap[s[i]]=pattern[i]
        return True