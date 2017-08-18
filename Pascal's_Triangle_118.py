class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows + 1):
            l = []
            for j in range(0,i):
                if j == 0:
                    l.append(1)
                elif j == i - 1:
                    l.append(1)
                else:
                    l.append(res[i-2][j] + res[i-2][j-1])
            res.append(l)
            
        
        return res
                    
                    
