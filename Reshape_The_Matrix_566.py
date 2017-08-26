class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        a = len(nums)
        b = len(nums[0])
        
        if a * b != r * c:
            return nums
        
        d = []
        for i in range(a):
            for j in range(b):
                d.append(nums[i][j])
        
        e = 0
        res = []
        for i in range(r):
            l = []
            for j in range(c):
                l.append(d[e])
                e += 1
            res.append(l)
        return res

        """
    
        row = len(nums)
        col = len(nums[0])
        if (row * col) == (r * c):
            res = [[None] * c for _ in range(r)]
            x, y = 0, 0
            for rows in nums:
                for num in rows:
                    res[x][y] = num
                    y += 1
                    if y == c:
                        y = 0
                        x += 1
            return res
                
        return nums
        """
