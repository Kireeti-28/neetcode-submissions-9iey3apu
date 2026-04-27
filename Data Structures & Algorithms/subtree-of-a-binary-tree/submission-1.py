# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(node1, node2):
            if node1 is None and node2 is None:
                return True
            
            if node1 is None or node2 is None:
                return False

            return node1.val == node2.val and isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
        
        queue = deque([root])

        while len(queue) != 0:
            cur = queue.popleft()

            if isSame(cur, subRoot):
                return True
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return False
            
