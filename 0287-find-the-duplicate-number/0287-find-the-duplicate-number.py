class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                return nums[idx]
        