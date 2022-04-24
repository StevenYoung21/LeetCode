class Solution:
    def targetIndices(self, nums, target: int):

        nums.sort()

        res = []

        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        if res != []:
            return res
        else:
            return []


nums = [1,2,5,2,3]
target = 2

s1 = Solution()
print(s1.targetIndices(nums,target))    