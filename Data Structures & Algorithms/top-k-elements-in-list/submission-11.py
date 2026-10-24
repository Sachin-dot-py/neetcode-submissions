from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        # First, count frequencies
        frequencies = defaultdict(int) # num: frequency O(n)
        for num in nums: # O(n) where n is len(nums)
            frequencies[num] += 1
        # Theoretical max frequency is n = len(nums)
        n = len(nums)
        frequency_num = [[] for _ in range(n + 1)] # Index is frequency, value is a list of the nums with that frequency
        for num, freq in frequencies.items(): # O(n)
            frequency_num[freq].append(num)
        
        res = []
        for i in range(n, -1, -1): # O(n)
            for num in frequency_num[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # Frequency + Min-Heap
        # First, count frequencies
        # frequencies = defaultdict(int) # num: frequency O(n)
        # for num in nums: # O(n) where n is len(nums)
        #     frequencies[num] += 1
        
        # # Now get the top k frequent elements
        # heap = [] # O(k) in O(n)
        # for num, frequency in frequencies.items(): # O(nlogk)
        #     heapq.heappush(heap, (frequency, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [num for freq, num in heap]