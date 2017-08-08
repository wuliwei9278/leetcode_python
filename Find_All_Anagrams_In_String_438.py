class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lp = len(p)  
        ls = len(s)  
          
         
        dp = {}
        ds = {}
          
          
        for i in s[:lp]:  
            ds[i] = ds.get(i,0) + 1  
        for i in p[:lp]:  
            dp[i] = dp.get(i,0) + 1  
              
          
        res = []  
        i = 0  
          
        while i < (ls-lp):  
            if dp == ds:  
                res += i,  
              
            ds[s[i]] -= 1  
            if ds[s[i]] == 0:  
                del ds[s[i]]  
            ds[s[i+lp]] = ds.get(s[i+lp],0) + 1  
            i+= 1  
        if ds == dp:  
            res += i,  
              
        return res 
                
