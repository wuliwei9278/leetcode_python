class Solution(object):
    def romanToInt(self, s):
        """
            :type s: str
            :rtype: int
            """
        dic = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        
        current_value = 0
        total = 0
        
        for i in range(len(s)-1):
            current_value = dic[s[i]]
            if current_value >= dic[s[i+1]] :
                total += current_value
            else:
                total -= current_value
        
        total += dic[s[len(s)-1]]
        
        return total

