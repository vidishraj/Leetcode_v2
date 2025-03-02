# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        itemCount = defaultdict(int)
        q=deque()
        q.append(root)
        while(len(q)>0):
            currItem = q.popleft()
            itemCount[currItem.val]+=1
            if currItem.left:
                q.append(currItem.left)
            if currItem.right:
                q.append(currItem.right)
        maxItem = 0
        for key in itemCount:
            maxItem = max(maxItem, itemCount[key])
        res = []
        for key in itemCount:
            if itemCount[key] ==maxItem:
                res.append(key)
        return res
