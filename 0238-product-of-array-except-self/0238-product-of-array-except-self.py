class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        last_nums=[1]
        next_nums=[1]

        for i in range(1,len(nums)):
            last_nums.append(last_nums[i-1]*nums[i-1])
        
        nums=nums[::-1]
        for j in range(1,len(nums)):
            next_nums.append(next_nums[j-1]*nums[j-1])
        next_nums=next_nums[::-1]
        
        for a in range(len(nums)):
            answer.append(last_nums[a]*next_nums[a])
        
        return answer
            
         
