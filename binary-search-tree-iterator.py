# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    firstVal: bool = True
    curr: TreeNode
    orderList:list
    listIndex:int

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root    
        self.listIndex = 0 
        self.orderList = []
        self.inorder(root)

    def inorder(self, root):
        if root is None:
            return root
        self.inorder(root.left)
        self.orderList.append(root.val)
        self.inorder(root.right)
    
    def next(self) -> int:
        val = self.orderList[self.listIndex]
        self.listIndex+=1
        return val

    def hasNext(self) -> bool:
        if self.listIndex!=len(self.orderList):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()