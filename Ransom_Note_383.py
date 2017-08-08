class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}
        
        for char in ransomNote:
            dict1[char] = dict1.get(char,0) + 1
            
        for char in magazine:
            dict2[char] = dict2.get(char,0) + 1
            
        for char in ransomNote:
            if char not in dict2 or dict1[char] > dict2[char] :
                return False
        return True
        
#   class Solution(object):
#        def canConstruct(self, ransomNote, magazine):
#        """
#        :type ransomNote: str
#        :type magazine: str
#        :rtype: bool
#        """
#        for x in set(ransomNote):
#            if x not in magazine:
#               return False
#           if ransomNote.count(x) > magazine.count(x):
#               return False
#       return True
