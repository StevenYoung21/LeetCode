class Solution:
    def containsDuplicate(self, nums) -> bool:

        length = len(nums)

        nums.sort()
        
        for i in range(length-1):
            if nums[i] == nums[i+1]:
                return True

        return False




 



nums = [1,2,3,4]


## 排序

s1 = Solution()
res = s1.containsDuplicate(nums)

print(res)