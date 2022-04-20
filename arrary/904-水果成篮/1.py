class Solution:
    def totalFruit(self, fruits) -> int:

        start =  0

        length = len(fruits)

        res = []
        numbers = set()
        maxLen = 0

        for end in range(length):

            numbers.add(fruits[end])
            res.append(fruits[end])

            while len(numbers) > 2:
                res.pop(0)
                start += 1
                numbers = set(res)
            resLen = end - start + 1 

            maxLen = max(maxLen, resLen)

        return maxLen


fruits = [1,2,3,2,2]

s1 = Solution()

print(s1.totalFruit(fruits))