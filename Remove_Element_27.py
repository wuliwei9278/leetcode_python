class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for x in nums:
            if x != val:         #如果不是val，就加入list
                nums[i] = x
                i += 1           #每加一个element，就把index加一
        return i
