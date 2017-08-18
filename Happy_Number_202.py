class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """    
        if n == 1:
            return True   
        
        
        curr = n          #curr等于当前数
        res = 0
        values = []     #used to store values appeared before
        values.append(n)
        i = 0
        
        
        while curr != 1:                  
            num = str(curr)                #num代表当前数转换成str
            res = 0
            for i in range(len(num)):
                res += int(num[i])**2
                curr = res
            values.append(curr)
            if curr == 1:
                return True
            if curr == 4:    #why cannot use curr in values
                return False
        
        

        
        while 1:
            if n == 1: 
                return True
            if n == 4: 
                return False
            sum = 0
            while n:
                sum += (n%10)**2
                n /= 10
            n = sum
        """
        curr = n
        while True:              
            num = str(curr)               
            res = 0
            for i in range(len(num)):
                res += int(num[i])**2
                curr = res

            if curr == 1:
                return True
            if curr == 4:    #why cannot use curr in values
                return False
