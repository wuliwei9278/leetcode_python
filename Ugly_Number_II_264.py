class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        def isUgly(num):
            if num <= 0: 
                return False
            for x in [2, 3, 5]:
                while num % x == 0:
                    num /= x
            return num == 1
        
        count = 1
        temp = 1
        
        while count < n:
            temp +=1
            if isUgly(temp):
                count += 1
        return temp
        """
        res = [1] * n
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            new = min(res[i2] * 2, res[i3] * 3, res[i5] * 5)
            if new == res[i2] * 2:
                i2 += 1
            if new == res[i3] * 3:
                i3 += 1
            if new == res[i5] * 5:
                i5 += 1
            res[i] = new
        return res[-1]
        
    
    
    
    
