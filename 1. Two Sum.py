class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = False

        for i in range(len(nums)):
            for j in range(len(nums) - i):
                if nums[i] + nums[i + j] == target:
                    if i != j + i:
                        found = True
                        break
            if found:
                break
        return [i, j + i]
    