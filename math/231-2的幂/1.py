
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0 : return False

        res = [1]

        for i in range(32):
            res.append(res[i] * 2) 
            if n in res:
                return True


        return False 


n = 32

s1 = Solution()

res = s1.isPowerOfTwo(n)

print(res)