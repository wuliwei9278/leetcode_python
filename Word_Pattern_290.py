class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        l = str.split()                 #如果pattern的长度和letter的个数不一样直接归错误
        if len(pattern) != len(l):
            return False
        
        
        
        mydict = {}
        for i in range(len(l)):               #对应找出pattern和letter是不是一样哒 
            if l[i] not in mydict:            
                mydict[l[i]] = pattern[i]
            if pattern.count(pattern[i]) != l.count(l[i]): #看出现的次数
                return False
            else:
                if pattern[i] != mydict[l[i]] :
                    return False
        return True
                       
                       
        """               
        
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)
        """
