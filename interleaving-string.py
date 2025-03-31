class Solution:
    @lru_cache(None)
    def rec(self, s1, s2, s3, left):
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True
        if (len(s1) == 0 and left) or (len(s2) == 0 and not left) or len(s3)==0:
            return False
        if left:
            # Have to match s1 here in s3
            # Call more till we get a True
            curr = 0 
            while curr< len(s1) and curr<len(s3):
                currS1 = s1[curr]
                currS3 = s3[curr]
                if currS1 == currS3:
                    check = self.rec(s1[curr+1:], s2, s3[curr+1:], False)
                    if check:
                        return True
                else:
                    break
                curr+=1
        else:
            # Have to match s2 here in s3
            curr = 0 
            while curr< len(s2) and curr<len(s3):
                currS2 = s2[curr]
                currS3 = s3[curr]
                if currS2 == currS3:
                    check = self.rec(s1, s2[curr+1:], s3[curr+1:], True)
                    if check:
                        return True
                else:
                    break
                curr+=1
        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.rec(s1, s2, s3, True) or self.rec(s1, s2, s3, False)
        