"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {node: Node(node.val)}
        frontier = deque([node])

        while frontier:
            current = frontier.popleft()
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    frontier.append(neighbor)
                visited[current].neighbors.append(visited[neighbor])
        
        return visited[node]