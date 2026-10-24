class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            new_num = 0
            while n != 0:
                new_num += (n % 10) ** 2
                n //= 10
            n = new_num
        return True