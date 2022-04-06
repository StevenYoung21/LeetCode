class Solution:
    def twoSum(self, nums, target: int) :

        length = len(nums)

        for i in range(length):
            for j in range(i+1,length):
                if nums[i] + nums[j] == target:
                    return [i,j]
   


numbers = [0,2,7,11,15,0]
target = 0


## 双循环暴力解法

s1 = Solution()
res = s1.twoSum(numbers,target)

print(res)