class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        prefix = [0]
        #Creating the list of sum till last index
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        res = 1  #To return number with frequency of one
        n = len(nums)
        
        for r in range(n):
            l = 0
            low, high = 0, r
            while low <= high:
                mid = (low + high) // 2
                total = nums[r] * (r - mid + 1) - (prefix[r + 1] - prefix[mid])
                
                if total <= k:
                    l = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            res = max(res, r - l + 1)
        
        return res