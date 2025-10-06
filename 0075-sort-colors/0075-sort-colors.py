class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = white = blue = 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        count = 0
        for _ in range(red):
            nums[count] = 0
            count += 1
        for _ in range(white):
            nums[count] = 1
            count += 1
        for _ in range(blue):
            nums[count] = 2
            count += 1