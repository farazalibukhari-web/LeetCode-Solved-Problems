class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        count = 0
        max_count=0
        for i in nums:
            if i==1:
                count=count+1
            else:
                count=0
            max_count=max(max_count,count)
        return max_count
       
        