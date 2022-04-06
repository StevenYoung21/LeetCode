
class Solution:
    def twoSum(self, nums, target: int) :

        length = len(nums)

        for i in range(length):
            index = target - nums[i]
            if index in nums and i != nums.index(index) :
                return[i,nums.index(index)]  





nums = [2,7,11,15]
target = 9


s1 = Solution()
res = s1.twoSum(nums,target)

print(res)