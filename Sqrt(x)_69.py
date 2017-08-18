class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        i = 0
        j = x
        
        
        
        while i <= j :
            m = (i+j)/2
            if m * m <= x and (m + 1) * (m + 1) > x:
                return m
            elif m ** 2 > x:
                j = m
            elif m ** 2 < x:
                i = m + 1
