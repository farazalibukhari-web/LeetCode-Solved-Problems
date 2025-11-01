class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max_num=0
        for row in range(len(mat)):
            num=max(mat[row])
            
            if max_num<num:
                max_num=max(num,max_num)
                max_num_index = mat[row].index(num)
                row1=row
        
        return [row1,max_num_index]