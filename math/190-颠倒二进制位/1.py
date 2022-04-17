
class Solution:
    def reverseBits(self, n: int) -> int:

        str1 = str(bin(n))
        # nums0 = 32 - len(str1)

        str2 = str1[2:]
        str2 = str2[::-1]
        nums0 = 32 - len(str2)

        while nums0 > 0:
            str2 = str2 + '0'
            nums0 -= 1

        res = int(str2,2)

        return res

n = 0B00000010100101000001111010011100

s1 = Solution()

res = s1.reverseBits(n)

print(res)
