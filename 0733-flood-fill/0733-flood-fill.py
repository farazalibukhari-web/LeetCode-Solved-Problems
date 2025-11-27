class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        stack=[]
        
        origColor=image[sr][sc]
        image[sr][sc]=color
        stack.append((sr,sc))
        a=0
        while stack:
            if a==len(stack) or a==len(image)*len(image[0]):
                return image
            r,c=stack[a][0],stack[a][1]
            # UP
            if r-1 >= 0 and image[r-1][c] == origColor:
                stack.append((r-1, c))
                image[r-1][c] = color
            # DOWN
            if r+1 < len(image) and image[r+1][c] == origColor:
                stack.append((r+1, c))
                image[r+1][c] = color
            # LEFT
            if c-1 >= 0 and image[r][c-1] == origColor:
                stack.append((r, c-1))
                image[r][c-1] = color
            # RIGHT
            if c+1 < len(image[0]) and image[r][c+1] == origColor:
                stack.append((r, c+1))
                image[r][c+1] = color
            a+=1
