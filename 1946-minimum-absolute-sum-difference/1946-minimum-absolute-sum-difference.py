class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        sort_nums1 = sorted(nums1)
        total = 0
        max_gain = 0
        
        if nums1==nums2:
            return 0
        
        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            total += diff

            # binary search
            l, r = 0, len(nums1) - 1
            best_diff = diff

            while l <= r:
                mid = (l + r) // 2
                if sort_nums1[mid] == nums2[i]:
                    best_diff = 0
                    break
                elif sort_nums1[mid] < nums2[i]:
                    l = mid + 1
                else:
                    r = mid - 1

            # check closest neighbors
            if l < len(nums1):
                best_diff = min(best_diff, abs(sort_nums1[l] - nums2[i]))
            if r >= 0:
                best_diff = min(best_diff, abs(sort_nums1[r] - nums2[i]))

            max_gain = max(max_gain, diff - best_diff)

        return (total - max_gain) % MOD
            
                    