class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """

        target = abs(target)
        pos = 0
        step = 0
        while pos < target or (pos - target) % 2 != 0:
            step += 1
            pos += step
        return step        