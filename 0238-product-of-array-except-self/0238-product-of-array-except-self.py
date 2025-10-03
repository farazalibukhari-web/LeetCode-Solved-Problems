class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[1]*len(nums)
        for i in range(1,len(nums)):
            answer[i]=answer[i-1]*nums[i-1]
        next_num=1
        for j in range(len(nums)-1,-1,-1):
                answer[j]=answer[j]*next_num
                next_num=next_num*nums[j]
        return answer  
            
