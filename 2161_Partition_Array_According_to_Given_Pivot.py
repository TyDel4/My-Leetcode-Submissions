from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        greater_than_pivot = []
        equal_to_pivot = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                less_than_pivot.append(nums[i])
            elif nums[i] > pivot:
                greater_than_pivot.append(nums[i])
            else:
                equal_to_pivot.append(nums[i])
        
        return less_than_pivot + equal_to_pivot + greater_than_pivot