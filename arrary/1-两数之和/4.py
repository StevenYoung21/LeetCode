
class Solution:
    def twoSum(self, nums, target: int) :

        dis = {}

        for index, val in enumerate(nums):
            if target - val not in dis:
                dis[val] = index
            else:
                return[dis[target-val], index]

        return dis



## 哈希表

nums = [2,7,11,15]
target = 9


s1 = Solution()
res = s1.twoSum(nums,target)

print(res)