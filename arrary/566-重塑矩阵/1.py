class Solution:
    def matrixReshape(self, mat, r: int, c: int) :

        m = len(mat)
        n = len(mat[0])

        if m*n != r*c :
            return mat

        all = []

        for i in mat:
            for j in i :
                all.append(j)

        res = []

        for i in range(r):
            res.append(all[i*c:i*c+c])
            
        return res



mat = [[1,2],[3,4]] 
r = 4
c = 1



s1 = Solution()
res = s1.matrixReshape(mat,r,c)

print(res)