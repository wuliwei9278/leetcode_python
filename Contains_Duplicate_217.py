class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mydict = {}
        
        for num in nums:
            if num in mydict:
                return True
            else:
                mydict[num] = 1
        return False
    
    
        """
        return len(nums)>len(set(nums))   a = [1,2,3,3] set(a) => [1,2,3]
        """
