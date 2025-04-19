class Solution:
    target: int
    res: set
    candidates:list

    def backtrack(self, arr, idx, currSum):
        # print(arr, currSum)
        if currSum == self.target:
            self.res.add(tuple(arr))
        if currSum>self.target or idx>=len(self.candidates):
            # Sum is exceeding, no need to take this path
            return

        remaining = self.target - currSum 
        currNum = self.candidates[idx]
        curr = currNum
        item = [curr]
        while remaining>=0:
            # Add currNum and check
            self.backtrack(arr+item, idx+1, currSum+curr)
            item.append(currNum)
            remaining-=currNum
            curr+=currNum

        self.backtrack(arr, idx+1, currSum)
        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.res = set()
        self.candidates = candidates
        self.backtrack([], 0, 0)
        return list(self.res)