class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1:
            return True
        if n == 0:
            return False
        if n % 4 == 0:
            n = n / 4
            return self.isPowerOfFour(n)
        else:
            return False


'''
递归:
1. 确定参数和返回值
2. 终止条件
3. 单层递归逻辑


1. 参数:n, 返回值 T/F
2. n == 1 or n % 4 != 0
3. 如果 n % 4 == 0 , 则继续递归

'''


n = 16

s1 = Solution()

print(s1.isPowerOfFour(n))