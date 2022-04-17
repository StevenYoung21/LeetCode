class Solution:
    def singleNumber(self, nums) -> int:

        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i]

        return res


nums = [2,1,2]
s1 = Solution()

res = s1.singleNumber(nums)

print(res)

# a=1
# b=2
# print(a^b^a^b)