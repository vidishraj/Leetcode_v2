# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, root, curr, val):
        if root == None:
            return ''
        if root.val == val:
            return str(root.val)
        leftVal = self.rec(root.left, curr, val)
        rightVal = self.rec(root.right, curr, val)
        if leftVal !='':
            return str(root.val)+","+leftVal
        if rightVal !='':
            return str(root.val)+","+rightVal
        return ''

    def findNode(self, root, target):
        if root is None:
            return None
        if root.val == int(target):
            return root
        
        left_search = self.findNode(root.left, target)
        if left_search:  # If found in the left subtree, return immediately
            return left_search
        
        return self.findNode(root.right, target)  # Search in the right subtree

            
    def rowWiseBfs(self, root):
        levelDict = defaultdict(list)
        q = deque()
        q.append((root, 0))
        while len(q)!=0:
            node, level = q.popleft()
            levelDict[level].append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return levelDict
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Find the deepest child first 
        # Run a bottom - up iterative approach to mark the path in dicts 
        # check dicts for common value 
        if root.left is None and root.right is None: 
            return root
        levelDict = self.rowWiseBfs(root)
        keys = list(levelDict.keys())
        keys.sort(reverse=True)
        lowestNodes = []
        key = keys[0]
        for node in levelDict[key]:
            lowestNodes.append(node)
        if len(lowestNodes)==1:
            return self.findNode(root, lowestNodes[0])
        paths = []
        for node in lowestNodes:
            paths.append(self.rec(root, '', node).split(','))
        common = None
        # print(paths)
        for i in range(len(paths[0])-1, -1, -1):
            curr = paths[0][i]
            for j in range(1, len(paths)):
                if curr!= paths[j][i]:
                    curr=None
                    break
            if curr is not None:
                common = curr
                break

        node = self.findNode(root,common)
        # print(node.val)
        return node