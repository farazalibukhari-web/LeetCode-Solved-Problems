class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if nums[mid]==nums[mid-1] and mid%2==0 or nums[mid]==nums[mid+1] and mid%2!=0:
                right = mid
            else:
                left = mid+1
        return nums[left]
        