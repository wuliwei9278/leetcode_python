class Solution(object):
    def reverse(self, x):
        res = 0
        if x >= 0:
            pos = True
        else:
            pos  = False
            x = -x
        while not x == 0:
            if res > 214748364:
                return 0
            else:
                res = res * 10 + x % 10
                x = x / 10
        if pos:
            return res
        else:
            return -res
