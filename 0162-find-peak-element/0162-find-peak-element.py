class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        l=0
        r=len(nums)-1
        while l<r:
            mid = (r+l)//2
            if nums[mid]>nums[mid+1]:
                r=mid
            else:
                l=mid+1
        return l