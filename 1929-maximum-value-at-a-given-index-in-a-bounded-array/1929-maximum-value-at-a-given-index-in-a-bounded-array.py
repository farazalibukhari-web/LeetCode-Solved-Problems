class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """

        def side_sum(peak, length):

            # number of values before reaching 1 on that side
            dec_steps = peak - 1
            if dec_steps >= length:
                return length * (2 * peak - length - 1) // 2
            else:
                return (dec_steps * (dec_steps + 1)) // 2 + (length - dec_steps)

        low, high = 1, maxSum
        ans = 1

        while low <= high:
            mid = (low + high) // 2  # candidate peak value

            left = side_sum(mid, index)                # sum of left side (index elements)
            right = side_sum(mid, n - index - 1)       # sum of right side
            total = left + mid + right

            if total <= maxSum:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans