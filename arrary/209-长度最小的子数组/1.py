from copy import deepcopy


class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:

        start = 0
        end = 0

        res1 = []
        res2 = []

        while start <= end and end < :

            if sum(res1) < target: 
                res1.append(nums[end])
                end += 1

                # if end == len(nums)-1:
                #     continue
                # elif end < len(nums):
                #     res1.append(nums[end])
                #     end += 1
                # print('小于:',res1)
            # if sum(res1) > target:
            #     res1.pop(0)
            #     start += 1
                # print('大于:',res1)
            if sum(res1) >= target:
                res2.append(deepcopy(res1))
                res1.pop(0)
                start += 1

        return res2

        # if res2 == []: return 0

        # minLen = 106

        # for i in res2:
        #     minLen = min(minLen, len(i))

        # return minLen

target = 11
nums = [1,2,3,4,5]

s1 = Solution()
res = s1.minSubArrayLen(target,nums)

print(res)