class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_s = s.split()
        return len(new_s)
    
        """
        
        count, n = 0, 0
        if s == '':
            return 0 
        for char in s:
            if char != ' ':
                n += 1
            if n > 0 and char == ' ':
                count += 1
                n = 0
        if n > 0:
            count += 1
        return count 
        
        """
