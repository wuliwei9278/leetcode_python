class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #排除所有错误的情况，那么剩下来的就是正确的
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':#只要是碰到了open的括号，就将其存入到list里面
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':    #遇到了close的括号，如果list里面是空的或者上一个括号不是对应括号，那么就是错的，与此同时，在list 中删除那个对应的括号
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:           #检查stake里面还有没有open的括号
            return False
        else:
            return True
        """
        list.pop() => is the last element in the list, then remove the last one
        """
        
        
#        d = {')': '(', ']': '[', '}': '{'}    close 的括号作为keys
#        stack = []                            
#        for c in s:
#            if c not in d:
#                stack.append(c)               如果不是close的括号，那么就把这些括号存入list
#            else:                             是open的括号，
#                if not stack: return False    如果list不空，那么就错了
#                _c = stack.pop()              _c是list里面的最后一个char（加入的open括号）
#                if _c != d[c]: return False   如果说_c不是对应的open括号，那么就错了
#        return not stack  检查最后是不是空了


#思维都是一样哒，因为后面的那个用的dictionary， 所以说runtime比用if statement 快
