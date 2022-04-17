class Solution:
    def singleNumber(self, nums) -> int:

        res = []

        for i in range(len(nums)):
            if nums[i] not in res:
                res.append(nums[i])
            else:
                res.remove(nums[i])

        return res[0]


nums = [4,1,2,1,2]
s1 = Solution()

res = s1.singleNumber(nums)

print(res)
