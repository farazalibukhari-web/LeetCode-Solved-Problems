class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=max(nums)
        for x in range(n+1):        
            left=0
            right=len(nums)-1
            count=0
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>=x:
                    right=mid-1
                else:
                    left=mid+1
            count=len(nums)-left
            if count==x:
                return count
        return (-1)

