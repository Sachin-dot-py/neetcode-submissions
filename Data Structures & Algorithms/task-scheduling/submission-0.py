from collections import defaultdict, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # character : count
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # actually does -1
                if cnt:
                    q.append([cnt, time + n])
            else:
                time = q[0][1] # skip time to next timeout exceed
            
            if q and q[0][1] == time:
                # we have something ready to queue again
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


            