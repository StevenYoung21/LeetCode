
class Solution:
    def generateMatrix(self, n: int) :

        if n == 1 : return [[1]]

        matrix = [[0 for _ in range(n)] for _ in range(n) ]

        left, top, right, down = 0, 0, n-1, n-1

        num, target = 1, n*n

        while num < target:
            for i in range(left, right):
                matrix[top][i] = num
                num += 1
            for i in range(top, down):
                matrix[i][right] = num
                num += 1
            for i in range(right, left,-1):
                matrix[down][i] = num
                num += 1
            for i in range(down, top,-1):
                matrix[i][left] = num
                num += 1

            left += 1
            top += 1
            right -= 1
            down -= 1
        
        if num == target:
            matrix[top][left] = num
        return matrix

n = 3

s1 = Solution()

print(s1.generateMatrix(n))