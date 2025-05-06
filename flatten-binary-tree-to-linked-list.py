# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def build(self, root):
        if root is None:
            return None, None
        if root.left is None and root.right is None:
            #leaf Node
            return root, root
        
        leftVal, leftRightMost = self.build(root.left)
        rightVal, rightRightMost = self.build(root.right)
        # if leftVal is None:
        if leftVal is None:
            root.left = None
        elif rightVal is None:
            root.right = leftVal
            rightRightMost = leftRightMost
            root.left = None
        else:
            root.right = leftVal
            leftRightMost.right = rightVal
            root.left = None
        return root, rightRightMost
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        
        Basically doing dfs
        """
        return self.build(root)



        