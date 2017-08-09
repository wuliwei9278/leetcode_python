# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        """Binary research"""
        i=1
        j=n
        while i<j:
            k=(i+j)/2
            if isBadVersion(k):
                j=k
            else:
                i=k+1
        return i
        
