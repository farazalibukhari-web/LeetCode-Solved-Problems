class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right_most=0,len(nums)-1
        left_most,right=0,len(nums)-1
        new_list=[-1,-1]
        
        while left<=right_most:
            mid=(left+right_most)//2
            if nums[mid]==target:
                new_list[0]=mid
                right_most=mid-1
            elif nums[mid]>target:
                right_most=mid-1
            elif nums[mid]<target:
                left=mid+1
        
        
        while left_most<=right:
            mid=(left_most+right)//2
            if nums[mid]==target:
                new_list[1]=mid
                left_most=mid+1
            elif nums[mid]<target:
                left_most=mid+1
            elif nums[mid]>target:
                right=mid-1

        return new_list
     
