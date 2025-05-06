# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum:int
    def rec(self, root, currNum:str):
        if root is None:
            return  
        currNum = currNum+str(root.val)
        if root.left is None and root.right is None:
            # print("Here",currNum, root.val) 
            self.sum+=int(currNum)
            return 
        # print(currNum)
        self.rec(root.right, currNum)
        self.rec(root.left, currNum)
        return currNum
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum =0 
        self.rec(root, '')
        return self.sum