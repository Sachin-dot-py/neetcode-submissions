# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findPath(self, root, target, path):
        if not root:
            return False
        path.append(root)
        if root.val == target.val:
            return True
        
        if self.findPath(root.left, target, path) or self.findPath(root.right, target, path):
            return True
        
        path.pop()
        return False


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = []
        q_path = []
        self.findPath(root, p, p_path)
        self.findPath(root, q, q_path)

        lca = None
        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            lca = p_path[i]
            i += 1
        return lca
        