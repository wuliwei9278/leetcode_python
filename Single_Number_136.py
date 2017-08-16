class Solution(object):
    def singleNumber(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        
        """nums.sort()
            i=0
            while i < len(nums)-1:
            if nums[i] == nums[i+1]:
            i+1
            else:
            return nums[i]
            
            return nums[0]
            """
        
        
        
        
        
        
        
        mydict = {}
        for num in nums:
            mydict[num] = mydict.get(num, 0) + 1
        for num in mydict:
            if mydict[num] == 1:
                return num
    
    """
        res = 0
        for n in nums:
        res ^= n
        return res
        """
