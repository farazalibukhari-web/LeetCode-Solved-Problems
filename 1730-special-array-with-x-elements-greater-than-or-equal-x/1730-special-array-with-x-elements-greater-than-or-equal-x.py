class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=max(nums)
        for x in range(n+1):
            count=0
            for i in nums:
                if x<=i:
                    count+=1
            if count==x:
                return (count)
        return (-1)

