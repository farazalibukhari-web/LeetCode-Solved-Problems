class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return nums
        k=k%len(nums)
        def reverse_list(left,right): #Defined Function For List Reversing
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse_list(0,len(nums)-1) # Reversing Complete List 
        reverse_list(0,k-1)         # Reversing Again First of List
        reverse_list(k,len(nums)-1) # Reversing Again Second of List
        return nums
