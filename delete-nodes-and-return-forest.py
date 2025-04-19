# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findChildren(self, root, val, h):
        if root is None:
            return None
        if root.val == val:
            return root.left, root.right, h
        l = self.findChildren(root.left, val, h+1)
        r = self.findChildren(root.right, val, h+1)
        if l is not None:
            return l
        return r

    def removeNode(self, root, val):
        if root is None:
            return None
        if root.left and root.left.val==val:
            root.left = None
            return 
                
        if root.right and root.right.val==val:
            root.right = None
            return 

        self.removeNode(root.left, val)
        self.removeNode(root.right, val)
        
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # Just have to find the direct childs of breaking nodes
        toDel = {}
        for n in to_delete:
            toDel[n] = True
        nodes = []
        hHeap = []
        for node in to_delete:
            l, r, h = self.findChildren(root, node, 0)
            hHeap.append((-h, node))
            if l is not None and toDel.get(l.val) is None:
                nodes.append(l)
            if r is not None and toDel.get(r.val) is None:
                nodes.append(r)
        heapq.heapify(hHeap)
        while len(hHeap)>0:
            h, val = heapq.heappop(hHeap)
            self.removeNode(root, val) 
        if toDel.get(root.val) is None:
            nodes.append(root)
        return nodes