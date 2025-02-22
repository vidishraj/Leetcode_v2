# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class FindElements:
    root: TreeNode
    valuesInTree: defaultdict
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.valuesInTree = defaultdict(bool)
        height = self.findHeightOfTree(self.root, 0)
        self.checkPossibleValuesInTree(height)
        return 
    
    def findHeightOfTree(self, node, currHeight):
        if node is None:
            return currHeight
        return max(self.findHeightOfTree(node.left,1+currHeight), self.findHeightOfTree(node.right,1+currHeight))
    
    def checkPossibleValuesInTree(self, height):
        q = deque()
        self.valuesInTree[0] = True
        q.append(self.root)
        elementsConsumed = -1
        itemsToConsume = 2**height-1+1
        while len(q)>0:
            elementsConsumed+=1
            if elementsConsumed==itemsToConsume:
                return
            node = q.popleft()
            if node is not None:
                self.valuesInTree[elementsConsumed]=True
                q.append(node.left)
                q.append(node.right)
            else:
                q.append(None)
                q.append(None)
        return

    def find(self, target: int) -> bool:
        return self.valuesInTree[target]


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)