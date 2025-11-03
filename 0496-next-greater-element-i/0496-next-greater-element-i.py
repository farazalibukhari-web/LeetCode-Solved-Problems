class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater_map = {}

        for num2 in nums2:
            while stack and num2 >stack[-1]:
                smaller_num = stack.pop()            
                next_greater_map[smaller_num] = num2  

            stack.append(num2)

        result = []
        for num1 in nums1:
            result.append(next_greater_map.get(num1, -1))

        return result