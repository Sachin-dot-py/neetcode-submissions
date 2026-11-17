from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        
        order = []
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(order) == numCourses
            
