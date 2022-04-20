class Solution:
    def totalFruit(self, fruits) -> int:

        start =  0

        length = len(fruits)
        res = {}
        maxLen = 0

        for end in range(length):

            if len(res) <= 2:

                if fruits[end] not in res:
                    res[fruits[end]] = 1
                else:
                    res[fruits[end]] += 1

            while len(res) > 2:
                res[fruits[start]] -= 1
                if res[fruits[start]] == 0:
                    del res[fruits[start]]
                    # res.pop(fruits[start])
                start += 1

            maxLen = max( maxLen,end - start + 1 )

        return maxLen


fruits = [1,2,3,2,2]

s1 = Solution()

print(s1.totalFruit(fruits))