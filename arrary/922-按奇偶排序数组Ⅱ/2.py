from turtle import right


class Solution:
    def sortArrayByParityII(self, nums) :

        i, j, n = 0, 1, len(nums)

        while i < n:
            if nums[i] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 2
            else: 
                i += 2

        return nums


nums = [1,2,4,2,5,7]

s1 = Solution()

print(s1.sortArrayByParityII(nums))