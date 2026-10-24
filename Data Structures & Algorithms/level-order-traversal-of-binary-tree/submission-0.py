# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output = []
        queue = deque([root])

        while queue:
            # Process this level
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level)
            
        return output
        

# Test Case 1:
# root = TreeNode(1)
# output: [[1], [2, 3], [4,5,6,7]]]

# Psuedocode:
# bfs level by level, where each loop pushes in the nodes to visit in the next iteration
# O(N) Time, O(N) Space