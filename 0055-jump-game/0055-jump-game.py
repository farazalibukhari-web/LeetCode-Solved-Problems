class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
            """
        last_num=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=last_num:
                last_num=i
        return last_num==0
        