from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, speed) for pos, speed in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = deque()
        for pos, speed in pairs:
            time_taken = (target - pos) / speed
            if not stack or time_taken > stack[-1]:
                stack.append(time_taken)
        return len(stack)