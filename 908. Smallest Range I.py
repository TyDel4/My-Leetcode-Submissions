class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max1 = max(nums)
        min1 = min(nums)

        if (max1 - min1 <= k * 2):
            return 0
        else:
            return (max1 - min1) - k * 2
        