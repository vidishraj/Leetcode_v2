# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levelStack = defaultdict(list)
        def nextIdxAndNum(idx):
            nonlocal traversal
            num = ""
            while idx<len(traversal) and traversal[idx]!="-":
                num+=traversal[idx]
                idx+=1
            return idx,int( num)
        idx, num = nextIdxAndNum(0)
        rootNode = TreeNode(num)
        levelStack[0].append(rootNode)
        while idx<len(traversal):
            dashes = 0
            tempIdx = idx
            while tempIdx<len(traversal) and traversal[tempIdx] =="-":
                tempIdx+=1
                dashes+=1
            if tempIdx == len(traversal):
                return levelStack[0][0]
            nextIdx, num = nextIdxAndNum(tempIdx)
            lastParent = levelStack[dashes-1][-1]
            newNode = TreeNode(num)
            if lastParent.left:
                lastParent.right = newNode
            else:
                lastParent.left = newNode
            levelStack[dashes].append(newNode)
            idx=nextIdx

        return levelStack[0][0]