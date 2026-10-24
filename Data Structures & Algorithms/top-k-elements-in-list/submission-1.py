class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        counts = [[] for i in range(len(nums)+1)]
        for num in nums:
            freqs[num] += 1
        
        for num, count in freqs.items():
            counts[count].append(num)
        
        ans = []
        for i in range (len(counts)-1, -1, -1):
            for num in counts[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans