class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l,r=max(weights),sum(weights)
        
        def shipcap(weights,days,max_load):
            ship=1
            cap=0
            for w in weights:
                if cap+w>max_load:
                    cap=0
                    ship+=1
                cap+=w
                if ship>days:
                    return False                   
            return True
        while(l<r):
            mid=(l+r)//2
            if shipcap(weights,days,mid):
                r=mid
            else:
                l=mid+1
        return l