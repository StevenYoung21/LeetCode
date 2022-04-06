class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums) 

        # k = 0

        for i in range(length):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        
        return nums


nums =[0,1,0,3,12]


s1 = Solution()
res = s1.moveZeroes(nums)

print(res)