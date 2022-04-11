class Solution:
    def matrixReshape(self, mat, r: int, c: int) :

        m = len(mat)
        n = len(mat[0])

        if m*n != r*c :
            return mat

        res = []
        path = []

        for words in mat:
            for word in words :
                path.append(word)
                if len(path) == c:
                    res.append(path)
                    path = []

        return res



mat = [[1,2],[3,4]] 
r = 1
c = 4



s1 = Solution()
res = s1.matrixReshape(mat,r,c)

print(res)