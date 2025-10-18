class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
        if not nums or len(nums)==1 and nums[0]!=target:
            return -1

        # Find pivot: index of the smallest element
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # pivot is to the right
                l = mid + 1
            else:
                # pivot is at mid or to the left
                r = mid
        pivot = l  # smallest element index

        # Decide which half to binary-search
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1

        # Standard binary search in chosen half
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1



