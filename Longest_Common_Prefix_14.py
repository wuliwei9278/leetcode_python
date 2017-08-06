class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
	    # abccc abc => abc
        # dsdsds => ? 'dsdsds'
        # [] => ''
        # aa aa
        def check(target, i, strs):
            """
            check if target character exists in all of the strings in strs list

            args:
                target: character
                i: ith place to look at in str in strs
                strs: string list
            return:
                boolean
            """
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != target:
                    return False
            return True

        if not strs:
            return ''
        first_str = strs[0]
        index_longest = 0
        for i in range(len(first_str)):
            target = first_str[i]
            if not check(target, i, strs):
                break
            else:
                index_longest += 1
        return first_str[:index_longest]

def main():
    sol = Solution()
    print(sol.longestCommonPrefix(["absd", "ab"]))
    print(sol.longestCommonPrefix(["absd"]))
    print(sol.longestCommonPrefix(["ab", "ab"]))

if __name__ == '__main__':
    main()
