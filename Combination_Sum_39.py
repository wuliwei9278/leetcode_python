def combinationSum(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(remaining, chosen, candidates):
            """remaining => int
               chosen => List[int]
               candidates => List[int]"""
            if remaining == 0:
                res.append(chosen)
                return
            for i in range(len(candidates)):
                if remaining - candidates[i] >= 0:
                    print(i)
                    print(remaining - candidates[i])
                    print(chosen + [candidates[i]])
                    print(candidates[i:])
                    print("                  ")
                    dfs(remaining - candidates[i], chosen + [candidates[i]], candidates[i:])
                else:
                    return 
        dfs(target, [], candidates)
        return res
