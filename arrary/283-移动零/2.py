from re import A
from sklearn.cluster import k_means


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums) 

        
        a = 0

        for i in range(length):
            if nums[i] != 0:
                nums[a] = nums[i]
                a = a + 1

        b = length - a

        while( b > 0):
            nums[length - b] = 0
            b = b - 1

        return nums


nums =[0,1,0,3,12]


s1 = Solution()
res = s1.moveZeroes(nums)

print(res)