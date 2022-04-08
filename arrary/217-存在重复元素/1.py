class Solution:
    def containsDuplicate(self, nums) -> bool:

        length = len(nums)

        for i in range(length):
            for j in range(i+1,length):
                if nums[i] == nums[j]:
                    return True
        return False


nums = [1,2,3,4,1]


## 暴力超时

s1 = Solution()
res = s1.containsDuplicate(nums)

print(res)