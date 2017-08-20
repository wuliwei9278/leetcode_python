class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while abs(num) >= 0:
            temp = num
            if num % 2 == 0:
                num = num / 2
            if num % 3 == 0:
                num = num / 3
            if num % 5 == 0:
                num = num / 5
            if num == 1:
                return True
            if num == temp:
                return False
                
            """
            if num <= 0: 
                return False
            for x in [2, 3, 5]:
            
                while num % x == 0:
                    num /= x
                    return num == 1
            """
