import math

class Solution(object):

    def findmax(self, piles):
        maxi = float('-inf')
        n = len(piles)
        for i in range(n):
            maxi = max(maxi, piles[i])
        return maxi

    def calculatehours(self, piles, hourly):
        totalh = 0
        n = len(piles)

        for i in range(n):
            totalh += math.ceil(float(piles[i]) / hourly)
        return totalh

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            totalh = self.calculatehours(piles, mid)

            if totalh <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low