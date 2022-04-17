class Solution:
    def singleNumber(self, nums) -> int:

        res = {}

        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]] = 1
            else:
                res[nums[i]] += 1

        # for i in res.values():
        #     if i == 1:
        #         return 

        def get_keys(d, value):
            return [k for k,v in d.items() if v == value]

        return get_keys(res,1)[0]


nums = [4,1,2,1,2]
s1 = Solution()

res = s1.singleNumber(nums)

print(res)
