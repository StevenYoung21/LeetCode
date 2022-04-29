
class Solution:
    def fourSum(self, nums, target: int) :

        if len(nums) < 4 : return []
        nums.sort()
        res = []

        for i in range(len(nums)):

            if i >= 1 and nums[i] == nums[i-1]: continue

            for j in range(i+1,len(nums)):

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    tar = nums[i] + nums[j] + nums[left] + nums[right]
                    if tar > target:
                        right -= 1
                    elif tar < target:
                        left += 1
                    else:
                        res.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        left += 1
                        right -= 1                        

        s1 = set()

        for i in res:
            s1.add(tuple(i))

        return list(s1)


nums = [1,-2,-5,-4,-3,3,3,5]

target = -11

s1 = Solution()

print(s1.fourSum(nums,target))