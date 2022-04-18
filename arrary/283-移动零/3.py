
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = 0
        slow = 0

        length = len(nums) 

        while fast < length :
            if nums[fast] != 0:
                nums[slow] , nums[fast]= nums[fast] , nums[slow] 
                slow += 1
            fast += 1

                    
                    
        
        return nums


nums = [0,1]


s1 = Solution()
res = s1.moveZeroes(nums)

print(res)