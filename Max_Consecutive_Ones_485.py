class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        m = 0                      
        count = 0
        '''
        m => max number of 1
        count => used to count consecutive 1s
        '''
        
        for i in range(len(nums)):    
            if nums[i] == 1:         
                count += 1
                if i == len(nums) - 1 and count > m:
                    return count
                
            
            else:
                if count > m:
                    m = count
                count = 0
        return m
        
