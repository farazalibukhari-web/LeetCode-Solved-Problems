class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicate i
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue  # skip duplicate j
                for k in range(j+1, n):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue  # skip duplicate k
                    for l in range(k+1, n):
                        if l > k+1 and nums[l] == nums[l-1]:
                            continue  # skip duplicate l

                        total = nums[i] + nums[j] + nums[k] + nums[l]
                        if total == target:
                            res.append([nums[i], nums[j], nums[k], nums[l]])
                        elif total > target:
                            break  # stop inner loop early since array is sorted

        return res