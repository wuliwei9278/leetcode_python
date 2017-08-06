class Solution(object):
    def lengthOfLastWord(self, s):
        """
            :type s: str
            :rtype: int
            """
        if s == '':
            return 0
        new_str = s[::-1]
        num = 0
        
        while num < len(new_str) and new_str[num] == ' ':
            num += 1
        
        length = 0
        for i in range(num,len(new_str)):
            if new_str[i] != ' ':
                length += 1
            else:
                break
        
        return length
