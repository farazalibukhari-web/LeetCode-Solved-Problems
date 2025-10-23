class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        
        res = 1
        remain = maxSum - n

        req = 1
        expand = 0

        while remain >= req:
            res += 1
            remain -= req
            expand += 1
            left_e = min(index,expand)
            right_e = min(n-index-1,expand)
            req = left_e + right_e + 1
            if req == n:
                break
        if remain > 0:
            res += remain/n

        return res