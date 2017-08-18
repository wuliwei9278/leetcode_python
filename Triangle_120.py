class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        """
        l = len(triangle)
        res = triangle[0][0]
        j = 0
        if l == 1:
            return triangle[0][0]
        
        for i in range(0,l-1):  #number of each rows
            if triangle[i+1][j] > triangle[i+1][j+1]:        
                res += triangle[i+1][j+1]
                j += 1
            else:
                res += triangle[i+1][j]
                j = j
        return res
    
        """
        for i in reversed(range(len(triangle) - 1)):
            for j in range(0, i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
