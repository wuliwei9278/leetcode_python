class Solution(object):
    def searchInsert(self, nums, target):
        
        
        nums = sorted(nums)
        
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        
        for i in range(len(nums)):
            if target > nums[i] and target < nums[i+1]:
                return i+1
            elif target == nums[i]:
                return i
"""            
class Solution(object):
    def searchInsert(self, nums, key):
        if key > nums[len(nums) - 1]:
            return len(nums)

        if key < nums[0]:
            return 0

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)/2
            if nums[m] > key:
                r = m - 1
                if r >= 0:
                    if nums[r] < key:
                        return r + 1
                else:
                    return 0

            elif nums[m] < key:
                l = m + 1
                if l < len(nums):
                    if nums[l] > key:
                        return l
                else:
                    return len(nums)
            else:
                return m
"""

