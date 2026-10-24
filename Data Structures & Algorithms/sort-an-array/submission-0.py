class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge Sort
        def merge(list1: List[int], list2: List[int]) -> List[int]:
            merged = []
            i = j = 0
            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    merged.append(list1[i])
                    i += 1
                else:
                    merged.append(list2[j])
                    j += 1
            merged.extend(list1[i:])
            merged.extend(list2[j:])
            return merged
        if len(nums) <= 1:
            return nums
        m = len(nums) // 2
        return merge(self.sortArray(nums[:m]), self.sortArray(nums[m:]))