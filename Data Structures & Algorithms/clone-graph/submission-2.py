from functools import cache
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(n):
            if not n:
                return None
            if n in copies:
                return copies[n]
            copies[n] = Node(val=n.val)
            for neigh in n.neighbors:
                copies[n].neighbors.append(dfs(neigh))
            return copies[n]
        copies = {}
        return dfs(node)