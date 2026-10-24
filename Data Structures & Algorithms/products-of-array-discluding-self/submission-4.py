from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nonzeroentries = [x for x in nums if x != 0]
        # has_zero = False
        # if len(nonzeroentries) <= len(nums) - 2:
        #     return [0] * len(nums)
        # elif len(nonzeroentries) == len(nums) - 1:
        #     has_zero = True
        # else:
        #     has_zero = False
        # nonzeroproduct = int(prod(nonzeroentries))
        # output = []
        # for num in nums:
        #     if num == 0:
        #         output.append(nonzeroproduct)
        #     elif has_zero:
        #         output.append(0)
        #     else:
        #         output.append(nonzeroproduct // num)
        # return output

        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n

        pref[0] = suff[n-1] = 1
        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

