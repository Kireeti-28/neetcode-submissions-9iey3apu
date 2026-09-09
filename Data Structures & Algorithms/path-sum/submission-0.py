# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, cur_path_sum):
            if node is None:
                return False

            cur_path_sum += node.val

            if node.left is None and node.right is None:
                return cur_path_sum == targetSum
            
            return dfs(node.left, cur_path_sum) or dfs(node.right, cur_path_sum)
        
        return dfs(root, 0)

            