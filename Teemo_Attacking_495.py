class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        
        res = duration
        for i in range(len(timeSeries)-1,0,-1):     #从后往前查，不检查第一个 
            if timeSeries[i] - timeSeries[i-1] >= duration:  #如果后一个比前一个的差大于duration，那么直接加
                res += duration
            else:
                res += timeSeries[i] - timeSeries[i-1]#不然的话就加上它们的差
        return res
    
