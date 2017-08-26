class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for num in nums:
            mydict[num] = mydict.get(num, 0) + 1
        for num in mydict:
            if mydict[num] == 1:
                return num
