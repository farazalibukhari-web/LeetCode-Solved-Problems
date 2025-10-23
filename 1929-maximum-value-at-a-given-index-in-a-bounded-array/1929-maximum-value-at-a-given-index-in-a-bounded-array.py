class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        low, high = 1, maxSum
        ans = 1

        while low <= high:
            mid = (low + high) // 2

            # Total sum = left side + middle + right side
            if mid - 1 >= index:
                left = index * mid - (index * (index + 1)) // 2
            else:
                left = (mid * (mid - 1)) // 2 + (index - (mid - 1))

            right_length = n - index - 1
            
            if mid - 1 >= right_length:
                right = right_length * mid - (right_length * (right_length + 1)) // 2
            else:
                right = (mid * (mid - 1)) // 2 + (right_length - (mid - 1))

            total = left + mid + right

            if total <= maxSum:
                ans = mid        # mid fits → try higher
                low = mid + 1
            else:
                high = mid - 1   # too big → go lower

        return ans