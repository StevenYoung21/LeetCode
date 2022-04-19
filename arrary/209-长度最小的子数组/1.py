
class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:

        start = 0
        end = 0

        sum = 0
        res = float('inf')


        while  end < len(nums):

            sum += nums[end]

            while sum >= target:
                res = min(res, end-start+1)
                sum -= nums[start]
                start += 1

            end += 1

        if res == float('inf') : return 0

        return res if res > 0 else 0

target = 11
nums = [1,1,1,1,1,1,1,1]

s1 = Solution()
res = s1.minSubArrayLen(target,nums)

print(res)