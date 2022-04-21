class Solution:
    def findDisappearedNumbers(self, nums) :

        length = len(nums)

        s1 = set(nums)

        res = []

        for i in range(1,length+1):
            if i not in s1:
                res.append(i)

        return res


nums = [1,1]

s1 = Solution()

print(s1.findDisappearedNumbers(nums))
