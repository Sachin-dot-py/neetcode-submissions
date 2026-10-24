from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        seen = set() # of node numbers explored
        cc = 0
        # Multi-source DFS
        # Start at each edge to be discovered
        for i in range(n):
            if i not in seen:
                # Found a new node, fully discover this one.
                cc += 1
                stack = deque()
                stack.append(i)
                while stack:
                    n = stack.pop()
                    seen.add(n)
                    for node in adj_list[n]:
                        if node not in seen:
                            stack.append(node)
        return cc
        
