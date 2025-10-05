class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach=nums[0]
        i=0
        
        while i<=max_reach:
            max_reach=max(max_reach,i+nums[i])
            i+=1
            if max_reach>=len(nums)-1:
                return True
        return False