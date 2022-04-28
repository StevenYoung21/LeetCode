
class Solution:
    def isHappy(self, n: int) -> bool:

        def fun1 (n):
            res = 0
            while n >= 1:
                a = n % 10
                res = a**2 + res
                n = n//10
            return res

        res = []

        while 1:

            num = fun1(n)

            if num not in res:
                if num == 1:
                    return True
                res.append(num)
            else:
                return False
            n = num





n = 2

s1 = Solution()

print(s1.isHappy(n))