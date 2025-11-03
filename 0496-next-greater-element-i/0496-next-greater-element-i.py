class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_list=[]
        
        for nums in nums1:
            pos=nums2.index(nums)
            next_greater_element=-1
            for i in range(pos+1,len(nums2)):
                if nums2[i]>nums:
                    next_greater_element=nums2[i]
                    break
            
            new_list.append(next_greater_element)
        
        return new_list