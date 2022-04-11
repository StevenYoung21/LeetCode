from gettext import dpgettext


class Solution:
    def generate(self, numRows: int) :

        
        if numRows == 1 :
            return [[1]]

        dp = [] 


        for i in range(1, numRows + 1):
            dp.append([1]*i )

        for i in range(2,len(dp)):
            for j in range(1,len(dp[i])-1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp


numRows = 5


s1 = Solution()
res = s1.generate(numRows)

print(res)