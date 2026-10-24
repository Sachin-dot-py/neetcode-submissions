class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        return [y[0] for y in (sorted(freqs.items(), key=lambda x: x[1], reverse=True))][:k]