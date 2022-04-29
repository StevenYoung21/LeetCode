
class Solution:
    def threeSum(self, nums) :

        if len(nums) < 3 : return []
        nums.sort()

        res = []

        for i in range(len(nums)):

            if nums[i] > 0 : break
            if i >= 1 and nums[i] == nums[i-1]: continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

        s1 = set()

        for i in res:
            s1.add(tuple(i))

        return list(s1)




nums = [-2,0,0,2,2]

s1 = Solution()
print(s1.threeSum(nums))