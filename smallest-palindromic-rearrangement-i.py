class Solution:
    def smallestPalindrome(self, s: str) -> str:
        """
            Properties: A word is a palindrome if it has even number of letters 
            # Start filling these letters in order using 2 pointers 
        """
        mid = None
        # If odd, remove the mid, do the operations and then put it back
        if len(s)%2!=0:
            midI = len(s)//2
            mid = s[midI]
            s = s[:midI]+s[midI+1:]
        heap = [(ord(letter),letter) for letter in s]
        heapq.heapify(heap)
        left = ""
        right = ""
        while len(heap)>0:
            ord1, l = heapq.heappop(heap)
            ord2, r = heapq.heappop(heap)
            left+=l
            right = r+right
        res = left+right
        if mid is not None:
            res = left+mid+right
        return res
        