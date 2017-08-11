class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for z in nums:
            if z != 0:
                nums[i] = z
                i += 1
        
        for i in range(i,len(nums)):
            nums[i] = 0
