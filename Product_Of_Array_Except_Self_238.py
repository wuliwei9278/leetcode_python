class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #每一个output的数应该是左边的积乘以右边的积
        
        l = 1
        n = len(nums)
        res = []
        for i in range(0,n):          #过一边nums里的数，存到res里=>对应当前数是之前数的积
            res.append(l)            # res:[1,1,2,6]
            l = l * nums[i]
        
        r = 1
        for i in range(n-1,-1,-1):
            res[i] = res[i] * r     #res：[,,,6] [,,8,6] [24,12,8,6]
            r = r * nums[i]         #r : 1，4，12， 24  （代表非本身的右边的数）
        return res
        
