# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSideView = []
        if root is None:
            return rightSideView

        queue = deque([root])
        while len(queue) != 0:
            level = []
            n = len(queue)

            for i in range(n):
                levelNode = queue.popleft()

                if levelNode.left:
                    queue.append(levelNode.left)
                if levelNode.right:
                    queue.append(levelNode.right)
                
                level.append(levelNode.val)

            rightSideView.append(level[-1])

        return rightSideView