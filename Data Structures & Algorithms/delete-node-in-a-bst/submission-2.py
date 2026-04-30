# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if node is None:
                return
            
            if node.val > key:
                node.left = dfs(node.left, key)
            elif node.val < key:
                node.right = dfs(node.right, key)
            else:
                if (node.left is None and node.right is None):
                    return None
                
                if (node.left is None):
                    return node.right
                
                if node.right is None:
                    return node.left
                
                cur = node.right
                while cur.left:
                    cur = cur.left
                
                node.val = cur.val

                node.right = dfs(node.right, node.val)
            
            return node
        
        return dfs(root, key)
        
                
