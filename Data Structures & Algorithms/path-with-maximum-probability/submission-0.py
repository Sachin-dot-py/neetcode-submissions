import heapq
from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            # undirected - add both directions
            adj_list[a].append((b, succProb[i]))
            adj_list[b].append((a, succProb[i]))

        heap = [(-1, start_node)]
        visited = set()
        while heap:
            dist, node = heapq.heappop(heap)
            dist = -dist
            if node in visited:
                continue
            visited.add(node)
            if node == end_node:
                return dist
            
            for neigh, prob in adj_list[node]:
                if neigh not in visited:
                    heapq.heappush(heap, (-dist * prob, neigh))

        return 0