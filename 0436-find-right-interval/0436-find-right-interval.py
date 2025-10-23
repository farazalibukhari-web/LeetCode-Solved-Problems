class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        new_list=[]
        start=[(intervals[i][0],i)for i in range(len(intervals))]
        start.sort()
        
        for j in range(len(intervals)):
            end_num=intervals[j][1]
            
            l,r=0,len(intervals)-1
            start_num=-1
            while l<=r:
                mid=(l+r)//2
                if end_num<=start[mid][0]:
                    start_num=start[mid][1]
                    r=mid-1
                else:
                    l=mid+1
                
            new_list.append(start_num)
        return new_list
