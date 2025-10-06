class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        mid=0
        right=len(nums)-1
        
        while mid<=right:
            if nums[mid]==0:
                nums[mid],nums[left]=nums[left],nums[mid]
                mid+=1
                left+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
        return nums