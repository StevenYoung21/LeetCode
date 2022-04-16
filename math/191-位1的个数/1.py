
class Solution:
    def hammingWeight(self, n: int) -> int:

        str1 = str(bin(n))

        k = 0

        for i in range(len(str1)):
            if str1[i] == '1':
                k += 1

        return k



n = 0B00000000000000000000000000001011

s1 = Solution()

res = s1.hammingWeight(n)

print(res)