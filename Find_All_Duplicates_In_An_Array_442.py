class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #因为nums里的数是不会超过nums的个数的，所以可以直接用nums来找出现了两次的数
        res = []
        for x in nums:                  #先按顺序过一遍nums里的数  x=>index
            if nums[abs(x) - 1] < 0:    #如果x指示的词是负数，说明之前我们见过它啦，那么就把他加入到res里吧
                res.append(abs(x))      
            else:
                nums[abs(x) - 1] *= -1  #如果木有见过它嘞，那么就把它弄成负数吧   
        return res
    
    
        """
        # hash
        h = {}
        ans = []
        
        for x in nums:
            if x in h:
                ans.append(x)
            else:
                h[x] = 1
                
        return ans"""
