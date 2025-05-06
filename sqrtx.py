class Solution:
    def mySqrt(self, x: int) -> int:
        check = True
        if x==0 or x==1:
            return x
        for i in range((x//2)+2):
            curr = i * i 
            if curr > x:
                check = False
            if not check:
                # Flipped 
                return i-1
