class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l,r=max(weights),sum(weights)
                    
        while l<r:
            cap=0
            ship=1    
            mid=(l+r)//2
            for w in weights:
                if cap + w > mid:
                    ship += 1
                    cap = 0
                cap += w

            if ship> days:
                l=mid+1
            else:
                r=mid
        return l        