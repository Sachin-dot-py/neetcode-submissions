class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy
        # At each iteration, keep a window of the furthest we can reach
        n = len(nums)
        furthest_reach = 0
        for i in range(n):
            if i > furthest_reach:
                return False
            furthest_reach = max(furthest_reach, i + nums[i])

            if furthest_reach >= n - 1:
                return True
        
        return True # reached position
