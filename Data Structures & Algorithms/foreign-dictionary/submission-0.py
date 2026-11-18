from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build chars set
        chars = set()
        for word in words:
            for c in word:
                chars.add(c)

        # build lexi graph
        lexi = defaultdict(list) # adj list of graph a -> b if a < b
        indegree = defaultdict(int) # indegree of lexi graph
        for i in range(len(words) - 1): # all indices except last
            # compare each word with the next
            j = 0
            while j < len(words[i]) and j < len(words[i + 1]):
                if words[i][j] != words[i + 1][j]:
                    lexi[words[i][j]].append(words[i + 1][j])
                    indegree[words[i + 1][j]] += 1
                    break
                j += 1
            if j == len(words[i + 1]) and j < len(words[i]):
                # illegal case
                return ""
            
        # made the indegree and adj list based on all the info we have
        # now make the string
        result = []
        queue = deque([c for c in chars if indegree[c] == 0])
        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in lexi[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return "".join(result) if len(result) == len(chars) else ""