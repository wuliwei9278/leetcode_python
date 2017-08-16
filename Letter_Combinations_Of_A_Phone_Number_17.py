def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        """
DFS "2,3,4"
map:
2 => a,b,c
3 => d,e,f
4 => g,h,i

num:    2       3       4
        a-----> ad------>adg
        a-----> ad------>adh
        a-----> ad------>adi
        a-----> ae------>aeg
        a-----> ae------>aeh
        a-----> ae------>aei
                af
                ...
        b
        ...
        c
        ...

1. variable in recursive function: current string, index, string after
2. termination： index = num.length

"""

        def dfs(num, sr, res):
            """
            num => index of strings
            sr => string that have already been generated  
            """
            
            if num == length:                   #finish all the digits
                res.append(sr) 
                return
            for ch in mydict[digits[num]]:    # ['a', 'b', 'c'] => a, b, c 
                dfs(num + 1, sr + ch, res)
 
        mydict = {'2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'], 
                  '4': ['g', 'h', 'i'], 
                  '5': ['j', 'k', 'l'], 
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'], 
                  '9': ['w', 'x', 'y', 'z']
        }

        res = []
        length = len(digits)
        if length == 0:
            return []
        dfs(0, '', res)
        return res
