class Solution:
    def sortArrayByParityII(self, nums) :

        a1 = []
        a2 = []

        for i in nums:
            if i %2 != 0:
                a1.append(i)
            else:
                a2.append(i)

        res = []

        for i in range(len(a1)):
            res.append(a2[i])
            res.append(a1[i])

        return res


nums = [4,2,5,7]

s1 = Solution()

print(s1.sortArrayByParityII(nums))