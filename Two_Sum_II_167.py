class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        
        for i in range(len(numbers)):
            if numbers[i] in mydict:
                return [mydict[numbers[i]]+1, i+1]
            else:
                mydict[target - numbers[i]] = i
        
        

