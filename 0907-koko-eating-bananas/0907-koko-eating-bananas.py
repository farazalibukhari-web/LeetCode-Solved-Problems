class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        k = right

        while left <= right:
            mid = (left + right) // 2  #mid=Speed of Koko eating Banana
            hours = 0

            for p in piles:
                time = math.ceil(p / float(mid))  #Time taken by koko to finish the piles
                hours += time
                
            if hours <= h:
                k = mid
                right = mid - 1   
            else:
                left = mid + 1    

        return k

