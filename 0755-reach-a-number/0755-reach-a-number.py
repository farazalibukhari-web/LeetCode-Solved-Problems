class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target=abs(target)
        steps = 0
        l = 0
        r = target
        while l <= r:
            mid = (l+r)//2
            s = mid*(mid+1)/2
            if s >= target:
                steps = mid
                r = mid-1
            else:
                l = mid+1
        s = steps*(steps+1)/2
        if (s-target)%2 == 0:
            return steps
        else:
            if (steps+1)%2 != 0:
                return steps+1
            else:
                return steps+2   