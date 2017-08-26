class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        mydict = {}
        for num in nums:
            mydict[num] = 1
        
        res = []
        for i in range(1,len(nums)+1):
            if i not in mydict:
                res.append(i)
            
        return res  
