from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for ui, vi, ti in times:
            adj_list[ui].append((vi, ti))
        
        queue = deque()
        queue.append((k, 0))
        distances = {n: float('inf') for n in range(1, n + 1)}
        distances[k] = 0
        while queue:
            node, dist = queue.popleft()
            if distances[node] < dist:
                continue
            for vi, ti in adj_list[node]:
                if dist + ti < distances[vi]:
                    distances[vi] = dist + ti
                    queue.append((vi, distances[vi]))
        max_dist = max(distances.values())
        if max_dist == float('inf'):
            return -1
        return max_dist
                
