from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand = defaultdict(int)
        for bill in bills:
            if bill == 5:
                hand[5] += 1
            elif bill == 10:
                if hand[5] > 0:
                    hand[5] -= 1
                else:
                    return False
                hand[10] += 1
            else:
                if (hand[10] > 0 and hand[5] > 0):
                    hand[10] -= 1
                    hand[5] -= 1
                elif (hand[5] >= 3):
                    hand[5] -= 3
                else:
                    return False
                hand[20] += 1
        return True
