class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # Base cases
        if not nums or (len(nums) == 1 and nums[0] != target):
            return False
        elif len(nums) == 1 and nums[0] == target:
            return True

        l, r = 0, len(nums) - 1
        pivot = 0   # ✅ define pivot safely at start

        # --- Find pivot (largest element index) ---
        while l < r:
            mid = (l + r) // 2

            if nums[l] == nums[mid] == nums[r]:
                # Handle duplicates on both ends
                if l + 1 < len(nums) and nums[l] > nums[l + 1]:
                    pivot = l
                    break
                l += 1
                if r - 1 >= 0 and nums[r] < nums[r - 1]:
                    pivot = r - 1
                    break
                r -= 1
            else:
                # Normal pivot detection
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
                pivot = l - 1  # track latest possible pivot

        # ✅ ensure pivot is within valid range
        if pivot < 0:
            pivot = len(nums) - 1

        # --- Binary search in correct half ---
        if target >= nums[(pivot + 1) % len(nums)] and target <= nums[-1]:
            l, r = (pivot + 1) % len(nums), len(nums) - 1
        else:
            l, r = 0, pivot

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
