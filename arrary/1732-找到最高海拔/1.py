class Solution:
    def largestAltitude(self, gain) -> int:

        start = 0

        maxNum = -float('inf')

        for i in range(len(gain)):

            start += gain[i]

            maxNum = max(start,maxNum,0)


        return maxNum

gain = [-5,1,5,0,-7]

s1 = Solution()

print(s1.largestAltitude(gain))

