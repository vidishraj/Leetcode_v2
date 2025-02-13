class Solution:
    def countSegments(self, s: str) -> int:
        if( s==""):
            return 0
        count=0
        words=s.split(' ')
        for i in range(len(words)):
            if(words[i]!=""):
                count+=1;
        return count
        