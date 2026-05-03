# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        goodNodes = 0
        def dfs(node, maxSoFar):
            nonlocal goodNodes
            if node is None:
                return
            
            if node.val >= maxSoFar:
                maxSoFar = node.val
                goodNodes += 1
            
            dfs(node.left, maxSoFar)
            dfs(node.right, maxSoFar)
        

        dfs(root, float('-inf'))
        return goodNodes